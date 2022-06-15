from django.test import TestCase
from .models import Profile,Projects,Review
from django.contrib.auth.models import User
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
        User.objects.create(id=1,username='Hypebeast',email = 'Oscar@gmail.com')
        Profile.objects.create(id=1,profile_photo='image/upload/v1655038396/fbn9op5jgdyqs0vv55g0.jpg',bio='Mans a beast',linkedin='https://www.linkedin.com/in/jeff-owuor-a0074a224/',github='https://github.com/Jeff-Owuor',user_id=1)
        Projects.objects.create(id=2,project='image/upload/v1655109327/dwyenacgbnrdmsh9hd10.jpg',project_title='Welcome to Kenya',project_description='this is basically a gallery showcasing various beautiful images of our country Kenya.',site_link='https://welcometokenya.herokuapp.com/',score=0,user_id=1)
        
    
    def test_instance(self):
        project = Projects.objects.get(id=2)
        self.assertTrue(isinstance(project,Projects))
        
    def test_save_project(self):
        project = Projects.objects.get(id=2)
        project.save_post()
        projo = Projects.objects.all()
        self.assertTrue(len(projo) > 0)
        
    def test_get_posts(self):
        project = Projects.objects.get(id=2)
        project.save_post()
        posts = Projects.all_projects()
        self.assertTrue(len(posts) > 0)

    def test_search_post(self):
        project = Projects.objects.get(id=2)
        project.save_post()
        post = Projects.search_project('Welcome to Kenya')
        self.assertTrue(len(post) > 0)

    def test_delete_post(self):
        project = Projects.objects.get(id=2)
        project.save_post()
        project.delete_project()
        post = Projects.search_project('test')
        self.assertTrue(len(post) < 1)
        
        
class RatingTestCase(TestCase):
    '''
    Class that test rating model
    '''
    def setUp(self):
        Profile.objects.create(id=1,profile_photo='image/upload/v1655038396/fbn9op5jgdyqs0vv55g0.jpg',bio='Mans a beast',linkedin='https://www.linkedin.com/in/jeff-owuor-a0074a224/',github='https://github.com/Jeff-Owuor',user_id=1)
        User.objects.create(id=1,username='Hypebeast',email = 'Oscar@gmail.com')
        Projects.objects.create(id=2,project='image/upload/v1655109327/dwyenacgbnrdmsh9hd10.jpg',project_title='Welcome to Kenya',project_description='this is basically a gallery showcasing various beautiful images of our country Kenya.',site_link='https://welcometokenya.herokuapp.com/',score=0,user_id=1)
        Review.objects.create(id=1,body='The design is above average',project_id =2,user_id=1,rate_design=6,rate_content=0,rate_usability=0)

    def test_instance(self):
        review = Review.objects.get(id=1)
        self.assertTrue(isinstance(review,Review))
        
    def test_save_rating(self):
        review = Review.objects.get(id=1)
        review.save()
        rating = Review.objects.all()
        self.assertTrue(len(rating) > 0)
        
    def test_get_post_rating(self):
        rating = Review.get_ratings(2)
        self.assertTrue(len(rating) == 1)
