# Login function for pools password manager

from cryptography.fernet import Fernet 	 
import hashlib
import functions 
import time

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
	with open(r'C:\Users\h0hr\Secrets\login_hash.txt', 'r') as secret:
		hashed = secret.readline()

	try:
		key = input('    | Enter KEY: ')
		key_ = Fernet(key)

		data = key_.decrypt(bytes(hashed.encode()))
		#print(help(Fernet.decode()))
		print('\n     SUCCESS!')
	except:
		print('\n     Invalid KEY!')
