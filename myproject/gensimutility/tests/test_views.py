from django.test import TestCase, Client
import datetime
from faker import Faker
from django.urls import reverse
from gensimutility.models import blog , datasets , team
import json 

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.overview_url = reverse('overview')
        self.dataset_url = reverse('dataset')
        self.about_url = reverse('about')
        self.learnmore_url = reverse('learnmore')

        self.fake = Faker()
        self.u1 = self.fake.domain_name()
        self.u2 = self.fake.domain_name()

        #self.display_url = reverse('display')
        #self.result_url = reverse('result')



         
    
    def test_Overview_GET(self):
        client = Client()

        response = self.client.get(self.overview_url)
        self.assertEquals(response.status_code , 200)
        self.assertTemplateUsed(response , 'overview.html')
    
    def test_Home_GET(self):
        client = Client()

        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code , 200)
        self.assertTemplateUsed(response , 'home.html')
    
    def test_dataset_GET(self):
        client = Client()

        response = self.client.get(self.dataset_url)
        self.assertEquals(response.status_code , 200)
        self.assertTemplateUsed(response , 'simgen.html')
    
    def test_about_GET(self):
        client = Client()

        response = self.client.get(self.about_url)
        self.assertEquals(response.status_code , 200)
        self.assertTemplateUsed(response , 'aboutus.html')
    
    """def test_learnmore_GET(self):
        client = Client()

        blogID = 1

        response = self.client.get(self.learnmore_url)
        self.assertEquals(response.status_code , 200)
        self.assertTemplateUsed(response , 'display.html')"""

    #NOT NEEDED
    """def test_overview_POST_create_Data(self):
        #blog.objects.create()
        client = Client() 
        
        
        
        
     response = self.client.post(self.overview_url, data = {
            'name' : 'blogId' ,
            'content' : " It is a demo blog content to check for testing",
            'description' : 'It is a demo description',
            'advantages' : 'It is a demo advantages content',
            'disadvantages':'It is a demo disadvantage content',
            'applications' : ' It is a demo disadvantage content',
            'written_by' : 'It is written by me',
            'created_at': '2021-05-17 00:00:00' ,
            'formula_pic' : 'images/dtbg.jpg' 
        } )

        self.assertTemplateUsed(response, overview.html)
        self.assertEquals(response.status_code,302)
        #self.assertEquals(self.Blog1.name,'Blog1')"""


    
    def test_dataset_POST_create_Data_invalid_url(self):
        #blog.objects.create()
        
        response = self.client.post(self.dataset_url, data = {
            'dset1':self.u1 , 'dset2':self.u2
        } )

        self.assertEquals(response.status_code,200)
        #self.assertEquals(self.Blog1.name,'Blog1')
    
    def test_dataset_POST_create_data_dataname(self):
        response = self.client.post(self.dataset_url , data = { 
            'dset1': 'https://raw.githubusercontent.com/scikit-multiflow/streaming-datasets/master/iris_timestamp.csv' , 
            'dset2': 'https://code.datasciencedojo.com/datasciencedojo/datasets/raw/master/Occupancy%20Detection/datatest.csv'
        })

        self.assertEquals(response.status_code,302)

    
    # NOT SURE IF NEEDED
    """def test_team_POST_create_Data(self):
        #blog.objects.create()
        
        response = self.client.post(self.about_url, {
            'name' : 'Admin11' ,
            'description': "It is a demo description about an admin who contributed in creating the project",
            'email_addr' : 'iit2019502@iiita.ac.in',
            'profile_pic' : '\0'
            
        } )

        self.assertEquals(response.status_code,200)
        #self.assertEquals(self.Blog1.name,'Blog1')"""
    


