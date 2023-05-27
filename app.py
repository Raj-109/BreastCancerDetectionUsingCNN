import os
import uuid
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)

@app.route('/', methods=['GET'])
def hello():
    return "API SUPPORT FOR BREAST_CANCER_DETECTION_USING_CNN"

@app.route('/Saveuser',methods=['POST'])
def saveUser():
    return "User Details Saved"

@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():
    from BreastCancer import predictImage  # Import predictImage function here
    if 'image' not in request.files:
        return jsonify({'message': 'No image provided'})

    image = request.files['image']
    filename = str(uuid.uuid4()) + '.jpg'  # Generate a unique filename
    

    img_path = os.path.join('./', filename)  # Specify the path to save the image

    # Save the image to disk
    image.save(img_path)

    data = predictImage(img_path)
    if data:
        return data

    return jsonify({
        "Benign":"",
        "InSitu":"",
        "Invasive":"",
        "Normal":""
    })


if __name__ == '__main__':
    app.run(debug=True)
