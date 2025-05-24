monthly_income =int(input("Enter your monthly income: ")) #prompt user for their monthly income
monthly_expenses = int(input("Enter your total monthly expenses: "))  #prompt user for their monthly expenses
monthly_savings = monthly_income - monthly_expenses  #calculate monthly savings
Projected_Savings = monthly_savings * 12   + (monthly_savings * 12 * 0.05) #calculate projected savings for the year
print("Enter your monthly income:", monthly_income)
print("Enter your total monthly expenses:", monthly_expenses)
print("Your monthly savings are $", monthly_savings,".")
print("Your projected savings after one year, with interest, is: $", Projected_Savings,".")