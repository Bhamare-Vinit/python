def find_triplets(arr):
    """
    Description:function takes the list of array and return count of tuples
    Parameter:list of numbers
    Return:list of tuples and number of tuples 
    """
    n = len(arr)
    triplets = []
    count = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == 0:
                    triplet = sorted([arr[i], arr[j], arr[k]])
                    if triplet not in triplets:
                        triplets.append(triplet)
                        count += 1

    return count, triplets

arr=[]
N = int(input("Enter the number of integers: "))
for i in range(N):
    arr.append(int(input(f"Enter the {i+1}th number:")))
count, triplets = find_triplets(arr)

print(f"Number of distinct triplets: {count}")
print("Distinct triplets that sum to zero:")
for triplet in triplets:
    print(triplet)

                