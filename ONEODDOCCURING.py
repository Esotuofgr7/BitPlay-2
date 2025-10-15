def OddOccuring(arr):
    res = 0
    for element in arr:
        res = res ^ element
    return res

arr = []
n = int(input("Enter the Array Size"))
while(n):
    num = int(input("Enter a number: "))
    arr.append(num)
    n-=1

print("OddOccuring number is... ", OddOccuring(arr))