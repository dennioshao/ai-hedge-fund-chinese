from datetime import datetime
from dateutil.relativedelta import relativedelta
from src.main import run_hedge_fund
from src.utils.analysts import get_analyst_nodes


def run_analysis(tickers: str, language: str = "zh") -> str:
    """
    接收前端字符串形式的股票列表和语言参数，调用核心 run_hedge_fund 得到分析结果后，
    将结果拼接成中文或英文的自然语言摘要返回。
    """
    # ➕ 新增：拆分并清洗 ticker 字符串，初始化原始列表 raw_tickers
    raw_tickers = [t.strip() for t in tickers.split(',') if t.strip()]

    # ➕ 新增：自动为中国股票代码补充交易所后缀
    ticker_list = []
    for t in raw_tickers:
        if '.' not in t:
            # ✅ 修改：根据首位数字决定交易所，6 开头为沪市，其余为深市
            if t.startswith('6'):
                ticker_list.append(f"{t}.SH")
            else:
                ticker_list.append(f"{t}.SZ")
        else:
            ticker_list.append(t)

    # 计算默认日期范围：结束日期为今天，开始日期为三个月前
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - relativedelta(months=3)).strftime('%Y-%m-%d')

    # 初始化投资组合
    portfolio = {
        'cash': 100000.0,
        'margin_requirement': 0.0,
        'margin_used': 0.0,
        'positions': {
            ticker: {
                'long': 0,
                'short': 0,
                'long_cost_basis': 0.0,
                'short_cost_basis': 0.0,
                'short_margin_used': 0.0,
            } for ticker in ticker_list
        },
        'realized_gains': {
            ticker: {
                'long': 0.0,
                'short': 0.0,
            } for ticker in ticker_list
        },
    }

    # 获取所有可用分析师列表，确保使用自定义工作流，而非全局 app
    analyst_keys = list(get_analyst_nodes().keys())

    # 调用核心函数
    result = run_hedge_fund(
        tickers=ticker_list,
        start_date=start_date,
        end_date=end_date,
        portfolio=portfolio,
        show_reasoning=False,
        selected_analysts=analyst_keys,
        model_name='gpt-4o-mini',
        model_provider='OpenAI',
    )

    # 解析决策结果
    decisions = result.get('decisions', {})

    # 拼接摘要字符串
    lines = []
    for ticker, info in decisions.items():
        action = info.get('action', '').capitalize()
        confidence = info.get('confidence', 0.0)
        reasoning = info.get('reasoning', '')
        if language == 'zh':
            lines.append(
                f"{ticker}：建议「{action}」 信心指数：{confidence}%\n原因：{reasoning}"
            )
        else:
            lines.append(
                f"{ticker}: Suggested {action} with {confidence}% confidence. Reason: {reasoning}"
            )

    return "\n\n".join(lines)
