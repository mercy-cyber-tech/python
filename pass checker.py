marks = [45,67,58,78,80,35,85,40,88,63]

while True:
  print("1.check passes and fails")
  print("2.marks")
  choice = input("option: ")
  if choice == "1":
    passes = 0
    fails = 0
    for mark in marks:
     if mark >= 50: 
      passes += 1
     elif mark< 50:
       fails += 1
    print(f"passes: {passes}")
    print(f"fails: {fails}")
  if choice == "2":
    for mark in marks:
      highest = max(marks)
      lowest = min(marks)
      average = sum(marks)/len(marks)
    print(f"highest mark: {highest}")
    print(f"lowest mark: {lowest}")
    print(f"average mark: {average}")
     
       



