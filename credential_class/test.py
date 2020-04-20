import unittest #Importing the unittest module
from credentialclass import User, Credentials  #importing the credentials class
import pyperclip

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines the test cases for our credentials and accounts.


    Args:
        unittest.TestCase: TestCase class that helps in running the test cases.
    '''    

def setUp(self):
    '''
    method to run before each test case.
    '''

    self.new_cred = User("Gerald","Mwanu","12345")

def test_init(self):
    '''
    testing for initialization
    '''
    self.assertEqual(self.new_cred.username,"Gerald")
    self.assertEqual(self.new_cred.lastname,"Mwanu")
    self.assertEqual(self.new_cred.password,"12345")

def test_save_credentials(self):
    '''
    tests if the credentials object is being saved into the list of contacts
    '''

    self.new_cred.save_credentials()   #saves the new credentials keyed in
    self.asserEqual(len(Credentials.credentials_list),1)

class TestUsr(unittest.TestCase):
    '''
    test cavse for user class behaviour
    
    Args:
    unittest.TestCase: creates test classes
    '''
    def setUp(self):

        self.new_usr = User("Gerald", "Mwanu", "12345")

    def test__iniit__(self):
        '''
        checks initialization of new instances
        '''
        self.asserEqual(self.new_usr.firstname,'Gerald')
        self.assertEqual(self.new_usr.lastname,'Mwanu')
        self.assertEqual(SELF.new_usr.password,'12345')

    def test_save_usr(self):
        '''
        Test for saved user
        '''


        self.new_usr.save_usr()
        self.assertEqual(len(User.users_list),1)





if __name__ == '__main__':
    unittest.main()
