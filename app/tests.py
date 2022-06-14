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


class PostTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='Hypebeast')
        self.post = Projects.objects.create(id=1, project_title='test post', project='https://ucarecdn.com/0ccf61ff-508e-46c6-b713-db51daa6626e', project_description='desc',
                                        user=self.user, site_link='http://ur.coml')

    def test_instance(self):
        self.assertTrue(isinstance(self.post, Projects))

    def test_save_post(self):
        self.post.save_post()
        post =Projects.objects.all()
        self.assertTrue(len(post) > 0)

    def test_get_posts(self):
        self.post.save()
        posts = Projects.all_posts()
        self.assertTrue(len(posts) > 0)

    def test_search_post(self):
        self.post.save()
        post = Projects.search_project('test')
        self.assertTrue(len(post) > 0)

    def test_delete_post(self):
        self.post.delete_post()
        post = Projects.search_project('test')
        self.assertTrue(len(post) < 1)


class RatingTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='Hypebeast')
        self.post = Projects.objects.create(id=1, title='test post', photo='https://ucarecdn.com/0ccf61ff-508e-46c6-b713-db51daa6626e', description='desc',
                                        user=self.user, url='http://ur.coml')
        self.rating = Review.objects.create(id=1, rate_design=6, rate_usability=7, rate_content=9, user=self.user, post=self.post)

    def test_instance(self):
        self.assertTrue(isinstance(self.rating, Review))

    def test_save_rating(self):
        self.rating.save()
        rating = Review.objects.all()
        self.assertTrue(len(rating) > 0)

    def test_get_post_rating(self, id):
        self.rating.save()
        rating = Review.get_ratings(post_id=id)
        self.assertTrue(len(rating) == 1)
