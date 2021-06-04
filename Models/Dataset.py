# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 12:46:37 2021

@author: hp
"""

import os
import psycopg2

class DatasetModel():
    TABLE_NAME = 'dataset'
    DATABASE_URL = os.environ['DATABASE_URL']  
    
    def __init__(self, _id, beach_Name, wave_Period, water_Temperature, turbidity):
        self.id = _id
        self.beach_Name = beach_Name
        self.wave_Period = wave_Period
        self.water_Temperature = water_Temperature
        self.turbidity = turbidity
        
    def json(self):
        #Note: Decimal is not json seriablizable so converting it to float for printing purpose
        return {"id": self.id, 
                "Beach_Name": self.beach_Name,
                "Wave_Period": float(self.wave_Period),
                "Water_Temperature": float(self.water_Temperature),
                "Turbidity": float(self.turbidity)
                }
    
    @classmethod
    def get_list(cls, limit, offset):   
        connection = psycopg2.connect(cls.DATABASE_URL)     
    
        cursor = connection.cursor()
        query = "SELECT id,Beach_Name,Wave_Period,Water_Temperature,Turbidity FROM {0} ORDER BY id LIMIT {1} OFFSET {2}".format(cls.TABLE_NAME, limit, offset)
        print("query:",query)
        cursor.execute(query)
        
        rows = cursor.fetchall()
        dsl=[]
        for row in rows:
            #print(row)
            ds = cls(*row)
            #print(ds.json())
            dsl.append(ds)
        connection.close()
        return dsl
    
    @classmethod
    def get_by_id(cls, _id):   
        connection = psycopg2.connect(cls.DATABASE_URL)     
    
        cursor = connection.cursor()
        query = "SELECT id,Beach_Name,Wave_Period,Water_Temperature,Turbidity FROM {0} WHERE id={1}".format(cls.TABLE_NAME, _id)
        print("query:",query)
        cursor.execute(query)
        
        row = cursor.fetchone()
        return cls(*row)
    
    
    def update(self): 
        connection = psycopg2.connect(self.DATABASE_URL)     
    
        cursor = connection.cursor()
        query = "UPDATE {0} SET Beach_Name ='{1}', Wave_Period={2}, Water_Temperature= {3}, Turbidity={4} where id={5}".format(self.TABLE_NAME, self.beach_Name, self.wave_Period, self.water_Temperature, self.turbidity, self.id)
        print("query:",query)
        cursor.execute(query)
        connection.commit()

        connection.close()
        return True
    
    