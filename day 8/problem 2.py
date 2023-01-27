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
print(visibility)
highest = 0
for i in range(len(visibility)):
    for x in range(len(visibility[i])):
        r_score = 0
        l_score = 0
        u_score = 0
        d_score = 0
        
        if visibility[i][x] == 0 or visibility[i][x] == 1:
            # look right
            col = x
            col += 1

            while col < len(grid[i]):
                if grid[i][col] < grid[i][x]:
                    r_score += 1
                if grid[i][col] >= grid[i][x]:
                    r_score += 1
                    break
                col += 1

            # look left
            col = x
            col -= 1

            while col >= 0:
                if grid[i][col] < grid[i][x]:
                    l_score += 1
                if grid[i][col] >= grid[i][x]:
                    l_score += 1
                    break
                col -= 1

            # look up

            r = i
            r -= 1

            while r >= 0:
                if grid[r][x] < grid[i][x]:
                    u_score += 1
                if grid[r][x] >= grid[i][x]:
                    u_score += 1
                    break
                r -= 1

            # look down

            r = i
            r += 1

            while r < len(grid):
                if grid[r][x] < grid[i][x]:
                    d_score += 1
                if grid[r][x] >= grid[i][x]:
                    d_score += 1
                    break
                r += 1
            #print(i,x)
            #print(r_score,l_score,u_score,d_score)
            new_score = r_score * l_score * u_score * d_score
            #print(new_score)
            if new_score > highest:
                highest = new_score

print(highest)










                    
