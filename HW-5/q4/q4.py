def print_triangle(n):
    if not isinstance(n, int) or n < 0: 
        return "Invalid Input"
    start, end = 1,1
    for i in range(1,n+1):
        for j in range(start, end+i):
            print(j, end = ' ')
        start = start + i
        end = end + i
        print()

print_triangle(3)
print_triangle(6)