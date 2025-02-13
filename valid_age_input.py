# TASK: Write a function that asks for a valid age input and handles invalid inputs.

# Define a function that takes one string parameter
def age_var(q: str) -> int:
    # Create a loop that keeps asking for input until a valid age is entered
    while True:
        try:
            # Try to convert the input to an integer
            age = int(input(q))
            # If successful, check if the number is positive
            if age > 0:
                # If valid, return the number
                return age
            else: 
                print("Please input a valid number." )
        # If not valid, show an error message and prompt again
        except ValueError:
            print("Please input a number." )

# Call the function and store the result
userage = age_var("Enter your age: ")

# Display the valid age
if userage == 1:
    print(f"You are one year old. ")
else:
    print(f"You are {userage} year(s) old." )