#! /usr/bin/env python3
import pyperclip
from credentialclass import User, Credentials

def create_user(fname,lname,password):
	'''
	Function to create a new user account
	'''
	new_user = User(fname,lname,password)
	return new_user

def save_usr(user):
	'''
	Function to save a new user account
	'''
	User.save_usr(user)


def validate_user(first_name,password):
	'''
	Function that verifies the existance of the user before creating credentials
	'''
	checking_user = Credentials.validate_user(first_name,password)
	return checking_user

def generate_password():
	'''
	Function to generate a password automatically
	'''
	gen_pass = Credentials.generate_password()
	return gen_pass

def create_credential(first_name,site_name,ac_name,password):
	'''
	Function to create a new credential
	'''
	new_credential=Credentials(first_name,site_name,ac_name,password)
	return new_credential

def save_cred(first_name,site_name,ac_name,password):
	'''
	Function to save a newly created credential
	'''
    
	return Credentials.save_cred(credential)

def show_cred(first_name):
	'''
	Function to display credentials saved by a user
	'''
	return Credentials.show_cred(first_name)
	
def copy_credential(site_name):
	'''
	Function to copy a credentials details to the clipboard
	'''
	return Credential.copy_credential(site_name)


def main():
	print(' ')
	print(' PASSWORD LOCKER .')
	while True:
		print("-"*60)
		print('Select oprion: \n c-Create an Account \n l-Log In \n x-Exit')
		short_code = input('Enter a choice: ').lower().strip()
		if short_code == 'x':
			break

		elif short_code == 'c':
			print("-"*100)
			print('To create a new account:')
			first_name = input('Enter your first name - ').strip()
			last_name = input('Enter your last name - ').strip()
			password = input('Enter your password - ').strip()
			save_usr(create_user(first_name,last_name,password))
			print(" ")
			print(f'New Account Created for: {first_name} {last_name} using password: {password}')
		elif short_code == 'l':
			print("-"*60)
			print(' ')
			print('To login, enter your account details:')
			first_name = input('Enter your first name - ').strip()
			password = str(input('Enter your password - '))
			user_exists = validate_user(first_name,password)
			if user_exists == first_name:
				print(" ")
				print(f'Welcome {first_name}. Please choose an option to continue.')
				print(' ')
				while True:
					print("-"*60)
					print('Select the following options: \n createc-Create a Credential \n dispcred-Display Credentials \n Cp-Copy Password \n x-Exit')
					short_code = input('Enter a choice: ').lower().strip()
					print("-"*60)
					if short_code == 'x':
						print(" ")
						print(f'Goodbye {first_name}')
						break
					elif short_code == 'createc':
						print(' ')
						print('Enter your credential details:')
						site_name = input('Enter the site\'s name- ').strip()
						ac_name = input('Enter your account\'s name - ').strip()
						while True:
							print(' ')
							print("-"*60)
							print('Please choose an option for entering a password: \n ep-enter existing password \n gp-generate a password \n ex-exit')
							psw_choice = input('Enter an option: ').lower().strip()
							print("-"*60)
							if psw_choice == 'ep':
								print(" ")
								password = input('Enter your password: ').strip()
								break
							elif psw_choice == 'gp':
								password = generate_password()
								break
							elif psw_choice == 'ex':
								break
							else:
								print('Oops! Wrong option entered. Try again.')
						save_cred(create_credential(first_name,site_name,ac_name,password))
						print(' ')
						print(f'Credential Created: Site Name: {site_name} - Account Name: {ac_name} - Password: {password}')
						print(' ')
					elif short_code == 'dispcred':
						print(' ')
						if show_cred(first_name):
							print('Here is a list of all your credentials')
							print(' ')
							for credential in show_cred(first_name):
								print(f'Site Name: {credential.site_name} - Account Name: {credential.ac_name} - Password: {credential.password}')
							print(' ')	
						else:
							print(' ')
							print("You don't seem to have any credentials saved yet")
							print(' ')
					elif short_code == 'cp':
						print(' ')
						chosen_site = input('Enter the site name for the credential password to copy: ')
						copy_cred(chosen_site)
						print('')
					else:
						print('Oops! Wrong option entered. Try again.')
				





if __name__ == '__main__':
	main()

