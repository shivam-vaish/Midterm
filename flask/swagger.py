from flask import Flask, request
from flasgger import Swagger
import pickle
from sklearn.linear_model import LinearRegression


app = Flask(__name__) # contsructor it is very important 
Swagger(app)


pickled_model_file = open("pickle_diabetes_model.pkl","rb")
regressor = pickle.load(pickled_model_file)

@app.route('/') # it will give the base route
def home():
    return "Welcome to diabetes data"

@app.route('/predict')

def predict_diabetes():

    """ Lets try Swagger From Flasgger
    --- 
    parameters:
        - name: Age
          in: query
          type: int
          required: true
        - name: Sex
          in: query
          type: string
          required: true
        - name: BodyMassIndex
          in: query
          type: string
          required: true
        - name: BloodPressure
          in: query
          type: string
          required: true
    responses:
        200:
            description : The result is 
    """
    age = request.args.get("Age")
    sex = request.args.get("Sex")
    bmi = request.args.get("BMI")
    bp = request.args.get("BP")
    result = regressor.predict([[age,sex,bmi,bp]])
    return f"Disease progression after a year is {result}"



# Calling the constructor
if __name__ == "__main__":

    app.run(debug = True)

