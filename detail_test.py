import unittest  # Importing the unittest module
import pyperclip

from detail import Detail  # Importing the detail class


class TestDetail(unittest.TestCase):
    # import pyperclip
    '''
    Test class that defines test cases for the detail class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
 # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_detail = Detail(
            "xyz", "xyz", "2222222222", "xyz@user.com")  # create detail object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_detail.user_name, "xyz")
        self.assertEqual(self.new_detail.user_name, "xyz")
        self.assertEqual(self.new_detail.account_password, "2222222222")
        self.assertEqual(self.new_detail.email, "xyz@user.com")
    
    def test_save_detail(self):
        '''
        test_save_detail test case to test if the detail object is saved into
         the detail list
        '''
        self.new_detail.save_detail()  # saving the new detail
        self.assertEqual(len(Detail.detail_list), 1)
     def test_find_detail_by_password(self):
        '''
        test to check if we can find a detail by account password and display information
        '''

        self.new_detail.save_detail()
        test_detail = Detail("Test", "user", "2222222222",
                               "xyz@user.com")  # new detail
        test_detail.save_detail()

        found_detail = Detail.find_by_password("2222222222")

        self.assertEqual(found_detail.email, test_detail.email)



    def test_detail_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the detail.
        '''

        self.new_detail.save_detail()
        test_detail = Detail("Test", "user", "2222222222",
                               "xyz@user.com")  # new detail
        test_detail.save_detail()

        detail_exists = Detail.detail_exist("2222222222")
        self.assertTrue(detail_exists)


    def test_display_all_details(self):
        '''
        method that returns a list of all details saved
        '''

        self.assertEqual(Detail.display_details(), Detail.detail_list)

    def test_copy_email(self):
        '''
        Test to confirm that we are copying the email address from a found detail
        '''

        self.new_detail.save_detail()
        Detail.copy_email("2222222222")

        self.assertEqual(self.new_detail.email, pyperclip.paste())


if __name__ == '__main__':
    unittest.main()
        