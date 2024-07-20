import os
from datetime import datetime, timedelta

# Define the pattern for "Hunterdii" using a grid
# '.' for no commit, '#' for commit
pattern = [
    "##..#..#...#...#.###..##...##...##.##.###..#..#.###..###.",
    "#.#.#.#.#.#.#.#.#.....#.#.#.#.#.#...#.#.#.#.#.#.#.#.#.#.",
    "##..#.#.#.#.#.#.#.##..##..##...##...#.#.#.#.#.#.#.#.#.#.",
    "#.#.#.#.#.#.#.#.#...#.#.#.#.#.#.#...#.#.#.#.#.#.#.#.#.#.",
    "##...##...##...#.#.#.#.#...##..###..#..#.###..#.#.#.###."
]

def make_art_commits():
    start_date = datetime.now() - timedelta(days=365)  # Start a year ago
    days_offset = 0  # Offset to move through the pattern
    
    for row in pattern:
        for cell in row:
            if cell == '#':
                commit_with_days(days_offset)
            days_offset += 1

def commit_with_days(offset: int):
    dates = (datetime.now() - timedelta(days=365-offset)).strftime('%Y-%m-%d %H:%M:%S')
    
    with open('data.txt', 'a') as file:
        file.write(f'{dates}\n')
        
    os.system('git add data.txt')
    os.system(f'git commit --date="{dates}" -m "Commit {offset} days ago"')

make_art_commits()
