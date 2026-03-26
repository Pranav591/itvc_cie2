n = int(input("Enter the number of elements: "))                 
a = list(map(int, input("Enter the elements: ").split()))  

for i in range(0, n-1, 2):
    a[i], a[i+1] = a[i+1], a[i]

print(*a)