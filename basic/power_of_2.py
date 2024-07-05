
m = int(input("Enter the ^ Power :"))

def table(m):
    if m < 31 and m>0:

        for i in range(m):
            print(f"2^{i} = {2**i}")
        
table(m)