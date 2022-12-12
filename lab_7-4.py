#Creator cs 11/18/2022

def find_sum(num1, num2): #Create function find_sum
    num_sum = num1 + num2
    return num_sum #return the sum 

my_sum = find_sum(111, 222) #Find the sum of 111 + 222
print(my_sum)
#create test cases
print(find_sum(111, 222) == 333) #true
print(find_sum(111, 22) == 333) #False
print(find_sum(111, 272) == 333) #false
print(find_sum(111, 922) == 333) #false





