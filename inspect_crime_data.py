import pandas as pd

# Load the crime dataset

df = pd.read_csv(
"sapacr-2005-2026-v1.5.csv",
decimal=","
)

# Display the first five records

print(df.head())

# Display the number of rows and columns

print("\nDataset shape:")
print(df.shape)

# Display all column names

print("\nColumn names:")
print(df.columns.tolist())

# Display information about the dataset

print("\nDataset information:")
df.info()

# 1. Check missing values in every column

print("\nMissing values by column:")

print(
df.isnull().sum()[df.isnull().sum() > 0]
)

# 2. Check the total number of duplicate rows

print("\nTotal duplicate rows:")

print(df.duplicated().sum())

# 3. Check duplicates using station and year

print("\nDuplicate station-year combinations:")

print(
df.duplicated(subset=["station", "year"]).sum()
)

# 4. Check missing values in our main crime categories

crime_columns = [
"burglary_nonres",
"burglary_res",
"robbery_nonres",
"robbery_res",
"aggr_robbery",
"common_robbery",
"bank_robbery",
"cash_transit_robbery"
]

print("\nMissing values in main crime categories:")

print(df[crime_columns].isnull().sum())


# Select the crime categories relevant to our project

crime_columns = [
"burglary_nonres",
"burglary_res",
"robbery_nonres",
"robbery_res",
"aggr_robbery",
"common_robbery",
"bank_robbery",
"cash_transit_robbery"
]

# Calculate the total for each crime category

crime_totals = df[crime_columns].sum().sort_values(ascending=False)

print("\nTotal reported crimes by category:")
print(crime_totals)

# Calculate total burglary counts

df["total_burglary"] = (
df["burglary_nonres"] + df["burglary_res"]
)

# Calculate total robbery counts for the selected categories

df["total_selected_robbery"] = df[
[
"robbery_nonres",
"robbery_res",
"aggr_robbery",
"common_robbery",
"bank_robbery",
"cash_transit_robbery"
]
].sum(axis=1)

# Display the overall totals

print("\nTotal reported burglaries:")
print(df["total_burglary"].sum())

print("\nTotal across selected robbery categories:")
print(df["total_selected_robbery"].sum())


# Group records by police station

station_burglary = (
df.groupby("station", as_index=False)["total_burglary"]
.sum()
.sort_values("total_burglary", ascending=False)
)

# Display the top 10 stations

print("\nTop 10 police stations by cumulative burglary counts:")
print(station_burglary.head(10).to_string(index=False))


# Group records by police station

station_robbery = (
df.groupby("station", as_index=False)["total_selected_robbery"]
.sum()
.sort_values("total_selected_robbery", ascending=False)
)

# Display the top 10 stations

print("\nTop 10 police stations by cumulative selected robbery counts:")
print(station_robbery.head(10).to_string(index=False))


# Check the geographical coordinates

print("Total records:", len(df))

print("Records with missing longitude:",
      df["longitude"].isna().sum())

print("Records with missing latitude:",
      df["latitude"].isna().sum())

# South Africa's approximate geographical boundaries
valid_coordinates = (
    df["longitude"].between(16, 33) &
    df["latitude"].between(-36, -22)
)

print("Records within approximate South African boundaries:",
      valid_coordinates.sum())

print("Records outside approximate boundaries:",
      (~valid_coordinates).sum())


# Create a copy containing records with valid coordinates

crime_map_df = df.dropna(
    subset=["longitude", "latitude"]
).copy()

# Keep coordinates within approximate South African boundaries
crime_map_df = crime_map_df[
    crime_map_df["longitude"].between(16, 33) &
    crime_map_df["latitude"].between(-36, -22)
].copy()

# Check the results
print("Original dataset:", df.shape)
print("Mapping dataset:", crime_map_df.shape)

print("\nMissing coordinates:")
print(crime_map_df[["longitude", "latitude"]].isna().sum())

print("\nSample mapping data:")
print(
    crime_map_df[
        ["year", "station", "longitude", "latitude"]
    ].head()
)

# Calculate total burglaries for each record

crime_map_df["total_burglary"] = (
    crime_map_df["burglary_res"] +
    crime_map_df["burglary_nonres"]
)

# Aggregate burglary counts by police station

