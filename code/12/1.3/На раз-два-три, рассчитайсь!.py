heights = []

for i in range(3):
    height = int(input("Введите рост мальчика: "))
    heights.append(height)

n = len(heights)
for i in range(n):
    for j in range(0, n-i-1):
        if heights[j] < heights[j+1]:
            heights[j], heights[j+1] = heights[j+1], heights[j]

for height in heights:
    print(height)