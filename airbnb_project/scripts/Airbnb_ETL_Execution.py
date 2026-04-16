# Importing libraries
import pandas as pd
import sqlite3
import numpy as np

# --- CONFIGURATION & PATHS ---
DATA_URL = "https://data.insideairbnb.com/ireland/leinster/dublin/2025-09-16/data/listings.csv.gz"
DB_PATH = r"C:\Users\gabri\OneDrive\Desktop\Airbnb_Dublin\Files\Listings_DB.db"
OUTPUT_CSV = r"C:\Users\gabri\OneDrive\Desktop\Airbnb_Dublin\Files\listings_csv.csv"
OUTPUT_DROPPED_CSV = r"C:\Users\gabri\OneDrive\Desktop\Airbnb_Dublin\Files\dropped_items.csv"

# --- 1. EXTRACTION ---
print("Downloading and extracting data...")
listing_file = pd.read_csv(DATA_URL, compression='gzip')

# Selecting necessary columns
listing_file = listing_file[[
    "id", 
    "name", 
    "neighbourhood", 
    "neighbourhood_cleansed", 
    "room_type", 
    "price",
    "minimum_nights", 
    "number_of_reviews", 
    "reviews_per_month", 
    "availability_365",
    "latitude", 
    "longitude", 
    "property_type", 
    "accommodates", 
    "bedrooms",
    "host_response_time", 
    "host_response_rate", 
    "host_acceptance_rate",
    "host_is_superhost", 
    "estimated_occupancy_l365d", 
    "review_scores_rating"
]].copy()

# --- 2. DATA TREATMENT & AUDIT ---

# A. Bulk cleaning symbols and converting to numeric
cols_to_clean = ['price', 'host_response_rate', 'host_acceptance_rate']
listing_file[cols_to_clean] = listing_file[cols_to_clean].replace(r'[\$,\%]', '', regex=True)

numeric_cols = cols_to_clean + [
    'availability_365', 
    'minimum_nights', 
    'number_of_reviews', 
    'reviews_per_month', 
    'accommodates', 
    'bedrooms', 
    'estimated_occupancy_l365d', 
    'review_scores_rating', 
    'latitude', 
    'longitude'
]

for col in numeric_cols:
    listing_file[col] = pd.to_numeric(listing_file[col], errors='coerce').fillna(0.0)

# B. Creating the Audit Log (removing rows with price or availability equal zero)
dropped_mask = (
    (listing_file['price'] <= 0) | 
    (listing_file['availability_365'] <= 0) | 
    (listing_file['estimated_occupancy_l365d'] <= 0)
)
dropped_items = listing_file[dropped_mask].copy()

conditions = [
    (dropped_items['price'] <= 0),
    (dropped_items['availability_365'] <= 0),
    (dropped_items['estimated_occupancy_l365d'] <= 0)
]
choices = [
    "Price equal zero: invalid listing",
    "Availability equal zero: invalid listing",
    "Estimated occupancy equal zero: invalid listing"
]
dropped_items['reason_for_dropping'] = np.select(conditions, choices, default="Multiple reasons")

dropped_items.to_csv(OUTPUT_DROPPED_CSV, index=False, encoding='utf-8-sig')

# Keeping only active listings
listing_file = listing_file[~dropped_mask].copy()
del dropped_mask

# C. Generating Sequential ID and converting to String (Char)
listing_file = listing_file.reset_index(drop=True)
listing_file['id'] = (listing_file.index + 1).astype(str)

# D. Adjusting specific Integer types
cols_to_int = ["minimum_nights", "number_of_reviews", "availability_365", "accommodates", "estimated_occupancy_l365d"]
listing_file[cols_to_int] = listing_file[cols_to_int].astype(int)

# E. Clustering by Minimum Nights 
bins_nights = [0, 2, 6, 29, 9999]
labels_nights = ['1-2 nights', '3-6 nights', '7-29 nights', '30+ nights']
listing_file['stay_category'] = pd.cut(
    listing_file['minimum_nights'], 
    bins=bins_nights, 
    labels=labels_nights, 
    include_lowest=True
)

# F. Clustering by Minimum Nights estimated occupancy
# Based on estimatives of from airbnb healty occupancy 
# 0 to 91.25 equals ===== 0 to 25% of 365 days of the year and so on
bins_occ = [0, 91.25, 182.5, 273.75, 365]
labels_occ = ['0-25%', '25-50%', '50-75%', '75-100%']
listing_file['occupancy_cluster'] = pd.cut(
    listing_file['estimated_occupancy_l365d'], 
    bins=bins_occ, 
    labels=labels_occ, 
    include_lowest=True
)

# G. Location column for Power BI Map and Superhost formatting
listing_file['location'] = listing_file['latitude'].astype(str) + ", " + listing_file['longitude'].astype(str)
listing_file['host_is_superhost'] = listing_file['host_is_superhost'].fillna('f').str.upper()

# H. Strings treatment and Neighbourhood correction 
cols_to_str = [
    "name", 
    "neighbourhood", 
    "neighbourhood_cleansed", 
    "room_type", 
    "property_type", 
    "location", 
    "stay_category", 
    "occupancy_cluster", 
    "host_response_time"
]
for col in cols_to_str:
    listing_file[col] = listing_file[col].astype(str).str.strip()

listing_file['neighbourhood_cleansed'] = listing_file['neighbourhood_cleansed'].replace(
    'Dn Laoghaire-Rathdown', 'Dun Laoghaire-Rathdown'
)

listing_file['host_is_superhost'] = listing_file['host_is_superhost'].replace(
    'F', 'No'
)

listing_file['host_is_superhost'] = listing_file['host_is_superhost'].replace(
    'T', 'Yes'
)

# I. Calculated columns
listing_file['max_revenue'] = listing_file["availability_365"] * listing_file["price"]
listing_file['estimated_revenue'] = listing_file["estimated_occupancy_l365d"] * listing_file["price"]

# --- 3. DATABASE LOADING ---
conn = sqlite3.connect(DB_PATH)

db_schema = {
    "id": "TEXT", 
    "price": "REAL", 
    "minimum_nights": "INTEGER", 
    "availability_365": "INTEGER", 
    "estimated_occupancy_l365d": "INTEGER",
    "occupancy_cluster": "TEXT",
    "max_revenue": "REAL",
    "estimated_revenue": "REAL"
}

listing_file.to_sql("listings", conn, if_exists="replace", index=False, dtype=db_schema)
dropped_items.to_sql("dropped_listings", conn, if_exists="replace", index=False)

conn.close()

# --- 4. EXPORTING FINAL FILES ---
listing_file.to_csv(OUTPUT_CSV, index=False, encoding='utf-8-sig')

print("-" * 30)
print("ETL Process completed successfully!")
print("-" * 30)
