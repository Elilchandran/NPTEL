# from flask import Flask, render_template
# from app.queries import fetch_course_registration_data
# import os


# app = Flask(__name__)

# @app.route('/')
# def index():
#     df = fetch_course_registration_data()
#     data = df.to_dict(orient='records') if df is not None else []
#     return render_template('index.html', data=data)

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)), debug=True)

from flask import Flask, render_template
from app.queries import fetch_course_registration_data


app = Flask(__name__)

@app.route('/')
def index():
    df = fetch_course_registration_data()
    data = df.to_dict(orient='records') if df is not None else []
    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)
