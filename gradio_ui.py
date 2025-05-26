import gradio as gr
from run_main import run_analysis

TICKER_DEFAULT = "AAPL,MSFT,NVDA"
MODEL_OPTIONS = ["gpt-4o-mini", "deepseek-chat", "gpt-3.5-turbo"]
ANALYST_OPTIONS = ["Warren Buffett", "Cathie Wood", "Ray Dalio"]


def gradio_interface(tickers, start_date, end_date, model_name, analysts, show_reasoning):
    return run_analysis(
        tickers=[t.strip() for t in tickers.split(",") if t.strip()],
        start_date=start_date,
        end_date=end_date,
        model_name=model_name,
        selected_analysts=analysts,
        show_reasoning=show_reasoning
    )


def launch_ui():
    with gr.Blocks(title="AI Hedge Fund") as demo:
        gr.Markdown("# 📊 AI Hedge Fund 分析应用")

        with gr.Row():
            tickers_input = gr.Textbox(label="股票代码 (,分割)", value=TICKER_DEFAULT)
            start_date = gr.Textbox(label="起始日 (YYYY-MM-DD)", value="2024-01-01")
            end_date = gr.Textbox(label="结束日 (YYYY-MM-DD)", value="2024-03-01")

        model_select = gr.Dropdown(label="选择 LLM 模型", choices=MODEL_OPTIONS, value="gpt-4o-mini")
        analyst_checkboxes = gr.CheckboxGroup(label="分析师列表", choices=ANALYST_OPTIONS, value=["Warren Buffett"])
        show_reasoning_checkbox = gr.Checkbox(label="显示理由过程", value=True)

        run_btn = gr.Button("进行分析")
        output_text = gr.Textbox(label="分析结果", lines=30)

        run_btn.click(
            gradio_interface,
            inputs=[tickers_input, start_date, end_date, model_select, analyst_checkboxes, show_reasoning_checkbox],
            outputs=output_text
        )

    demo.launch(server_port=8888)


if __name__ == "__main__":
    launch_ui()
