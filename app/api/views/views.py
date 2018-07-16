from flask import Flask, jsonify, abort, make_response, Blueprint
from flask_restful import Api, Resource, reqparse
from app.api.models.request import Requests
app_bp = Blueprint('app', __name__)
api = Api(app_bp)

REQUESTS = []


class RequestList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('requests', type=str, required=True,
                                   help='No request provided',
                                   location='json')
        self.reqparse.add_argument('type', type=str, required=True,
                                   help='Type provided',
                                   location='json')
        super(RequestList, self).__init__()

    def get(self):
        json_requests = [request.to_json() for request in REQUESTS]
        if len(json_requests) == 0:
            return make_response(jsonify({'message': 'sorry no REQUESTS yet'}))
        return make_response(jsonify(json_requests), 200)

    def post(self):
        args = self.reqparse.parse_args()
        request = Requests(args['requests'], args['type'])
        REQUESTS.append(request)
        return make_response(jsonify({
            'message': 'Ride Offer Created with id: ' + request.get_id(),
            'status': 'success'
        }), 201)




api.add_resource(RequestList, '/api/v1/requests')

