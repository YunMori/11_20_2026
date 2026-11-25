#2609 04/16
import sys, math
one, two = map(int, sys.stdin.readline().split())
print(math.gcd(one, two))
print(math.lcm(one, two))