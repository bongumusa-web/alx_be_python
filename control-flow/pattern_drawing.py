pattern = int(input("Enter the size of the pattern: "))
row = pattern
row_count = pattern

while  row_count > 0:
    
    for i in range(row):
        print("*", end="")

    print()
    row_count -= 1

