import pandas as pd
from .db import create_connection

def fetch_course_registration_data():
    engine = create_connection()
    if engine is None:
        return None

    query = """
SELECT
    ac.program AS program,                    -- Fetch the program from the Account table
    ac.email AS email,
    ac.student_email AS student_email,
    ac.level AS current_level,                -- Current level from Account table
    t.applying_level AS applying_level,       -- Applying level from TermCourseRegistrationApplication table
    c.course_code AS course_code,
    c.course_name AS course_name,
    c.course_type AS type,
    ac.fee_waiver AS fee_waiver,
    c.full_fee * (1 - IFNULL(ac.fee_waiver, 0)/100) AS final_fee,
    t.term_code AS term_code
FROM
    Application app
JOIN
    TermCourseRegistrationApplication t ON app.term_code = t.term_code  -- Correct join order
JOIN
    Account ac ON app.student_email = ac.student_email
JOIN
    Course c ON c.term_code = t.term_code;
"""

    try:
        df = pd.read_sql(query, engine)
        return df
    except Exception as e:
        print(f"Query execution error: {e}")
        return None
