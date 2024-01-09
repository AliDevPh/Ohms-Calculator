import time

def main():  # main module
    print("=" * 40)
    print("\t    OHMS CALCULATOR")
    print("=" * 40)
    print("\nChoose the number you want to calculate\n")
    print("1. VOLTAGE")
    print("2. CURRENT")
    print("3. RESISTANCE")

    ask = input("\n> ")      # sets the variable to input the desired number to calculate
    if ask == "1":       # sets the condition in getting the voltage
        print("\n----- Calculating Voltage -----")
        i = float(input("Current: "))        # collect the values of the current
        r = float(input("Resistance: "))         # collect the values of the resistance
        v = i * r       # formula in getting the voltage
        time.sleep(2)        # delays the execution of the next line of code for 2 seconds
        print("\nThe Voltage is = ", format(v, ".2f"))          # displays the voltage result

    elif ask == "2":           # sets the condition in getting the current
        print("\n----- Calculating Current -----\n")
        v = float(input("Voltage: "))       # collects the value of the voltage
        r = float(input("Resistance: "))        # collects the value of the resistance
        i = v / r       # formula in getting the current
        time.sleep(2)       # delays the execution of the next line of code for 2 seconds
        print("\nThe Resistance is = ", format(i, ".2f"))        # displays the current result

    elif ask == "3":         # sets the condition in getting the resistance
        print("----- Calculating Resistance -----")
        v = float(input("Voltage: "))       # collects the value of the voltage
        i = float(input("Current: "))       # collects the value of the current
        r = v / i       # formula in getting the resistance
        time.sleep(2)       # delays the execution of the next line of code for 2 seconds
        print("\n The Resistance is = ", format(r, ".2f"))          # displays the resistance result


main()

choice = input("Do you want to use the calculator again? Y/N: ")  # asks the user if they want another calculation
while choice.lower() == "y":  # sets the parameter if the loop will continue
    main()

