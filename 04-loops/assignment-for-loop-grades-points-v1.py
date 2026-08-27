my_ranks = {
  'Math': 'A',
  "Science": 'B',
  'Drawing': 'A',
  'Sports': 'C'
}

grades = {
    'A' : '100',
    'B' : '80',
    'C' : '40'
}

sum = 0

for sub , grade in my_ranks.items() :
    
    print(f"My Rank in {sub} Is {grade} And This Equal {grades[grade]} Points")
    
    sum += int(grades[grade])
    
else :
    
    print(f"Total Points Is {sum}")