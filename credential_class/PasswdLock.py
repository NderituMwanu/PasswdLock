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

def generate_passkey():
	'''
	Function to generate a password automatically
	'''
	form_key = Credentials.generate_passkey()
	return form_key

def create_credential(first_name,site_name,ac_name,password):
	'''
	Function to create a new credential
	'''
	new_credential=Credentials(first_name,site_name,ac_name,password)
	return new_credential

def save_cred(credential):
	'''
	Function to save a newly created credential
	'''
    
	Credentials.save_cred(credential)

def show_cred(first_name):
	'''
	Function to display credentials saved by a user
	'''
	return Credentials.show_cred(first_name)
	
def copy_cred(site_name):
	'''
	Function to copy a credentials details to the clipboard
	'''
	return Credentials.copy_cred(site_name)


def main():
	print(' ')
	print(' *******************************************PASSWORD LOCKER*****************************************')
	while True:
		print("-"*100)
		print('Select an Option: \n c --> Create an Account \n l --> Log In \n x --> Exit')
		short_code = input('Key in your Choice: ').lower().strip()
		if short_code == 'x':
			break

		elif short_code == 'c':
            
			print("-"*100)
			print('For  a NEW ACCOUNT:')
			first_name = input('Key in your First Name: ').strip()
			last_name = input('Key in your Last Name: ').strip()
			password = input('Key in your desired Passcode/Passkey - ').strip()
			save_usr(create_user(first_name,last_name,password))
			
			print(f'Congratulations! A New Account has been created for: {first_name} {last_name}. Your login password is: {password}')
		elif short_code == 'l':
			print("-"*100)
			print(' ')
			print('To login, enter your account details:')
			first_name = input('Enter your first name - ').strip()
			password = str(input('Enter your password - '))
			user_exists = validate_user(first_name,password)
			if user_exists == first_name:
				
               
				print(f'Account Owner: {first_name}.')
				print(' ')
				while True:
					print("-"*100)
					print('Key in any of the following options: \n createc ---> Create a Credential \n dispcred ---> Display Credentials \n Cp ---> Copy Password \n x ---> Exit')
					short_code = input('Enter a choice: ').lower().strip()
					print("-"*100)
					if short_code == 'x':
						print(" ")
						print(f'Successful logout for: {first_name}')
						break
					elif short_code == 'createc':
						print(' ')
						print('Enter your credential details:')
						site_name = input('Enter the site\'s name- ').strip()
						ac_name = input('Enter your account\'s name - ').strip()
						while True:
							print(' ')
							print("-"*100)
							print('Choose from selecting a key or have it generated for you: \n ep ---> Key in The password you created  \n gp ---> Get generated passcode/key/word \n ex ---> exit')
							psw_choice = input('Enter an option: ').lower().strip()
							print("-"*100)
							if psw_choice == 'ep':
								print(" ")
								password = input('Key in your Passcode/key/word: ').strip()
								break
							elif psw_choice == 'gp':
								password = generate_passkey()
								break
							elif psw_choice == 'ex':
								break
							else:
								print('Make another attempt.Sorry.')
						save_cred(create_credential(first_name,site_name,ac_name,password))
						print(' ')
						print(f'Credentials made: Site Name: {site_name} -- Account Name: {ac_name} --Password: {password}')
						print(' ')
					elif short_code == 'dispcred':
						print(' ')
						if show_cred(first_name):
							print('All your credentials:')
							print(' ')
							for credential in show_cred(first_name):
								print(f' Account Name: {credential.ac_name} -- Password: {credential.password}')
							print(' ')	
						else:
							print(' ')
							print("No credentials saved!")
							print(' ')
					elif short_code == 'cp':
						print(' ')
						selected_site = input('Key in the name of the site you need to copy: ')
						copy_cred(selected_site)
						print('')
					else:
						print('Oops! Wrong option entered. Try again.')
				





if __name__ == '__main__':
	main()

