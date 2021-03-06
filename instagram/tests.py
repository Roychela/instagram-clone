from django.test import TestCase
from .models import Image,Profile
from django.contrib.auth.models import User
# Create your tests here.
class ImageTestClass(TestCase):
    def setUp(self):
        self.user = User.objects.create_user("newuser", "test")
        self.image_ferrari = Image(image_name='image_ferrari',image_caption='this is a test instance',image='test.png',user=self.user)
        self.image_ferrari.save_image()
        self.image_gucci = Image(image_name='image_gucci',image_caption='this is a test instance',image='test2.png',user=self.user)
        self.image_gucci.save_image()

    def test_instance(self):
        self.assertTrue(isinstance(self.image_ferrari,Image))

    def tearDown(self):
        Image.objects.all().delete()
        Profile.objects.all().delete()
        User.objects.all().delete()

        
    def test_save_image(self):
        self.image_ferrari.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)
class ProfileTestClass(TestCase):
    '''
    test class for Profile model
    '''
    def setUp(self):
        self.user = User.objects.create_user("testuser", "secret")
        self.profile_test = Profile(image='image.png',user=self.user)
        self.profile_test.save()

    def test_instance_true(self):
        self.profile_test.save()
        self.assertTrue(isinstance(self.profile_test, Profile))