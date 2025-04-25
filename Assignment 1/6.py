points = []
n =int(input("enter number of points :"))
for i in range(n):
    pt = input(f"Enter point {i+1} (i.e. x, y, z): ").split(',')
    pt = tuple(map(float, pt))
    points.append(pt)

ans = []

for i in range(n):
    min_dist = float('inf')
    pt = points[i]
    for j in range(n):
        if i != j:
            dist = ((pt[0] - points[j][0])**2 + (pt[1] - points[j][1])**2 + (pt[2] - points[j][2])**2)**0.5
            if dist < min_dist:
                min_dist = dist
                nearest_pt = (points[j][0], points[j][1], points[j][2])
    ans.append([pt, nearest_pt])

print(ans)