station_burglary = (
    crime_map_df.groupby(
        ["station", "longitude", "latitude"],
        as_index=False
    )
    .agg(
        total_burglary=("total_burglary", "sum")
    )
    .sort_values(
        by="total_burglary",
        ascending=False
    )
)

# Display the 10 stations with the highest counts

print(station_burglary.head(10))



# Calculate total burglaries for each record
crime_map_df["total_burglary"] = (
    crime_map_df["burglary_res"] +
    crime_map_df["burglary_nonres"]
)

# Group burglary counts by police station and coordinates
station_burglary = (
    crime_map_df
    .groupby(
        ["station", "longitude", "latitude"],
        as_index=False
    )
    .agg(
        total_burglary=("total_burglary", "sum")
    )
    .sort_values(
        by="total_burglary",
        ascending=False
    )
)

# Display the top 10 stations
print(station_burglary.head(10))

# Check the number of unique station-coordinate combinations
print("\nTotal station-coordinate combinations:",
      len(station_burglary))


import pandas as pd
import folium

# 1. Load the crime dataset
df = pd.read_csv(
    "sapacr-2005-2026-v1.5.csv",
    decimal=","
)

print("Dataset loaded successfully!")
print("Original dataset shape:", df.shape)

# Check the available reporting years
print("\nAvailable reporting years:")
print(sorted(df["year"].dropna().unique()))

# 2. Keep records with valid geographical coordinates
crime_map_df = df.dropna(
    subset=["longitude", "latitude"]
).copy()

# Keep coordinates within approximate South African boundaries
crime_map_df = crime_map_df[
    crime_map_df["longitude"].between(16, 33)
    & crime_map_df["latitude"].between(-36, -22)
].copy()

print("Mapping dataset shape:", crime_map_df.shape)

# 3. Calculate total burglaries
crime_map_df["total_burglary"] = (
    crime_map_df["burglary_res"]
    + crime_map_df["burglary_nonres"]
)

# 4. Aggregate burglaries by station and coordinates
station_burglary = (
    crime_map_df
    .groupby(
        ["station", "longitude", "latitude"],
        as_index=False
    )
    .agg(
        total_burglary=("total_burglary", "sum")
    )
    .sort_values(
        "total_burglary",
        ascending=False
    )
)

print("Station-coordinate combinations:", len(station_burglary))

print("\nTop 10 stations by cumulative burglaries:")
print(station_burglary.head(10).to_string(index=False))

# 4A. Analyse burglaries for a selected reporting year

selected_year = "2024/2025"

year_df = crime_map_df[
    crime_map_df["year"] == selected_year
].copy()

# Combine residential and non-residential burglaries
year_df["total_burglary"] = (
    year_df["burglary_res"]
    + year_df["burglary_nonres"]
)

# Calculate total burglaries for each police station
year_burglary = (
    year_df
    .groupby(
        ["station", "longitude", "latitude"],
        as_index=False
    )
    .agg(
        total_burglary=("total_burglary", "sum")
    )
    .sort_values(
        "total_burglary",
        ascending=False
    )
)

print(f"\nTop 10 burglary stations for {selected_year}:")
print(year_burglary.head(10).to_string(index=False))

# Compare crime incidents across two reporting years

previous_year = "2023/2024"
current_year = selected_year

# Select records from both reporting years
comparison_df = crime_map_df[
    crime_map_df["year"].isin([previous_year, current_year])
].copy()

# Calculate burglary incidents
comparison_df["total_burglary"] = (
    comparison_df["burglary_res"]
    + comparison_df["burglary_nonres"]
)

# Calculate robbery incidents
robbery_columns = [
    "robbery_res",
    "robbery_nonres",
    "aggr_robbery",
    "common_robbery",
    "bank_robbery",
    "cash_transit_robbery"
]

comparison_df["total_robbery"] = (
    comparison_df[robbery_columns].sum(axis=1)
)

# Calculate combined incidents across the four categories
comparison_df["total_crime"] = (
    comparison_df["total_burglary"]
    + comparison_df["total_robbery"]
    + comparison_df["theft_from_vehicle"]
    + comparison_df["other_theft"]
)

# Summarise incidents by station and reporting year
comparison_totals = comparison_df.groupby(
    ["station", "longitude", "latitude", "year"],
    as_index=False
).agg(
    total_crime=("total_crime", "sum")
)

