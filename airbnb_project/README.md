# Airbnb Dublin Market Performance Analysis

## 🎯 Business Case
The goal of this project was to analyze the Airbnb market in Dublin to help potential investors or hosts understand which property attributes contribute most to monthly revenue and occupancy rates.

## 🛠️ The Pipeline
1.  **Data Extraction & Cleaning (Python):**
    * Extracted the data from the online repository.
    * Handled missing values in price and rating columns.
    * Removed misleading data that was negatively impacting the analysis
    * Transfered all the removed data to a auditable repository for tracking purpouses.
    * Standardized currency and date formats for time-series analysis.
    * Created calculated columns to generate key insights.
      
3.  **Data Modeling (SQL):**
    * Loaded cleaned data into a SQLite database.
    * Established a connection to the SQL database to improve data loading and performance
      
5.  **Visualization (Power BI):**
    * Developed an interactive dashboard focusing on **Revenue per Available Room (RevPAR)** and **Occupancy Rates**.
    * Designed the dashboard based on the client's visual identity.
  
6. **Result:**
   <img width="1494" height="840" alt="image" src="https://github.com/user-attachments/assets/118d64ec-150b-4abd-a487-2f072b9e2e4f" />
   <img width="1493" height="844" alt="image" src="https://github.com/user-attachments/assets/dbbbefb1-0761-4a01-9f0c-f4010d841600" />


## 💡 Key Insights
* **Revenue Leaders:** Properties classified as "Entire Homes" outperform private rooms by an average of 45% in Dublin.
* **Long-term rents importance:** Long-term properties, even though in Airbnb, still have the greatest capacity of bringing estable income.


## 📂 Project Files
* [Python ETL scripts.](./scripts)
* [Power BI (.pbix) file and PDF.](./dashboard)
