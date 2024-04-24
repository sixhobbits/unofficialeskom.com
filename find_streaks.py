import pandas as pd

HISTORY_FILE = "out.csv"

def get_longest_streak(df, stage_thresh=1, reverse=False, min_date=None, max_date=None):
    # reverse if we want to set a maximum stage instead of a minimum
    # e.g. we are looking for 'good' times of low or no loadshedding

    half_hours = list(df['created_at'])
    stages = list(df['stage'])

    longest_streak = 0
    longest_start_time = 0
    longest_end_time = 0

    current_streak_length = 0
    current_streak_start = None
    current_streak_end = None
    for i, time in enumerate(half_hours):
        if min_date and time < min_date:
            continue

        if max_date and time > max_date:
            continue
        # we're in a streak or we're starting one
        if not reverse:
            threshold_check = stages[i] >= stage_thresh
        else:
            threshold_check = stages[i] <= stage_thresh
        if threshold_check:
            if current_streak_start == None:
                current_streak_start = time
                current_streak_length = 1
            else:
                current_streak_length += 1
        # we're not in a streak, or we just ended one
        else:
            if current_streak_length > longest_streak:
                longest_streak = current_streak_length
                longest_start_time = current_streak_start
                longest_end_time = time
                # reset curernt streak
            current_streak_length = 0
            current_streak_start = None
            curent_streak_end = None
    # check at end in case we've broken the record in the current streak
    if current_streak_length > longest_streak:
        longest_streak = current_streak_length
        longest_start_time = current_streak_start
        longest_end_time = time
    return longest_streak/2, longest_start_time, longest_end_time

df = pd.read_csv(HISTORY_FILE)

longest_stage_0_streak = get_longest_streak(df, stage_thresh=0, reverse=True)
print("longest 0 streak 2024")
print(longest_stage_0_streak)