# Put both reporting years side by side
comparison_totals = comparison_totals.pivot_table(
    index=["station", "longitude", "latitude"],
    columns="year",
    values="total_crime",
    aggfunc="sum",
    fill_value=0
).reset_index()

# Ensure both years are available as columns
comparison_totals = comparison_totals.reindex(
    columns=[
        "station",
        "longitude",
        "latitude",
        previous_year,
        current_year
    ],
    fill_value=0
)

# Give the year columns clearer names
comparison_totals = comparison_totals.rename(columns={
    previous_year: "previous_year_total",
    current_year: "current_year_total"
})

# Calculate the change in recorded incidents
comparison_totals["incident_change"] = (
    comparison_totals["current_year_total"]
    - comparison_totals["previous_year_total"]
)

print("\nYEAR-ON-YEAR CRIME COMPARISON")
print("-----------------------------")
print(f"Previous year: {previous_year}")
print(f"Current year: {current_year}")

print("\nTop 10 stations with the largest increases:")
print(
    comparison_totals.sort_values(
        "incident_change",
        ascending=False
    )[
        [
            "station",
            "previous_year_total",
            "current_year_total",
            "incident_change"
        ]
    ].head(10).to_string(index=False)
)

# Display the stations with the largest decreases

print("\nTop 10 stations with the largest decreases:")
print(
    comparison_totals[
        comparison_totals["incident_change"] < 0
    ]
    .sort_values("incident_change", ascending=True)[
        [
            "station",
            "previous_year_total",
            "current_year_total",
            "incident_change"
        ]
    ]
    .head(10)
    .to_string(index=False)
)

# 4B. Calculate total robberies for the selected reporting year

robbery_columns = [
    "robbery_res",
    "robbery_nonres",
    "aggr_robbery",
    "common_robbery",
    "bank_robbery",
    "cash_transit_robbery"
]

# Filter records for the selected year
year_robbery_df = crime_map_df[
    crime_map_df["year"] == selected_year
].copy()

# Calculate total robberies
year_robbery_df["total_robbery"] = (
    year_robbery_df[robbery_columns].sum(axis=1)
)

# Aggregate robberies by station and coordinates
station_robbery = (
    year_robbery_df
    .groupby(
        ["station", "longitude", "latitude"],
        as_index=False
    )
    .agg(
        total_robbery=("total_robbery", "sum")
    )
    .sort_values(
        "total_robbery",
        ascending=False
    )
)

print(f"\nTop 10 robbery stations for {selected_year}:")
print(station_robbery.head(10).to_string(index=False))

# 4C. Calculate vehicle theft for the selected reporting year

year_vehicle_df = crime_map_df[
    crime_map_df["year"] == selected_year
].copy()

station_vehicle_theft = (
    year_vehicle_df
    .groupby(
        ["station", "longitude", "latitude"],
        as_index=False
    )
    .agg(
        total_vehicle_theft=("theft_from_vehicle", "sum")
    )
    .sort_values(
        "total_vehicle_theft",
        ascending=False
    )
)

print(f"\nTop 10 vehicle theft stations for {selected_year}:")
print(
    station_vehicle_theft.head(10).to_string(index=False)
)

# 4D. Calculate other theft for the selected reporting year

year_other_df = crime_map_df[
    crime_map_df["year"] == selected_year
].copy()

station_other_theft = (
    year_other_df
    .groupby(
        ["station", "longitude", "latitude"],
        as_index=False
    )
    .agg(
        total_other_theft=("other_theft", "sum")
    )
    .sort_values(
        "total_other_theft",
        ascending=False
    )
)

print(f"\nTop 10 other theft stations for {selected_year}:")
print(
    station_other_theft.head(10).to_string(index=False)
)

# Combine the four crime categories into one risk dataset

risk_df = year_burglary.merge(
station_robbery[
["station", "longitude", "latitude", "total_robbery"]
],
on=["station", "longitude", "latitude"],
how="outer"
)

risk_df = risk_df.merge(
station_vehicle_theft[
["station", "longitude", "latitude", "total_vehicle_theft"]
],
on=["station", "longitude", "latitude"],
how="outer"
)

risk_df = risk_df.merge(
station_other_theft[
["station", "longitude", "latitude", "total_other_theft"]
],
on=["station", "longitude", "latitude"],
how="outer"
)

# Replace missing crime totals with zero

crime_columns = [
"total_burglary",
"total_robbery",
"total_vehicle_theft",
"total_other_theft"
]

