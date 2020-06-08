import pandas as pd
import flask 
from joblib import load, dump


with open('RandomFor.joblib', 'rb') as f:
    model = load(f)


app = flask.Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return flask.render_template('index.html')

    if flask.request.method == 'POST':
        sex = flask.request.form['sex']
        sibsp = flask.request.form['sibsp']
        parch = flask.request.form['parch']
        age = flask.request.form['age']
        pclass = flask.request.form['pclass']
        fare = flask.request.form['fare']
        embarked = flask.request.form['embarked']
    
    input_variables = pd.DataFrame([[sex, sibsp, parch, age, pclass, fare, embarked]],
    columns=[sex, sibsp, parch, age, pclass, fare, embarked],dtype='float',index=['input'])

    predictions = model.predict(input_variables)[0]

    print(predictions)

    return flask.render_template('index.html', original_input={
        'Sex':sex,
        'Sibsb':sibsp,
        'Parch':parch,
        'Age':age,
        'Fare':fare,
        'Embarked':embarked
    }, result=predictions)


if __name__ == '__main__':
    app.run(debug=True)