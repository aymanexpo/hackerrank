# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
a = int(input())
b = int(input())
M = math.sqrt(a**2+b**2)
deg = math.acos(b/M )
print(str(round(math.degrees(deg)))+chr(176))