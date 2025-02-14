# TASK: Write a function that validates an email format.

# Define a function that takes a string parameter
def email_validator(email: str) -> str:
    """Checks if an email is real or not"""
    if "@" in email and email[-4::] == ".com":
        return "True"
    else:
        return False
# Check if '@' is in the email
# Extract the last four characters of the email
# Check if it ends with '.com' or '.net'
# Return True if valid, False otherwise
# Prompt the user for an email input and call the function
# Display whether the email is valid

email = email_validator(input("Please enter your email. "))

if email == "True":
    print("Your email is valid. ")
else:
    print("This is not a valid email. ")