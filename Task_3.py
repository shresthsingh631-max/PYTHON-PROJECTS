import string
import random

lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation

All = lower_case+upper_case+numbers+symbols
password_length=9

random = "".join(random.sample(All,password_length))

print(random)
