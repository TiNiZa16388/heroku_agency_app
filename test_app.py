import unittest
import json
import os
from flask_sqlalchemy import SQLAlchemy
from models import setup_db

from app import create_app

class AgencyTestCase(unittest.TestCase):
    """This class represents the Agency Unit test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.new_movie_id=0
        self.new_actor_id=0
        self.token_casting_assistant    = os.environ['AUTH0_CASTING_ASSISTANT_TOKEN']
        self.token_casting_director     = os.environ['AUTH0_CASTING_DIRECTOR_TOKEN']
        self.token_executive_director   = os.environ['AUTH0_EXECUTIVE_PRODUCER_TOKEN']
        self.client = self.app.test_client()
        self.database_name = "agency_test"
        self.database_path = "postgresql://{}:{}@{}/{}".format(
            "tim", 
            "drawer16388",
            "localhost:5432",
            self.database_name
        )
        setup_db(self.app, self.database_path)

    def tearDown(self):
        """Executed after each test"""
        pass


    def test_get_actors(self):
        headers = {
            'Authorization': f'Bearer {self.token_casting_assistant}'
        }
        response = self.client.get("/actors", headers=headers)

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["actors"])


    def test_get_actors_fail(self):
        response = self.client.get("/actors")

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data["success"], False)


    def test_create_actor(self):
        headers = {
            'Authorization': f'Bearer {self.token_casting_director}'
        }
        
        response = self.client.post(
            "/actors", 
            json={
                'name': 'Kirsten Dunst', 
                'age': 39, 
                'gender': 'male', 
                'movies':[] }, 
            headers=headers)  
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)  
        self.assertEqual(data["success"], True)


    def test_create_actor_fail(self):
        headers = {
            'Authorization': f'Bearer {self.token_casting_assistant}'
        }
        
        response = self.client.post(
            "/actors", 
            json={
                'name': 'Kirsten Dunst', 
                'age': 39, 
                'gender': 'male', 
                'movies':[] }, 
            headers=headers)  
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 403) 
        self.assertEqual(data["success"], False) 


    def test_patch_actor(self):
        headers = {
            'Authorization': f'Bearer {self.token_casting_director}'
        }
        
        response = self.client.patch(
            '/actors/'+str(2), 
            json={
                'name': 'Kate Winslet', 
                'age': 48, 
                'gender': 'female', 
                'movies':[{
                    'title': 'Titanic',
                    'id': 1
                }] }, 
            headers=headers) 
        
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)  
        self.assertEqual(data["success"], True)   


    def test_patch_actor_fail(self):
        headers = {
            'Authorization': f'Bearer {self.token_casting_assistant}'
        }
        
        response = self.client.patch(
            '/actors/'+str(2), 
            json={
                'name': 'Kate Winslet', 
                'age': 48, 
                'gender': 'female', 
                'movies':[{
                    'title': 'Titanic',
                    'id': 1
                }] }, 
            headers=headers) 
        
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 403)  
        self.assertEqual(data["success"], False)  


    def test_delete_actor(self):
        headers = {
            'Authorization': f'Bearer {self.token_casting_director}'
        }
        
        response = self.client.delete(
            '/actors/'+str(3),  
            headers=headers) 
        
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)  


    def test_delete_actor(self):
        headers = {
            'Authorization': f'Bearer {self.token_casting_assistant}'
        }
        
        response = self.client.delete(
            '/actors/'+str(3),  
            headers=headers) 
        
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 403) 
        self.assertEqual(data["success"], False) 


    def test_get_movies(self):
        headers = {
            'Authorization': f'Bearer {self.token_casting_assistant}'
        }
        response = self.client.get("/movies", headers=headers)

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["movies"])


    def test_get_movies_fail(self):

        response = self.client.get("/movies")

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data["success"], False)


    def test_create_movie(self):
        headers = {
            'Authorization': f'Bearer {self.token_casting_director}'
        }
        response = self.client.post("/movies", 
            json={
                'title': "Independence Day 2", 
                'release_date': "1/1/2000, 11:0:0 AM", 
                'actors':[
                    {
                        'id': 2
                    }
                ]}, 
            headers=headers)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)  
        

    def test_create_movie_fail(self):
        headers = {
            'Authorization': f'Bearer {self.token_casting_assistant}'
        }
        response = self.client.post("/movies", 
            json={
                'title': "Independence Day 2", 
                'release_date': "1/1/2000, 11:0:0 AM", 
                'actors':[
                    {
                        'id': 2
                    }
                ]}, 
            headers=headers)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 403)     


    def test_patch_movie(self):
        headers = {
            'Authorization': f'Bearer {self.token_casting_director}'
        }

        response = self.client.patch(
            '/movies/' + str(1), 
            json={
                'title': "Titanic", 
                'release_date': "1/1/1998, 11:0:0 AM", 
                'actors':[{
                     'name': 'Kate Winslet',
                     'id': 2
                }]}, 
            headers=headers)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)  


    def test_patch_movie_fail(self):
        headers = {
            'Authorization': f'Bearer {self.token_casting_assistant}'
        }

        response = self.client.patch(
            '/movies/' + str(1), 
            json={
                'title': "Titanic", 
                'release_date': "1/1/1998, 11:0:0 AM", 
                'actors':[{
                     'name': 'Kate Winslet',
                     'id': 2
                }]}, 
            headers=headers)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 403) 


    def test_delete_movie(self):
        headers = {
            'Authorization': f'Bearer {self.token_executive_director}'
        }

        response = self.client.delete(
            '/movies/' + str(2),
            headers=headers)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)   


    def test_delete_movie_fail(self):
        headers = {
            'Authorization': f'Bearer {self.token_casting_assistant}'
        }

        response = self.client.delete(
            '/movies/' + str(2),
            headers=headers)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 403)  


# Make the tests executable
if __name__ == "__main__":
    unittest.main()
        