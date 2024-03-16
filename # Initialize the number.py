# Initialize the number
num = 1578

# Initialize the sum and position
sum_of_digits = 0
position = 1

# Reverse the number first to multiply each digit by its position correctly
reversed_num = 0
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10

# Now, calculate the sum of digits each multiplied by its position
num = reversed_num  # Work with the reversed number
while num > 0:
    digit = num % 10
    sum_of_digits += digit * position
    num = num // 10
    position += 1

# Display the result
print(f"The sum of digits of the number 1578, with each digit multiplied by its position, is: {sum_of_digits}")
