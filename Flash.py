import os

def commit_on_specific_date():
    date = '2024-06-30'  # Specific date to commit on
    commit_message = "Commit on 30th June 2024"
    
    with open('data.txt', 'a') as file:
        file.write(f'Committed on {date}\n')
        
    os.system('git add data.txt')
    os.system(f'git commit --date="{date}" -m "{commit_message}"')

commit_on_specific_date()