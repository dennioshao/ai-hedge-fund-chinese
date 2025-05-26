from dotenv import load_dotenv  # ➕ 新增
load_dotenv()                  # ➕ 新增，这行会把 .env 中的变量加载到环境

import os
from datetime import datetime
import tushare as ts

# ➕ 新增：从环境变量读取 Tushare Token 并初始化
TUSHARE_TOKEN = os.getenv("TUSHARE_TOKEN")
if TUSHARE_TOKEN:
    ts.set_token(TUSHARE_TOKEN)
    pro = ts.pro_api()
else:
    pro = None  # 让模块可以正常导入，后续调用时抛错


def get_cn_stock_data(ticker: str, start_date: str, end_date: str):
    if pro is None:
        raise ValueError("请在.env中设置 TUSHARE_TOKEN")
    """
    使用 Tushare 获取中国市场日线行情数据。

    参数:
      ticker: 中国股票代码，需包含交易所后缀，如 '000001.SZ' 或 '600000.SH'
      start_date: 开始日期，格式 'YYYY-MM-DD'
      end_date:   结束日期，格式 'YYYY-MM-DD'

    返回:
      pandas.DataFrame，字段包括 ['trade_date','open','high','low','close','vol',...]
    """
    # 转换日期至 tushare 格式 YYYYMMDD
    s = start_date.replace('-', '')
    e = end_date.replace('-', '')

    try:
        df = pro.daily(ts_code=ticker, start_date=s, end_date=e)
    except Exception as e:
        raise RuntimeError(f"获取 {ticker} 数据失败: {e}")

    # 按交易日期排序并返回
    if df.empty:
        raise ValueError(f"未获取到 {ticker} 在 {start_date} 到 {end_date} 的数据。")
    return df.sort_values('trade_date')
