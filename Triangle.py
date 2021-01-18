t = int(input())
for i in range(0, t):
    a, b, c = map(int, input().split())
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** (1 / 2)
    if a + b >= c and b + c >= a and c + a >= b:
        print("%.2f" % area)
    else:

        print("Oh, No!")
