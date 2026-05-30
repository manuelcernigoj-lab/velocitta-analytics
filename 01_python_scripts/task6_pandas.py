"""
Task 6 — Pandas: Loading, Cleaning and Analysis

Contents:
    6.1 — DataFrame Creation        : df_rides (80+ righe), df_bike (20+), df_users (25+)
    6.2 — Data Cleaning             : duplicates, NaN, datetime, derived columns
    6.3 — Apply e colonne           : ride_type, average_speed, estimated_cost
    6.4 — Aggregations and merge    : groupby, pivot, merge, top-N
"""

import pandas as pd
import numpy as np
import random
from task1_utils import rides_classifier


# --[DataFrame creation]--

# [ 1 ] df_rides: 185 rows (180 base + 5 explicit duplicates)
#                 present 8 dispersed NaN: 4 in duration_minutes, 4 in km_traveled
random.seed(42)
np.random.seed(42)

# --[base configurations]--
city_list = ["Milan", "Rome", "Turin"]
date_list = pd.date_range(
    start = "2026-05-01",
    end   = "2026-05-15",
    freq  = "D")
slots = ["morning", "afternoon", "evening"]

# days with realistic peaks:
days_peak = {
    "Monday":    1.7,
    "Tuesday":   1.8,
    "Wednesday": 1.9,
    "Thursday":  1.8,
    "Friday":    1.6,
    # ↘ Monday/Friday: commuting
    "Saturday":  1.0,
    "Sunday":    0.8}
    # ↘ weekend: leisure usage

# distribution of time slots
slot_weights_weekday = [
    0.45,  # morning        -> commuting
    0.20,  # afternoon      -> normal usage
    0.35]  # evening        -> leisure / return route
slot_weights_weekend = [
    0.20,  # morning
    0.35,  # afternoon
    0.45]  # evening

records = []
id_counter = 1

# --[data generation]--
for date in date_list:
    day_name = date.day_name()

    # base daily rides
    daily_rides = 8

    # peaks application
    multiplier = days_peak.get(day_name, 1)
    daily_rides = int(daily_rides * multiplier)

    # realistic noise
    daily_rides += np.random.randint(low = 0, high = 2)
    for _ in range(daily_rides):
        # list of cities with different weights
        city = random.choices(
            city_list,
            weights = [0.45, 0.35, 0.20])[0]

        # city ​​acronyms for id_bike
        acronyms = {
            "Milan":   "MI",
            "Rome":    "RM",
            "Turin":   "TO"
            }[city]

        # different weekend/weekday slot distribution
        if day_name in ["Saturday", "Sunday"]:
            slot = random.choices(
                population = slots,
                weights = slot_weights_weekend)[0]
        else:
            slot = random.choices(
                population = slots,
                weights = slot_weights_weekday)[0]

        # realistic durations for slots
        if slot == "morning":
            duration = np.random.randint(low = 8, high = 30)
            km = round(np.random.uniform(low = 1.5, high = 6.0), 2)
        elif slot == "afternoon":
            duration = np.random.randint(low = 15, high = 45)
            km = round(np.random.uniform(low = 2.0, high = 10.0), 2)
        else:
            duration = np.random.randint(low = 20, high = 60)
            km = round(np.random.uniform(low = 3.0, high = 15.0), 2)

        record = {
            "ride_id": f"C-{id_counter:03d}",
            "id_bike": f"{acronyms}-{np.random.randint(1, 41):03d}",
            "user_id": f"U-{acronyms}-{np.random.randint(1, 81):02d}",
            "city": city,
            "ride_date": date.strftime("%Y-%m-%d"),
            "duration_minutes": duration,
            "km_traveled": km,
            "time_slot": slot}

        records.append(record)
        id_counter += 1

# --[DataFrame creation]--
df_rides = pd.DataFrame(records)

# --[inserting 5 duplicates]--
duplicates = df_rides.sample(n = 5, random_state = 42)
df_rides = pd.concat([df_rides, duplicates], ignore_index = True)

# --[inserting 8 NaN]--
nan_idx_duration = np.random.choice(df_rides.index, size = 4, replace = False)
nan_idx_km = np.random.choice(df_rides.index, size = 4, replace = False)

df_rides.loc[nan_idx_duration, "duration_minutes"] = np.nan
df_rides.loc[nan_idx_km, "km_traveled"] = np.nan

# [ 2 ] df_bike: 80 rowa (30 for Milan/Rome, 20 for Turin)

# --[base configurations]--
bike_types = ["classic", "electric"]
years = [2020, 2021, 2022, 2023, 2024]
bike_data = []

# realistic bike distributions compared to df_rides
bike_distribution = {
    "Milan":   30,
    "Rome":    30,
    "Turin":   20}

