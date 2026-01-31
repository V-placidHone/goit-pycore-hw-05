hours_entry = input ("Enter your hours: \n")
rate = 10

try:
    if float(hours_entry)> 40:
        payout = (float(hours_entry)-40) * (rate * 1.5) + 40 * rate
        print (f"Your payout: {payout}" )
    else:
        payout = float(hours_entry)*rate
        print (f"Your payout: {payout}" )
        
except:
    print("Not valid hours entry, please enter digits only")



"""
to test:
    positive: 10; 40; 40.1; 45.3
    negative: (empty), eight, 22ww


"""

