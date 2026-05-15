import pandas as pd
import io
import re

def transform_data(input_buffer, file_name):
    """Applies transformations via Pandas and returns a new safe buffer."""
    
    if not (file_name.endswith('.csv') or file_name.endswith('.xlsx')):
        return input_buffer

    # Load data
    if file_name.endswith('.csv'):
        try:
            df = pd.read_csv(input_buffer, encoding='utf-8')
        except UnicodeDecodeError:
            input_buffer.seek(0)
            df = pd.read_csv(input_buffer, encoding='latin1', sep=None, engine='python')
    else:
        df = pd.read_excel(input_buffer)

    df = df.reset_index(drop=True)

    # Clean spaces and special symbols
    regex_clean = r'[^\w\s\-\+\,]'
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].astype(str).str.strip()
            df[col] = df[col].str.replace(regex_clean, '', regex=True)
            df[col] = df[col].replace(['nan', 'None', '0.0', '0'], '')

    # Standardize Names
    if 'Name' in df.columns:
        df['Name'] = df['Name'].str.title()

    # Clean Doctor column
    if 'Doctor' in df.columns:
        titles_regex = r'\b(Dr|Dr\.|Miss|MD|Mrs|Mr|PhD|Dra|Dra\.)\b'
        df['Doctor'] = df['Doctor'].str.replace(titles_regex, '', regex=True, flags=re.IGNORECASE)
        df['Doctor'] = df['Doctor'].str.strip().str.title()

    # Create Record_ID
    if 'Year' in df.columns:
        df['Record_ID'] = [f"{i+1}_{year}" for i, year in enumerate(df['Year'])]
        cols = ['Record_ID'] + [c for c in df.columns if c != 'Record_ID']
        df = df[cols]

    # Ensure numeric columns
    if 'Billing Amount' in df.columns:
        df['Billing Amount'] = df['Billing Amount'].astype(str).str.replace(',', '.', regex=False)
        df['Billing Amount'] = pd.to_numeric(df['Billing Amount'], errors='coerce').fillna(0.0)
    
    if 'Age' in df.columns:
        df['Age'] = pd.to_numeric(df['Age'], errors='coerce').fillna(0).astype(int)

    # Date Processing
    date_columns = ['Date of Admission', 'Discharge Date']
    for col in date_columns:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce')
            df[col] = df[col].dt.strftime('%Y-%m-%d')

    output_buffer = io.BytesIO()
    if file_name.endswith('.csv'):
        df.to_csv(output_buffer, index=False, encoding='utf-8', decimal='.')
    else:
        df.to_excel(output_buffer, index=False, engine='openpyxl')
    
    output_buffer.seek(0)
    return output_buffer