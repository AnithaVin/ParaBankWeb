import time
import unittest
from pages.signup import signup
import pytest


@pytest.mark.usefixtures("setup")
class signupPage(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObject(self):
        self.sp = signup(self.driver)

    def test_navagte(self):
        self.sp.nevagate_reg_page() #called method here from signup page
        time.sleep(60)