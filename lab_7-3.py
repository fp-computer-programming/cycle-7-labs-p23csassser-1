#Creator CS 11/18/2022

def greeting(): #create docstring
    """
    Print "hello world" on one line.
    This function only has one print statement, 
    which will prints the string "hello world" on a single line. 
    """
    return("hello world")

greeting() #Call the function and create test cases

print(greeting()== "hello world") #True
print(greeting()== "hello globe") #False
print(greeting()== "hello earth") #false
print(greeting()== "hello mars") #False 



