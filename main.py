## Main menu for pools password manager


import login
import banners
import register
import functions
import os

def main():
	banners.banner1()
	main_menu = input(f'    [>] ')
	if main_menu == '1':
		register.register()
	elif main_menu == '2':
		exit()


main()
