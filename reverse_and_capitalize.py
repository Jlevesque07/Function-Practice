# TASK: Write a function that reverses a word and capitalizes it.

def reverser(word: str) -> str:
    """takes a word input, reverses and capitalizes it"""
    reverse = word[-1::-1]
    return reverse.upper()

print(reverser(input("Enter a word. ")))