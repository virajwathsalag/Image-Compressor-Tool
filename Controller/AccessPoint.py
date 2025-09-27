from flask import Flask, jsonify, request
import os

from Service.arrangeFiles import create_deque
from Service.quicksort import quickSort

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
    
    uploaded_fileSize = []
    for file in image_files:
        size = len(file.read())
        file.seek(0)  # reset pointer
        uploaded_fileSize.append(size)
        
    uploaded_files = []
    for fileAll in image_files:
          uploaded_files.append(fileAll)
    
    quickSort(uploaded_files,uploaded_fileSize,0,len(uploaded_fileSize) - 1) 
    created_dequeue = create_deque(uploaded_files)   
    fileNameDequeue = create_deque(uploaded_fileSize)    
    # return jsonify({
    #     'message ': uploaded_fileSize,
    #     'quality ': quality,
    #     'max ': maxSize
    #     }),200
    
    return jsonify({
        "values: " : list(fileNameDequeue)
        }),200
    
    
if __name__ == '__main__':
    app.run(debug=True)
