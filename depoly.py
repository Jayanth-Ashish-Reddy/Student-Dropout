from flask import Flask, render_template, request
import pickle

app = Flask(__name__ , template_folder='templates')
# load the model
model = pickle.load(open('student_dropout1.pkl', 'rb'))

@app.route('/')
def home():
    result = ''
    return render_template('index.html', **locals())


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    feature1 = float(request.form['maritalStatus'])
    feature2 = float(request.form['courses'])
    feature3 = float(request.form['attendance'])
    feature4 = float(request.form['previousQualification'])
    feature5 = float(request.form['motherQualification'])
    feature6 = float(request.form['fatherQualification'])
    feature7 = float(request.form['motherOccupation'])
    feature8 = float(request.form['fatherOccupation'])
    feature9 = float(request.form['displaced'])
    feature10 = float(request.form['debtorStatus'])
    feature11 = float(request.form['gender'])
    feature12 = float(request.form['scholarship'])
    feature13 = float(request.form['inflationRate'])
    feature14 = float(request.form['unemploymentRate'])
    feature15 = float(request.form['gdp'])
    
    prediction = model.predict([[feature1, feature2 , feature3  , feature4  , feature5 , feature6 , feature7 , feature8 ,  feature9  , feature10 ,feature11 , feature12 , feature13 , feature14 , feature15 ]])[0]

    return render_template('index.html', **locals())

if __name__ == '__main__':
    app.run(debug=True)