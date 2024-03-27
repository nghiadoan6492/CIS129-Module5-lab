# Nghia Doan
# CIS129-Module5-Lab

# Declare variables
totalbottles = 0 # Total bottles for the week
counter = 1 # Control the loop
todaybottles = 0 # Bottles collected in 1 day
totalpayout = 0 # Total payout for the week
keepgoing = 'y' # Used to run program again
 
# Loop to run program again
while keepgoing == 'y':
   
    # Code to set value of variables
    for counter in range (1,8):
        todaybottles = int(input(f'Enter number of bottles for day #{counter}: '))
        totalbottles += todaybottles
        totalpayout = totalbottles * .10
        counter += 1
    
    # Print info code    
    print(f'The number of bottles collected is {totalbottles}\nThe total paid out is $ {totalpayout:.1f}') 
    
    # Reset the variables
    totalbottles = 0 
    counter = 1 
    todaybottles = 0 
    totalpayout = 0 
    
    # This code repeat the loop
    keepgoing = input('Do you want to enter another weeks worth of data?\n(Enter y or n): ') 

