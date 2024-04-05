# Login function for pools password manager

from cryptography.fernet import Fernet 	 
import hashlib
import functions 
import time
import os

def vault_unlocked():
	functions.clear_screen()
	vault = input('''

	Welcome to your vault, here you can access your passwords. This is a safe place. 

	1) Add logins 
	2) View logins


	VAULT: ''')
	if vault == '1':
		website = input('\n        Enter website: ')
		username = input('\n	Enter username: ')
		password = input('\n	Enter password: ')

		USER = os.getlogin()
		os.chdir(f'C:\\Users\\{USER}\\Secrets')
		with open('contents.txt', 'a') as content:
			content.write(f''' Encrypted text: 
 {website}\n {username}\n {password}
		''')


def login():
	functions.clear_screen()
	print('''    
   	

    8""""8    l o g i n      login      ## USE GENERATED KEY! ##  
    8    8 eeeee eeeee e     eeeee L
    8eeee8 8  88 8  88 8     8   " O 	 
    88     8   8 8   8 8e    8eeee G		  
    88     8   8 8   8 88       88 I	
    88     8eee8 8eee8 88eee 8ee88 N



		''')
	user = os.getlogin()
	with open(f'C:\\Users\\{user}\\Secrets\\secret.txt', 'r') as secret:
		hashed = secret.readline()

	try:
		key = input('    | Enter KEY: ')
		key_ = Fernet(key)

		data = key_.decrypt(bytes(hashed.encode()))
		#print(help(Fernet.decode()))
		print('\n     SUCCESS!')
		time.sleep(2)
		vault_unlocked()
	except:
		print('\n     Invalid KEY!')
		time.sleep(2)
		login()
