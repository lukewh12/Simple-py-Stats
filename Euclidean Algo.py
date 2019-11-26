listofinput = []
for i in range(2):
    inp = int(input("Please add 2 numbers "))
    listofinput.append(inp)
print(listofinput)

A = listofinput[0]
B = listofinput[1]

ans = 0
tmp = 0

if A < B:
    B = tmp
    tmp = A
    A = B
    x = A // B 
    r = A % B
    if r == 0:
        ans = B
print("GCD = " + str(ans))
print(ans)