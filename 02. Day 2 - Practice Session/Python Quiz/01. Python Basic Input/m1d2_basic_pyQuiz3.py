# Create a program that accepts input for the number of days and then
# converts it into `Year`, `Month`, `Week`, and `Day`

# Constraint.
# 1 month = 30 days
# 1 year = 360 days

# Example.
# Input: 850
# Output: 2 Years 4 Month 1 Week 2 Days

# Your code here
import math

year = 360
month = 30

user_input = int(input('Masukkan jumlah hari yang mau dihitung: '))

year_result = user_input // year

# user_input % year = 130
month_result = (user_input % year) // month

week_result = (user_input % year) % month // 7

days_result = math.ceil((user_input % year) % month / 7)

result = f'{year_result} Years {month_result} Month {week_result} Week {days_result} Days'
print(result)