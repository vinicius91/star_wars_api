from django.test import TestCase
from rest_framework import status

from star_wars_api.models import UserProfile
from star_wars_api.helpers.swapi import get_planet_appearances


class UserProfileTest(TestCase):

    def setUp(self):
        # We want to go ahead and originally create a user.
        self.test_user = UserProfile.objects.create_user('test@example.com', 'testuser', 'testpassword')

    def test_verify_number_of_created_users(self):
        # We want to make sure we have two users in the database..
        self.assertEqual(UserProfile.objects.count(), 1)

    def test_verify_user_data(self):
        """Ensure that the user is created properly"""
        data = {
            'email': 'foobar@example.com',
            'name': 'foobar',
            'password': 'somepassword'
        }
        response = self.client.post('/users/', data, format='json')
        # We want to make sure we have two users in the database..
        self.assertEqual(UserProfile.objects.count(), 2)
        # And that we're returning a 201 created code.
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Additionally, we want to return the username and email upon successful creation.
        self.assertEqual(response.data['username'], data['username'])
        self.assertEqual(response.data['email'], data['email'])
        self.assertFalse('password' in response.data)


class SwapiMovieAppearancesTest(TestCase):

    def test_check_alderaan_count(self):
        """First Test case to Check an normal name"""
        alderaan = get_planet_appearances('Alderaan')
        self.assertEqual(alderaan, 2)

    def test_check_polis_massa_count(self):
        """Check a name with a space between it"""
        polis_massa = get_planet_appearances('Polis Massa')
        self.assertEqual(polis_massa, 1)
        
    def test_check_invalid_planet_count(self):
        """Check a name with a space between it"""
        invalid = get_planet_appearances('Lorem Ipsum')
        self.assertEqual(invalid, 0)
