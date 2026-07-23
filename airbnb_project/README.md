# Airbnb Dublin Market Performance Analysis

## 🎯 Business Case
The goal of this project was to analyze the Airbnb market in Dublin to help potential investors or hosts understand which property attributes contribute most to monthly revenue and occupancy rates.

## 🛠️ The Pipeline

1. **Data Extraction & Cleaning (Python):**
   - Extracted data directly from the official Airbnb data repository (CSV compressed).
   - Selected only relevant columns for the analysis.
   - Handled missing values and removed invalid records (e.g., zero price or availability).
   - Created an audit log (`dropped_items.csv`) to track removed listings for traceability.
   - Standardized currency symbols and percentage signs, converting fields to numeric types.
   - Generated calculated columns: `max_revenue`, `estimated_revenue`, `stay_category`, `occupancy_cluster`, and `location`.
   - All paths are relative to the script location, ensuring portability and avoiding exposure of absolute paths.
   - The script is modular (ETL functions) and includes logging for better monitoring and error handling.

2. **Data Modeling (SQL):**
   - Loaded cleaned data into a local SQLite database (`Listings_DB.db`) for efficient querying.
   - The database and all output files are stored in a `data/` folder, created automatically if it doesn't exist.

3. **Visualization (Power BI):**
   - Developed an interactive dashboard focusing on **Revenue per Available Room (RevPAR)** and **Occupancy Rates**.
   - Designed the dashboard based on the client's visual identity.

4. **Results:**

   <img width="1407" height="791" alt="p1" src="https://github.com/user-attachments/assets/601de033-94e6-4a3d-8217-745dec16113b" />
   <img width="1385" height="789" alt="p2" src="https://github.com/user-attachments/assets/19bfaac1-7fa1-4736-8d1a-f91f5424e98a" />
   <img width="1389" height="787" alt="p3" src="https://github.com/user-attachments/assets/3875b5d4-b78b-4c61-b821-85874244ea54" />

## 💡 Key Insights
- **Revenue Leaders:** Properties classified as "Entire Homes" outperform private rooms by an average of 45% in Dublin.
- **Long-term Rents Importance:** Long-term properties, even within Airbnb, still have the greatest capacity to bring stable income.

## 📂 Project Files
- [Python ETL script](./scripts) – The main ETL script (`Airbnb_ETL_Execution.py`) with relative paths and modular structure.
- [Power BI (.pbix) file and PDF](./Dashboard) – The interactive dashboard and a static PDF export.
