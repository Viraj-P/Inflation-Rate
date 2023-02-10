#Viraj Patel
#06/09/2022
#Inflation Rate Calculator

totalExpensesPreviousYear = 0
totalExpensesYearInterest = 0

yearInterest = int(input("Please enter the year that you want to calculate the personal interest for: "))
# using int()function to convert the number/string to an integer consequently removing the decimal. Allows for input.

expenditureCategories = int(input("Please enter the number expenditure categories: "))
# allows for user input for number of expenditure categories

if expenditureCategories >= 0:
    counter = 0
    while counter < expenditureCategories:
        expensesPreviousYear = float(input("Please enter expenses for previous year: "))
        expensesYearInterest = float(input("Please enter expenses for year  interest: "))
        totalExpensesPreviousYear += expensesPreviousYear
        totalExpensesYearInterest += expensesYearInterest
        counter = counter + 1
'''
This block of code above handles the repeating of the input for the user and the calculation for the total values.
The while function sets the counter below the number of categories and will only be repeated up to the number given
as a counter is added each time the code is repeated. The total amount is summed at the end of every code before a 
a counter is added and will be repeated when the code is repeated. We assume the expenses our floats. Line 7 and Line 8
indicate clear "0s" and decreases the risk of errors. 
'''

infRate = ((totalExpensesYearInterest - totalExpensesPreviousYear) / totalExpensesYearInterest) * 100
# calculates the inflation rate using formula given in percent value

print("Personal inflation rate for", str(yearInterest), "is", "{}%".format(infRate))
# Print command for the personal inflate rate with year and rate.
# Printed str of year of interest to differentiate it from the constant code/text.
# Uses format function to add percentage to the print.

if infRate < 3:  # anything under 3 will be set to low
    infType = 'Low'
elif infRate < 5:  # as we are using elif, when less than 3 isn't valid, anything less than 5 above 3 will be set to moderate
    infType = 'Moderate'
elif infRate < 10:  # elif use if under 5 isn't valid code validates under 10 above 5
    infType = 'High'
else:
    infType = 'Hyper'  # anything over 10 will be set to hyper

print("Type of inflation:", str(infType))
# simple print command for type of inflation that outputs the set infType.