# Conditional statement if,else
# Check if a number is positive, negative, or zero
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
# Loop (for loop)
# Print numbers from 1 to 5
for i in range(1, 6):
    print(i)
#(While loop)
# Print numbers until user enters 0
number = int(input("Enter a number (0 to stop): "))

while number != 0:
    print("You entered:", number)
    number = int(input("Enter again (0 to stop): "))

print("Loop ended.")
# (do while loop )
# Simulating a do-while loop in Python

while True:
    num = int(input("Enter a number (0 to exit): "))
    print("You entered:", num)

    # Condition to stop (like while condition in do-while)
    if num == 0:
        break
