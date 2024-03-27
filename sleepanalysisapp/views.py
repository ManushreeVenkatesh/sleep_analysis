from django.shortcuts import render
from django.http import JsonResponse
import joblib
import requests

clf = joblib.load('sleepanalysisapp/templates/sleepanalysisapp/sleep_disorder_prediction_model.pkl')

# OCCUPATION_MAPPING = {
#     'Nurse': 5,
#     'Doctor': 1,
#     'Engineer': 2,
#     'Lawyer': 3,
#     'Teacher': 10,
#     'Accountant': 0,
#     'Salesperson': 7,
#     'Software Engineer': 9,
#     'Scientist': 8,
#     'Sales Representative': 6,
#     'Manager': 4,
# }

# GENDER_MAPPING = {
#     'Male': 1,
#     'Female': 0,
# }

SLEEP_DISORDER_MAPPING = {
    0: "None",
    1: "Sleep Apnea",
    2: "Insomnia"
}
def predict(request):
    result = None
    if request.method == 'POST':
        # Get form data
        gender = float(request.POST.get('gender'))
        # gender_str = request.POST.get('gender')
        # gender = GENDER_MAPPING.get(gender_str)
        age = float(request.POST.get('age'))
        occupation = float(request.POST.get('occupation'))
        # occupation_str = request.POST.get('occupation')
        # Convert occupation string to corresponding integer value
        # occupation = OCCUPATION_MAPPING.get(occupation_str)
        sleep_duration = float(request.POST.get('sleep_duration'))
        quality_of_sleep = float(request.POST.get('quality_of_sleep'))
        physical_activity_level = float(request.POST.get('physical_activity_level'))
        stress_level = float(request.POST.get('stress_level'))
        bmi_category = request.POST.get('bmi_category')
        blood_pressure = request.POST.get('blood_pressure')
        heart_rate = float(request.POST.get('heart_rate'))
        daily_steps = float(request.POST.get('daily_steps'))

        # Prepare input features for prediction
        features = [[gender, age, occupation, sleep_duration, quality_of_sleep, 
                     physical_activity_level, stress_level, bmi_category, 
                     blood_pressure, heart_rate, daily_steps]]

        # Make prediction
        prediction = clf.predict(features)
        result = SLEEP_DISORDER_MAPPING.get(prediction[0], "Unknown")

    return render(request, 'sleepanalysisapp/index.html', {'result': result})
