import uuid
import json
from flask import jsonify


class Requests():
    """
    class for requests
    """

    def __init__(self, request, _type):

        self.id = uuid.uuid4().hex
        self.request = request
        self.type = _type
        

    def get_id(self):
        return self.id

    def get_request(self):
        return self.request

    def get_type(self):
        return self.type

  

    def to_json(self):
        """
        json representation of Request
        """
        return {
            'id': self.id,
            'Request': self.request,
            'Type': self.type
        }


