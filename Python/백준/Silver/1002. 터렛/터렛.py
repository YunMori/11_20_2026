import sys


def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    idx = 1
    for _ in range(t):
        x1 = int(data[idx])
        y1 = int(data[idx+1])
        r1 = int(data[idx+2])
        x2 = int(data[idx+3])
        y2 = int(data[idx+4])
        r2 = int(data[idx+5])
        idx += 6
        if x1 == x2 and y1 == y2 and r1 == r2:
            print(-1)
            continue
        dx = x1 - x2
        dy = y1 - y2
        dist_sq = dx * dx + dy * dy
        r_sum = r1 + r2
        r_diff = abs(r1 - r2)
        if dist_sq > r_sum * r_sum or dist_sq < r_diff * r_diff:
            print(0)
        elif dist_sq == r_sum * r_sum or dist_sq == r_diff * r_diff:
            print(1)
        else:
            print(2)


if __name__ == "__main__":
    main()
