import pandas as pd
import os

# Get the directory where generate_codebook.py is located
base_dir = os.path.dirname(os.path.abspath(__file__))
# Ensure the documentation folder exists
docs_dir = os.path.join(base_dir, 'documentation')
os.makedirs(docs_dir, exist_ok=True)
codebook_path = os.path.join(docs_dir, 'codebook.csv')

# Define the exact column headers required by the rubric (Section 6)
columns = [
    "variable name", "variable label", "definition", "data_type", "unit",
    "allowed values", "missing value", "source indicator code",
    "source indicator name", "source", "transformation", "notes"
]

# Define the metadata for each column in the curated_dataset.csv
codebook_data = [
    ["IndicatorCode", "Indicator Code", "Unique identifier for the health indicator", "String", "N/A", "HIV_0000000001, MALARIA_EST_INCIDENCE, TB_e_inc_num", "N/A", "Mixed", "Mixed", "WHO Global Health Observatory", "None", "Code assigned by WHO"],
    ["Indicator", "Indicator Name", "Full descriptive name of the health indicator", "String", "N/A", "Free text", "N/A", "Mixed", "Mixed", "WHO Global Health Observatory", "None", "Name assigned by WHO"],
    ["SpatialDimValueCode", "Country Code", "ISO 3166-1 alpha-3 country code", "String", "N/A", "Valid ISO-3 codes for Sub-Saharan Africa", "N/A", "N/A", "N/A", "WHO", "None", "Filtered to Sub-Saharan Africa"],
    ["Location", "Country Name", "Name of the country or territory", "String", "N/A", "Sub-Saharan African countries", "N/A", "N/A", "N/A", "WHO", "Filtered list", "Follows World Bank classification"],
    ["Period", "Year", "The year of the observation or estimate", "Integer", "Year", "2000-2025", "N/A", "N/A", "N/A", "WHO", "None", "Coverage varies by disease"],
    ["Dim1", "Disaggregation", "Sex or age group disaggregation if applicable", "String", "N/A", "Male, Female, Both sexes, specific age ranges", "N/A", "N/A", "N/A", "WHO", "None", "Not all indicators have disaggregations"],
    ["FactValueNumeric", "Numeric Value", "The central numeric value of the observation", "Decimal", "Varies (see FactValueUoM)", "Positive numbers", "NA", "Mixed", "Mixed", "WHO", "Replaced blanks with NA", "May be an estimate or reported count"],
    ["FactValueUoM", "Unit of Measure", "The unit corresponding to the numeric value", "String", "N/A", "Free text", "NA", "N/A", "N/A", "WHO", "None", "Often blank if the unit is implied by the indicator"],
    ["FactValueNumericLow", "Lower Bound", "Lower bound of the uncertainty interval", "Decimal", "Varies", "Positive numbers", "NA", "Mixed", "Mixed", "WHO", "Replaced blanks with NA", "Provided for modeled estimates"],
    ["FactValueNumericHigh", "Upper Bound", "Upper bound of the uncertainty interval", "Decimal", "Varies", "Positive numbers", "NA", "Mixed", "Mixed", "WHO", "Replaced blanks with NA", "Provided for modeled estimates"],
    ["Value", "Formatted Value", "String representation of the value including bounds", "String", "N/A", "Free text", "NA", "Mixed", "Mixed", "WHO", "None", "Useful for display purposes"],
    ["MetricType", "Metric Type", "Distinguishes between counts and rates", "String", "N/A", "Incidence Count, Incidence Rate", "N/A", "N/A", "N/A", "Derived", "Derived based on indicator", "Added to satisfy rubric requirement"],
    ["Denominator", "Rate Denominator", "The denominator used if the metric is a rate", "String", "N/A", "1000 population at risk, N/A", "N/A", "N/A", "N/A", "Derived", "Derived based on indicator", "Added to satisfy rubric requirement"]
]

# Create and save the dataframe
df_codebook = pd.DataFrame(codebook_data, columns=columns)
df_codebook.to_csv(codebook_path, index=False)
print(f"Codebook saved to {codebook_path}")
