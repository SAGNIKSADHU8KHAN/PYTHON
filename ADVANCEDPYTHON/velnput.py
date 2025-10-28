def take_input():

    num = int(input("Enter a number (Negative to stop) "))


    if num < 0:
        print("Stopping input. Negative number entered.")
        return
    else:
        print(f"You entered :{num} which is positive .")
        take_input()


take_input()