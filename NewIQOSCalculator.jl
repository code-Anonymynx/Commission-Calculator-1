# The first section of code will allow me to define the number of days worked
# And store how many sales were made each day 

# Define a function to initialize the list with zeros
function initialize_list(n)
    return fill(0, n)
end

# Display the days in an empty list, ask the user for input to define number of days
println("How many days have you worked this week?")
n = parse(Int, readline())

SalesPerWeek = initialize_list(n)
println("List of shifts worked each day this week:", NoShiftsWeek)

# Identify which day of the week it is
x = 1

# Ask the user how many sales they made each day, populate NoShiftsWeek List
function populate_list!(SalesPerWeek)
    for i in 1:length(SalesPerWeek)
        println("How many sales have you made on day ", x, "?")
        SalesPerWeek[i] = parse(Int, readline())
        global x += 1  # Increment x for the next day
    end
end

populate_list!(SalesPerWeek)
println("Updated list of shifts worked each day this week:", SalesPerWeek)

# Now I have an array with the number of sales made each day
# The next step is to repeat this method to create an equal length array 
# with the number of lead generations per day 
