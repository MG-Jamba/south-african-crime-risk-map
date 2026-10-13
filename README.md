# South African Crime Risk Map

## Project Overview

The South African Crime Risk Map is an interactive Python data analytics project that visualises recorded crime incidents across South African police stations.

The project explores geographic crime patterns, compares crime categories, and highlights changes in recorded incidents over time. It demonstrates how Python can transform crime statistics into an interactive map that may support exploratory analysis for retailers, insurers, and other organisations.

## Project Objectives

- Visualise recorded crime incidents by police station.
- Explore burglary, robbery, vehicle theft, and other theft.
- Group police stations into relative crime-risk categories.
- Compare recorded crime totals between reporting years.
- Highlight police stations where recorded incidents have increased or decreased.

## Interactive Map Features

The map includes:

- **Burglary layer:** Displays recorded burglary incidents.
- **Robbery layer:** Displays recorded robbery incidents.
- **Vehicle theft layer:** Displays recorded theft from vehicles.
- **Other theft layer:** Displays other recorded theft incidents.
- **Crime risk classification:** Groups stations into relative Low, Medium, and High categories.
- **Crime trend layer:** Compares recorded incidents for 2023/2024 and 2024/2025.
- **Interactive popups:** Show crime totals, category breakdowns, and percentages.
- **Summary panel:** Displays the reporting year, station count, and risk-category totals.

## Technologies Used

- Python
- Pandas
- Folium
- HTML
- Visual Studio Code
- Git and GitHub

## Dataset

The project uses the dataset:

`sapacr-2005-2026-v1.5.csv`

The dataset contains South African police-station crime statistics, including reporting years, station names, geographic coordinates, and recorded crime categories.

The Python script processes the data and uses available geographic coordinates to prepare the records for mapping.

**Data attribution:** The original dataset source and its applicable licence or terms of use should be acknowledged before the data is redistributed. If redistribution is not permitted, obtain the dataset directly from its original source.

## How to Run the Project

### 1. Install Python

Install Python if it is not already available on your computer.

### 2. Install the required libraries

Open a terminal in the project folder and run:

```bash
python -m pip install pandas folium
```

### 3. Prepare the dataset

Place `sapacr-2005-2026-v1.5.csv` in the same folder as `inspect_crime_data.py`.

### 4. Generate the interactive map

Run:

```bash
python inspect_crime_data.py
```

The script generates or updates:

`south_africa_crime_map.html`

### 5. Open the map

Open `south_africa_crime_map.html` in a web browser to explore the interactive map.

## Understanding the Risk Categories

The Low, Medium, and High categories represent relative classifications based on recorded incident totals in the analysed dataset.

They are **not official South African Police Service risk ratings** and are not adjusted for population, business activity, visitor numbers, or other exposure factors.

Recorded incident totals alone cannot establish the actual probability of crime affecting a particular person or business.

## Understanding Crime Trends

The trend layer compares recorded crime totals for 2023/2024 and 2024/2025.

It highlights increases and decreases in recorded incidents. When the previous year's total is zero, a conventional percentage change cannot be calculated.

Changes in recorded incidents may reflect changes in crime, reporting behaviour, data coverage, classification, or recording practices. An increase should not automatically be interpreted as proof that actual crime risk has increased.

## Potential Applications

The project demonstrates how geographic crime data could support exploratory analysis for:

- Retail store-location research.
- Insurance risk assessment.
- Geographic crime-pattern analysis.
- Year-on-year crime monitoring.
- Data-driven decision support.

The map is an exploratory analytics tool, not a validated insurance-pricing model or a substitute for a comprehensive security assessment.

## Limitations

- The analysis relies on recorded crime statistics.
- Results depend on the completeness and quality of the source data.
- Risk categories are relative and do not account for population or exposure.
- Geographic results depend on the availability and accuracy of station coordinates.
- Observed changes do not establish the causes of changes in crime.

## Future Improvements

Potential extensions include:

- Adding population-adjusted crime rates.
- Developing a complementary Power BI dashboard.
- Investigating crime trends using suitable statistical or machine-learning methods.
- Automating data processing and map generation.

## Author

Developed as a practical Python data analytics portfolio project focused on South African crime statistics.

## Citation

**South African Police Service.** South African Police Service Annual Crime Records 2005-2026 [dataset]. Version 1.5. Pretoria: South African Police Service (SAPS) [producers], 2026. Pretoria: DataFirst [distributor], 2026. DOI: [https://doi.org/10.25828/5MAW-4H90](https://doi.org/10.25828/5MAW-4H90)

You can also copy and paste the citation in BibTex to your LaTeX script if you are using LaTeX.

```bibtex
@dataset{sapsacr-2026-v1.5,
  author       = {{South African Police Service}},
  title        = {South African Police Service Annual Crime Records 2005-2026},
  year         = {2026},
  version      = {1.5},
  publisher    = {DataFirst},
  address      = {Pretoria},
  note         = {Produced by South African Police Service (SAPS), Pretoria},
  doi          = {10.25828/5MAW-4H90},
  url          = {https://doi.org/10.25828/5MAW-4H90}
}
```
