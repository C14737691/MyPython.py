int_num = int(input("Please enter the integer"))
bin_stack = []
size = 0
while int_num>0:
      size+= 1
      int_reminder=int_num%2
      if int_reminder == 1:
         #print(int_reminder)
         int_num = int_num//2
         bin_stack.append(1)
      elif int_reminder == 0:
         #print(int_reminder)
         int_num = int_num//2
         bin_stack.append(0)
print(bin_stack)

power = 0
int_sum = 0
while size > 0:
    int_num = 2**power*bin_stack[-size]
    print("num",int_num)
    
    int_sum = int_sum+int_num 
    print("sum",int_sum)
    power+= 1
    size-= 1
    print(power)
print(int_sum)
