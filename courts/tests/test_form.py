from django.test import TestCase
from ..forms import EmailSignupForm
from ..models import Signup

class SignupFormTest(TestCase):
    def signup_form(self, email: str) -> EmailSignupForm:
        return EmailSignupForm(data={'email': email})

    def test_signup(self):
        signup = self.signup_form(email='user@dummy.com')
        self.assertTrue(signup.is_valid())
        self.assertTrue(isinstance(signup, EmailSignupForm))


    def test_duplicate_email(self):
        signup = self.signup_form(email='user@dummy.com')
        signup.is_valid()
        
        new_signup = Signup()
        new_signup.email = 'user@dummy.com'
        new_signup.save()

        duplicate_signup = self.signup_form(email='user@dummy.com')
        self.assertFalse(duplicate_signup.is_valid())

        error = {'email': ['Signup with this Email already exists.']}
        self.assertEqual(duplicate_signup.errors, error)
