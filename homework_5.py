#3-1. Names: Store the names of a few of your friends in a list called names . Print each person’s name by accessing
#each element in the list, one at a time .

names = ['Gina', 'Cody', 'Kyle', 'Bryan']
print(names)

#3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a
#message to them . The text of each message should be the same, but each message should be personalized with the
#person’s name .
names = ['Gina', 'Cody', 'Kyle', 'Bryan']
message = "My friend is " + names[0].title() + "."
print(message)
message = "My friend is " + names[1].title() + "."
print(message)
message = "My friend is " + names[2].title() + "."
print(message)
message = "My friend is " + names[3].title() + "."
print(message)

#3-3. Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that
#stores several examples . Use your list to print a series of statements about these items, such as “I would like to
#own a Honda motorcycle .”

transportation = ['truck', 'corvette', 'motorcycle', 'jet']
message = "My favorite car to drive is a " + transportation[0].title() + "."
print(message)
message = "My favorites sport car is a " + transportation[1].title() + "."
print(message)
message = "My dad has owned a " + transportation[2].title() + "."
print(message)
message = "The fastest mode of transportation is " + transportation[3].title() + "."
print(message)

#3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that
#includes at least three people you’d like to invite to dinner . Then use your list to print a message to each person,
#inviting them to dinner .

dinner = ['Michael Jordan', 'LeBron James', 'Kobe Bryant']
message = "Dear " + dinner[0].title() + ", will you please accept this invitation to dinner?"
print(message)
message = "Dear " + dinner[1].title() + ", will you please accept this invitation to dinner?"
print(message)
message = "Dear " + dinner[2].title() + ", will you please accept this invitation to dinner?"
print(message)
message = "Unfortunately, " + dinner[2].title() + " will not be able to make it to dinner."
print(message)

#3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a
#new set of invitations . You’ll have to think of someone else to invite .
#•	Start with your program from Exercise 3-4 . Add a print statement at the end of your program stating the name of
#the guest who can’t make it .
#•	Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are
#inviting .
#•	Print a second set of invitation messages, one for each person who is still in your list .

dinner = ['Michael Jordan', 'LeBron James', 'Shaq']
message = "Dear " + dinner[0].title() + ", will you please accept this invitation to dinner?"
print(message)
message = "Dear " + dinner[1].title() + ", will you please accept this invitation to dinner?"
print(message)
message = "Dear " + dinner[2].title() + ", will you please accept this invitation to dinner?"
print(message)
message = "Dear " + dinner[0].title() + "," " " + dinner[1].title() + ", and " "" + dinner[2].title() + ", we have " \
"found a bigger table and are inviting 3 more people to dinner."
print(message)

#3-6. More Guests: You just found a bigger dinner table, so now more space is available . Think of three more guests to
#invite to dinner .
#•	Start with your program from Exercise 3-4 or Exercise 3-5 . Add a print statement to the end of your program
#informing people that you found a bigger dinner table .
#•	Use insert() to add one new guest to the beginning of your list .
#•	Use insert() to add one new guest to the middle of your list .
#•	Use append() to add one new guest to the end of your list .
#•	Print a new set of invitation messages, one for each person in your list .

dinner = ['Michael Jordan', 'LeBron James', 'Shaq']
dinner.insert(0, 'Russel Westbrook')
dinner.insert(2, 'Kyrie Irving')
dinner.insert(5, 'James Harden')
print(dinner)

message = "Dear " + dinner[0].title() + ", will you please accept this invitation to dinner?"
print(message)
message = "Dear " + dinner[1].title() + ", will you please accept this invitation to dinner?"
print(message)
message = "Dear " + dinner[2].title() + ", will you please accept this invitation to dinner?"
print(message)
message = "Dear " + dinner[3].title() + ", will you please accept this invitation to dinner?"
print(message)
message = "Dear " + dinner[4].title() + ", will you please accept this invitation to dinner?"
print(message)
message = "Dear " + dinner[5].title() + ", will you please accept this invitation to dinner?"
print(message)
message = "Dear " + dinner[0].title() + "," " " + dinner[1].title() + ", " " " + dinner[2].title() + "," \
" " + dinner[3].title() + ", " " " + dinner[4].title() + ", and """ + dinner[5].title() + ", the table will not arrive on" \
" time, and I can therefore only invite 2 of you."
print(message)

