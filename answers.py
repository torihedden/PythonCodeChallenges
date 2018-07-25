# http://codingbat.com

# Warmup-1 > sleep_in 

# def sleep_in(weekday, vacation):
#   if vacation == True or weekday == False:
#     return True
#   else:
#     return False


# Warmup-1 > monkey_trouble

# def monkey_trouble(a_smile, b_smile):
#   if a_smile == b_smile:
#     return True
#   else:
#     return False


# Warmup-1 > sum_double 

# def sum_double(a, b):
#   if a == b:
#     return 2 * (a + b)
#   else:
#     return a + b


# Warmup-1 > diff21 
# Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.

# def diff21(n):
#   if n > 21:
#     return 2 * (n - 21)
#   else:
#     return 21 - n

# print(diff21(25))


# Warmup-1 > front_back 

# def front_back(str):
#   if len(str) == 1:
#     return str
#   else:
#     return str[-1:] + str[1:-1] + str[0:1]


# Warmup-1 > parrot_trouble 
# We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.

# def parrot_trouble(talking, hour):
#   if talking == True and (hour < 7 or hour > 20):
#     return True
#   else:
#     return False

# print(parrot_trouble(True, 6))

# def parrot_trouble(talking, hour):
#   if talking == True and not (6 < hour < 21):
#     return True
#   else:
#     return False


# Warmup-1 > makes10

# def makes10(a, b):
#   if a == 10 or b == 10:
#     return True
#   elif a + b == 10:
#     return True
#   else:
#     return False


# Warmup-1 > near_hundred 

# def near_hundred(n):
#   if 90 <= n <= 110 or 190 <= n <= 210:
#     return True
#   else:
#     return False


# Warmup-1 > pos_neg 

# def pos_neg(a, b, negative):
#   if negative == True:
#     if a < 0 and b < 0:
#       return True
#     else:
#       return False
#   elif (a < 0 and b >=0) or (a >= 0 and b < 0):
#     return True
#   else:
#     return False


# Warmup-1 > not_string 

# def not_string(str):
#   if str[0:3] == 'not':
#     return str
#   else:
#     return 'not ' + str


# Warmup-1 > missing_char 

# def missing_char(str, n):
#   if n > 0:
#     return str[:n] + str[n+1:]
#   else:
#     return str[1:]
