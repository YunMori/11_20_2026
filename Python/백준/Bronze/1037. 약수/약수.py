#1037 04/16
import sys, math
# sys.stdin = open('/Users/yunjongseo/Downloads/sample_input (1).txt', 'rt')
len = int(sys.stdin.readline())
table = list(map(int, sys.stdin.readline().split()))
a = math.lcm (*table)
b = math.gcd(*table)
print(a*b)