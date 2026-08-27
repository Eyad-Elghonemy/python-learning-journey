students = {
  "Ahmed": {
    "Math": "A",
    "Science": "D",
    "Draw": "B",
    "Sports": "C",
    "Thinking": "A"
  },
  "Sayed": {
    "Math": "B",
    "Science": "B",
    "Draw": "B",
    "Sports": "D",
    "Thinking": "A"
  },
  "Mahmoud": {
    "Math": "D",
    "Science": "A",
    "Draw": "A",
    "Sports": "B",
    "Thinking": "B"
  }
}

grades = {
    'A' : '100',
    'B' : '80',
    'C' : '40',
    'D' : '20'
}

sum = 0

for name in students :
    
    print("-"*40)
    
    print(f"-- Student Name => {name}")
    
    print("-"*40)
    
    for sub in students[name] :
        
        key = students[name][sub]
        
        print(f"- {sub} => {grades[key]}")
        
        sum += int(grades[key])
        
    else:
        
        print(f"Total Points For {name} Is {sum}")
        
        sum = 0
        
else :
    
    pass
