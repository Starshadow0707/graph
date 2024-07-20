import os
from datetime import datetime, timedelta

def make_daily_commits():
    start_days_ago = 2500  # Number of days ago to start committing
    end_days_ago = 0  # Today
    
    for days_ago in range(start_days_ago, end_days_ago - 1, -1):
        commit_with_days(days_ago)

def commit_with_days(days: int):
    dates = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d %H:%M:%S')
    
    with open('data.txt', 'a') as file:
        file.write(f'{dates}\n')
        
    os.system('git add data.txt')
    os.system(f'git commit --date="{dates}" -m "Commit {days} days ago"')

make_daily_commits()
