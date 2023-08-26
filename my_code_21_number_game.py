print("Welcome to play 21 Number game.")

def nearestMultiple(number):
    if number >= 4:
        near = number + (4-(number%4))
    else:
        near = 4

    return near

def check(xyz):
    i = 1
    while i < len(xyz):
        if (xyz[i]-xyz[i-1])!=1:
            return False
        i+=1
        return True

def loose():
    print("You loose!!!\nBetter luck next time.")
    exit(0)

def start1():
    xyz = []
    last = 0

    while True:
        print("Do you wanna take first turn or the second, if first press (f) else press (s)")
        chance = input("Enter your choice: ")
        chance = chance.lower()

        if chance == "f":
            while True:
                if last == 20:
                    loose()
                else:
                    input_amount = int(input("Your turn, plz enter number of values you wish to enter: "))

                    if input_amount > 0 and input_amount <= 3:
                        comp_input_amount = 4-input_amount
                        i,j = 1,1
                        print("Now enter the values: ")
                        while i <= input_amount:
                            input_value = input("Value {}: ".format(i))
                            xyz.append(input_value)
                            i+=1

                        last = xyz[-1]

                        #to check wheteher concescutive values are been entered
                        if check(xyz) == True:
                            if last == 21:
                                loose()
                            else:
                                while j <= comp_input_amount:
                                    xyz.append(last+j)
                                    j +=1

                            print(xyz)
                            last = xyz[-1]

                        else:
                            print("You didn't enter consecutive values.")
                            loose()


                    else:
                        print("You have entered invalid values, You are disqualified.")
                        loose()


        elif chance == "s":
            comp_input_amount = 1
            last = 0

            while last < 20:
                j = 1
                while j <= comp_input_amount:
                    xyz.append(last+j)
                    j += 1

                print("Order of inputs.\n{}".format(xyz))

                if xyz[-1] == 20:
                    loose()
                else:
                    input_amount = int(input("It's your turn now.\nHow many numbers do you wish to enter: "))
                    i = 1
                    while i <= input_amount:
                        xyz.append(int((input("Enter your value: "))))
                        i +=1

                    last = xyz[-1]

                    if check(xyz) == True:
                        print(xyz)
                        near = nearestMultiple(last)

                        comp_input_amount = near - last

                        if comp_input_amount == 4:
                            comp_input_amount = 3
                        else:
                            comp_input_amount = comp_input_amount

            print("Congrats you won!!!")

        else:
            print("Wrong choice, try again.")



game = True

while game == True:
    print("Player 2 is the computer.")

    answer = input("Do you wanna play the game (Yes/No)? ")
    answer = answer.lower()
    if answer == "yes":
        print("play")
        start1()
    else:
        answer = input("Do you wanna quit the game (Yes/No)? ")
        answer = answer.lower()
        if(answer == "yes"):
            print("Exiting the game...")
            exit(0)
        elif(answer == "no"):
            print("Continue...")
        else:
            print("check the values.")


