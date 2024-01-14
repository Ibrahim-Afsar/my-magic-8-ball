# import the library random
import random

# title and instructions
print("Welcome to My Magic 8 ball!")
print("Ask the ball any question then type shake to get an answer")

# random number generator
random_number = random.randint(0, 7)

# answers that the user can get
ans =("That will prove to be beneficial for you!",
"Stay as far as you can from it!",
"That seems about right",
"That will help you grow as a person a lot",
"If I were you, I would go nuts!",
"Are you mad???",
"I think you should ask your parents about that",
"Please dont do that")

# taking the user's question
question = input("\nPlease ask your question from the Magic 8 ball: \n")
print("shaking...\n" *4)

# give the random answer to the user
print(ans[random_number])
input(" ")
