# Script to register users pools password manager (locally)

from cryptography.fernet import Fernet
import os
import banners
import functions
import random 
import string
import time


def register():
	POOLS_PATH = os.getcwd()
	NODE_USERNAME = os.getlogin()
	functions.clear_screen()
	banners.register_banner()
	
	CAPITAL = string.ascii_uppercase
	LOWERCASE = string.ascii_lowercase
	NUMBERS = string.digits
	RAND_CHAR = string.punctuation
	LENGTH = 8
	
	combo = CAPITAL + LOWERCASE + NUMBERS + RAND_CHAR
	
	password = ''
	for i in range(LENGTH):
		a=random.choice(combo) 
		password += a 

	password_encoded = password.encode()
	key = Fernet.generate_key()
	key_f = Fernet(key)
	encrypted_password = key_f.encrypt(bytes(password_encoded))
		
	hash_decoded=f'{encrypted_password.decode()}'
	key_decoded=(f'key: {key.decode()}')

	time.sleep(1)
	print(f'    Your key: {key_decoded}')
	print(f'\n    [:] Key stored in Desktop! ')
	print('    [:] Re-run python main.py!! ')

	time.sleep(2)

	os.chdir(f'C:\\Users\\{NODE_USERNAME}')
	try:
	    os.mkdir('Secrets')
	except:
	    os.chdir(f'C:\\Users\\{NODE_USERNAME}\\Secrets')
	    with open('secret.txt', 'w') as login:
	        login.write(f'{hash_decoded}')

		
	os.chdir(f'C:\\Users\\{NODE_USERNAME}\\Desktop')
	with open('key.txt', 'w') as key:
		key.write(f'{key_decoded}')

	os.chdir(POOLS_PATH)
	functions.re_write_banner()
