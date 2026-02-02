


#if client_input == "stop"

"""if float(client_input) <= 1.0 and float(client_input) >= 0:
    
    score = float(client_input)
    if score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    else:
        print("F")

else:
    print("Bad score")
"""

while True: 
    client_input = input("\nType \'stop\' if you want to stop\n\n\nEnter score between 0 - 1.0  ->   ")
    if client_input == "stop":
        break
    
    if float(client_input) <= 1.0 and float(client_input) >= 0:
    
        score = float(client_input)
        if score >= 0.9:
            print("A")
        elif score >= 0.8:
            print("B")
        elif score >= 0.7:
            print("C")
        elif score >= 0.6:
            print("D")
        else:
            print("F")
    
    else:
        print ("Bad Score")

