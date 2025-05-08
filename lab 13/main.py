import puppy
import puppy_state
import check_input


def main():

    pup = puppy.Puppy()

    print("Congratulations on your new puppy!")

    userQuit = False



    while not userQuit:

        print("""1. Feed the puppy \n2. Play with the puppy \n3. Quit""")

        userChoice = check_input.get_int_range("Enter Choice: ", 1, 3)

        if userChoice == 1:
            print(pup.give_food())

        if userChoice == 2:
            print(pup.throw_ball())

        if userChoice == 3:
            userQuit = True

       

main()