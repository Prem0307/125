from flask import Flask,jsonify,request
from main import get_prediction

app=Flask(__name__)

@app.route('/')

def api():
    return 'Success'
@app.route("/predict-alphabet",methods=["POST"])
def predict_data():
    image=request.files.get("alphabet")
    prediction=get_prediction(image)
    return jsonify({
        'prediction':prediction
    }),200
if __name__ =='__main__':
    app.run(debug=True,port=8000)