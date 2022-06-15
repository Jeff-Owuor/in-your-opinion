from django.test import TestCase
from .models import *
# Create your tests here.

class TestProfile(TestCase):
    def setUp(self):
        self.user = User(id=1, username='Hypebeast')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()


class ProjectTestClass(TestCase):
    '''
    Class that tests Project model
    '''
    def setUp(self):
        self.project = Projects(project_title='Landing page', project_description='This is the greatest show')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.project, Projects))
        
        
class RatingTestClass(TestCase):
    '''
    Class that test rating model
    '''
    def setup(self):
        self.rates = Review(rate_design=10,rate_usability=10, rate_content=10)

    def test_instance(self):
        self.assertTrue(isinstance(self.rates, Review))
