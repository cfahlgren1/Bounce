from django.test import TestCase

from ..forms import EmailSignupForm
from ..models import Signup


class SignupTests(TestCase):
    def test_duplicate_email_signup(self):
        """
            If an existing email is used, an appropriate error message is thrown.
        """
        email = "valid@email.com"

        signup_form = EmailSignupForm(data={'email': email})
        signup_form.is_valid()
        
        signup = Signup()
        signup.email = email
        signup.save()

        response = self.client.post("", {"email": email})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "valid@email.com is already registered.")
