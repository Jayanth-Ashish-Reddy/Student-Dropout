from flask import Flask, render_template, request
import joblib
import os

model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Student_dropout1.pkl')
model = joblib.load(model_path)

app = Flask(__name__, template_folder='template')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        feature1 = int(request.form['maritalStatus'])
        feature2 = int(request.form['application_mode'])
        feature3 = int(request.form['courses'])
        feature4 = int(request.form['previousQualification'])
        feature5 = int(request.form['displaced'])
        feature6 = int(request.form['debtorStatus'])
        feature7 = int(request.form['tuition_fees'])
        feature8 = int(request.form['gender'])
        feature9 = int(request.form['scholarship'])
        feature10 = int(request.form['age_at_enrollment'])
        feature11 = int(request.form['enrolled_units_1st_year'])
        feature12 = int(request.form['approved_units_1st_year'])
        feature13 = int(request.form['enrolled_units_2nd_year'])
        feature14 = int(request.form['approved_units_2nd_year'])
        feature15 = int(request.form['enrolled_units_3rd_year'])
        feature16 = int(request.form['approved_units_3rd_year'])
        feature17 = int(request.form['enrolled_units_4th_year'])
        feature18 = int(request.form['approved_units_4th_year'])

        # Convert features to a 2D array for prediction
        input_features = [[feature1, feature2, feature3, feature4, feature5, feature6, feature7, feature8, feature9, feature10, feature11, feature12 , feature13 , feature14 , feature15 , feature16 , feature17 , feature18]]

        result = model.predict(input_features)
        out = 'At the stage to dropout' if result == 0 else 'Not at the stage of Dropping out'

        return render_template('result.html', output=out)

if __name__ == '__main__':
    app.run(debug=True)




















































































