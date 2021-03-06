import pyperclip
import string
import random

global users_list
class Credentials:
    """
    This class generates new instances of contacts
    """
    credentials_list = []  # empty list of stored credentials.
    user_cred_list = []
    @classmethod
    def validate_user(cls,first_name,password):
        '''
        checks if the name and password entered are correct
        '''
        current_user = ''
        for user in User.users_list:
            if(user.first_name == first_name and user.password == password):
                current_user = user.first_name
        return current_user

    def __init__ (self,first_name,platform_name,ac_name,password):
        '''
        for each object created, its properties
        '''

        self.first_name =  first_name
        self.platformname = platform_name
        self.ac_name = ac_name
        self.password = password

    def save_cred(self):
        '''
        saves a new credential
        '''
        
        Credentials.credentials_list.append(self)
    
    def delete_credential(self):
        '''
        Deletes a credential added
        '''
        Credentials.credentials_list.remove(self)

    def generate_passkey(char=string.ascii_uppercase+string.digits):
        '''
        generates 10 character passkey
        '''
        key_pass =''.join(random.choice(char) for _ in range(0,10))
        return key_pass


    @classmethod
    def get_site_name(cls,site_name):
        '''
        takes a site name and returns creds
        '''
        for credential in cls.credentials_list:
            if credential.site_name == site_name:
                return credential
    
    @classmethod
    def copy_cred(cls,site_name):
        find_cred = Credentials.get_site_name(site_name)
        return pyperclip.copy(find_cred.password)

    @classmethod
    def show_cred(cls,first_name):
        ''''
        shows all credentials
        '''
        user_cred_list = []
        for credential in cls.credentials_list:
            if credential.first_name == first_name:
                user_cred_list.append(credential)
        return user_cred_list

    
class User:
    '''
    This class creates user accounts
    '''
    users_list = []
    def __init__(self, first_name,lastname,password):
        '''
        properties for each user
        '''

        #instances
        self.first_name = first_name
        self.lastname = lastname
        self.password = password
    
    def save_usr(self):
        '''
        saves a newly created user
        '''
        User.users_list.append(self)

    @classmethod
    def show_cred(cls,first_name):
        ''''
        shows all credentials
        '''
        user_cred_list = []
        for credentials in cls.credentials_list:
            if credential.first_name == first_name:
                user_cred_list.append(credentials)
        return user_credentials_list
    
        
    
