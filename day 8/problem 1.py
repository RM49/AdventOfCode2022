d = open("data.txt", 'r')

grid = []
visibility = []
for l in d:
    a = l.strip("\n")
    int(a)
    a = list(a)
    grid.append(a)
    for i in range(len(a)):
        a[i] = int(a[i])
        
    v = []
    for i in range(len(a)):
        v.append(0)
    visibility.append(v)
    
print(grid)
print(visibility)
        
# looking horizontally right

for i in range(len(grid)):
    count = 0
    tallest = grid[i][0]
    visibility[i][0] = 1
    for t in grid[i]:
        if t > tallest:
            visibility[i][count] = 1
            tallest = t
        count += 1

# looking horizontally left        
for i in range(len(grid)):
    count = len(grid[i]) - 1 
    tallest = grid[i][-1]
    visibility[i][-1] = 1
    for x in range(len(grid[i]) - 1, 0, -1):
        if grid[i][x] > tallest:
            visibility[i][count] = 1
            tallest = grid[i][x]
        count -= 1

# looking down

for i in range(len(grid[0])):
    tallest = -1
    for x in range(len(grid)):
        if grid[x][i] > tallest:
            visibility[x][i] = 1
            tallest = grid[x][i]

# looking up

for i in range(len(grid[0])):
    tallest = -1
    for x in range(len(grid)-1, 0, -1):
        if grid[x][i] > tallest:
            visibility[x][i] = 1
            tallest = grid[x][i]
            
total = 0

for x in visibility:
    for n in x:
        if n == 1:
            total += 1

print(total)