# separate counters for city
city_counters = {
    "Milan":   1,
    "Rome":    1,
    "Turin":   1}

# --[data generation]--
for city, amount in bike_distribution.items():
    acronyms = {
        "Milan":   "MI",
        "Rome":     "RM",
        "Turin":   "TO"
        }[city]
    for _ in range(amount):
        bike_number = city_counters[city]
        city_counters[city] += 1

        # classic distribution more abundant than electric ones
        type = random.choices(
            population = bike_types,
            weights = [0.65, 0.35])[0]
        
        year = random.choice(years)

        # costi realistici
        if type == "classic":
            # classic bikes: around €250 - €500 
            cost = round(np.random.uniform(low = 250, high = 500), 2)
        else:
            # electric bikes: around €1200 - €2800
            cost = round(np.random.uniform(low = 1200, high = 2800), 2)

        bike_data.append(
            (f"{acronyms}-{bike_number:03d}",
            type,
            city,
            year,
            cost))

# --[creazione DataFrame]--
df_bike = pd.DataFrame(bike_data, columns = [
    "id_bike",
    "type",
    "city",
    "year",
    "cost"])


# [ 3 ] df_users: 25 rows

# --[base configurations]--
names = ["Luca", "Marco", "Giulia", "Anna", "Francesca",
         "Davide", "Alessandro", "Sara", "Matteo", "Chiara",
         "Stefano", "Elena", "Simone", "Martina", "Paolo",
         "Federica", "Andrea", "Valentina", "Riccardo", "Laura",
         "Giorgio", "Beatrice", "Fabio", "Marta", "Daniele",
         "Irene", "Emanuele", "Camilla", "Filippo", "Silvia"]
surnames = ["Rossi", "Bianchi", "Romeno", "Ricci", "Marino",
            "Greco", "Bruno", "Gallo", "Conti", "De Luca",
            "Mancini", "Costa", "Giordano", "Rizzo", "Lombardi",
            "Moretti", "Barbieri", "Fontana", "Santoro", "Mariani",
            "Caruso", "Ferrara", "Leone", "Serra", "Villa",
            "Ferri", "Longo", "Martinelli", "Testa", "Sala"]
city_config = {
    "Milan":   {"acronyms":       "MI",
                 "n_users":        25},
    "Rome":     {"acronyms":       "RM",
                 "n_users":        15},
    "Turin":   {"acronyms":        "TO",
                 "n_users":        10}}
subscription_types = [
    "Basic",
    "Premium",
    "Student"]

# realistic distribution
weights_subscriptions = [0.45, 0.25, 0.30]

# registration period
registration_date = pd.date_range(
    start = "2026-04-01",
    end =   "2026-05-15",
    freq =  "D")

users_data = []

# --[users generation]--
for city, config in city_config.items():
    acronyms = config["acronyms"]
    
    for i in range(1, config["n_users"] + 1):
        full_name = (
            f"{random.choice(names)} "
            f"{random.choice(surnames)}")
        
        subscription_type = random.choices(
            subscription_types,
            weights = weights_subscriptions)[0]

        signup_date = random.choice(registration_date).strftime("%Y-%m-%d")
        
        users_data.append(
            (f"U-{acronyms}-{i:02d}",
            full_name,
            city,
            subscription_type,
            signup_date))

# --[DataFrame creation]--
df_users = pd.DataFrame(users_data, columns = [
    "user_id",
    "name",
    "city",
    "subscription_type",
    "signup_date"])

# --[data cleaning]--
print(f"\n[ 6.2 ] — Data Cleaning")

print("\n• BEFORE CLEANING\n")
print("\n", df_rides.info())
print("\n", df_rides.describe())

print("\n• CLEANING ...")
# --[duplicate removal]--
n_before = len(df_rides)
df_rides = df_rides.drop_duplicates()
print(f"\n • Duplicate rows removed: {n_before - len(df_rides)} ...")

# --[duration_minutes NaN → median by city]--
median_by_city = df_rides.groupby("city")["duration_minutes"].transform("median")
# ↘ groupby + transform calculates the median by city and propagates it on each row
df_rides["duration_minutes"] = df_rides["duration_minutes"].fillna(median_by_city)
# ↘ fillna replaces only the NaNs with the median value corresponding to the city
print(" • NaN values in duration_minutes replaced with median by city ...")

# --[km_traveled NaN → duration_minutes * 0.18]--
df_rides["km_traveled"] = df_rides["km_traveled"].fillna(df_rides["duration_minutes"] * 0.18)
# ↘ estimates the kilometers traveled based on the duration of the ride
print(" • NaN values in km_traveled replaced with estimate (duration_minutes * 0.18) ...")

# --[convert ride_date from string to datetime]--
df_rides["ride_date"] = pd.to_datetime(df_rides["ride_date"])
print(" • Convert ride_date from string to datetime ...")

