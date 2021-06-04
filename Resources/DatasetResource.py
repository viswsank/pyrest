# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 16:02:26 2021

@author: hp
"""

from flask_restful import Resource, request
from Models.Dataset import DatasetModel

from flask_jwt import jwt_required

class DatasetResource(Resource):
    
    @jwt_required()
    def get(self):
        id = request.args.get('id')
        #print("id:",id)
        return DatasetModel.get_by_id(id).json()
    @jwt_required()
    def put(self):   
        #print(request.get_json())
        request_data = request.get_json()
        
        ds = DatasetModel(request_data['id'], 
                  request_data['Beach_Name'], 
                  request_data['Wave_Period'], 
                  request_data['Water_Temperature'], 
                  request_data['Turbidity'])
        #print(ds.json())
        if(ds.update()):
            return "Beach record successfully updated"
    

class DatasetListResource(Resource):
    
    @jwt_required()
    def get(self):
        limit = request.args.get('limit')
        offset = request.args.get('offset')
        #print("limit:",limit,"offset:",offset)
        return {"BeachRecords": [x.json() for x in DatasetModel.get_list(limit,offset)]}