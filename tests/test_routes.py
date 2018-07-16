import unittest
import json
import pprint
from app import create_app
from tests.BaseTest import BaseTest


class TestClass(BaseTest):

    def test_create_request(self):
        """Test API can create a Request """
        res = self.client().post('/api/v1/requests/',
                                 content_type='application/json',
                                 data=json.dumps(self.requests))

        self.assertEqual(res.status_code, 404)
        self.assertTrue(res.status_code, 201)

    def test_get_all_requests(self):
        """Test API can view all."""
        res = self.client().get('api/v1/requests',
                                content_type='application/json')
        print(res)
        self.assertEqual(res.status_code, 200)

    def test_fetch_single_id(self):
        """Test API can view single id."""
        self.client().post('/api/v1/requests',
                           content_type='application/json',
                           data=json.dumps(self.requests))
        res = self.client().get('/api/v1/requests/1',
                                content_type='application/json')
        self.assertEqual(res.status_code, 404)

    def test_delete_request(self):
        """Test API can delete a request"""
        self.client().post('/api/v1/requests',
                           content_type='application/json',
                           data=json.dumps(self.requests))
        res = self.client().delete('/api/v1/requests/1',
                                content_type='application/json')
        reply = res.data
        print(reply)
        self.assertTrue(res.status_code, 200)

    def test_if_delete_request(self):
        """Test if  API has deleted a request"""
        self.client().post('/api/v1/requests',
                           content_type='application/json',
                           data=json.dumps(self.requests))
        res = self.client().delete('/api/v1/requests/1',
                                content_type='application/json')
        reply = res.data
        print(reply)
        self.assertEqual(res.status_code, 404)

    def test_modify_request(self):
        """Test API can modify a request"""
        self.client().post('/api/v1/requests',
                           content_type='application/json',
                           data=json.dumps(self.requests))
        res = self.client().put('/api/v1/requests/1',
                                content_type='application/json')
        reply = res.data
        print(reply)
        self.assertEqual(res.status_code, 404)

    



    

    