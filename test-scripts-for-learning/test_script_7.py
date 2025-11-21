# Create a function called  monthly_salary(annual_salary)  that takes an annual salary as a 
# parameter and returns the corresponding monthly salary by dividing the annual salary by 12.

# Create a function called  weekly_salary(monthly_salary)  that takes a monthly salary as a 
# parameter and returns the corresponding weekly salary by dividing the monthly salary by 4.

# Create a function called  hourly_salary(weekly_salary, hours_worked)  
# that takes parameters for the weekly salary and the number of hours worked per week, and 
# returns the corresponding hourly wage by dividing the weekly salary by the number of hours worked per week.

# Ask the user to enter their annual salary.

# Ask the user to enter the number of hours worked per week.

# Call the previously created functions to calculate the corresponding hourly wage.

# Display the result in the format:  "Your hourly wage is XX dollars".

def monthly_salary(annual_salary):
    return annual_salary / 12

def weekly_salary(monthly_salary):
    return monthly_salary / 4

def hourly_wage(weekly_salary, hours_worked):
    return weekly_salary / hours_worked
    
def main():
    annual_salary = int(input("Enter your annual salary. \n")) # ex. 120000
    hours_worked = int(input("\nEnter how many hours worked per week. \n")) # ex. 40)
    
    monthly_sal = monthly_salary(annual_salary) #120000 / 12 = 10000
    weekly_sal = weekly_salary(monthly_sal)
    hourly_wage = hourly_wage(weekly_sal, hours_worked)
    
    a = monthly_salary(12000)
    print(f"\nYour annual salary is {annual_salary}. \n")    
    print(f"Your hourly wage is {hourly_wage} dollars. \n")    

if __name__ == "__main__":
    main()