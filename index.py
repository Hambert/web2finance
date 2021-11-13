#!/usr/bin/python

from flask import Flask, render_template, jsonify, redirect

from bs4 import BeautifulSoup
import requests

from os import environ as env

#SQL API
import mysql
from mysql.connector import Error
from mysql.connector import errorcode
connection = mysql.connector

# Sleep timer
from time import sleep
import datetime


app = Flask(__name__)


@app.route('/')
def home():
    return redirect(f"/fug")


@app.route('/fug')
def fug():
   return render_template("index.html")

@app.route('/api')
def getFug():
    return jsonify(getDataFromDB())



def getDataFromDB():
    try:
      
      connection = mysql.connector.connect(
            host='mysql.webhosting73.1blu.de',
            user=env['SQLUSER'],
            password=env['SQLPW'],
            database=env['SQLDB']
        )
      
      if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL database... MySQL Server version on ",db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print ("Your connected to - ", record)

        datadict = {}

        table = "finance_fug_CNN"
        cursor.execute("SELECT value, sourceDate FROM " + table + " ORDER BY timestamp DESC LIMIT 1")
        
        result = cursor.fetchall()

        datadict.update({'cnn_fug_now':{"value" : result[0][0], 'sourceDate':result[0][1]}})
   
        table = "finance_fug_BTC"
        cursor.execute("SELECT value, sourceDate FROM " + table + " ORDER BY timestamp DESC LIMIT 1")
        result = cursor.fetchall()

        datadict.update({'btc_fug_now':{"value" : result[0][0], 'sourceDate':result[0][1]} })
  
        return datadict


      if(connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

    except Error as err :
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
      else:
        print(err)

    else:
      #closing database connection.
      connection.close()
      print("MySQL connection is closed [finally]")




if __name__ == '__main__':
    # running app
    app.run(use_reloader=True, debug=True)