# --[derived columns from ride_date]--
df_rides["month"] = df_rides["ride_date"].dt.month
print(" • Added 'month' column (int) ...")

df_rides["weekday"] = df_rides["ride_date"].dt.day_name()
print(" • Added 'weekday' column (e.g. Monday).")

print("\n• AFTER CLEANING\n")
print("\n", df_rides.info())
print("\n", df_rides.describe())


# --[apply and derived columns]--
print(f"\n[ 6.3 ] — Apply and derived columns")

# --[ride_type: apply rides_classifier() imported from task1_utils]--
df_rides["ride_type"] = df_rides["duration_minutes"].apply(rides_classifier)

# --[average_speed in km/h]--
df_rides["average_speed"] = df_rides["km_traveled"] / (df_rides["duration_minutes"] / 60).round(2)

# --[estimated_cost with bracket logic]--
def calculate_cost(duration: float) -> float:
    """
    Calculate the estimated cost of a ride based on its duration in minutes.
    Rates:
        short (< 15 min):   €1.50 fixed
        medium (15-45 min): €2.50 + €0.10 x (minutes - 15)
        long (> 45 min):    €5.00 + €0.08 x (minutes - 45)
    """
    if duration < 15:
        return 1.50
    elif duration <= 45:
        return round(2.50 + 0.10 * (duration - 15), 2)
    else:
        return round(5.00 + 0.08 * (duration - 45), 2)

df_rides["estimated_cost"] = df_rides["duration_minutes"].apply(calculate_cost)

print("\n• ADDED COLUMNS: 'ride_type' | 'average_speed' | 'estimated_cost'")
print("\n• First 10 rows with columns added:")
print(df_rides.head(10))

# --[aggregations e merge]--
print(f"\n[ 6.4 ] — Aggregations and merge")

# --[groupby city]--
agg_city = df_rides.groupby("city").agg(
    n_rides         = ("ride_id",           "count"),
    duration_medium = ("duration_minutes",  "mean"),
    km_totali       = ("km_traveled",       "sum"),
    cost_totale     = ("estimated_cost",    "sum")
).round(2)

print("\n• Statistics by city:")
print(agg_city)

# --[groupby time_slot]--
agg_slot = df_rides.groupby("time_slot").agg(
    n_rides         = ("ride_id",       "count"),
    average_speed   = ("average_speed", "mean")
).round(2)

print("\n• Statistics by time slot:")
print(agg_slot)

# --[pivot table: city x ride_type]--
pivot = pd.pivot_table(
    df_rides,
    index       = "city",
    columns     = "ride_type",
    values      = "ride_id",
    aggfunc     = "count",
    fill_value  = 0             # fill_value = 0 replaces NaN with 0
)

print("\n• Pivot - rides for city and type:")
print(pivot)

# --[merge: df_rides + df_bike + df_users]--
df_merged = (
    df_rides
    .merge(df_bike,     on = "id_bike",     how = "left")
    .merge(df_users,    on = "user_id",     how = "left")
    # ↘ left join: keeps all rides even if the bike or user is not present in
    #              df_bike / df_users (e.g., bikes not listed in the dataset)
    )

print("\n• Merge - first 5 rows:")
print(df_merged.head())
print(f"\n• Available columns ({len(df_merged.columns)}):")
print(list(df_merged.columns))

# --[top-N]--

# top 5 bikes by rides number
top5_bike = (
    df_rides
    .groupby("id_bike")["ride_id"]
    .count()
    .sort_values(ascending = False)
    .head(5)
    .reset_index()                              # reset id_bike from index to column
    .rename(columns = {"ride_id": "n_rides"})   # rename after reset_index
    )
print("\n• Top 5 bikes by rides number:")
print(top5_bike)

# top 3 Premium users by total cost
top3_premium = (
    df_merged[df_merged["subscription_type"] == "Premium"]
    .groupby(["user_id", "name"])["estimated_cost"]
    .sum()
    .sort_values(ascending = False)
    .head(3)
    .reset_index()                             
    .rename(columns = {"estimated_cost": "cost_totale"})
    .round(2)
    )
print("\n• Top 3 Premium users by total cost:")
print(top3_premium.to_string())

# extra statistics → city with highest average speed
print("\n• Average speed by city:")
print(
    df_rides.groupby("city")["average_speed"]
    .mean()
    .round(2)
    .sort_values(ascending = False)
    .reset_index()
    )

# extra statistics → distribution of season tickets by city
print("\n• Distribution of season tickets by city:")
print(
    df_merged.groupby(["city", "subscription_type"])["ride_id"]
    .count()
    .unstack(fill_value = 0)    # unstack data by building a pivot format
    )