risk_df[crime_columns] = risk_df[crime_columns].fillna(0)

# Calculate combined recorded crime incidents

risk_df["total_crime"] = risk_df[crime_columns].sum(axis=1)


# Calculate crime category percentages

risk_df["burglary_percentage"] = (
risk_df["total_burglary"]
.div(risk_df["total_crime"].where(risk_df["total_crime"] != 0))
.mul(100)
.fillna(0)
)

risk_df["robbery_percentage"] = (
risk_df["total_robbery"]
.div(risk_df["total_crime"].where(risk_df["total_crime"] != 0))
.mul(100)
.fillna(0)
)

risk_df["vehicle_theft_percentage"] = (
risk_df["total_vehicle_theft"]
.div(risk_df["total_crime"].where(risk_df["total_crime"] != 0))
.mul(100)
.fillna(0)
)

risk_df["other_theft_percentage"] = (
risk_df["total_other_theft"]
.div(risk_df["total_crime"].where(risk_df["total_crime"] != 0))
.mul(100)
.fillna(0)
)


# Display the stations with the highest combined totals

print("\nTop 10 stations by combined crime incidents:")
print(
risk_df.sort_values("total_crime", ascending=False)[
["station", "total_crime"]
].head(10)
)

print("\nChecking crime percentage columns:")
print(risk_df[[
    "station",
    "burglary_percentage",
    "robbery_percentage",
    "vehicle_theft_percentage",
    "other_theft_percentage"
]].head())

# Calculate crime volume thresholds

medium_threshold = risk_df["total_crime"].quantile(0.50)
high_threshold = risk_df["total_crime"].quantile(0.80)

# Assign a relative risk category to each station

def classify_risk(total):
    if total <= medium_threshold:
        return "Low"
    elif total <= high_threshold:
        return "Medium"
    else:
        return "High"


risk_df["risk_level"] = risk_df["total_crime"].apply(classify_risk)

# Prepare crime risk summary statistics
total_stations = len(risk_df)

risk_counts = risk_df["risk_level"].value_counts()

low_risk_count = risk_counts.get("Low", 0)
medium_risk_count = risk_counts.get("Medium", 0)
high_risk_count = risk_counts.get("High", 0)

print("\nCrime Risk Summary")
print("------------------")
print(f"Reporting Year: {selected_year}")
print(f"Total Stations: {total_stations}")
print(f"Low Risk: {low_risk_count}")
print(f"Medium Risk: {medium_risk_count}")
print(f"High Risk: {high_risk_count}")

# Display the number of stations in each risk category

print("\nPolice stations by crime risk level:")
print(risk_df["risk_level"].value_counts())

# Display the 10 highest-crime stations and their risk levels

print("\nTop 10 stations with risk classifications:")
print(
risk_df.sort_values("total_crime", ascending=False)[
["station", "total_crime", "risk_level"]
].head(10)
)


# 5. Create a map centred on South Africa
crime_map = folium.Map(
    location=[-29.0, 24.0],
    zoom_start=5,
    tiles="CartoDB positron"
)

# Add a title to the map
title_html = f"""
<h3 align="center" style="font-size:20px">
<b>South African Crime Risk Map — {selected_year}</b>
</h3>
"""
crime_map.get_root().add_child(
    folium.Element(title_html)
)

# ==========================================
# CRIME TREND LAYER
# Comparing 2023/2024 with 2024/2025
# ==========================================

trend_layer = folium.FeatureGroup(
    name="Crime Trend: Year-on-Year Change",
    show=False
)

for _, row in comparison_totals.iterrows():

    previous_total = row["previous_year_total"]
    current_total = row["current_year_total"]
    change = row["incident_change"]

    # Classify the year-on-year trend

if previous_total == 0 and current_total > 0:
    marker_colour = "purple"
    trend_label = "Newly recorded / previous-year total was zero"

elif change > 0:
    marker_colour = "red"
    trend_label = "Increase in recorded incidents"

elif change < 0:
    marker_colour = "green"
    trend_label = "Decrease in recorded incidents"

