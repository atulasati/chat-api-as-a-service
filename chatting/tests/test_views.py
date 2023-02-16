from django.test import TestCase, Client
from django.urls import reverse
from chatting.views import Room, Message, RoomUsers
import json 
from rest_framework import status
from django.contrib.auth import get_user_model
import time

User = get_user_model()

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = User.objects.create_superuser(
            username='testbe@example.com',
            email='test@beexample.com',
            password='12345'
        )
        self.normal_user = User.objects.create_user(
            username='normalbe@example.com',
            email='normalbe@example.com',
            password='12345'
        )

        token = self.client.post('/users/login/', {
            'username': 'normalbe@example.com',
            'email': 'normalbe@example.com',
            'password': '12345'
        })
        token = f'Bearer {token.data["token"]}'
        self.headers_normanUser = {'HTTP_AUTHORIZATION' : token, 'content_type':'application/json'}
        
        token = self.client.post('/users/login/', {
            'username': 'testbe@example.com',
            'email': 'testbe@example.com',
            'password': '12345'
        })
        token = f'Bearer {token.data["token"]}'
        self.headers_superuser = {'HTTP_AUTHORIZATION' : token, 'content_type':'application/json'}
        

    def test_entire_user_management(self):
        # User Login 
        response_login = self.client.post('/users/login/', {
            'username': 'normalbe@example.com',
            'email': 'normalbe@example.com',
            'password': '12345'
        })
        self.assertEqual(response_login.status_code, status.HTTP_200_OK)
        time.sleep(1)

        #Update User 

        response = self.client.patch('/users/updateUser/', {
            'username': 'test_normalbe@example.com'   
        }, **self.headers_normanUser )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        #User Logout
        
        response_login = self.client.post('/users/logout/')
        self.assertEqual(response_login.status_code, status.HTTP_200_OK)
        time.sleep(1)
   
    def test_entire_room_management(self):

        # Creating Group
       
        response = self.client.post('/chatting/createGroup/', {
            'room_name': '1'
        }, **self.headers_normanUser)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Adding Members in the Group 
        response = self.client.post('/chatting/addUser/', {
            'user':'12',
            'room_id':'1'
            
        }, **self.headers_normanUser)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
     
         # Searching Members in Group

        response = self.client.get('/chatting/searchUser/?search=all&room_id=11',**self.headers_normanUser)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

         #Sending Message to The room

        response = self.client.post('/chatting/api/messages/update/db',{
           "prompt": "Hello",
           "user[room]":"1"

        },**self.headers_normanUser)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

         #View Messages Sent to Room 

        response = self.client.get('/chatting/api/messages_view/',{
           'room':"1"
        },**self.headers_normanUser)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        

        # Deleting Member from Group 

        response = self.client.delete('/chatting/delUser/',{
            "room_id":'1',
            "user":'12'

        },**self.headers_normanUser)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


       
        

     

