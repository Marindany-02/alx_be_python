# pattern drawing.py
# prompt the user to input a positive intereger for the pattern size
size = int(input("Enter the size of the pattern: "))
#validate the size positive 
if size > 0:
    # use a while loop to iterate through each row
    row = 0
    while row < size:
        # use a for loop to print asterisks for the current roow
        for _ in range(size):
            print("*", end="")
        # move to the next line after completing the row
        print()
        row += 1
else:
    print("Please enter a positive interger.")