else:
    marker_colour = "orange"
    trend_label = "No change in recorded incidents"

    # Calculate percentage change where meaningful
    if previous_total > 0:
        percentage_change = (
            (current_total - previous_total)
            / previous_total
        ) * 100

        percentage_text = f"{percentage_change:+.1f}%"

    else:
        percentage_text = "Not calculable (previous total was zero)"

    # Build the marker popup
    popup_text = (
        f"<h4>{row['station'].title()}</h4>"
        f"<b>Comparison:</b> {previous_year} vs {current_year}<br>"
        f"<b>Trend:</b> {trend_label}<br><hr>"
        f"<b>{previous_year} incidents:</b> "
        f"{previous_total:,.0f}<br>"
        f"<b>{current_year} incidents:</b> "
        f"{current_total:,.0f}<br>"
        f"<b>Incident change:</b> {change:+,.0f}<br>"
        f"<b>Percentage change:</b> {percentage_text}"
    )

    folium.CircleMarker(
        location=[row["latitude"], row["longitude"]],
        radius=max(4, min(12, abs(change) / 100)),
        color=marker_colour,
        fill=True,
        fill_color=marker_colour,
        fill_opacity=0.7,
        weight=1,
        popup=folium.Popup(popup_text, max_width=350),
        tooltip=(
            f"{row['station'].title()}: "
            f"{change:+,.0f} recorded incidents"
        )
    ).add_to(trend_layer)

trend_layer.add_to(crime_map)

# Investigate Makhaza's records in both reporting years

print("\nMAKHAZA DATA CHECK")
print("------------------")

makhaza_check = comparison_df[
    comparison_df["station"].str.lower().str.strip() == "makhaza"
]

print(
    makhaza_check[
        ["year", "station", "burglary_res", "burglary_nonres",
         "robbery_res", "robbery_nonres", "aggr_robbery",
         "common_robbery", "bank_robbery", "cash_transit_robbery",
         "theft_from_vehicle", "other_theft"]
    ].to_string(index=False)
)

# Crime Risk Summary panel

summary_html = f"""

<div style="
    position: fixed;
    top: 80px;
    left: 50px;
    width: 230px;
    background-color: white;
    border: 2px solid #555;
    border-radius: 8px;
    z-index: 9999;
    padding: 12px;
    font-size: 14px;
    box-shadow: 2px 2px 6px rgba(0,0,0,0.3);
">
    <h4 style="margin-top: 0; margin-bottom: 10px;">
        Crime Risk Summary
    </h4>

    <b>Reporting Year:</b> {selected_year}<br>
    <b>Stations Analysed:</b> {total_stations:,}<br>
    <hr style="margin: 8px 0;">

    <span style="color: green;">&#9679;</span>
    <b>Low Risk:</b> {low_risk_count:,}<br>

    <span style="color: orange;">&#9679;</span>
    <b>Medium Risk:</b> {medium_risk_count:,}<br>

    <span style="color: red;">&#9679;</span>
    <b>High Risk:</b> {high_risk_count:,}

</div>"""

crime_map.get_root().add_child(
    folium.Element(summary_html)
)


# 6. Create separate layers for different crime categories

# Burglaries layer
burglary_layer = folium.FeatureGroup(
    name="Residential and Non-Residential Burglaries",
    show=True
)

for _, row in year_burglary.iterrows():

    radius = max(
        4,
        min(row["total_burglary"] / 2000, 18)
    )

    popup_text = (
f"<b>Police Station:</b> {row['station'].title()}<br>"
f"<b>Reporting Year:</b> {selected_year}<br>"
f"<b>Total Burglaries:</b> {row['total_burglary']:,}"
)

    folium.CircleMarker(
        location=[row["latitude"], row["longitude"]],
        radius=max(4, min(15, row["total_burglary"] / 100)),
        color="darkred",
        fill=True,
        fill_color="red",
        fill_opacity=0.6,
        weight=1,
        tooltip=row["station"].title(),
        popup=folium.Popup(popup_text, max_width=300)
    ).add_to(burglary_layer)

burglary_layer.add_to(crime_map)


# Robberies layer
robbery_layer = folium.FeatureGroup(
    name="Robberies",
    show=False
)

for _, row in station_robbery.iterrows():

    radius = max(4, min(15, row["total_robbery"] / 200))

    popup_text = (
f"<b>Police Station:</b> {row['station'].title()}<br>"
f"<b>Reporting Year:</b> {selected_year}<br>"
f"<b>Total Robberies:</b> {row['total_robbery']:,}"
)


    folium.CircleMarker(
        location=[row["latitude"], row["longitude"]],
        radius=radius,
        color="darkblue",
        fill=True,
        fill_color="blue",
        fill_opacity=0.6,
        weight=1,
        tooltip=row["station"].title(),
        popup=folium.Popup(popup_text, max_width=300)
    ).add_to(robbery_layer)

