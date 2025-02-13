# TASK: Write a function that returns a random encouragement message.

# Import the random module
import random

# Define a function with no parameters that returns a string
def fetch() -> str:
    # returns a positive message
    # Create four different message variables
    message1 = "You are awesome!"
    message2 = "I wish I was as cool as you :0"
    message3 = "You shine bright."
    message4 = "Have a good day."
# Generate a random number from 1 to 4
    num = random.randint(1,4)

# Use if-elif statements to return the corresponding message
    if num == 1:
        return message1
    elif num == 2:
        return message2
    if num == 3:
        return message3
    else:
        return message4
# Call the function and print the result
print(fetch())

