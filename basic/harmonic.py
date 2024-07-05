def harmon_num(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return 1/n + harmon_num(n-1)
        

n = int(input("Enter the Number "))
print(harmon_num(n))