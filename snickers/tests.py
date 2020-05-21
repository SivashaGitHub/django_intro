#from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse 


class ThingsTest(SimpleTestCase):
    def test_home_page(self):
        url = reverse("home")
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_home_page_template(self):
        url = reverse("home")
        response = self.client.get(url)
        self.assertTemplateUsed(response,"base.html")
        self.assertTemplateUsed(response,"home.html")
        #self.assertTemplateUsed(response,"about.html")
       
       
            



