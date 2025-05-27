# AI Hedge Fund for Chinese Stock Market

This project is a localized deployment of the original **ai-hedge-fund** framework, reconfigured to analyze and simulate trading decisions using data from the **Chinese stock market**. While it leverages the same multi-agent architecture, all data inputs, valuation models, and market signals are tailored for onshore Chinese exchanges. The output remains in **English**, ensuring consistency with the original project's interface and reporting.

## System Architecture

The system consists of a network of specialized agents working in concert:

1. **Aswath Damodaran Agent** – Story-driven valuation expert.
2. **Ben Graham Agent** – Seeks value bargains with a margin of safety.
3. **Bill Ackman Agent** – Activist investing strategies.
4. **Cathie Wood Agent** – Growth-focused, innovation-driven picks.
5. **Charlie Munger Agent** – Value and quality oriented investments.
6. **Michael Burry Agent** – Contrarian deep-value strategies.
7. **Peter Lynch Agent** – Practical ten-bagger seeker.
8. **Phil Fisher Agent** – In-depth scuttlebutt research for growth stories.
9. **Stanley Druckenmiller Agent** – Macro-driven asymmetric opportunities.
10. **Warren Buffett Agent** – Long-term, fair-price value investing.
11. **Valuation Agent** – Calculates intrinsic values and signals.
12. **Sentiment Agent** – Monitors market mood and sentiment.
13. **Fundamentals Agent** – Analyzes corporate financial data.
14. **Technicals Agent** – Generates signals from price patterns.
15. **Risk Manager** – Assesses risk and enforces position limits.
16. **Portfolio Manager** – Integrates signals and outputs final orders.

> **Note:** This system simulates trading decisions—it does **not** execute real trades.

## Chinese Market Customization

* **Data Source:** Onshore exchanges (Shanghai, Shenzhen) with local APIs and data feeds.
* **Valuation Models:** Adapted to A-share market conventions, accounting for onshore accounting standards.
* **Risk Parameters:** Calibrated to Chinese market volatility and regulatory requirements.

*Reminder: This project is for **educational** purposes only and should not be used for live trading.*

## Disclaimer

This project is for **educational and research purposes only**.

- Not intended for real trading or investment
- No warranties or guarantees provided
- Past performance does not indicate future results
- Creator assumes no liability for financial losses
- Consult a financial advisor for investment decisions

By using this software, you agree to use it solely for learning purposes.

