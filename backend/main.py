from flask import Flask,jsonify,request 
from flask_cors import CORS
import os
  
app =   Flask(__name__) 
cors = CORS()
cors.init_app(app, resource={r"/*": {"origins": "*"}})

# Endpoint de prueba GET /returnjson --> Devuelve JSON
@app.route('/returnjson', methods = ['GET']) 
def ReturnJSON(): 
    if(request.method == 'GET'): 
        data = [{ 
            "id" : 15, 
            "content" : "Data Structures and Algorithms", 
        },{"id" : 35, 
            "content" : "Data Structures and Algorithms 2"}, { 
            "id" : 24, 
            "content" : "Data Structures and Algorithms", 
        },{"id" : 39, 
            "content" : "Data Structures and Algorithms 444"}]
  
        return jsonify(data) 


# Endpoint POST /upload --> Sube una foto
@app.route('/upload', methods=['POST'])
def upload():
    print(1)
    for fname in request.files:
        print(fname)
        f = request.files.get(fname)
        print(f)
        f.save('./uploads/' + fname);

    return 'Okay!'

if __name__ == '__main__':
    print(0)
    if not os.path.exists('./uploads'):
        os.mkdir('./uploads')
    app.run(debug=True)