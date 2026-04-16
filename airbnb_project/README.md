# Airbnb Dublin Market Performance Analysis

## 🎯 Business Case
The goal of this project was to analyze the Airbnb market in Dublin to help potential investors or hosts understand which property attributes contribute most to monthly revenue and occupancy rates.

## 🛠️ The Pipeline
1.  **Data Extraction & Cleaning (Python):**
    * Extracted the data from the online repository.
    * Handled missing values in price and rating columns.
    * Removed misleading data that was negatively impacting the analysis 
    * Standardized currency and date formats for time-series analysis.
    * Created calculated columns to generate key insights.
      
3.  **Data Modeling (SQL):**
    * Loaded cleaned data into a SQLite database.
    * Established a connection to the SQL database to improve data loading and performance
      
5.  **Visualization (Power BI):**
    * Developed an interactive dashboard focusing on **Revenue per Available Room (RevPAR)** and **Occupancy Rates**.
    * Designed the dashboard based on the client's visual identity.

## 💡 Key Insights
* **Revenue Leaders:** Properties classified as "Entire Homes" outperform private rooms by an average of 45% in Dublin.


## 📂 Project Files
* `/scripts`: Python ETL notebooks.
* `/dashboard`: Power BI (.pbix) file and screenshots.
