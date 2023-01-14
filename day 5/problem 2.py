
crates = [["B", "Q", "C"],
          ["R", "Q", "W", "Z"],
          ["B", "M", "R", "L", "V"],
          ["C", "Z", "H", "V", "T", "W"],
          ["D", "Z", "H", "B", "N", "V", "G"],
          ["H", "N", "P", "C", "J", "F", "V", "Q"],
          ["D", "G", "T", "R", "W", "Z", "S"],
          ["C", "G", "M", "N", "B", "W", "Z", "P"],
          ["N", "J", "B", "M", "W", "Q", "F", "P"]
          ]

file = open("data.txt", "r")
data = file.readlines()
instructions = []
for d in data:
    instructions.append(d.split(" "))

held = []
for t in instructions:
    for i in range(int(t[1])):
        d = crates[int(t[3])-1].pop()
        held.append(d)
    held.reverse()
    for h in held:
        crates[int(t[5])-1].append(h)
    held = []
    
for c in crates:
    print(c.pop())
