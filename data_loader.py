import pandas as pd
import os
from typing import Dict, List, Tuple
import warnings

warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl')

# Industry mapping from sheet names to full names
INDUSTRY_MAPPING = {
    'T4': 'All Industries',
    'T4.1': 'Manufacturing',
    'T4.2': 'Construction',
    'T4.3': 'Wholesale and Retail Trade',
    'T4.4': 'Transportation and Storage',
    'T4.5': 'Accommodation and Food Services',
    'T4.6': 'Information and Communications',
    'T4.7': 'Financial and Insurance Services',
    'T4.8': 'Real Estate Services',
    'T4.9': 'Professional Services',
    'T4.10': 'Administrative and Support Services',
    'T4.11': 'Public Administration and Education',
    'T4.12': 'Health and Social Services',
    'T4.13': 'Arts, Entertainment and Recreation',
    'T4.14': 'Other Community, Social and Personal Services'
}

def load_excel_file(filepath: str) -> Dict[str, pd.DataFrame]:
    """Load all sheets from an Excel file."""
    xl = pd.ExcelFile(filepath)
    sheets = {}
    
    for sheet_name in xl.sheet_names:
        if sheet_name.startswith('T4'):
            try:
                df = pd.read_excel(filepath, sheet_name=sheet_name, header=None)
                sheets[sheet_name] = df
            except Exception as e:
                print(f"Error reading sheet {sheet_name}: {e}")
    
    return sheets

def find_data_start_row(df: pd.DataFrame) -> int:
    """Find the row where actual data starts (after headers)."""
    for idx, row in df.iterrows():
        # Look for the first row with a numeric value in column 0 (row number)
        # and valid occupation data in column 2
        if pd.notna(row.iloc[0]) and pd.notna(row.iloc[2]):
            try:
                # Check if first column is numeric (row number)
                float(row.iloc[0])
                # Check if it's not a header row
                if 'Occupation' not in str(row.iloc[2]) and 'MANAGERS' not in str(row.iloc[2]):
                    return idx
            except:
                continue
    return -1

def clean_wage_value(value):
    """Clean wage values, converting 's' (suppressed) to None."""
    if pd.isna(value) or value == 's' or str(value).strip() == 's':
        return None
    try:
        return float(value)
    except:
        return None

def process_sheet(df: pd.DataFrame, year: int, industry: str) -> pd.DataFrame:
    """Process a single sheet and extract wage data."""
    # Find where data starts
    data_start = find_data_start_row(df)
    if data_start == -1:
        return pd.DataFrame()
    
    # Extract data rows
    data_rows = []
    
    for idx in range(data_start, len(df)):
        row = df.iloc[idx]
        
        # Skip if no occupation name
        if pd.isna(row.iloc[2]):
            continue
            
        # Skip section headers (e.g., "MANAGERS", "PROFESSIONALS")
        occupation = str(row.iloc[2]).strip()
        if occupation.isupper() and len(occupation.split()) <= 3:
            continue
        
        # Extract data
        try:
            data_rows.append({
                'Year': year,
                'Industry': industry,
                'SSOC_Code': str(row.iloc[1]) if pd.notna(row.iloc[1]) else '',
                'Occupation': occupation,
                'Basic_P25': clean_wage_value(row.iloc[3]),
                'Basic_Median': clean_wage_value(row.iloc[4]),
                'Basic_P75': clean_wage_value(row.iloc[5]),
                'Gross_P25': clean_wage_value(row.iloc[6]),
                'Gross_Median': clean_wage_value(row.iloc[7]),
                'Gross_P75': clean_wage_value(row.iloc[8])
            })
        except Exception as e:
            continue
    
    return pd.DataFrame(data_rows)

def load_all_wage_data() -> pd.DataFrame:
    """Load and combine wage data from all Excel files."""
    all_data = []
    
    # Get all Excel files in current directory
    excel_files = [f for f in os.listdir('.') if f.endswith('.xlsx') and 'monthly basic and gross wages' in f]
    
    for filepath in excel_files:
        # Extract year from filename
        year = None
        for y in ['2021', '2022', '2023', '2024']:
            if y in filepath:
                year = int(y)
                break
        
        if not year:
            continue
        
        print(f"Loading data from {filepath}...")
        sheets = load_excel_file(filepath)
        
        # Process each sheet
        for sheet_name, df in sheets.items():
            if sheet_name in INDUSTRY_MAPPING:
                industry = INDUSTRY_MAPPING[sheet_name]
                sheet_data = process_sheet(df, year, industry)
                if not sheet_data.empty:
                    all_data.append(sheet_data)
    
    # Combine all data
    if all_data:
        combined_df = pd.concat(all_data, ignore_index=True)
        
        # Remove duplicates if any
        combined_df = combined_df.drop_duplicates(subset=['Year', 'Industry', 'Occupation'])
        
        # Sort by Year, Industry, Occupation
        combined_df = combined_df.sort_values(['Year', 'Industry', 'Occupation'])
        
        return combined_df
    else:
        return pd.DataFrame()

def get_unique_occupations(df: pd.DataFrame) -> List[str]:
    """Get sorted list of unique occupations."""
    return sorted(df['Occupation'].unique())

def get_industries() -> List[str]:
    """Get list of all industries."""
    return list(INDUSTRY_MAPPING.values())

def filter_data(df: pd.DataFrame, occupation: str, industry: str) -> pd.DataFrame:
    """Filter data for specific occupation and industry."""
    # Case-insensitive matching
    mask = (df['Occupation'].str.lower() == occupation.lower()) & \
           (df['Industry'] == industry)
    return df[mask].sort_values('Year')

if __name__ == "__main__":
    # Test the data loader
    print("Loading wage data...")
    df = load_all_wage_data()
    print(f"Loaded {len(df)} records")
    print(f"Years: {sorted(df['Year'].unique())}")
    print(f"Industries: {len(df['Industry'].unique())}")
    print(f"Occupations: {len(df['Occupation'].unique())}")