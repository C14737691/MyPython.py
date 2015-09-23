int_num = int(input("Please enter the integer"))
bin_stack = ' '
while int_num>0:
      int_reminder=int_num%2
      if int_reminder == 1:
         #print(int_reminder)
         int_num = int_num//2
         bin_stack+= '1'
      elif int_reminder == 0:
         #print(int_reminder)
         int_num = int_num//2
         bin_stack+= '0'
print(bin_stack)

power = 0
int_sum =0
length = 0
str_length = len(bin_stack)-1
print("str_length",str_length)
while str_length > 0:
    bit=int(bin_stack[-str_length])
    print("bit",bit)
    
    int_num = 2**power*bit
    print("num",int_num)
    
    int_sum = int_sum+int_num 
    print("sum",int_sum)
    
    power = power+1
    str_length = str_length - 1
    print("length",str_length)
    #i= i+1
print(int_sum
