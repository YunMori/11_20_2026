while True:
    line = input().split()
    n = int(line[0])
    if n == 0:
        break
    heights = list(map(int, line[1:]))
    stack = []
    max_area = 0
    for i in range(n):
        start = i
        while stack and stack[-1][1] > heights[i]:
            idx, h = stack.pop()
            area = h * (i - idx)
            if area > max_area:
                max_area = area
            start = idx
        stack.append((start, heights[i]))
    for idx, h in stack:
        area = h * (n - idx)
        if area > max_area:
            max_area = area
    print(max_area)