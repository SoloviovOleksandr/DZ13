import random
from random_words import RandomWords
int_list = []
float_list = []
str_list = []

w = RandomWords()

def create_int_list(k):
     for k in range(0,k):
      int_list.append(random.randint(0,1000))
     return int_list

def create_float_list(k):
      for k in range(0,k):
          float_list.append(random.uniform(0.1, 100.0))
      return float_list
def creat_str_list(k):
    for k in range(0,k):
        str_list.append(w.random_word())
    return str_list

print("Int List", create_int_list(1000))
print("Float List", create_float_list(100))
print("String List", str_list)