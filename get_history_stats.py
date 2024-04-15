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

def get_current_streak(df):
    half_hours = list(df['created_at'])[::-1]
    stages = list(df['stage'])[::-1]

    currently_loadshedding = True
    if stages[0] == 0:
        currently_loadshedding = False
    for i, time in enumerate(half_hours):
        if currently_loadshedding:
            if stages[i] == 0:
                return i/2, time, currently_loadshedding, half_hours[-1]
        else:
            if stages[i] != 0:
                return i/2, time, currently_loadshedding, half_hours[-1]
        
        
    
def get_hours_of_loadshedding_by_month(df, stage_thresh=1):
    half_hours = list(df['created_at'])
    stages = list(df['stage'])
    
    summary = {}
    
    for i, time in enumerate(half_hours):
        if stages[i] >= stage_thresh:
            key = time[:7]
            
            if key in summary:
                summary[key] += 1
            else:
                summary[key] = 1
    return {k: summary[k]/2 for k in summary}

def get_hours_of_loadshedding_by_year(df, stage_thresh=1):
    half_hours = list(df['created_at'])
    stages = list(df['stage'])
    
    summary = {}
    
    for i, time in enumerate(half_hours):
        if stages[i] >= stage_thresh:
            key = time[:4]
            
            if key in summary:
                summary[key] += 1
            else:
                summary[key] = 1
    return {k: summary[k]/2 for k in summary}
    
    


df = pd.read_csv(HISTORY_FILE)
longest_stage_1_streak = get_longest_streak(df)
longest_stage_6_streak = get_longest_streak(df, stage_thresh=6)

longest_stage_0_streak_2024 = get_longest_streak(df, stage_thresh=0, reverse=True, min_date="2024-01-01", max_date="2024-12-31")
print("longest 0 streak 2024")
print(longest_stage_0_streak_2024)

longest_stage_0_streak_2023 = get_longest_streak(df, stage_thresh=0, reverse=True, min_date="2023-01-01", max_date="2024-01-31")
print("longest 0 streak 2023")
print(longest_stage_0_streak_2023)

longest_stage_0_streak_2022 = get_longest_streak(df, stage_thresh=0, reverse=True, min_date="2022-07-01", max_date="2022-12-31")
print("longest 0 streak 2022")
print(longest_stage_0_streak_2022)
print("==")

current_streak = get_current_streak(df)
hours_by_month = get_hours_of_loadshedding_by_month(df)
hours_by_year = get_hours_of_loadshedding_by_year(df)




print(longest_stage_1_streak)
print(longest_stage_6_streak)
print(current_streak)

'''
(997.0, '2023-02-05 16:00:00', '2023-03-19 05:00:00')
(153.0, '2023-02-19 20:00:00', '2023-02-26 05:00:00')
(83.0, '2023-05-14 07:00:00')
'''

currently_loadshedding = current_streak[2]

if currently_loadshedding:
    current_streak_text = "We have been loadshedding continuously for "
else:
    current_streak_text = "We haven't had loadshedding for "

last_updated = current_streak[3]

TEXT = f"<i>Last updated: {last_updated}</i>\n\n" + current_streak_text + f"{current_streak[0]} hours, since {current_streak[1]}."


TEXT += f"\n\nThe longest stage 1 (or more) streak started on {longest_stage_1_streak[1]} and ended on {longest_stage_1_streak[2]}, for a total of {longest_stage_1_streak[0]} hours.\n\nThe longest stage 6 (or more) streak started on {longest_stage_6_streak[1]} and ended on {longest_stage_6_streak[2]}, for a total of {longest_stage_6_streak[0]} hours."


print(TEXT)

with open("docs/heatmap/index.md") as f:
    s = f.read()
    lines = s.split("\n")

    for i, v in enumerate(lines):
        if v.startswith("###"):
            break
    lines[1:i] = [TEXT]
    towrite = '\n'.join(lines)
    

with open("docs/heatmap/index.md", "w") as f:
    f.write(towrite)