## Table of Contents
- [Setup](#setup)
  - [Using Poetry](#using-poetry)
  - [Using Docker](#using-docker)
- [Usage](#usage)
  - [Running the Hedge Fund](#running-the-hedge-fund)
  - [Running the Backtester](#running-the-backtester)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [Feature Requests](#feature-requests)
- [License](#license)

## Setup

### Using Poetry

Clone the repository:
```bash
git clone https://github.com/dennioshao/ai-hedge-fund-chinese.git
cd ai-hedge-fund-chinese
```

1. Install Poetry (if not already installed):
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

2. Install dependencies:
```bash
poetry install
```

3. Set up your environment variables:
```bash
# Create .env file for your API keys
cp .env.example .env
```

4. Set your API keys:
```bash
# For running LLMs hosted by openai (gpt-4o, gpt-4o-mini, etc.)
# Get your OpenAI API key from https://platform.openai.com/
OPENAI_API_KEY=your-openai-api-key

# For running LLMs hosted by groq (deepseek, llama3, etc.)
# Get your Groq API key from https://groq.com/
GROQ_API_KEY=your-groq-api-key

# For getting financial data to power the hedge fund
# Get your Financial Datasets API key from https://financialdatasets.ai/
FINANCIAL_DATASETS_API_KEY=your-financial-datasets-api-key
```

### Using Docker

1. Make sure you have Docker installed on your system. If not, you can download it from [Docker's official website](https://www.docker.com/get-started).

2. Clone the repository:
```bash
git clone https://github.com/dennioshao/ai-hedge-fund-chinese.git
cd ai-hedge-fund-chinese
```

3. Set up your environment variables:
```bash
# Create .env file for your API keys
cp .env.example .env
```

4. Edit the .env file to add your API keys as described above.

5. Build the Docker image:
```bash
# On Linux/Mac:
./run.sh build

# On Windows:
run.bat build
```

**Important**: You must set `OPENAI_API_KEY`, `GROQ_API_KEY`, `ANTHROPIC_API_KEY`, or `DEEPSEEK_API_KEY` for the hedge fund to work.  If you want to use LLMs from all providers, you will need to set all API keys.

Financial data for tickers, you will need to set the `FINANCIAL_DATASETS_API_KEY` in the .env file.

## Usage

### Running the Hedge Fund for Chiese Stock Market

#### With Poetry
```bash
poetry run python src/main.py --ticker 000001.SZ
```

#### With Docker
```bash
# On Linux/Mac:
./run.sh --ticker 000001.SZ main

# On Windows:
run.bat --ticker 000001.SZ main
```

**Example Output:**
<img width="992" alt="Screenshot 2025-01-06 at 5 50 17 PM" src="https://github.com/user-attachments/assets/e8ca04bf-9989-4a7d-a8b4-34e04666663b" />

You can also specify a `--ollama` flag to run the AI hedge fund using local LLMs.

```bash
# With Poetry:
poetry run python src/main.py --ticker 000001.SZ --ollama

# With Docker (on Linux/Mac):
./run.sh --ticker 000001.SZ --ollama main

# With Docker (on Windows):
run.bat --ticker 000001.SZ --ollama main
```

You can also specify a `--show-reasoning` flag to print the reasoning of each agent to the console.

```bash
# With Poetry:
poetry run python src/main.py --ticker 000001.SZ --show-reasoning

# With Docker (on Linux/Mac):
./run.sh --ticker 000001.SZ --show-reasoning main

# With Docker (on Windows):
run.bat --ticker 000001.SZ --show-reasoning main
```

You can optionally specify the start and end dates to make decisions for a specific time period.

```bash
# With Poetry:
poetry run python src/main.py --ticker 000001.SZ --start-date 2024-01-01 --end-date 2024-03-01 

# With Docker (on Linux/Mac):
./run.sh --ticker 000001.SZ --start-date 2024-01-01 --end-date 2024-03-01 main

# With Docker (on Windows):
run.bat --ticker 000001.SZ --start-date 2024-01-01 --end-date 2024-03-01 main
```

### Running the Backtester

#### With Poetry
```bash
poetry run python src/backtester.py --ticker 000001.SZ
```

#### With Docker
```bash
# On Linux/Mac:
./run.sh --ticker 000001.SZ backtest

# On Windows:
run.bat --ticker 000001.SZ backtest
```

**Example Output:**
<img width="941" alt="Screenshot 2025-01-06 at 5 47 52 PM" src="https://github.com/user-attachments/assets/00e794ea-8628-44e6-9a84-8f8a31ad3b47" />


You can optionally specify the start and end dates to backtest over a specific time period.

```bash
# With Poetry:
poetry run python src/backtester.py --ticker 000001.SZ --start-date 2024-01-01 --end-date 2024-03-01

# With Docker (on Linux/Mac):
./run.sh --ticker 000001.SZ --start-date 2024-01-01 --end-date 2024-03-01 backtest

# With Docker (on Windows):
run.bat --ticker 000001.SZ --start-date 2024-01-01 --end-date 2024-03-01 backtest
```

You can also specify a `--ollama` flag to run the backtester using local LLMs.
```bash
# With Poetry:
poetry run python src/backtester.py --ticker 000001.SZ --ollama

# With Docker (on Linux/Mac):
./run.sh --ticker 000001.SZ --ollama backtest

# With Docker (on Windows):
run.bat --ticker 000001.SZ --ollama backtest
```


## Project Structure 
```
ai-hedge-fund-chinese/
├── hedge_ui                      # UI for the analyzing app
├── src/
│   ├── agents/                   # Agent definitions and workflow
│   │   ├── bill_ackman.py        # Bill Ackman agent
│   │   ├── fundamentals.py       # Fundamental analysis agent
│   │   ├── portfolio_manager.py  # Portfolio management agent
│   │   ├── risk_manager.py       # Risk management agent
│   │   ├── sentiment.py          # Sentiment analysis agent
│   │   ├── technicals.py         # Technical analysis agent
│   │   ├── valuation.py          # Valuation analysis agent
│   │   ├── ...                   # Other agents
│   │   ├── warren_buffett.py     # Warren Buffett agent
│   │   ├── aswath_damodaran.py   # Aswath Damodaran agent
│   │   ├── ...                   # Other agents
│   │   ├── ...                   # Other agents
│   ├── tools/                    # Agent tools
│   │   ├── api.py                # API tools
│   ├── backtester.py             # Backtesting tools
│   ├── main.py # Main entry point
├── pyproject.toml
├── ...
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

**Important**: Please keep your pull requests small and focused.  This will make it easier to review and merge.

## Feature Requests

If you have a feature request, please open an [issue](https://github.com/dennioshao/ai-hedge-fund-chinese/issues) and make sure it is tagged with `enhancement`.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
