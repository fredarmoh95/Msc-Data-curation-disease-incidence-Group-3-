# Data Processing and Provenance Log

## 1. Source Identification & Retrieval
* **Data Provider:** World Health Organization (WHO).
* **Portal / Landing Page:** [WHO Global Health Observatory](https://www.who.int/data/gho?utm_source=copilot.com)[cite: 1].
* **Retrieval Date:** September 24, 2026.
* **Raw Files in `data/raw/`:**
  * `HIV.xlsx` (Indicator: Estimated number of people living with HIV, all ages)[cite: 1].
  * `Malaria.xlsx` (Indicator: Estimated malaria incidence per 1,000 population at risk)[cite: 1].
  * `TUBERCULOSIS.xlsx` (Indicator: Number of incident tuberculosis cases)[cite: 1].

## 2. Scope & Inclusion Criteria
* **Geographic Boundary:** Sub-Saharan Africa defined strictly using the World Bank regional classification[cite: 1].
* **Exclusions:** Regional aggregates (e.g., "Africa", "Global") were removed to prevent distortion and ensure unit uniformity at the sovereign country level[cite: 1].
* **Temporal Window:** 2000–2025 (covering 25+ consecutive years)[cite: 1].

## 3. Data Transformation & Cleaning
* **Header Normalization:** First two descriptive rows in the raw WHO files were skipped to set column names correctly.
* **Column Retention:** Preserved standard keys (`IndicatorCode`, `SpatialDimValueCode`, `Location`, `Period`, `Dim1`, `FactValueNumeric`, `FactValueUoM`, `FactValueNumericLow`, `FactValueNumericHigh`, `Value`)[cite: 1].
* **Metric Standardization:**
  * Added `MetricType` to explicitly distinguish counts from rates[cite: 1].
  * Added `Denominator` to document rate units (e.g., `1000 population at risk` for Malaria; `N/A` for counts)[cite: 1].
* **Missing Value Handling:** Missing numeric values were converted to explicit `NA` strings to prevent confusion with true zero values[cite: 1].

## 4. Quality Control Verification
* **Duplicate Checks:** Evaluated unique country-year-indicator composite keys to ensure no duplicated reporting entries exist.
* **Boundary Validation:** Verified that uncertainty intervals satisfy $\text{FactValueNumericLow} \le \text{FactValueNumeric} \le \text{FactValueNumericHigh}$.
* **Export:** Output generated as RFC 4180-compliant CSV at `data/processed/curated_dataset.csv`[cite: 1].
