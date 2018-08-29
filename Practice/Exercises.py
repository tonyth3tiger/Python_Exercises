import random


'''All exercises and solutions are at https://www.practicepython.org/
This project is for practice and learning Python from scratch.'''

def character_input():###returns a string based on user input
    name = input("Please enter your name: ")
    age = input("Please enter your age: ")
    timer = 100 - int(age)
    if int(age) <= 100:
        print (name + " you will turn 100 in " + str(timer) + " years")
    else:
        print(name + ", you are already over 100!")

def multiple_numbers():###prints a number as many times as the user tells it to
    number = input("Please enter a number: ")
    multiple = input("How many times would you like it printed: ")

    while int(multiple) > 0:
        print(number + "\n")
        multiple = int(multiple) - 1

def odd_even():###determines if user inputted number is even, odd, or divisible by 4
    number = input("Enter a number: ")
    if int(number) % 2 is 0 and int(number) % 4 is 0:
        print(number + " is even and a multiple of 4.")
    elif int(number) % 2 is 0:
        print(number + " is even")
    else:
        print(number + " is odd.")
def check_num():###checks if a user input is divisible by another user input number
    num = input("Enter a number: ")
    check = input("Enter another number: ")
    if int(num) % int(check) is 0:
        print(check + " divides perfectly into " + num)
    else:
        print(check + " does not divide perfectly into " + num)

def less_than_ten():######does not work. Need to solve this one. Exercise 3
    list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    ans = range(0,11)
    for x in list[range(10)]:
        ans.copy()
    print(ans)

def divisors():###finds all numbers that divide into user inputted number
    num = int(input("Enter a number: "))
    div = range(1 , num+1)
    for ans in div:
        if num % ans is 0:
            print(ans)

def list_overlap():###compares 2 randomly generated lists and returns numbers in both lists.
    list_a = []
    list_b = []

    for x in range(random.randint(1,50)):#randomly generates a range for the size of the lists
        list_a.append(random.randint(1,50))#adds a random int to the list
        list_b.append(random.randint(1,50))#adds a random int to the list

    #Code after learning about sets.
    print(set(list_a) & set(list_b))

    #Code before learning about sets.
    """final_list_a = []
    final_list_b = []


    #removes duplicates from the lists
    for num in list_a:
        if num not in final_list_a:
            final_list_a.append(num)

    for num in list_b:
        if num not in final_list_b:
            final_list_b.append(num)

    #prints the lists so user can verify
    print(final_list_a)
    print(final_list_b)


    #uses the longer list to compare since there will be more elements to compare.
    if len(final_list_a) > len(final_list_b):
        for x in final_list_a:
            if x in final_list_b:
                print(x)

    else:
        for x in final_list_b:
            if x in final_list_a:
                print(x)"""

def string_lists():
    string = input("Enter a word: ")
    reverse = string[::-1]

    if reverse.upper() == string.upper():
        print(string + " is a palindrome.")
    else:
        print(string + " is not a palindrome.")


def list_comprehension():
    a = [rand for x in range(random.randint(1,50))]

    print(a)

    even = [num for num in a if num % 2 == 0]

    print(even)


def rock_paper_scissors():
    r_p_s = {"rock" : 1, "paper" : 2, "scissors" : 3}

    print(r_p_s)

    player1 = int(input("Player 1, enter the number of your choice: "))
    player2 = int(input("Player 2, enter the number of your choice: "))

    #god this is ugly
    if player1 is 1:
        if player2 is 1:
            print("It's a tie!")
        if player2 is 2:
            print("Player 2 wins!")
        if player2 is 3:
            print("Player 1 wins!")

    elif player1 is 2:
        if player2 is 1:
            print("Player 1 wins!")
        if player2 is 2:
            print("It's a tie!")
        if player2 is 3:
            print("Player 2 wins!")

    elif player1 is 3:
        if player2 is 1:
            print("Player 2 wins!")
        if player2 is 2:
            print("Player 1 wins!")
        if player2 is 3:
            print("It's a tie!")

    else:
        print("This game is broken")


def guessing_game_1():
    print("Welcome to the Guessing Game Part 1!")

    def game_guess():

        ans = random.randint(1, 10)
        user = 0

        while user is not ans:


            user = input("Now enter your guess: ")

            if int(user) > ans:
                print("Your guess is too high. (Enter 'exit' to quit")
                user = user

            elif int(user) < ans:
                print("Your guess is too low. (Enter 'exit' to quit")
                user = user

            elif user == 'exit':
                break

            else:
                print("That's correct!")
                again = input("Would you like to play again? y/n: ")

                if again is 'y':
                    game_guess()
                else:
                    print("Thanks for playing.")
                    break

    game_guess()



guessing_game_1()