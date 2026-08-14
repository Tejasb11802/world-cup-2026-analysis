# 2026 FIFA World Cup Intelligence Report

Social media, broadcast, and sponsor performance analysis for the 2026 FIFA World Cup.

## Overview

This project demonstrates end-to-end data analytics methodology for sports sponsorship measurement. It analyzes social media performance during the 2026 World Cup using publicly available data and transforms raw metrics into actionable business intelligence.

**Key Metrics:**
- 504.8M total views across 10 official videos
- 10.6M total engagements (likes + comments)
- $10.1M estimated social value
- $2.0M estimated sponsor value

## What This Project Shows

This portfolio project demonstrates the Associate Data Analyst skillset:
- **KPI Quantification**: Transform raw social media data into business metrics
- **Trend Identification**: Analyze performance patterns across content types
- **Insights Communication**: Create professional dashboards and reports
- **Methodology Documentation**: Transparent, defensible analysis framework

## Deliverables

1. **Interactive Dashboard** (`app/dashboard.py`)
   - Real-time KPI cards
   - Performance charts by video and channel
   - Engagement analysis
   - Methodology documentation

2. **Professional PDF Report** (`reports/World_Cup_2026_Intelligence_Report.pdf`)
   - 5-page executive report
   - Key metrics and findings
   - Top content analysis
   - Methodology & assumptions

3. **Complete Data Pipeline**
   - Raw data ingestion
   - KPI calculations
   - Report generation
   - Reproducible analysis

## Data Sources

- **Social Media**: YouTube official team and FIFA channels
- **Metrics**: Views, likes, comments from public APIs
- **Tournament Period**: May 26 - July 19, 2026
- **Data Type**: Sample data demonstrating real-world methodology

## Project Structure


    world-cup-2026-analysis/
    ├── data/
    │   ├── raw/           - Raw YouTube data (CSV)
    │   └── processed/     - Processed KPI metrics
    ├── src/               - Python analysis scripts
    ├── app/               - Streamlit dashboard
    ├── reports/           - PDF reports
    ├── README.md
    ├── requirements.txt
    └── youtube_credentials.json (git-ignored)
    
## Getting Started

### Prerequisites
- Python 3.8+
- pip package manager
- Virtual environment (recommended)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/world-cup-2026-analysis.git
cd world-cup-2026-analysis
```

2. Create and activate virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Analysis

**Generate analysis and KPIs:**
```bash
python src/analysis.py
```

**Generate PDF report:**
```bash
python src/generate_report.py
```

**Launch interactive dashboard:**
```bash
streamlit run app/dashboard.py
```

The dashboard will open in your browser at `http://localhost:8501`

## Key Metrics & Calculations

### Engagement Rate

Engagement Rate = (Likes + Comments) / Views × 100

### Social Value

Social Value = Total Engagements × Cost Per Engagement ($0.95)

### Sponsor Value

Sponsor Value = Total Views × CPM ($4.00) / 1,000

## Methodology

**Data Collection:**
- Official YouTube channels (FIFA, US Soccer)
- Public video statistics (no private APIs)
- Tournament window: May 26 - July 19, 2026

**Analysis Approach:**
1. Aggregate social media metrics by video
2. Calculate KPIs (engagement rate, social value, sponsor value)
3. Identify top-performing content
4. Create visualizations and reports
5. Document assumptions and limitations

**Key Assumptions:**
- CPE (Cost Per Engagement): $0.95
- CPM (Cost Per Thousand): $4.00
- Sample data demonstrates real-world methodology
- Results are reproducible and auditable

## Results

**Total Engagement:** 10.6M engagements
**Engagement Rate:** 2.10%
**Top Video:** World Cup Finals (125.3M views, 2.15M engagement)

See `reports/World_Cup_2026_Intelligence_Report.pdf` for full analysis.

## Technologies Used

- **Python 3.8+** - Core language
- **Pandas** - Data processing and analysis
- **Matplotlib/Seaborn** - Visualizations
- **Plotly** - Interactive charts
- **Streamlit** - Interactive dashboard
- **Google APIs** - YouTube data (optional)

## About

This project was built to demonstrate end-to-end analytics capability for sports sponsorship measurement, matching the methodology used by Zoomph and other sports analytics platforms.

**The Smarter Way to Measure Partnerships**

Zoomph enables brands, leagues, teams, and media to measure partnership portfolios and gain insights into their target audience through real-time social and broadcast analytics.

## License

This project is open source and available for demonstration and educational purposes.

## Contact

Built by Tejas Bhanushali  
GitHub: [@Tejasb11802](https://github.com/Tejasb11802)

---

*Last Updated: August 14, 2026*
