from flask import Flask, jsonify, request
import os

from Service.arrangeFiles import create_deque

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to my Flask API!"})

@app.route('/hello/<name>', methods=['GET'])
def hello(name):
    return jsonify({"message": f"Hello, {name}!"})

@app.route('/upload-images/<quality>/<maxSize>/<resize>', methods=['POST'])
def upload_images(quality,maxSize,resize):
    if 'images' not in request.files:
        return jsonify({'error' : 'No images part in the request'}), 400
    
    image_files = request.files.getlist('images')
    if not image_files:
        return jsonify({'error' : 'No images selected for upload'}), 400
    
    uploaded_filenames = []
    for file in image_files:
        if file.filename != '':
            uploaded_filenames.append(file.filename)
    new_created_deque = create_deque(uploaded_filenames)     
            
    return jsonify({
        'message ': list(new_created_deque),
        'quality ': quality,
        'max ': maxSize
        }),200
    
    
if __name__ == '__main__':
    app.run(debug=True)
