import pandas as pd
from datetime import datetime, timedelta


def load_data(file_path):
    return pd.read_csv(file_path, parse_dates=['created_at'], infer_datetime_format=True)

def find_zero_streaks(df):
    streaks = []
    current_streak_start = None

    for i in range(len(df)):
        if df.iloc[i]['stage'] == 0.0:
            if current_streak_start is None:
                current_streak_start = df.iloc[i]['created_at']
            current_streak_end = df.iloc[i]['created_at']
        else:
            if current_streak_start is not None:
                streaks.append((current_streak_start, current_streak_end))
                current_streak_start = None

    if current_streak_start is not None:
        streaks.append((current_streak_start, current_streak_end))

    return streaks

def calculate_streak_hours(streaks):
    return [(start, end, (end-start).total_seconds() / 3600) for start, end in streaks]

def sort_streaks(streaks):
    return sorted(streaks, key=lambda x: x[2], reverse=True)

def print_streaks(sorted_streaks):
    for start, end, hours in sorted_streaks:
        print(f"Streak from {start} to {end} lasting {hours} hours")

# Your CSV file path
file_path = 'out.csv'

# Process the data
df = load_data(file_path)
streaks = find_zero_streaks(df)
streaks_with_hours = calculate_streak_hours(streaks)
sorted_streaks = sort_streaks(streaks_with_hours)

# Print the results
print_streaks(sorted_streaks)

