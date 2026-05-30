"""
Task 7 — Visualization
 
Contents:
    Chart 1  — Daily rides time series by city          → output/01_time_series.png
    Chart 1b — Rides by day of the week                 → output/01b_rides_day_of_the_week.png
    Chart 2  — Duration distribution by city            → output/02_durations_distribution.png
    Chart 3  — Rides by time slot and bike type         → output/03_time_slots.png
    Chart 4  — Scatter duration vs speed + trend line   → output/04_scatter_duration_speed.png
    Chart 5  — Summary dashboard (2x2)                  → output/05_dashboard.png
 
VeloCittà Palette:
    Milan   #3DBFB8  teal
    Rome    #F5C842  yellow
    Turin   #5B8DB8  blue
    neutral teal / blue / dark green (#2E8B57)
    trend   #F5C842  yellow (contrast on scatter)
"""

import os
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import pandas as pd
import numpy as np

# import cleaned DataFrames from task6
from task6_pandas import df_rides, df_bike, df_users, df_merged
 
# -- [output folder] --
os.makedirs("output", exist_ok=True)
 
# -- [palette] --
CITY_COLORS = {
    "Milan": "#3DBFB8",
    "Rome":  "#F5C842",
    "Turin": "#5B8DB8",
}
NEUTRAL_COLORS = ["#3DBFB8", "#5B8DB8", "#2E8B57"]
TREND_COLOR    = "#F5C842"

# -- [global style] --
# rcParams: uniform font size and title weight across all charts
sns.set_style("white")              # white background, no grid
plt.rcParams.update({
    "figure.figsize":    (10, 6),
    "font.size":         11,
    "axes.titlesize":    13,
    "axes.titleweight":  "bold",
    "axes.labelweight":  "bold",
    "axes.spines.top":   False,
    "axes.spines.right": False,})

# [ CHART 1 ] — daily rides time series by city
# ↘ business question: how is service usage distributed over time across
#                      the three cities? Are there weekly peaks or patterns?

# -- [aggregate rides by date and city] --
time_series = (
    df_rides
    .groupby(["ride_date", "city"])["ride_id"]
    .count()
    .reset_index()
    .rename(columns={"ride_id": "n_rides"}))
time_series["day"] = time_series["ride_date"].dt.day
 
# -- [figure] --
fig, ax = plt.subplots()
 
for city, color in CITY_COLORS.items():
    data = time_series[time_series["city"] == city].sort_values("ride_date")
    ax.plot(data["day"], data["n_rides"],
            label=city, color=color,
            linewidth=2, marker="o", markersize=4)
 
ax.set_title("Daily rides by city")
ax.set_xticks(range(1, 16))         # one tick per day (1–15)
ax.set_xlabel("Day (May 2026)")
ax.set_ylabel("Number of rides")
ax.legend(title="City", frameon=False)
ax.yaxis.set_major_locator(mticker.MaxNLocator(integer=True))
 
fig.tight_layout()
fig.savefig("output/01_time_series.png", dpi=150)
plt.close(fig)
print("✓ Chart 1 saved")

# [ CHART 1b ] — rides aggregated by day of the week
# ↘ business question: which weekdays show the highest usage per city?

# --[rides aggregated by day of the week and city]--
day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
 
agg_weekday = (
    df_rides
    .groupby(["weekday", "city"])["ride_id"]
    .count()
    .reset_index()
    .rename(columns={"ride_id": "n_rides"}))
 
# convert to Categorical with fixed order — prevents alphabetical sorting
agg_weekday["weekday"] = pd.Categorical(
    agg_weekday["weekday"],
    categories=day_order,
    ordered=True)
agg_weekday = agg_weekday.sort_values("weekday")
 
fig, ax = plt.subplots()
 
sns.barplot(
    data    = agg_weekday,
    x       = "weekday",
    y       = "n_rides",
    hue     = "city",
    palette = CITY_COLORS,
    ax      = ax)
 
ax.set_title("Rides by day of the week and city")
ax.set_xlabel("Day")
ax.set_ylabel("Number of rides")
ax.legend(title="City", frameon=False)
fig.tight_layout()
fig.savefig("output/01b_rides_day_of_the_week.png", dpi=150)
plt.close(fig)
print("✓ Chart 1b saved")

# [ CHART 2 ] — duration distribution by city
# ↘ business question: does typical ride duration vary across cities? are there
#                      distributional differences suggesting different usage habits?

# --[creazione figura]--
fig, ax = plt.subplots()
 
sns.histplot(
    data    = df_rides,
    x       = "duration_minutes",
    hue     = "city",
    kde     = True,             # adds density curve
    palette = CITY_COLORS,
    alpha   = 0.45,             # transparency to read overlaps
    bins    = 30,
    ax      = ax)
 
ax.set_title("Duration distribution by city")
ax.set_xlabel("Duration (minutes)")
ax.set_xticks(range(5, 65, 5))  # ticks every 5 minutes from 5 to 60
ax.set_ylabel("Number of rides")
legend = ax.legend_
legend.set_title("City")
legend.set_frame_on(False)
 
fig.tight_layout()
fig.savefig("output/02_durations_distribution.png", dpi=150)
plt.close(fig)
print("✓ Chart 2 saved")

