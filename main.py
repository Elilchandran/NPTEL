from flask import Flask, render_template
from app.queries import fetch_course_registration_data, fetch_account_data, fetch_application_data, fetch_term_course_registration_data, fetch_course_data

app = Flask(__name__)

@app.route('/')
def index():
    course_data = fetch_course_registration_data()
    account_data = fetch_account_data()
    application_data = fetch_application_data()
    term_course_registration_data = fetch_term_course_registration_data()
    course_info_data = fetch_course_data()

    return render_template('index.html', 
                           course_data=course_data.to_dict(orient='records') if course_data is not None else [],
                           account_data=account_data.to_dict(orient='records') if account_data is not None else [],
                           application_data=application_data.to_dict(orient='records') if application_data is not None else [],
                           term_course_registration_data=term_course_registration_data.to_dict(orient='records') if term_course_registration_data is not None else [],
                           course_info_data=course_info_data.to_dict(orient='records') if course_info_data is not None else [])

if __name__ == "__main__":
    app.run(debug=True)  