#3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and
#you have space for only two guests .
#•	Start with your program from Exercise 3-6 . Add a new line that prints a message saying that you can invite only
#two people for dinner .
#•	Use pop() to remove guests from your list one at a time until only two names remain in your list . Each time you
#pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to
#dinner .
#•	Print a message to each of the two people still on your list, letting them know they’re still invited .
#•	Use del to remove the last two names from your list, so you have an empty list . Print your list to make sure you
#actually have an empty list at the end of your program .

print(dinner)
popped_dinner = dinner.pop(5)
print(dinner)
print(popped_dinner)
last_invited = dinner.pop()
print("I am sorry " + popped_dinner.title() + ", but you are no longer invited.")

#4-1. Pizzas: Think of at least three kinds of your favorite pizza . Store these pizza names in a list, and then use a
#for loop to print the name of each pizza .
#•	Modify your for loop to print a sentence using the name of the pizza instead of printing just the name of the
#pizza . For each pizza you should have one line of output containing a simple statement like I like pepperoni pizza.
#•	Add a line at the end of your program, outside the for loop, that states how much you like pizza . The output
#should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I
#really love pizza!

pizzas = ['pepperoni', 'sausage', 'everything pizza']
for pizza in pizzas:
    print(pizza.title() + " is very good pizza!")

print("I really love pizza!")

#4-2. Animals: Think of at least three different animals that have a common characteristic . Store the names of these
#animals in a list, and then use a for loop to print out the name of each animal .
#•	Modify your program to print a statement about each animal, such as A dog would make a great pet.
#•	Add a line at the end of your program stating what these animals have in common . You could print a sentence such
#as Any of these animals would make a great pet!

animals = ['dog','cat','bird']
for animal in animals:
    print("A " + animal.title() + " is a very good pet!")

print("Any of these animals would make great pets!")

#4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive .

for value in range(1,21):
    print(value)

#4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers .
#(If the output is taking too long, stop it by pressing ctrl-C or by closing the output window .

for value in range(1,1000001):
    print(value)

#4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20 .
#Use a for loop to print each number .

odd_numbers = list(range(1,20,2))
print(odd_numbers)

#4-7. Threes: Make a list of the multiples of 3 from 3 to 30 . Use a for loop to print the numbers in your list .

threes = list(range(3,30,3))
print(threes)

#4-8. Cubes: A number raised to the third power is called a cube . For example, the cube of 2 is written as 2**3 in
#Python . Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for
#loop to print out the value of each cube .

cubes = []
for value in range(1,11):
    cubes.append(value**3)

print(cubes)

#4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes

cubes = [value**3 for value in range(1,11)]
print(cubes)

#4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do
#the following:
#•	Print the message, The first three items in the list are: . Then use a slice to print the first three items from
#that program’s list .
#•	Print the message, Three items from the middle of the list are: . Use a slice to print three items from the middle
#of the list .
#•	Print the message, The last three items in the list are: . Use a slice to print the last three items in the list .

animals = ['dog','cat','bird','snake','fish']

print("The first three items in the list are:")
for animal in animals[0:3]:
    print(animal.title())

print("Three items from the middle of the list are:")
for animal in animals[2:4]:
    print(animal.title())

print("The last three items in the list are:")
for animal in animals[3:5]:
    print(animal.title())

#4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 (page 60) . Make a copy of the list of pizzas,
#and call it friend_pizzas . Then, do the following:
#•	Add a new pizza to the original list .
#•	Add a different pizza to the list friend_pizzas .
#•	Prove that you have two separate lists . Print the message, My favorite pizzas are:, and then use a for loop to
#print the first list . Print the message, My friend’s favorite pizzas are:, and then use a for loop to print the
#second list . Make sure each new pizza is stored in the appropriate list .

pizzas = ['pepperoni', 'sausage', 'everything pizza']
friend_pizzas = pizzas[:]

