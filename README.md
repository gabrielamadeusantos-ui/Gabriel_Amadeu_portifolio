# Gabriel Amadeu Santos  
### Data Engineer & Analyst 📊  

**Systems Analysis & Development Graduate** | Based in Dublin, Ireland 🇮🇪  

---

## 👨‍💻 About Me  

I'm a passionate Data Engineer and Analyst with a strong background in audit and analytics, currently based in Dublin. My journey in data began with a fascination for uncovering patterns and has evolved into building production-grade data pipelines that power real-world decision-making.  

I thrive at the intersection of engineering and analytics, creating end-to-end solutions that are both technically robust and business-focused.  

---

## 🛠️ Technical Stack  

| Layer | Technologies |
| :--- | :--- |
| **Data Processing & ETL** | Python (Pandas, NumPy, Requests, SQLAlchemy, Psycopg2) |
| **Databases** | SQL (PostgreSQL, SQLite), Supabase |
| **Orchestration & Automation** | GitHub Actions, Power Automate Desktop |
| **Cloud & Storage** | Google Drive API, Supabase, Google Cloud Platform |
| **Visualization & BI** | Power BI (DAX, Advanced Modeling), Google Looker Studio |
| **Languages** | English (Fluent), Portuguese (Native) |

---

## 🚀 Featured Projects  

### 🌍 Real-Time Global Earthquake Monitoring  
**End-to-end serverless data pipeline for ingesting, processing, and visualizing global seismic activity in near real-time.**  

📺 [**Watch the Explanation Video**](https://youtu.be/NdRpZVuqV8Y)  

#### 🧩 Business Challenge  
Ingest and visualize a high-volume stream of global earthquake data while operating within a strict free-tier budget and maintaining efficient query performance.  

#### ⚙️ Technical Solution  
- Built an automated ETL pipeline using Python to fetch data from the **USGS Earthquake API** with efficient pagination handling and monthly data extraction since 1996.  
- Implemented a **highly efficient incremental load strategy** with spatiotemporal deduplication, reducing data volume by over 80% while preserving analytical value.  
- Designed a robust architecture:  
  `USGS API → Python ETL → PostgreSQL (Supabase) → Looker Studio Dashboard`  
- Orchestrated the pipeline using **GitHub Actions** for scheduled, hands-off execution with CI/CD integration.  
- Stored processed data in a **cloud PostgreSQL** database (Supabase) and created a public-facing interactive dashboard in **Looker Studio**.  

#### 📊 Data Optimization Strategy  
Applied magnitude threshold filtering (≥ 4.0) and clustering logic to handle over 80% data reduction while maintaining analytical relevance.  

#### ✅ Outcome & Impact  
A cost-free, fully automated system that provides a macro-level, real-time view of global seismic activity, demonstrating advanced data engineering principles in a production-style environment.  

🔗 **[View Project Repository](https://github.com/gabrielamadeusantos-ui/earthquake_pipeline)** | **[Live Dashboard](https://datastudio.google.com/reporting/a4453d0c-f99f-4d4f-bdfd-2bc443434ed7)**  

---

### 🏥 Healthcare Data Pipeline & Analytics  
**A complete ETL pipeline designed to simulate real-world healthcare data ingestion and generate decision-oriented insights.**  

<img width="1255" height="703" alt="Healthcare Dashboard" src="https://github.com/user-attachments/assets/d313732b-01cc-40c1-bea4-eb4b127a8e17" />  

#### 🧩 Business Challenge  
Transform a consolidated, static dataset into a dynamic, incremental processing environment to mirror how data is typically ingested in real-world healthcare systems, where new data arrives periodically.  

#### ⚙️ Technical Solution  
- Simulated a real-world scenario by splitting a consolidated dataset into **incremental monthly files** with continuous ingestion and updates.  
- Developed a modular **Python ETL pipeline** integrated with the **Google Drive API** for automated file detection, processing, and smart overwrite logic.  
- Applied advanced feature engineering including age clusters, billing tiers, admission weekday, and length of stay analysis.  
- Automated the entire pipeline using **Power Automate Desktop** for reliable local execution and scheduling.  
- Created **interactive Power BI dashboards** with strong business decision-making focus covering:  
  - Revenue analysis by hospital and insurance provider with monthly trends  
  - Patient behavior analysis (admission type distribution by weekday)  
  - Demographic segmentation (age groups, gender distribution)  
  - Operational metrics (length of stay, medical condition distribution, test results)  

#### ✅ Outcome & Impact  
Delivered a scalable data service that bridges the gap between raw data and business insights, showcasing capabilities in both data engineering and data visualization.  

🔗 **[View Project Repository](https://github.com/gabrielamadeusantos-ui/Healthcare_Project)**  

---

### 📈 Airbnb Dublin: Revenue & Performance Analysis  
**A comprehensive analysis of the short-term rental market in Dublin, focusing on key drivers of revenue and occupancy rates.**  

<img width="1407" height="791" alt="Airbnb Dashboard" src="https://github.com/user-attachments/assets/07d1c756-1707-4a5c-8130-ee3d699a2355" />  

#### 🧩 Business Challenge  
Help potential investors and hosts understand which property attributes contribute most to monthly revenue and occupancy rates in the Dublin market, a market with restricted geographical data.  

#### ⚙️ Technical Solution  
- Built a focused **ETL pipeline in Python** for data extraction and cleaning, handling missing values in price and rating columns.  
- Removed misleading data while maintaining an auditable repository for tracking purposes.  
- Standardized currency and date formats for time-series analysis.  
- Created calculated columns to generate key insights for **Revenue per Available Room (RevPAR)** and **Occupancy Rates**.  
- Developed interactive **Power BI dashboards** designed based on the client's visual identity.  

#### 💡 Key Insights  
- **Revenue Leaders:** Properties classified as "Entire Homes" outperform private rooms by an average of 45% in Dublin.  
- **Long-term rents importance:** Long-term properties have the greatest capacity for bringing stable income, even in the Airbnb ecosystem.  

#### ✅ Outcome & Impact  
Isolated that specific property configurations can generate up to **20% higher revenue**, regardless of location, providing actionable insights for potential investors and hosts.  

🔗 **[View Project Repository](https://github.com/gabrielamadeusantos-ui/Airbnb_Project)**  

---

## 📫 Connect with Me  

- 📍 **Location:** Dublin, Ireland  
- 💼 [**LinkedIn**](https://www.linkedin.com/in/gabriel-amadeu/)  
- ✉️ **Email:** gabrielamadeusantos@gmail.com  
- 🐙 [**GitHub**](https://github.com/gabrielamadeusantos-ui)  
