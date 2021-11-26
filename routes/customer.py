from bson import objectid, json_util
from bson.objectid import ObjectId
from flask import Flask, request, Response, jsonify

from . import routes
from main import mongo

@routes.route('/customer', methods=['POST'])
def addCustomer():
    if request.json and 'name' in request.json and 'mobile' in request.json and 'status' in request.json:
        name = request.json['name']
        mobile = request.json['mobile']
        status = request.json['status']
        id = mongo.db.customer.insert({
            'name':name, 'mobile':mobile, 'status':status 
        })
        response = jsonify({'message':'Customer'+ name +' added successfully'})
        return response,201
    response = jsonify({'message':'something Fail'})
    return Response(response, mimetype='application/json', status=400)

@routes.route('/customer', methods=['GET'])
def getCustomer():
    customers = mongo.db.customer.find()
    res = json_util.dumps(customers)
    return Response(res, mimetype="application/json",status=200)

@routes.route('/customer/<id>', methods=['GET'])
def get_customer_by_id(id):
    customer = mongo.db.customer.find_one({'_id':ObjectId(id)})
    response = json_util.dumps(customer)          
    return Response(response, mimetype="application/json", status=200)

@routes.route('/customer/<id>', methods=['DELETE'])
def delete_customer(id):
    mongo.db.customer.delete_one({'_id':ObjectId(id)})
    response = jsonify({"message": "Customer "+id+" has been deletd"})         
    return response

@routes.route('/customer/<_id>', methods=['PUT'])
def update_customer(_id):
    if request.json and 'name' in request.json and 'mobile' in request.json and 'status' in request.json:
        name = request.json['name']
        mobile = request.json['mobile']
        status = request.json['status']
        mongo.db.customer.update_one(
            {'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, 
            {'$set': { 'name':name, 'mobile':mobile, 'status':status }})
        response = jsonify({'message': 'Customer ' + _id + ' Updated Successfully'})
        return response,200
    response = jsonify({'message':'something Fail'})
    return response,400