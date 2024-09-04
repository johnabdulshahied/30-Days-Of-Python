import random
import string

def user_id_gen_by_user(n,count): # 1.2 - user_id_gen_by_user() function
    for i in range(count):
        print(''.join(random.choices(string.ascii_letters + string.digits,k=n)))

user_id_gen_by_user(n = int(input('Enter number of characters: ')),count = int(input('Enter count: ')))


def rgb_color_gen():    # 1.3 - rgb_color_gen() function
    return f'rgb({random.randint(0,255)},{random.randint(0,255)},{random.randint(0,255)})'

print(rgb_color_gen())


def unique_rand_numbers(): # 3.3 - unique_rand_numbers() function
    return random.sample(range(10),k = 7)

print(unique_rand_numbers())
