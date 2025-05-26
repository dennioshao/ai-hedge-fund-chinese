import json
from langchain_core.messages import HumanMessage
from src.graph.state import AgentState, show_agent_reasoning
from src.utils.progress import progress
from src.utils.data_provider import get_cn_stock_data 



##### Risk Management Agent #####
def risk_management_agent(state: AgentState):
    """Controls position sizing based on real-world risk factors for multiple tickers."""
    portfolio = state["data"]["portfolio"]
    data = state["data"]
    tickers = data["tickers"]

    # Initialize risk analysis for each ticker
    risk_analysis = {}
    current_prices = {}  # Store prices here to avoid redundant API calls

    for ticker in tickers:
        progress.update_status("risk_management_agent", ticker, "Analyzing price data")

       # ➕ 新增：使用 Tushare 拉取中国市场日线数据
        try:
            df = get_cn_stock_data(
                ticker=ticker,
                start_date=data["start_date"],
                end_date=data["end_date"],
            )
        except Exception as e:
            progress.update_status("risk_management_agent", ticker, f"Failed: {e}")
            continue

        prices_df = df  # DataFrame 已经包含 ['trade_date','open','high','low','close','vol']

        progress.update_status("risk_management_agent", ticker, "Calculating position limits")

        # ✅ 修改：根据最后一个交易日收盘价作为当前价格
        current_price = float(df["close"].iloc[-1])
        current_prices[ticker] = current_price

        # ➕ 新增：计算当前成本价对应的持仓市值（与原逻辑一致）
        current_position_value = portfolio.get("cost_basis", {}).get(ticker, 0)

        # Calculate total portfolio value using stored prices
        total_portfolio_value = portfolio.get("cash", 0) + sum(portfolio.get("cost_basis", {}).get(t, 0) for t in portfolio.get("cost_basis", {}))

        # Base limit is 20% of portfolio for any single position
        position_limit = total_portfolio_value * 0.20

        # For existing positions, subtract current position value from limit
        remaining_position_limit = position_limit - current_position_value

        # Ensure we don't exceed available cash
        max_position_size = min(remaining_position_limit, portfolio.get("cash", 0))

        risk_analysis[ticker] = {
            "remaining_position_limit": float(max_position_size),
            "current_price": float(current_price),
            "reasoning": {
                "portfolio_value": float(total_portfolio_value),
                "current_position": float(current_position_value),
                "position_limit": float(position_limit),
                "remaining_limit": float(remaining_position_limit),
                "available_cash": float(portfolio.get("cash", 0)),
            },
        }

        progress.update_status("risk_management_agent", ticker, "Done")

    message = HumanMessage(
        content=json.dumps(risk_analysis),
        name="risk_management_agent",
    )

    if state["metadata"]["show_reasoning"]:
        show_agent_reasoning(risk_analysis, "Risk Management Agent")

    # Add the signal to the analyst_signals list
    state["data"]["analyst_signals"]["risk_management_agent"] = risk_analysis

    return {
        "messages": state["messages"] + [message],
        "data": data,
    }
