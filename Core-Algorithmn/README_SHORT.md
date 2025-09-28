# Huffman Image Compressor - Quick Start

## Setup
1. Create a virtualenv:
   python -m venv venv
   source venv/bin/activate   # on Windows: venv\Scripts\activate

2. Install deps:
   pip install -r requirements.txt

## Run Tkinter GUI (desktop)
python gui.py

- Choose an image (PNG/BMP), press "Compress Selected" to save to chosen folder.
- Or choose a folder and "Start Batch" to compress all PNG/BMP inside (sorted by size).

## Run Flask API
Set environment variables:
export API_KEY="mysecret"
export MONGO_URI="mongodb://..."  # optional
python api.py

POST to /compress with header X-API-KEY and form file field 'file' to receive compressed .huf file.

## Notes
- By default history is saved to `history.json` unless MONGO_URI is provided.
- The compressed format is lossless; decompress using the decompress function in huffman.py or the GUI 'Decompress'.
