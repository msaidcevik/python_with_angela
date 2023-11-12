# This program takes two inputs. The first input is stored in a variable called a.
# The secnd input is stored in a variable called b.
# Write a program that switches the values stored in the variables a and b.
# Your program should work for differents inputs.
'''
Example input
39
41

Outputs
a: 39
b:41

'''
a = input("What is your name ? ")
b = input("How old are you ? ")

# If you want to switch, you need a third variable
c = a
a = b
b = c

print("a: " + a)
print("b: " + b )