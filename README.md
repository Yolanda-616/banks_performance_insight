# Chinese Listed Banks Financial Performance Analysis (2020-2024)

## 1. Problem & User

This project analyzes the financial performance of Chinese listed commercial banks from 2020 to 2024, focusing on profitability (ROE), leverage (debt-to-asset ratio), and growth (CAGR) across different bank size tiers.

**Target Audience:** Finance students, investment analysts, and banking researchers.

## 2. Data Source

- **Platform:** WRDS (Wharton Research Data Services)
- **Database:** CSMAR - `csmar_financial`
- **Table:** `fs_bcombas` (bank annual financial statements)
- **Access Date:** April 2026
- **Time Period:** 2020–2024 (5 complete years, 2025 data not yet available)

## 3. Methods

- Adaptive column mapping with fuzzy matching (85% similarity threshold)
- Balanced panel construction to control survivorship bias
- Financial ratios: ROE, ROA, debt-to-asset, CAGR
- Tier classification by 2024 asset size: Regional (<1T), Mid-size (1T-5T), Large (>5T)

## 4. Key Findings

- Large banks show stable but lower ROE compared to regional banks
- Debt-to-asset ratios remained consistently around 0.90–0.93 across all tiers
- Profit growth (CAGR) varies significantly by tier, with regional banks showing higher volatility but greater expansion potential

## 5. How to Run

### Prerequisites
- Python 3.8 or higher

### Install dependencies
```bash
pip install -r requirements.txt
```

## Run the analysis notebook
Open Xiaoyu_Yang_2468581_ACC102_Task 2.ipynb in Jupyter Notebook and run all cells.

### Note: WRDS account is required for live data extraction. Without WRDS access, the notebook will work with the pre-saved CSV file in data/ folder.

## Run the interactive dashboard
Make sure you are in the same directory as bank_dashboard.py, then run:

```bash
streamlit run bank_dashboard.py
```
If streamlit command is not found, use:
```bash
python -m streamlit run bank_dashboard.py
```
The dashboard will open in your browser at http://localhost:8501.

## Dashboard features:

- Select a bank from the dropdown menu

- View ROE trend chart

- View Debt-to-Asset ratio trend chart

- View average key metrics


## 6. Repository Structure

README.md

requirements.txt

Xiaoyu_Yang_2468581_ACC102_Task 2.ipynb

bank_dashboard.py

data/

fs_bcombas_enhanced_with_metrics.csv

## 7. Limitations

- Survivorship bias: only banks with complete 2020-2024 data are included
- Annual granularity: quarterly data would better capture volatility
- 2025 data excluded due to disclosure timing (April 2026)
- Static tiering: bank size tiers based on 2024 assets only

## 8. AI Disclosure

| Tool | Version | Date | Purpose |
|------|---------|------|---------|
| DeepSeek | DeepSeek-V3 | April 2026 | Code debugging, column mapping, README template |
| ChatGPT | GPT-4o | April 2026 | Code optimization |
| Doubao | Doubao-pro-32k | April 2026 | Video script framework |

## 9. Demo Video

[Insert your 1-3 minute demo video link here]
