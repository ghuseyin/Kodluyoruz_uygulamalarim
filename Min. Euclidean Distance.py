def get_coordinates(index):
    x, y = input(f"x{index} ve y{index} değerlerini girin: ").split()
    return int(x), int(y)

def euclideanDistance(coor1, coor2):
     return ((coor1[0]-coor2[0])**2 + (coor1[1]-coor2[1])**2) ** 0.5

count = 5       # number of coordinates
points = [get_coordinates(i) for i in range(1, count+1)]

for i in range(count):
    print(f"Point{i+1}: {points[i]}")

distances = []  # a list for saving distances of between all coordinates
for i in range(count):
    for j in range(i+1, count):
        distances.append(euclideanDistance(points[i], points[j]))
        print(f"Distance between Point{i+1} and Point{j+1}: {distances[-1]:.5f}")

print(f"Minimum distance: {min(distances):.5f}")