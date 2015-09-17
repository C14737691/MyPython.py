#We are going to do some conversions, from integer to binary and then from binary back to integer.
# It will give us a chance to play with if-elif-else and while statements, as well as a little string slicing.
int_num = int(input("Please enter the integer:  "))
if int_num == 0:
    print(0)
elif int_num <0:
    print("The number is negative")
else:
    bin_stack = []
    while int_num > 0:
        int_reminder = int_num % 2
        if int_reminder == 1:
            int_num = int_num // 2
            bin_stack.append(1)
        elif int_reminder == 0:
            int_num = int_num // 2
            bin_stack.append(0)
    print(bin_stack)

    power = 0
    int_sum = 0
    for i in bin_stack:
        int_num = 2**power*bin_stack[-i]
        int_sum = int_sum + int_num
        power = power+1
    print(int_sum)
