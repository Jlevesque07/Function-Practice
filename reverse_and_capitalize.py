# TASK: Write a function that reverses a word and capitalizes it.

# Define a function that takes a string parameter
def reverser(word: str) -> str:
    reverse = word[-1::-1]
    return reverse.upper()
# Create an empty string to store the reversed word
# Loop through each character in the word
# Add each character to the front of the new string
# Convert the reversed word to uppercase
# Return the final result
# Prompt the user for input and call the function
# Display the transformed word
print(reverser(input("Enter a word. ")))