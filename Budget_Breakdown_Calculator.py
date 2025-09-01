# Variable for net monthly income.

net_month_income = float(input("What is your net monthly income?: "))

# Inputs in this section will lead to the initial sum of the budget before providing the 
# percentage each makes up int the total sum.

cost_of_housing_or_rent = float(input("What is the cost of your mortgage or rent payment each month?: "))
cost_of_utilities = float(input("What is the cost of your utility payment each month?: "))
cost_of_groceries = float(input("How much do you spend on groceries each month?: "))
cost_of_transportation = float(input("What is the cost of your transportation payment each month?: "))
cost_of_healthcare = float(input("What is the cost of your healthcare payment each month, if any?: "))
cost_of_personal_care = float(input("What is the cost of your personal indulgences each month, if any? Examples include, going to the movies, eating out, etc: "))
cost_of_clothing = float(input("What are your monthly clothing costs, if any?: "))
cost_of_debt = float(input("What is the monthly payment for any debt you might have?: "))

# Variable printing sum total of all monthly costs. 

sum_total_expenses = cost_of_housing_or_rent + cost_of_utilities + cost_of_groceries + cost_of_transportation + cost_of_healthcare + cost_of_personal_care + cost_of_clothing + cost_of_debt

sum_total_output = f'The sum total of your expenses is {sum_total_expenses}.'
print(sum_total_output)

remaining_income = f'This is what remains of your monthly net income {net_month_income - sum_total_expenses}'
print(remaining_income)

# Print statements and variables for showing what percentage each monthly cost is of net_month_income.

per_spent_on_housing = f'The percent of net income spent on rent or mortgage each month is.: {cost_of_housing_or_rent/net_month_income}%'
per_spent_on_util = f'The percent of net income spent on utilities each month is.: {cost_of_utilities/net_month_income}%'
per_spent_on_groc = f'The percent of net income spent on groceries each month is.: {cost_of_groceries/net_month_income}%'
per_spent_on_transport = f'The percent of net income spent on transportation each month is.: {cost_of_transportation/net_month_income}%'
per_spent_on_health = f'The percent of net income spent on healthcare each month is.: {cost_of_healthcare/net_month_income}%'
per_spent_on_pers_care = f'The percent of net income spent on personal care each month is.: {cost_of_personal_care/net_month_income}%'
per_spent_on_cloths = f'The percent of net income spent on clothes each month is.: {cost_of_clothing/net_month_income}%'
per_spent_on_debt = f'The percent of net income spent on debt each month is.: {cost_of_debt/net_month_income}%'

print(per_spent_on_housing)
print(per_spent_on_util)
print(per_spent_on_groc)
print(per_spent_on_transport)
print(per_spent_on_health)
print(per_spent_on_pers_care)
print(per_spent_on_cloths)
print(per_spent_on_debt)