robbery_layer.add_to(crime_map)


#7 Theft from Vehicles layer
vehicle_theft_layer = folium.FeatureGroup(
    name="Theft from Vehicles",
    show=False
)

for _, row in station_vehicle_theft.iterrows():

    radius = max(4, min(15, row["total_vehicle_theft"] / 200))

    popup_text = (
        f"<b>Police Station:</b> {row['station'].title()}<br>"
        f"<b>Reporting Year:</b> {selected_year}<br>"
        f"<b>Total Vehicle Thefts:</b> {row['total_vehicle_theft']:,}"
    )

    folium.CircleMarker(
        location=[
            row["latitude"],
            row["longitude"]
        ],
        radius=radius,
        color="darkgreen",
        fill=True,
        fill_color="green",
        fill_opacity=0.6,
        weight=1,
        tooltip=row["station"].title(),
        popup=folium.Popup(
            popup_text,
            max_width=300
        )
    ).add_to(vehicle_theft_layer)

vehicle_theft_layer.add_to(crime_map)


# Other Theft layer
other_theft_layer = folium.FeatureGroup(
    name="Other Theft",
    show=False
)

for _, row in station_other_theft.iterrows():

    radius = max(4, min(15, row["total_other_theft"] / 300))

    popup_text = (
f"<b>Police Station:</b> {row['station'].title()}<br>"
f"<b>Reporting Year:</b> {selected_year}<br>"
f"<b>Total Other Thefts:</b> {row['total_other_theft']:,}"
)


    folium.CircleMarker(
        location=[
            row["latitude"],
            row["longitude"]
        ],
        radius=radius,
        color="purple",
        fill=True,
        fill_color="purple",
        fill_opacity=0.6,
        weight=1,
        tooltip=row["station"].title(),
        popup=folium.Popup(
            popup_text,
            max_width=300
        )
    ).add_to(other_theft_layer)

other_theft_layer.add_to(crime_map)

# Crime Risk Classification layer

risk_layer = folium.FeatureGroup(
name="Crime Risk Classification",
show=False
)

# Assign a colour to each risk category

risk_colors = {
    "Low": "green",
    "Medium": "orange",
    "High": "red"
}

for _, row in risk_df.iterrows():
    risk_color = risk_colors[row["risk_level"]]

    popup_text = (
f"<h4 style='margin-bottom:8px;'>{row['station'].title()}</h4>"
f"<b>Reporting Year:</b> {selected_year}<br>"
f"<b>Risk Level:</b> {row['risk_level']}<hr>"
f"<b>Residential & Non-residential Burglary:</b> "
f"{row['total_burglary']:,.0f} "
f"({row['burglary_percentage']:.1f}%)<br>"
f"<b>Robbery:</b> {row['total_robbery']:,.0f} "
f"({row['robbery_percentage']:.1f}%)<br>"
f"<b>Theft from Vehicles:</b> "
f"{row['total_vehicle_theft']:,.0f} "
f"({row['vehicle_theft_percentage']:.1f}%)<br>"
f"<b>Other Theft:</b> {row['total_other_theft']:,.0f} "
f"({row['other_theft_percentage']:.1f}%)<hr>"
f"<b>Combined Recorded Incidents:</b> "
f"{row['total_crime']:,.0f}"
)

    folium.CircleMarker(
        location=[
            row["latitude"],
            row["longitude"]
        ],
        radius=6,
        color=risk_color,
        fill=True,
        fill_color=risk_color,
        fill_opacity=0.7,
        weight=1,
        tooltip=f"{row['station'].title()} - {row['risk_level']} Risk",
        popup=folium.Popup(
            popup_text,
            max_width=300
        )
    ).add_to(risk_layer)

risk_layer.add_to(crime_map)


# 8. Add the layer selector
folium.LayerControl(
    collapsed=False
).add_to(crime_map)

# 9. Save the interactive map
output_file = "south_africa_crime_map.html"

crime_map.save(output_file)

print(f"\nInteractive crime map saved as: {output_file}")
print("Open the HTML file in your browser to explore the map.")


