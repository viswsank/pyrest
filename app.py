# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 08:07:52 2021

@author: hp
"""

from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from Models.User import UserModel
from Resources.UserResource import UserResource
from Resources.DatasetResource import DatasetListResource, DatasetResource


from flask_jwt import JWT
from security import authenticate, identity


app = Flask(__name__)
app.secret_key = 'pranav'
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(UserResource,"/userlist")
api.add_resource(DatasetListResource,"/datasetlist")
api.add_resource(DatasetResource,"/dataset")


#api.add_resource(Employee, '/employee/<string:name>')    
#api.add_resource(EmpList, '/emplist')

if __name__ == '__main__':
    app.run(host='192.168.1.5', port=5100)  # important to mention debug=True
    #print(UserModel(None,'nu22', 'nu22@yahoo.com', 'pwd1234', 'y').save_to_db())
    #print(UserModel.get_by_email('nu22@yahoo.com'))