def print_pyramid(n):
    if not isinstance(n, int) or n < 0: 
        return "Invalid Input"
    all_space = 2*n-1
    for i in range(1,n+1):
        for j in range(1, all_space):
            num_between= i+(i-1)
            num_side = (all_space-num_between)/2
            if j <= num_side:
                print(" ", end = '')
            else:
                print("* "*i, end = '')
                break
        print()
print_pyramid(5)