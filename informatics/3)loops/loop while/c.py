a = int(input())
i = 0

while ((1 << i) <= a):
    print(1 << i, end = ' ')
    i += 1
#here we use bit table 2^0 =1 ,2^1 = 2,2^2 = 4 and so on