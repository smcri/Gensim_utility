from django.test import TestCase, Client
import datetime
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
        #self.display_url = reverse('display')
        #self.result_url = reverse('result')

        self.Blog1 = blog.objects.create(
            name = 'Blog1' ,
            content = ' It is a demo blog content',
            description = 'It is a demo description',
            advantages = 'It is a demo advantages content',
            disadvantages='It is a demo disadvantage content',
            applications = ' It is a demo disadvantage content',
            written_by = 'It is written by me',
            created_at= '2021-05-17 00:00:00' ,
            formula_pic = 'images/dtbg.jpg'              
                    
               )
    
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

    """def test_overview_POST_create_Data(self):
        #blog.objects.create()
        
        response = self.client.post(self.overview_url, {
            'name' : 'Blog1 for testing' ,
            'content' : " It is a demo blog content to check for testing",
            'description' : 'It is a demo description',
            'advantages' : 'It is a demo advantages content',
            'disadvantages':'It is a demo disadvantage content',
            'applications' : ' It is a demo disadvantage content',
            'written_by' : 'It is written by me',
            'created_at': '2021-05-17 00:00:00' ,
            'formula_pic' : 'images/dtbg.jpg' 
        } )

        self.assertEquals(response.status_code,200)
        #self.assertEquals(self.Blog1.name,'Blog1')"""
    
    """def test_dataset_POST_create_Data(self):
        #blog.objects.create()
        
        response = self.client.post(self.dataset_url, {
            'name' : 'dataset1 for testing' ,
            'path' : 'Gensim_utility\myproject\csv_files',
            'description' : "It is a demo description about a dataset created for testing"
        } )

        self.assertEquals(response.status_code,200)
        #self.assertEquals(self.Blog1.name,'Blog1')"""
    
    
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
    


