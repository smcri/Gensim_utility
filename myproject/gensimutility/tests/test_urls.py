from django.test import TestCase
from django.urls import reverse,resolve
from gensimutility.views import Overview , dataset , home , about 



class TestURL(TestCase):
    
    def test_home_url_loads_properly(self):
            url = reverse('home')
            #print(resolve(url))
            response = self.client.get(url)
            self.assertEquals(resolve(url).func ,home )
    
    def Main_url_loads_properly(self):
        url = reverse('')
       # print(resolve(url))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_Overview_url_loads_properly(self):
            url = reverse('overview')
            #print(resolve(url))
            #response = self.client.get(url)
            self.assertEquals(resolve(url).func ,Overview )
    
    def test_dataset_url_loads_properly(self):
            url = reverse('dataset')
            #print(resolve(url))
            #response = self.client.get(url)
            self.assertEquals(resolve(url).func ,dataset )
    
    def test_about_url_loads_properly(self):
            url = reverse('about')
            #print(resolve(url))
            #response = self.client.get(url)
            self.assertEquals(resolve(url).func ,about )
    
    """def test_learnmore_url_loads_properly(self):
            url = reverse('display')
            #print(resolve(url))
            #response = self.client.get(url)
            self.assertEquals(resolve(url).func ,learnmore )
    
    def test_result_url_loads_properly(self):
            url = reverse('result')
            #print(resolve(url))
            #response = self.client.get(url)
            self.assertEquals(resolve(url).func ,sim_graph ) """
   
