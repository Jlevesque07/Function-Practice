# TASK: Write a function that converts between Celsius and Fahrenheit.

def temp_converter(unit: str) -> int:
    """Function takes input of celcius or farenheight, and outputs the opposite."""
    if unit == "c":
        temp1 = int(input("What is your temperature in degrees Celcius? "))
        temp2 = (temp1 * 9/5) + 32
        print(f"That temperature in degrees Farenheit is {temp2}. ")
    else:
        temp1 = int(input("What is your temperature in degrees Farenheit? "))
        temp2 = (temp1 - 32) *5/9 
        print(f"That temperature in degrees Celcius is {temp2}. ")


temp_converter(input("Do you want to convert a temperature in degrees Celcius or farenheight? [c/f] ").strip().lower())
 