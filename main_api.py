from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from run_main import run_analysis

app = FastAPI(
    title="AI 对冲基金分析 API",
    description="提供股票分析服务，前端可POST请求获取分析结果",
)

# 跨域配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 请求体模型
class AnalyzeRequest(BaseModel):
    tickers: str = "000001.SZ" # 逗号分隔的股票代码列表
    language: str = "zh"  # 分析语言，zh 或 en

@app.post("/analyze")
async def analyze(req: AnalyzeRequest):
    """
    接收前端请求，调用 run_analysis，并返回摘要结果
    """
    try:
        summary = run_analysis(
            tickers=req.tickers,
            language=req.language
        )
        return JSONResponse(content={"summary": summary})
    except Exception as e:
        return JSONResponse(
            content={"error": f"服务异常：{str(e)}"},
            status_code=500
        )
