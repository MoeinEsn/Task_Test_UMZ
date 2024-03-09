operation = input("Please Type Your Opreation : sum Or difference Or multiple Or divide: ")

NUm_1 = int(input("Enter Your First Number:"))
NUm_2 = int(input("Enter Your Second Number:"))

if operation == 'sum' :
    Output = NUm_1 + NUm_2
    print (Output)
    
elif operation == 'difference':
    Output = NUm_1 - NUm_2
    print (Output)
    
elif operation == 'multiple':
    Output = NUm_1 * NUm_2
    print (Output)
    
elif operation == 'divide':
    Output = NUm_1 / NUm_2 
    print (Output)