print("My favorite pizzas are:")
print(pizzas)

print("\nMy friend's favorite pizzas are:")
print(friend_pizzas)

pizzas = ['pepperoni', 'sausage', 'everything pizza']
friend_pizzas = pizzas[:]

pizzas.append('cheese')
friend_pizzas.append('veggie')

print("\nMy favorite pizzas are:")
print(pizzas)

print("\nMy friend's favorite pizzas are:")
print(friend_pizzas)

#4-12. More Loops: All versions of foods.py in this section have avoided using for loops when printing to save space .
#Choose a version of foods.py, and write two for loops to print each list of foods

pizzas = ['pepperoni', 'sausage', 'everything pizza']
for pizza in pizzas:
    print(pizza)

#5-1. Conditional Tests: Write a series of conditional tests . Print a statement describing each test and your
#prediction for the results of each test . Your code should look something like this:

hot_colors = 'red''yellow''orange''white''tan'
print("Is red == 'hot color'? I predict True.")
print(hot_colors == 'red')

print("\nIs blue == 'hot color'? I predict False.")
print(hot_colors == 'blue')

hot_colors = 'red''yellow''orange''white''tan'
print("Is yellow == 'hot color'? I predict True.")
print(hot_colors == 'yellow')

print("\nIs green == 'hot color'? I predict False.")
print(hot_colors == 'green')

hot_colors = 'red''yellow''orange''white''tan'
print("Is orange == 'hot color'? I predict True.")
print(hot_colors == 'orange')

print("\nIs purple == 'hot color'? I predict False.")
print(hot_colors == 'purple')

hot_colors = 'red''yellow''orange''white''tan'
print("Is white == 'hot color'? I predict True.")
print(hot_colors == 'white')

print("\nIs black == 'hot color'? I predict False.")
print(hot_colors == 'black')

hot_colors = 'red''yellow''orange''white''tan'
print("Is tan == 'hot color'? I predict True.")
print(hot_colors == 'tan')

print("\nIs brown == 'hot color'? I predict False.")
print(hot_colors == 'brown')

#5-2. More Conditional Tests: You don’t have to limit the number of tests you create to 10 . If you want to try more
#comparisons, write more tests and add them to conditional_tests.py . Have at least one True and one False result for
#each of the following:
#•	Tests for equality and inequality with strings
#•	Tests using the lower() function •
#Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than
#or equal to
#•	Tests using the and keyword and the or keyword
#•	Test whether an item is in a list


##5-3 Imagine an alien was just shot down in a game . Create a variable called alien_color and assign it a value of
#'green', 'yellow', or 'red' .
#•	Write an if statement to test whether the alien’s color is green . If it is, print a message that the player just
#earned 5 points .
#•	Write one version of this program that passes the if test and another that fails . (The version that fails will
#have no output .)

alien_color = ['green','yellow','red']
if 'green' in alien_color:
    print("You just earned 5 points.")

alien_color = ['green','yellow','red']
if 'yellow' in alien_color:
    print("You just earned 5 points.")

alien_color = ['green','yellow','red']
if 'blue' in alien_color:
    print("You just earned 5 points.")

alien_color = ['green','yellow','red']
if 'red' in alien_color:
    print("You just earned 5 points.")

#5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain .
#  •	If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien .
# •	If the alien’s color isn’t green, print a statement that the player just earned 10 points .
# •	Write one version of this program that runs the if block and another that runs the else block .

alien_color = ['green']
if 'green' in alien_color:
    print("You just earned 5 points for shooting the alien!")
else:
    print("You just earned 10 points")

alien_color = ['blue']
if 'green' in alien_color:
    print("You just earned 5 points for shooting the alien!")
else:
    print("You just earned 10 points")

#5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elifelse chain .
#  •	If the alien is green, print a message that the player earned 5 points .
#  •	If the alien is yellow, print a message that the player earned 10 points .
#  •	If the alien is red, print a message that the player earned 15 points .
#  •	Write three versions of this program, making sure each message is printed for the appropriate color alien .

alien_color = ['green']
if 'green' in alien_color:
    print("That player earned five points")
