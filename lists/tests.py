# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import resolve
from django.test import TestCase
from views import Homepage
from django.http import HttpRequest
from django.template.loader import render_to_string

# Create your tests here.
class HomePageTest(TestCase):
    
    def test_uses_homepage_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, 'home.html')

    
    def test_can_save_a_POST_request(self):
        response  = self.client.post("/", data={"item_text":"A new to do item"})
        self.assertIn('A new to do item', response.content.decode())


    # def test_home_page_returns_correct_html(self):
    #     # request = HttpRequest()
    #     # response = Homepage(request)
    #     response = self.client.get("/")
    #     html = response.content.decode("UTF-8")
    #     self.assertTrue(html.startswith('<!DOCTYPE html>'))
    #     self.assertIn('<title>To-Do</title>', html)
    #     self.assertTrue(html.endswith('</html>'))
    #     # expected_html = render_to_string('home.html')
    #     # self.assertEqual(html, expected_html)

        self.assertTemplateUsed(response, 'home.html')
