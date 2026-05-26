text = input ("Input: ")
result = ""

for char in text:
    if char not in "aeiouAEIOU":
        result += char

print (f"Output: {result}")
