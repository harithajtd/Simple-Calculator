#Function to add two numbers
def add(x,y):
    return x+y

#Function to subtract two numbers
def subtract(x,y):
    return x-y


#function to multiply two numbers
def multiply(x,y):
    return x*y


#Function to divide two numbers
def divide(x,y):
    return x/y

print('select operation.')
print('1.Add')
print('2.Substract')
print('3.Multiply')
print('4.Divide')

while True:
    choice=input('Enter a choice(1/2/3/4):')
    if choice in('1','2','3','4'):
        try:
            num1=float(input('Enter first number:'))
            num2=float(input('Enter seecond number:'))
        except ValueError:
            print('Invalid input. please enter a number.')
            continue
        if choice=='1':
            print(num1,'+',num2,'=',add(num1,num2))
        elif choice=='2':
            print(num1,'-','num2','=',subtract(num1,num2))
        elif choice=='3':
            print(num1,'*',num2,'=',multiply(num1,num2))
        elif choice=='4':
            print(num1,'/',num2,'=',divide(num1,num2))

        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation=input('Let\'s do next calculation? (yes/no):')
        if next_calculation=='no':
            break
    else:
        print('Invalid input')
        

    


