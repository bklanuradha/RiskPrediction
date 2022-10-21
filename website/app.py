from flask import Flask, render_template, request
import pickle
import numpy as np

# setup application
app = Flask(__name__)

def prediction(lst):
    filename = 'model/predictor.pickle'
    with open(filename, 'rb') as file:
        model = pickle.load(file)
    pred_value = model.predict([lst])
    return pred_value

@app.route('/', methods=['POST', 'GET'])
def index():
    pred_value = 0
    if request.method == 'POST':
        gender = request.form['gender']
        age = request.form['age']
        equlify = request.form['equlify']
        q1 = request.form['q1']
        q2 = request.form['q2']
        q3 = request.form['q3']
        q4 = request.form['q4']
        q5 = request.form['q5']
        q6 = request.form['q6']
        q7 = request.form['q7']
        q8 = request.form['q8']
        q9 = request.form['q9']
        q10 = request.form['q10']

        feature_list = []

        gender_list = ['female', 'male']
        age_list = ['18-30','mthan30', 'lthan18']
        equlify_list = ['a/l',  'o/l','priedu', 'postgraduate', 'undergraduate']
        q1_list = ['no', 'yes']
        q2_list = ['no', 'yes']
        q3_list = ['no', 'yes']
        q4_list = ['no', 'yes']
        q5_list = ['no', 'yes']
        q6_list = ['no', 'yes']
        q7_list = ['no', 'yes']
        q8_list = ['no', 'yes']
        q9_list = ['no', 'yes']
        q10_list = ['no', 'yes']

        def traverse_list(lst, value):
            for item in lst:
                if item == value:
                    feature_list.append(1)
                else:
                    feature_list.append(0)

        traverse_list(gender_list, gender)
        traverse_list(age_list, age)
        traverse_list(equlify_list, equlify)
        traverse_list(q1_list, q1)
        traverse_list(q2_list, q2)
        traverse_list(q3_list, q3)
        traverse_list(q4_list, q4)
        traverse_list(q5_list, q5)
        traverse_list(q6_list, q6)
        traverse_list(q7_list, q7)
        traverse_list(q8_list, q8)
        traverse_list(q9_list, q9)
        traverse_list(q10_list, q10)

        pred_value = prediction(feature_list)*10
        pred_value = np.round(pred_value[0],2)
        # print(pred_value)
        
       
    return render_template('index.html', pred_value=pred_value)


if __name__== '__main__':
    app.run(debug=True)