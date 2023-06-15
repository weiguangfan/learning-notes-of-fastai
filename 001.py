# from flask import Flask, render_template, request
# from keras.models import load_model
# import numpy as np
#
# app = Flask(__name__)
# model = load_model('model.h5')
#
# labels = {0: '苹果', 1: '香蕉', 2: '橘子'}
#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
# @app.route('/predict/', methods=['GET', 'POST'])
# def predict():
#     file = request.files['file']
#     img = file.read()
#     x = np.fromstring(img, np.uint8)
#     x = x.reshape((1, 224, 224, 3))
#
#     preds = model.predict(x)
#     pred_class = labels[preds.argmax()]
#
#     return render_template('predict.html', pred_class=pred_class)
#
# if __name__ == '__main__':
#     app.run(debug=True)