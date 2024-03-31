
from flask import Flask, request, render_template
import numpy as np
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.inception_v3 import preprocess_input
from PIL import Image

model = load_model("C:\\Users\\MANIVANNAN\\Downloads\\AUTISM FINAL\\vgg16_custom.h5")
 
def predictImage(f):
    basepath = os.path.dirname(__file__)
    filepath = os.path.join(basepath, 'uploads', f.filename)
    f.save(filepath)

    img = image.load_img(filepath, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    img_data = preprocess_input(x)
    prediction = np.argmax(model.predict(img_data), axis=1)

    index = ['autistic','non-autistic']

    result = str(index[prediction[0]])
    return result


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')


@app.route('/upload', methods=["POST"])
def uploadImage():
    file = request.files['file']
    leaf_type = predictImage(file)
    return {"tea leaves": leaf_type}


if __name__ == '__main__':
    app.run(host="localhost")