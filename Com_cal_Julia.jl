sales = 0
LG_com = 1

d1 = 134.5           # Place to edit the daily total                
d2 = 112
d3 = 94.5
d4 = 0
d5 = 0
d6 = 0

w1 = 416             # Place to edit the weekly total            
w2 = 0
w3 = 0
w4 = 0

m_week = "This week you earned: £"
m_month = "This month you've earned: £"

if LG_com == 0       # Lead commission calculations
    LG_com = 0
elseif LG_com >= 4
    LG_com = 10 
else
    LG_com = LG_com * 2.5 
end

if sales == 0          # Sales commission calculations
    sales = 0
elseif sales > 2
    sales = sales * 10 + 20
else
    sales = sales * 20
end

println("Today you earned: £", 92 + sales + LG_com)

if d6 >= 92                     # Weekly calculations
    println(m_week, d1 + d2 + d3 + d4 + d5 + d6 + 100 + 50,"\n")
elseif d5 >= 92
    println(m_week, d1 + d2 + d3 + d4 + d5 + d6 + 50,"\n")
else
    print(m_week, d1 + d2 + d3 + d4,"\n")
end             

if w3 >= 535                    # Monthly calculations
    println(m_month, w1 + w2 + w3 + w4 + 150,"\n")
else 
    println(m_month, w1 + w2 + w3 + w4,"\n")
end