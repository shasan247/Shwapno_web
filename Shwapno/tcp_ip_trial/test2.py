
from flask import Flask, render_template, request, make_response
from flask import jsonify
import pymysql
import jwt 
import datetime
from functools import wraps
import json

app = Flask(__name__)
host = "127.0.0.1"
userx = "root"
password = ""
db = "test2"



@app.route('/login', methods=['POST'])                      #If any field kept blank signup and login executes. Need to solve this.
def insert_sensor():
    conn = pymysql.connect(host=host, user=userx, password=password, db=db, cursorclass=pymysql.cursors.DictCursor)
    cursor3 = conn.cursor()
    try:
        if request.authorization:
            if request.authorization.username == "" or request.authorization.password == "":
                res={"response": "Why blank!!!"}
                return jsonify(res)
                
            cursor3.execute("SELECT user, pass FROM user_table")
            users = cursor3.fetchall()

            user_data = json.dumps(users)
            user_data2 = json.loads(user_data)
            
            for user in user_data2:
                if user["user"] == request.authorization.username and user["pass"] == request.authorization.password:
                    res={"response": "Successful Login"}
                    return jsonify(res)  
    
            else:
                res={"response": "Wrong Credentials"}
                return jsonify(res)
            cursor3.close()
            conn.close()
    except:
        res={"response": "failed"}
        return jsonify(res)

 
if __name__ == '__main__':
    app.run(debug=True,host= '0.0.0.0', port='6000')