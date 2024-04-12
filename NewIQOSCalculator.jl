# The first section of code will allow me to define the number of days worked
# And store how many sales & lead generations were made each day 

# Define a function to initialize the list with zeros
function initialize_list(n)
    return fill(0, n)
end

# Display the days in an empty list, ask the user for input to define number of days
println("How many days have you worked this week?")
n = parse(Int, readline())

# Initialise two lists - one for sales per week and one for lead generations
SalesPerWeek = initialize_list(n)
LGPerWeek = initialize_list(n)
println("List of shifts worked each day this week:", NoShiftsWeek)

# Identify which day of the week it is
x = 1       # for SalesPerWeek
y = 1       # for LGPerWeek

# Ask the user how many sales they made each day, populate NoShiftsWeek List
function populate_list!(SalesPerWeek)
    for i in 1:length(SalesPerWeek)
        println("How many sales have you made on day ", x, "?")
        SalesPerWeek[i] = parse(Int, readline())
        global x += 1  # Increment x for the next day
    end
end

# Create & display a list with the #sales made per day
populate_list!(SalesPerWeek)
println("Updated list of sales made each day this week:", SalesPerWeek)

# Ask the user how many lead generations they made each day, populate NoShiftsWeek List
function populate_list!(LGPerWeek)
    for i in 1:length(LGPerWeek)
        println("How many lead generations have you made on day ", y, "?")
        LGPerWeek[i] = parse(Int, readline())
        global y += 1  # Increment x for the next day
    end
end

# Create & display an equal length list with the #lead generations made per day
populate_list!(LGPerWeek)
println("Updated list of lead generations made each day this week:", LGPerWeek)