elif 'yellow' in alien_color:
    print("That player earned ten points")
else:
    print("That player earned fifteen points.")

alien_color = ['yellow']
if 'green' in alien_color:
    print("That player earned five points")
elif 'yellow' in alien_color:
    print("That player earned ten points")
else:
    print("That player earned fifteen points.")

alien_color = ['red']
if 'green' in alien_color:
    print("That player earned five points")
elif 'yellow' in alien_color:
    print("That player earned ten points")
else:
    print("That player earned fifteen points.")

#5-6. Stages of Life: Write an if-elif-else chain that determines a person’s stage of life . Set a value for the variable
#age, and then:
#•	If the person is less than 2 years old, print a message that the person is a baby .
#•	If the person is at least 2 years old but less than 4, print a message that the person is a toddler .
#•	If the person is at least 4 years old but less than 13, print a message that the person is a kid .
#•	If the person is at least 13 years old but less than 20, print a message that the person is a teenager .
#•	If the person is at least 20 years old but less than 65, print a message that the person is an adult .
#•	If the person is age 65 or older, print a message that the person is an elder .

age = 2

if age < 2:
    print('This person is a baby')
elif age >= 2:
    print('This person is a toddler')
elif age < 4:
    print('This person is a toddler')
elif age >= 4:
    print('This person is a kid')
elif age < 13:
    print('This person is a kid')
elif age >= 13:
    print('This person is a teenager')
elif age < 20:
    print('This person is a teenager')
elif age >= 20:
    print('This person is an adult ')
elif age < 65:
    print('This person is an adult')
elif age >= 65:
    print('This person is an elder')

#5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of independent if statements that
#check for certain fruits in your list .
#•	Make a list of your three favorite fruits and call it favorite_fruits .
#•	Write five if statements . Each should check whether a certain kind of fruit is in your list . If the fruit is in
#your list, the if block should print a statement, such as You really like bananas!

fruits = ['apples', 'kiwis', 'grapes']
if 'apples' in fruits:
    print("I love fruit.")
if 'oranges' in fruits:
    print("I love fruit.")
if 'bananas' in fruits:
    print("I love fruit.")
if 'kiwis' in fruits:
    print("I love fruit.")
if 'grapes' in fruits:
    print("I love fruit.")

#5-8. Hello Admin: Make a list of five or more usernames, including the name 'admin' . Imagine you are writing code that
#will print a greeting to each user after they log in to a website . Loop through the list, and print a greeting to each
#user:
#•	If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
#•	Otherwise, print a generic greeting, such as Hello Eric, thank you for logging in again.

usernames = ['admin','person1','person2','peson3','person4']
if 'admin' in usernames:
        print('Hello admin, would you like to see a status report?')
else:
    print('Hello Eric, thank you for logging in again')

usernames = ['person0','person1','person2','peson3','person4']
if 'admin' in usernames:
        print('Hello admin, would you like to see a status report?')
else:
    print('Hello Eric, thank you for logging in again')

#5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty .
#•	If the list is empty, print the message We need to find some users!
#•	Remove all of the usernames from your list, and make sure the correct message is printed .

usernames = ['']
if 'admin' in usernames:
    print('Hello admin, would you like to see a status report?')
else:
    print('We need to find some users!')

#5-10. Checking Usernames: Do the following to create a program that simulates how websites ensure that everyone has a
#unique username .
#•	Make a list of five or more usernames called current_users .
#•	Make another list of five usernames called new_users . Make sure one or two of the new usernames are also in the
#current_users list .
#•	Loop through the new_users list to see if each new username has already been used . If it has, print a message that
#the person will need to enter a new username . If a username has not been used, print a message saying that the
#username is available .
#•	Make sure your comparison is case insensitive . If 'John' has been used, 'JOHN' should not be accepted .

current_users = ['user1','user2','user3','user4','user5']
new_users = ['user1','new2','user3','new4','new5']

for new_user in new_users:
    if new_user in current_users:
        print("The user named " + new_user + " needs to enter a new username.")
else:
    print("The username " + new_user + " is available.")

print("\nCongrats, you are online!")


