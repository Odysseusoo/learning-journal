# Ask user for their name 
name = input ("What is your name?").strip().title()

#Split user's name into first and last name
first, last = name.split(" ")

#Say hello to the user
print (f"hello, {first}")




