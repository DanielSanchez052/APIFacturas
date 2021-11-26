from bson import objectid, json_util
from bson.objectid import ObjectId
from flask import Flask, request, Response, jsonify

from . import routes
from main import mongo

@routes.route('/bill', methods=['POST'])
def bills():
    if request.json and 'id_customer' in request.json and 'number' in request.json and 'date' in request.json and 'price' in request.json and 'balance' in request.json:
        id_customer = request.json['id_customer']
        number = request.json['number']
        date = request.json['date']
        price = request.json['price']
        balance = request.json['balance']
        customer = json_util.dumps(
            mongo.db.customer.find_one({'_id':ObjectId(id_customer)})
            )
        if(len(customer)>4):
            id = mongo.db.bill.insert({
                'id_customer':id_customer, 
                'number':number, 
                'date':date,
                'price':price, 
                'balance':balance
            })
            response = jsonify({'message':'Bill number'+ number +' added successfully'})
            return response,201
        response = jsonify({'message':'User doesn´t exists'})
        return response,404
    response = jsonify({'message':'something Fail'})
    return response,400


@routes.route('/bill', methods=['GET'])
def getBills():
    bills = mongo.db.bill.find()
    res = json_util.dumps(bills)
    return Response(res, mimetype="application/json",status=200)


@routes.route('/bill/<id>', methods=['GET'])
def get_bill_by_id(id):
    bill = mongo.db.bill.find_one({'_id':ObjectId(id)})
    response = json_util.dumps(bill)          
    return Response(response, mimetype="application/json", status=200)

@routes.route('/bill/<id>', methods=['DELETE'])
def delete_bill(id):
    mongo.db.bill.delete_one({'_id':ObjectId(id)})
    response = jsonify({"message": "bill "+id+" has been deletd"})         
    return response

@routes.route('/bill/<_id>', methods=['PUT'])
def update_bill(_id):
    if request.json and 'id_customer' in request.json and 'number' in request.json and 'date' in request.json and 'price' in request.json and 'balance' in request.json:
        id_customer = request.json['id_customer']
        number = request.json['number']
        date = request.json['date']
        price = request.json['price']
        balance = request.json['balance']
        mongo.db.bill.update_one(
            {'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, 
            {'$set': {
                'id_customer':id_customer, 
                'number':number, 
                'date':date,
                'price':price, 
                'balance':balance
            }})
        response = jsonify({'message': 'Bill ' + _id + ' Updated Successfully'})
        return response,200
    response = jsonify({'message':'something Fail'})
    return response,400
