sales = 0                                   # Sales commission, uncapped
LG_com = 0                                  # Lead Generation, capped at 4 per day                      
d1 = 147                                    # Calculate your daily pay above, keep track here
d2 = 114.50
d3 = 117
d4 = 114.50
d5 = 139.50
d6 = 0
w1 = 707.5                                   # Calculate your weekly pay above, then keep track here
w2 = 720
w3 = 535
w4 = 535

# Messages to make it read well 
m_day = "Today you earned: £"
m_week = "This week you earned: £"
m_month = "This month you've earned: £"
m_tax = "If you include tax (assumed at 12.5%) you'll be paid: £"
d_pay = 92                                  # Do not edit anything below here

# Lead Generation commission
if LG_com == 0:
    LG_com = 0
else: 
    if LG_com > 4: 
        LG_com = 10
    else:
        LG_com = LG_com * 2.5

# Sales commission
if sales == 0:
    sales = 0
else: 
    if sales > 2: 
        sales = sales * 10 + 20
    else:
        sales = sales * 20
print(m_day, d_pay + LG_com + sales)

# Weekly total, including shift completion and mystery shopper bonus
if d6 >= 92:
    print(m_week, d1 + d2 + d3 + d4 + d5 + d6 + 100 + 25)
else:
    if d5 >= 92:
        print(m_week, d1 + d2 + d3 + d4 + d5 + 50 + 25) 
    else:
        print(m_week, d1 + d2 + d3 + d4)

# Monthly total, including monthly shift completion bonus and tax
if w3 >= 535:
    m_total = w1 + w2 + w3 + w4 + 150
else: 
    m_total = w1 + w2 + w3 + w4
print(m_month, m_total)
print(m_tax, m_total*0.875)