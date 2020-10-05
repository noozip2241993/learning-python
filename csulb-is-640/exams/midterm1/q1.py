'''
Write a program that asks the user to enter the weight of a package. 
Then display the shipping charge. The following is an example of the 
prompt message and the result message (please use exactly the same 
prompt and result message text, the values are different for 
different input).
'''
# 1 ask the user to input package weight
# 2 determine num of lbs at each rate (rate_1, rate_2, rate_3, rate_4)
# 3 determine price at each rate
# 4 add rate prices for the total
# 5 display a result message with the total shipping charge

#INITIALIZATION
weight = 0
price = 0
PROMPT_WEIGHT = 'Please enter the package weight: '

def get_price(weight):
    # currency values are in pennies for calculations
    BASE_PRICE = 300
    price = 0

    #weight variables
    RATE_1_MARK = 3.0
    RATE_2_MARK = 6.0
    RATE_3_MARK = 10.0

    rate_1_lb = 0
    rate_2_lb = 0
    rate_3_lb = 0
    rate_4_lb = 0

    # 2 determine num of lbs at each rate (rate_1, rate_2, rate_3, rate_4)
    # classify weight
    if weight <= RATE_1_MARK:
        rate_1_lb = weight
    elif weight <= RATE_2_MARK:
        rate_1_lb = RATE_1_MARK
        rate_2_lb = weight - rate_1_lb
    elif weight <= RATE_3_MARK:
        rate_1_lb = RATE_1_MARK
        rate_2_lb = RATE_2_MARK - rate_1_lb 
        rate_3_lb = weight - rate_1_lb - rate_2_lb
    else:
        rate_1_lb = RATE_1_MARK
        rate_2_lb = RATE_2_MARK - rate_1_lb 
        rate_3_lb = RATE_3_MARK - rate_1_lb - rate_2_lb
        rate_4_lb = weight - rate_1_lb - rate_2_lb - rate_3_lb

    # 3 determine price at each rate
    # 4 add rate prices for the total
    price = rate_1_lb * BASE_PRICE + rate_2_lb * (BASE_PRICE + 100) + rate_3_lb * (BASE_PRICE + 200) + rate_4_lb * (BASE_PRICE + 300) 
    return price / 100 # convert price to dollars
    
# PROCESSING
# 1 ask the user to input package weight
weight = float(input(PROMPT_WEIGHT))
price = get_price(weight)

# TERMINATION

print(f'The shipping price for a {weight:.1f}lb package is ${price:.2f}.')