# test_tushare.py

from src.utils.data_provider import get_cn_stock_data

if __name__ == "__main__":
    # 用一个你确定存在的 A 股代码测试
    ticker = "000001.SZ"
    start_date = "2025-05-20"
    end_date   = "2025-05-21"

    try:
        df = get_cn_stock_data(ticker, start_date, end_date)
        print("✅ 获取成功，数据预览：")
        print(df.head())
    except Exception as e:
        print("❌ 获取失败：", e)
