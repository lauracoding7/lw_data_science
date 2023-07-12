# If statements control the flow of your code
# Your code runs sequentially, and by setting up the correct conditions,
# you can filter the flow through to the desired outcome.

age = int(input("How old are you?")) # need to change DataType from string to int

# Order of if-statements are important
if age >= 18:
    print("You can vote")
elif age >= 21:
    print("You can become president")
else:
    print("Be patient!")
