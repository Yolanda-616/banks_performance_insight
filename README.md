## 1. Problem & User
This project analyzes the financial performance of Chinese listed commercial banks from 2020 to 2024, focusing on profitability (ROE), leverage (debt-to-asset ratio), and growth (CAGR) across different bank size tiers.

**Target Audience:** Finance students, investment analysts, and banking researchers.

## 2. Data Source
- **Platform:** WRDS (Wharton Research Data Services)
- **Database:** CSMAR - `csmar_financial`
- **Table:** `fs_bcombas` (bank annual financial statements)
- **Access Date:** April 2026
- **Time Period:** 2020–2024 (5 complete years; 2025 data not yet available)

## 3. Methods
- Adaptive column mapping with fuzzy matching (85% similarity threshold)
- Balanced panel construction to control survivorship bias
- Financial ratios: ROE, ROA, debt-to-asset ratio, CAGR
- Tier classification by 2024 total assets:
  - Regional (< 1T CNY)
  - Mid-size (1T – 5T CNY)
  - Large (> 5T CNY)

## 4. Key Findings
- Large banks show stable but lower ROE compared to regional banks
- Debt-to-asset ratios remained consistently around 0.90–0.93 across all tiers
- Profit growth (CAGR) varies significantly by tier, with regional banks showing higher volatility but greater expansion potential

## 5. How to Run
### Prerequisites
Python 3.8 or higher is required.

### Install dependencies
```bash
pip install -r requirements.txt
requirements.txt includes:
pandas, numpy, matplotlib, seaborn (data analysis & visualization)
wrds (database connection)
streamlit, plotly (interactive dashboard)
Run the analysis notebook
Open Xiaoyu_Yang_2468581_ACC102_Task 2.ipynb and run all cells.
Note: A WRDS account is optional. The notebook supports the pre-saved CSV file for direct use.
Run the interactive dashboard
bash
运行
streamlit run bank_dashboard.py
If the above command fails:
bash
运行
python -m streamlit run bank_dashboard.py
The dashboard will launch at: http://localhost:8501
Dashboard features:
Select any bank from the dropdown
View ROE trend chart
View debt-to-asset ratio trend chart
View key metrics (average ROE, average debt-to-asset ratio, average total assets)

## 6. Repository Structure
plaintext
banks_performance_insight/
├── README.md
├── requirements.txt
├── Xiaoyu_Yang_2468581_ACC102_Task 2.ipynb
├── bank_dashboard.py
└── data/
    └── fs_bcombas_enhanced_with_metrics.csv
## 7. Limitations
Survivorship bias: only banks with complete 2020–2024 data are included
Annual granularity: quarterly data would better capture short-term volatility
2025 data excluded due to disclosure timing (April 2026)
Static tiering: based on 2024 asset size only

## 8. AI Disclosure

Tool	Version	Date	Purpose
DeepSeek	DeepSeek-V3	April 2026	Code debugging, column mapping, README template
ChatGPT	GPT-4o	April 2026	Code optimization
Doubao	Doubao-pro-32k	April 2026	Video script framework

## 9. Demo Video
[Insert 1–3 minute demo video link here]