# [ CHART 3 ] — rides by time slot and bike type
# ↘ business question: which time slot drives the most usage? does the bike type
#                       (classic/electric) influence the preferred slot?

# --[merge with df_bike to get bike type per ride]--
df_rides_type = df_rides.merge(df_bike[["id_bike", "type"]], on="id_bike", how="left")
 
slot_order = ["morning", "afternoon", "evening"]
 
# aggregate rides by time slot and bike type
bar_data = (
    df_rides_type
    .groupby(["time_slot", "type"])["ride_id"]
    .count()
    .reset_index()
    .rename(columns={"ride_id": "n_rides"}))
 
fig, ax = plt.subplots()
 
sns.barplot(
    data    = bar_data,
    x       = "time_slot",
    y       = "n_rides",
    hue     = "type",
    order   = slot_order,
    palette = {"classic": "#3DBFB8", "electric": "#5B8DB8"},   # teal vs blue
    ax      = ax)
 
ax.set_title("Rides by time slot and bike type")
ax.set_xlabel("Time slot")
ax.set_ylabel("Number of rides")
ax.legend(title="Bike type", frameon=False)
fig.tight_layout()
fig.savefig("output/03_time_slots.png", dpi=150)
plt.close(fig)
print("✓ Chart 3 saved")

# [ CHART 4 ] — scatter duration vs speed with trend line
# ↘ business question: are longer rides inversely related to speed?
#                      are there outliers suggesting data anomalies?

fig, ax = plt.subplots()
 
ax.scatter(df_rides["duration_minutes"], df_rides["average_speed"],
           color="#3DBFB8", alpha=0.7, s=50, edgecolors="none")
 
# trend line via np.polyfit (degree 1 = linear)
x            = df_rides["duration_minutes"].values
y            = df_rides["average_speed"].values
coefficients = np.polyfit(x, y, deg=1)     # returns [m, q] of line y = mx + q
trend_line   = np.poly1d(coefficients)     # callable: trend_line(x) → y
x_range      = np.linspace(x.min(), x.max(), 100)
 
ax.plot(x_range, trend_line(x_range),
        color=TREND_COLOR, linewidth=2, linestyle="--", label="Trend")
 
ax.set_title("Average speed vs duration")
ax.set_xlabel("Duration (minutes)")
ax.set_ylabel("Average speed (km/h)")
ax.legend(frameon=False)
fig.tight_layout()
fig.savefig("output/04_scatter_duration_speed.png", dpi=150)
plt.close(fig)
print("✓ Chart 4 saved")

# [ CHART 5 ] — summary dashboard (2x2)
# ↘ Overview: volume, subscriptions, revenue, durations

fig, axes = plt.subplots(2, 2, figsize=(10, 8))
fig.suptitle("VeloCittà Dashboard — Summary", fontsize=15, fontweight="bold", y=1.01)
 
# -- [top left (↖): bar chart rides by city] --
ax = axes[0, 0]
rides_by_city = df_rides.groupby("city")["ride_id"].count()
 
ax.bar(rides_by_city.index, rides_by_city.values,
       color=[CITY_COLORS[c] for c in rides_by_city.index])
ax.set_title("Rides by city")
ax.set_xlabel("City")
ax.set_ylabel("Number of rides")
ax.yaxis.set_major_locator(mticker.MaxNLocator(integer=True))
 
# -- [top right (↗): pie chart subscription distribution] --
ax = axes[0, 1]
subscriptions = df_users["subscription_type"].value_counts()
 
ax.pie(
    subscriptions.values,
    labels     = subscriptions.index,
    colors     = NEUTRAL_COLORS,
    autopct    = "%1.0f%%",
    startangle = 90,
    wedgeprops = {"linewidth": 1, "edgecolor": "white"}
)
ax.set_title("Subscriptions distribution")
 
# -- [bottom left (↙): bar chart estimated revenue by city] --
ax = axes[1, 0]
revenue_by_city = (
    df_rides
    .groupby("city")["estimated_cost"]
    .sum()
    .round(2)
)
 
ax.bar(revenue_by_city.index, revenue_by_city.values,
       color=[CITY_COLORS[c] for c in revenue_by_city.index])
ax.set_title("Estimated revenue by city (€)")
ax.set_xlabel("City")
ax.set_ylabel("Total cost (€)")
 
# -- [bottom right (↘): boxplot durations by ride type] --
ax = axes[1, 1]
type_order = ["short", "medium", "long"]
 
sns.boxplot(
    data      = df_rides,
    x         = "ride_type",
    y         = "duration_minutes",
    order     = type_order,
    hue       = "ride_type",
    palette   = dict(zip(type_order, NEUTRAL_COLORS)),
    width     = 0.5,
    linewidth = 0.8,
    ax        = ax
)
ax.set_title("Durations by ride type")
ax.set_xlabel("Ride type")
ax.set_ylabel("Duration (minutes)")
 
fig.tight_layout()
fig.savefig("output/05_dashboard.png", dpi=150, bbox_inches="tight")
plt.close(fig)
print("✓ Chart 5 saved")
 
print("\n✓ All charts saved in output/")