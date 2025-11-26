# 📊 Direct Marketing Campaign Analysis – EDA Project

## 1. Project Description
This project analyzes direct marketing campaigns carried out by a Portuguese bank through phone calls.  
The goal is to understand customer behavior, measure the effectiveness of campaign strategies, and generate new metrics that support data-driven decision-making.

Two main datasets were used:

1. **bank-additional.csv** – client interactions, demographics, call details, macroeconomic indicators, and campaign outcomes.  
2. **customer-details.xlsx** – demographic and online behavior information (income, family composition, web visits, customer tenure).

---

## 2. Objectives 🎯
- Clean and transform raw datasets.  
- Generate advanced metrics combining engagement, tenure, and campaign effort.  
- Analyze distributions, outliers, correlations, and customer behavior patterns.  
- Segment customers using clustering techniques to optimize marketing strategies.  
- Produce a detailed analytic report with insights and business recommendations.  
- Organize the project following a clean, reproducible structure.

---

## 3. Repository Structure 📂

```
Proyecto EDA/
│
├── Data/ # Cleaned and processed datasets
│ ├── data_limpios_bank.csv # Cleaned bank dataset
│ ├── data_limpios_customer.csv # Cleaned customer dataset
│ ├── data_metricas_bank.csv # Metrics based on bank data
│ ├── data_metricas_datasetsmerged.csv # Metrics based on merged datasets
│ └── data_transformacion_limpieza_*.csv # Intermediate cleaning outputs
│
├── DataRaw/ # Raw unprocessed data
│ ├── bank-additional.csv
│ └── customer-details.xlsx
│
├── Jupyters_notebook/ # Full analysis in notebook format
│ ├── columnas_categoricas_bank.ipynb # Bank categorical analysis
│ ├── columnas_categoricas_customer.ipynb # Customer categorical analysis
│ ├── columnas_numericas_bank.ipynb # Bank numerical analysis
│ ├── columnas_numericas_customer.ipynb # Customer numerical analysis
│ ├── eda_preliminar_bank.ipynb # Preliminary bank EDA
│ ├── eda_preliminar_customer.ipynb # Preliminary customer EDA
│ ├── Informe_explicativo_del_analisis.ipynb # Full analysis report
│ ├── limpieza_bank.ipynb # Bank cleaning pipeline
│ ├── limpieza_customer.ipynb # Customer cleaning pipeline
│ ├── metricas_bank.ipynb # Bank metric creation
│ └── metricas_datasetsmerged.ipynb # Metrics after dataset merge
│
├── SRC/ # Python scripts with reusable functions
│ ├── sp_eda.py # General EDA utilities
│ ├── sp_limpieza_bank.py # Cleaning functions for bank data
│ ├── sp_limpieza_customer.py # Cleaning functions for customer data
│ ├── sp_nulos_num.py # Missing value handling for numeric cols
│ ├── sp_outliers.py # Outlier detection utilities
│ └── sp_visualizacion.py # Visualization utilities
│
├── README.md # Project documentation
├── requirements.txt # Python dependencies
└── venv/ # Virtual environment
```

---

## 4. Execution Steps 🏃‍♂️

1. **Clone the repository**:
```bash
git clone <https://github.com/danielamichellod/analisis_marketing.git>
cd Proyecto\ EDA

2. Create a virtual environment:

python -m venv venv
source venv/bin/activate  

3. Install dependencies:

pip install -r requirements.txt

4. Run Jupyter notebooks in order:

- limpieza_bank.ipynb & limpieza_customer.ipynb: data cleaning.
- columnas_categoricas_*.ipynb: categorical analysis.
- columnas_numericas_*.ipynb: numeric analysis & outliers.
- metricas_bank.ipynb & metricas_datasetsmerged.ipynb: generate metrics.
- Informe_explicativo_del_analisis.ipynb: visualizations, clustering, and insights.
```

## 5. Metrics Generated 📈
- **Customer_tenure_days/years:** Customer age in the bank
- **High_web_visit_flag:** Top 25% web users
- **Web_engagement_score & Web_visit_intensity:** Online activity metrics
- **Tenure_vs_campaign_effort:** Number of contacts per year of tenure
- **Engagement_score_total & Overall_interaction_score:** Combination of online engagement and campaign effort
- **Contact_effort_ratio, Avg_duration_per_contact, Web_activity_per_contact:** Contact behavior and activity metrics

## 6. Customer Segmentation 👥
- **KMeans Clustering (4 clusters)** using engagement and effort metrics:
    - **Cluster 0:** Prioritize campaign (high engagement)
    - **Cluster 1:** Evaluate further contacts (low engagement, high effort)
    - **Cluster 2:** Standard contact (medium)
    - **Cluster 3:** Strategic clients (high value, moderate interaction)
- Visualizations: Scatterplots, boxplots, and cluster centroids

## 7. Key Insights 💡
**1. Customer tenure and web activity** are important for segmenting and prioritizing campaigns.

**2. Campaign effort is uneven:** some clients receive many calls without conversion → potential fatigue.

**3. High web engagement + effective contact** increases likelihood of subscribing.

**4. Outliers** exist in multiple metrics; median/percentiles should be used for decision-making.

**5. Cluster segmentation** allows optimized resource allocation and targeting.

## 8. Conclusions 🧩
The analysis of the Portuguese bank’s direct marketing campaigns highlights several important findings that can guide more effective customer targeting and improve campaign efficiency:
- **Customer tenure and online engagement are strong indicators of conversion potential.** Clients who have been with the bank longer and show higher digital activity tend to respond better to marketing efforts.
- **Campaign effort is not always proportional to results.** Some customers received a high number of contact attempts without converting, suggesting the need to reduce unnecessary repeated calls and improve contact strategy.
- **Web engagement metrics enrich traditional campaign data.** Combining online behavior with call-based metrics offers a more complete view of customer interest and helps identify high-priority segments.
- **Clustering reveals distinct customer profiles.** The segmentation process shows clear groups with different engagement and effort patterns, allowing personalized strategies rather than uniform campaigns.
- **Outliers and skewed distributions require careful metric selection.** Median- and percentile-based analysis provides more reliable insights than mean-driven metrics.

Overall, the project demonstrates the value of integrating multiple data sources, applying metric engineering, and leveraging clustering to improve decision-making in direct marketing campaigns.

## 9. Recommendations ✅
- Focus campaigns on **Cluster 0 & 3**
- Monitor high **Contact_effort_ratio** clients to avoid oversaturation
- Adjust call duration and frequency according to engagement metrics
- Use combined metrics to plan future campaigns

## 10. Requirements 🐍
- Python 3.9+
- Libraries: pandas, numpy, matplotlib, seaborn, scikit-learn, etc.

## 11. Contributions ✨
Your contributions are appreciated. Please feel free to reach out with any suggestions, enhancements, or corrections.

Any kind of contribution — whether it's code, documentation, or feedback — will be appreciated. Thank you for your help and collaboration.

## 12. Author ✉️
- Daniela - [GitHub Profile](https://github.com/danielamichellod)

