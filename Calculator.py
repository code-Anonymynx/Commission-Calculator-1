# Define a function to initialize the list with zeros
def initialize_list(n):
    return [0] * n

# Display the number of weeks the user wants to calculate
print("How many weeks would you like to calculate?")
num_weeks = int(input())

# Initialize a list to store the sales data for each week
all_weeks_sales = []

# Iterate over each week and ask the user for input to define the number of days worked
for week in range(1, num_weeks + 1):
    print(f"\nWeek {week}:")
    print("How many days have you worked this week?")
    num_days = int(input())
    
    # Initialize a list for sales per week
    sales_per_week = initialize_list(num_days)
    
    # Ask the user how many sales they made each day, update sales_per_week list
    for day in range(1, num_days + 1):
        print(f"How many sales have you made on day {day} of week {week}?")
        sales_per_week[day - 1] = int(input())
    
    # Add the sales data for this week to the list of all weeks' sales
    all_weeks_sales.append(sales_per_week)

# Display the sales data for all weeks
print("\nSales data for all weeks:")
for week, sales in enumerate(all_weeks_sales, start=1):
    print(f"Week {week}: {sales}")
# Define a function to calculate earnings for each week
def calculate_earnings_for_week(sales_per_week):
    earnings = []
    for day, sales in enumerate(sales_per_week, start=1):
        if day == 1:
            earnings.append(92 + sales * 20)
        elif day <= 3:
            earnings.append(92 + sales * 20)
        else:
            earnings.append(92 + sales * 10 + 20)
    return earnings

# Initialize a list to store earnings for all weeks
all_weeks_earnings = []

# Iterate over each week's sales data and calculate earnings
for week, sales_per_week in enumerate(all_weeks_sales, start=1):
    week_earnings = calculate_earnings_for_week(sales_per_week)
    all_weeks_earnings.append(week_earnings)

# Display the earnings data for all weeks
print("\nEarnings data for all weeks:")
for week, earnings in enumerate(all_weeks_earnings, start=1):
    print(f"Week {week}: {earnings}")

# Initialize a list to store the total earnings for each week
total_earnings_per_week = []

# Iterate over each week's earnings data
for week, (earnings_per_week, sales_per_week) in enumerate(zip(all_weeks_earnings, all_weeks_sales), start=1):
    # Calculate the total earnings for the current week
    total_earnings = sum(earnings_per_week)
    
    # Check if the number of days worked is 5
    if len(sales_per_week) == 5:
        # Add 50 to the total earnings for this week
        total_earnings += 50
    
    if len(sales_per_week) == 6: 
        # Add 100 to the total earnings for this week
        total_earnings += 100
    
    # Check if the total sales for the week is at least 10
    if sum(sales_per_week) >= 10:
        # Add 50 to the total earnings for this week
        total_earnings += 50
    
    # Add the updated total earnings for this week to the list
    total_earnings_per_week.append(total_earnings)

# Display the updated total earnings for each week
print("\nTotal earnings for each week with added bonus':")
for week, earnings in enumerate(total_earnings_per_week, start=1):
    print(f"Week {week}: {earnings}")

# Calculate the total earnings for the month
total_earnings_month = sum(total_earnings_per_week)

# Display the total earnings for the month
print("\nTotal earnings for the month:", total_earnings_month)

# Ask the user for input: number of happy sales made over the month
num_happy_sales = int(input("How many happy hour sales were made over the month? "))

# Calculate the additional earnings for the month based on happy sales
additional_earnings_happy_sales = 10 * num_happy_sales

# Calculate the total earnings for the month
total_earnings_month = sum(total_earnings_per_week)

# If there were happy sales, add the additional earnings to the total earnings for the month
if num_happy_sales > 0:
    total_earnings_month += additional_earnings_happy_sales

# Display the total earnings for the month
print("\nTotal earnings for the month:", total_earnings_month)

# Account for tax
total_earnings_month = total_earnings_month * 0.8

# Display the total earnings for the month, accounting for tax
print("\Total after tax will be:", total_earnings_month)
