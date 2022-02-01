# this is a password generator
# Tell the digits and it will customize your password according to the choice

import string
import random

alpha=list(string.ascii_letters)
digit=list(string.digits)
special_char=list("~`!@#$%^&*()")
char=list(string.ascii_letters + string.digits + "~`!@#$%^&*()")

def rand_pass():
  length=int(input("Enter Password length"))
  alpha_count=int(input("Enter number of alphabets")) #Should be less than length
  digit_count=int(input("Enter number of digits")) # Should be less than length
  special_char_count=int(input("Enter number of Special characters")) # All of these should add up to length if you want the correct result
  char_count = alpha_count + digit_count + special_char_count
  if char_count > length:
    alpha_count = alpha_count//3
    digit_count = digit_count//3
    special_char_count = special_char_count//3
    char_count= alpha_count + digit_count + special_char_count
  password = []
  for a in range(alpha_count):
    password.append(random.choice(alpha))
  for b in range(digit_count):
    password.append(random.choice(digit))
  for c in range(special_char_count):
    password.append(random.choice(char))
  if char_count < length:
    random.shuffle(char)
    for i in range(length - char_count):
      password.append(random.choice(char))
  random.shuffle(password)
  print("".join(password))
  pass_len = len(password)
  print(f"Total number of characters in the password is {pass_len}")

 

rand_pass()


#Sample Output
#Enter Password length 50
#Enter number of alphabets 23
#Enter number of digits 5
#Enter number of Special characters 12
#zftWrYk7Gavvx^7vM%a~8H6j`QcvnG%oX8N7IfMJ69iQyTVip5
#Total number of characters in the password is 50
