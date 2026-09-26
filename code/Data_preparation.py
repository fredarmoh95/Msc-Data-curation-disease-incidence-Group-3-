import pandas as pd
import os

# Exact paths to your downloaded WHO data
raw_files = [
    r'C:\Users\antwi\OneDrive\Desktop\jones work\group 3\HIV.xlsx', 
    r'C:\Users\antwi\OneDrive\Desktop\jones work\group 3\Malaria.xlsx', 
    r'C:\Users\antwi\OneDrive\Desktop\jones work\group 3\TUBERCULOSIS.xlsx'
]

# Set the output path to save the cleaned CSV in the same folder
processed_path = r'C:\Users\antwi\OneDrive\Desktop\jones work\group 3\curated_dataset.csv'

# Authoritative Classification: World Bank Sub-Saharan Africa Region (Countries only)
ssa_countries = [
    "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cabo Verde", "Cameroon", 
    "Central African Republic", "Chad", "Comoros", "Congo", "Côte d'Ivoire", 
    "Democratic Republic of the Congo", "Equatorial Guinea", "Eritrea", "Eswatini", 
    "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", 
    "Lesotho", "Liberia", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", 
    "Mozambique", "Namibia", "Niger", "Nigeria", "Rwanda", "Sao Tome and Principe", 
    "Senegal", "Seychelles", "Sierra Leone", "Somalia", "South Africa", "South Sudan", 
    "Togo", "Uganda", "United Republic of Tanzania", "Zambia", "Zimbabwe"
]

# Required columns to retain based on rubric guidelines
cols_to_keep = [
    'IndicatorCode', 'Indicator', 'SpatialDimValueCode', 'Location', 
    'Period', 'Dim1', 'FactValueNumeric', 'FactValueUoM', 
    'FactValueNumericLow', 'FactValueNumericHigh', 'Value'
]

df_list = []

for file in raw_files:
    if os.path.exists(file):
        # The WHO exports contain metadata in the first two rows; skiprows=2 sets headers correctly
        df = pd.read_excel(file, skiprows=2)
        
        # Filter for Sub-Saharan African countries only
        df_filtered = df[df['Location'].isin(ssa_countries)].copy()
        
        # Retain only relevant columns to keep the curated dataset clean
        available_cols = [c for c in cols_to_keep if c in df_filtered.columns]
        df_filtered = df_filtered[available_cols]
        
        # Flag whether the values are counts vs rates based on the indicator
        if 'HIV' in file or 'TUBERCULOSIS' in file:
            df_filtered['MetricType'] = 'Incidence Count'
            df_filtered['Denominator'] = 'N/A'
        else:
            df_filtered['MetricType'] = 'Incidence Rate'
            df_filtered['Denominator'] = '1000 population at risk'
            
        df_list.append(df_filtered)
    else:
        print(f"Warning: Could not find {file}")

# Merge into a single longitudinal dataset
curated_df = pd.concat(df_list, ignore_index=True)

# Distinguish missing observations from zero values explicitly
curated_df.fillna({'FactValueNumeric': 'NA', 'FactValueNumericLow': 'NA', 'FactValueNumericHigh': 'NA'}, inplace=True)

# Export as non-proprietary CSV
os.makedirs(os.path.dirname(processed_path), exist_ok=True)
curated_df.to_csv(processed_path, index=False)
print(f"Curated dataset saved to {processed_path}")
