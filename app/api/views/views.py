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


class Request(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('requests', type=str, required=True,
                                   help='No request provided',
                                   location='json')
        self.reqparse.add_argument('type', type=str, required=True,
                                   help='Type provided',
                                   location='json')
        super(Request, self).__init__()

    def get(self, id):
        for request in REQUESTS:
            if request.get_id() == id:

                return make_response(jsonify(
                    request.to_json()
                ), 200)
        return make_response(jsonify({"message": "Ride not found."}), 404)

    def put(self, id):
        task = [request for request in REQUESTS if request.get_id() == id]
        if len(task) == 0:
            abort(404)
        request = task[0]
        args = self.reqparse.parse_args()
        for k, v in args.items():
            if k is not 'id':
                setattr(request, k, v)
               
        return make_response(jsonify(request.to_json()), 201)

    def delete(self, id):
        task = [request for request in REQUESTS if request.get_id() == id]
        if len(task) == 0:
            abort(404)
        REQUESTS.remove(task[0])
        return {'result': True}


api.add_resource(RequestList, '/api/v1/requests')
api.add_resource(Request, '/api/v1/requests/<string:id>')
