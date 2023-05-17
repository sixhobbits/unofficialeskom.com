import pandas as pd

HISTORY_FILE = "out.csv"

def get_longest_streak(df, stage_thresh=1):

    half_hours = list(df['created_at'])
    stages = list(df['stage'])

    longest_streak = 0
    longest_start_time = 0
    longest_end_time = 0

    current_streak_length = 0
    current_streak_start = None
    current_streak_end = None
    for i, time in enumerate(half_hours):
        # we're in a streak or we're starting one
        if stages[i] >= stage_thresh:

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
    return longest_streak/2, longest_start_time, longest_end_time

def get_current_streak(df, stage_thresh=1):
    half_hours = list(df['created_at'])[::-1]
    stages = list(df['stage'])[::-1]
    
    for i, time in enumerate(half_hours):
        if stages[i] == 0:
            return i/2, time
        
        
    
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

TEXT = f"We have been loadshedding continuously for {current_streak[0]} hours, since {current_streak[1]}. The longest stage 1 (or more) streak started on {longest_stage_1_streak[1]} and ended on {longest_stage_1_streak[2]}, for a total of {longest_stage_1_streak[0]} hours. The longest stage 6 (or more) streak started on {longest_stage_6_streak[1]} and ended on {longest_stage_6_streak[2]}, for a total of {longest_stage_6_streak[0]} hours."

with open("docs/heatmap/index.md") as f:
    s = f.read()
    s = s.replace("REPLACEME", TEXT)

with open("docs/heatmap/index.md", "w") as f:
    f.write(s)
