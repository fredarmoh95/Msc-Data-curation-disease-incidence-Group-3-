# Curated Sub-Saharan Africa Disease Incidence Dataset

**Description:** This repository contains a curated, longitudinal dataset of disease incidence covering HIV, Malaria, and Tuberculosis across Sub-Saharan African countries from 2000 to 2025. 
**Purpose:** The primary research and reuse purpose of this curated dataset is to provide a reliable, harmonized foundation for data-driven disease burden monitoring, epidemiological forecasting, and predictive modeling within the region.

## Group 3 Members
* **Frederick Armoh (SE/DMD/25/0009):** Data Engineer / Processing Pipeline
* **Bright Takyi (SE/DMD/25/0010):** Variable Analyst / Codebook Generation
* **Frank Annan (SE/DMD/25/0011):** DDI Metadata Curator 
* **Joseph Ennibil (SE/DMD/25/0012):** Discovery Metadata & Legal Documentation
* **Jones Kwasi Makafui Agbemaka (SE/DMD/25/0013):** Project Manager / Provenance & Release

## Data Provenance
* **Original Data Provider:** World Health Organization (WHO) Global Health Observatory (GHO)
* **Portal Link:** [https://www.who.int/data/gho](https://www.who.int/data/gho?utm_source=copilot.com)
* **Source Datasets:** 
  * Estimated number of people (all ages) living with HIV
  * Estimated malaria incidence (per 1000 population at risk)
  * Number of incident tuberculosis cases
* **Date of Retrieval:** September 24, 2026
* **Original Filenames:** `HIV.xlsx`, `Malaria.xlsx`, `TUBERCULOSIS.xlsx`

## Scope & Coverage
* **Geographic Scope:** Sub-Saharan Africa. 
* **Country-Selection Rule:** Selection is strictly based on the World Bank's regional classification for Sub-Saharan Africa. Non-sovereign entities and regional aggregates were explicitly excluded to maintain sovereign country-level analysis.
* **Country List (47):** Angola, Benin, Botswana, Burkina Faso, Burundi, Cabo Verde, Cameroon, Central African Republic, Chad, Comoros, Congo, Côte d'Ivoire, Democratic Republic of the Congo, Equatorial Guinea, Eritrea, Eswatini, Ethiopia, Gabon, Gambia, Ghana, Guinea, Guinea-Bissau, Kenya, Lesotho, Liberia, Madagascar, Malawi, Mali, Mauritania, Mauritius, Mozambique, Namibia, Niger, Nigeria, Rwanda, Sao Tome and Principe, Senegal, Seychelles, Sierra Leone, Somalia, South Africa, South Sudan, Togo, Uganda, United Republic of Tanzania, Zambia, Zimbabwe.
* **Temporal Scope:** 2000 to 2025.
* **Unit of Observation:** Country-Year.
* **Indicators Included:** HIV incidence counts, Malaria incidence rates (per 1000 at risk), Tuberculosis incident cases.

## Repository Structure
* `data/raw/`: Contains the unmodified original `.xlsx` downloads from the WHO GHO.
* `data/processed/`: Contains the final cleaned dataset (`curated_dataset.csv`).
* `code/`: Contains the Python scripts used for data preparation (`data_preparation.py`).
* `documentation/`: Contains the variable-level `codebook.csv` and the `processing_log.md`.
* `metadata/`: Contains the `dublin-core.jsonld` and `ddi-codebook.xml` files.

## Methodology & Processing
* **Acquisition:** Data was located via the WHO Global Health Observatory portal, filtered by indicator and location type (Country), and downloaded directly as Excel workbooks.
* **Processing Steps:** Using a custom Python script, the first two descriptive header rows of the WHO files were skipped during import. The datasets were merged and strictly filtered against the 47 World Bank Sub-Saharan African countries.
* **Validation & Cleaning:** New derived variables (`MetricType` and `Denominator`) were added to explicitly distinguish raw incidence counts from incidence rates. Columns with high sparsity that did not align with the core indicators were dropped.
* **Software Used:** Python 3, Pandas (via `pd.read_excel` and `pd.concat`).

## Data Quality & Limitations
* **Missing-Data Conventions:** Empty numeric observations (e.g., missing uncertainty bounds) were explicitly converted to the string `"NA"` to distinguish missing data from true zero values.
* **Limitations & Comparability:** The dataset merges reported counts with modeled estimates. Users should consult the `FactValueNumericLow` and `FactValueNumericHigh` uncertainty bounds when comparing modeled estimates (like Malaria rates) against direct incidence counts.

## Licensing & Citation
* **Licensing:** The curation scripts, metadata, and repository structure are provided under the open MIT License. The source data remains subject to the World Health Organization's terms of use and open access policies. 
* **Suggested Citation:** Group 3 Research Team (2026). *Longitudinal Disease Incidence in Sub-Saharan Africa: Curated Indicators for HIV, Malaria, and Tuberculosis*. Version 1.0. University of Cape Coast. Repository: https://github.com/fredarmoh95/Msc-Data-curation-disease-incidence-Group-3-

---

## Reproducibility & Metadata Examples
**Reproduction Instructions:** 
To reconstruct the processed CSV, download the raw indicators from the [WHO Global Health Observatory](https://www.who.int/data/gho?utm_source=copilot.com). Save the unmodified Excel workbooks in `data/raw/`. Execute `code/data_preparation.py` using Python to merge the sets, filter the 47 Sub-Saharan countries, and standardize the metrics.

**Dublin Core Metadata Example (`metadata/dublin-core.jsonld`):**
```json
"dcterms:title": "Longitudinal Disease Incidence in Sub-Saharan Africa: Curated Indicators for HIV, Malaria, and Tuberculosis (2000–2025)",
"dcterms:format": "text/csv"
