hours_entry = input ("Enter your hours: \n")
rate = 10

if float(hours_entry)<= 40 :
    payout = float(hours_entry) * rate
    print(payout)
elif float(hours_entry) > 40:
    payout = (float(hours_entry)-40) * (rate * 1.5) + 40 * rate 
    print(payout)
else:
    print("Enter the hours wih digits please")


