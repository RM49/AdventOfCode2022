data = open("data.txt", "r")

highest = 0
total = 0
new = False

for r in data:
    num = r.strip("\n")
    try:
        num = int(num)
    except ValueError:
        new = True
    if new == False:
        total += num
    elif new == True:
        if total > highest:
            highest = total
        total = 0
        new = False
print(highest)
    
