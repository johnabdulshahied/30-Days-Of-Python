import random
import string

def user_id_gen_by_user(n,count): # 2 - user_id_gen_by_user function
    for i in range(count):
        print(''.join(random.choices(string.ascii_lowercase + string.digits,k=n)))

user_id_gen_by_user(n = int(input('Enter number of characters: ')),count = int(input('Enter count: ')))
