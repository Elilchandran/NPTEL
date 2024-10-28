import pandas as pd
from .db import create_connection

def fetch_course_registration_data():
    engine = create_connection()
    if engine is None:
        return None

    query = """
    SELECT
        ac.program AS program,
        ac.email AS email,
        ac.student_email AS student_email,
        ac.level AS current_level,
        t.applying_level AS applying_level,
        c.course_code AS course_code,
        c.course_name AS course_name,
        c.course_type AS type,
        ac.fee_waiver AS fee_waiver,
        c.full_fee * (1 - IFNULL(ac.fee_waiver, 0) / 100) AS final_fee,
        t.term_code AS term_code
    FROM
        Application app
    JOIN
        TermCourseRegistrationApplication t ON app.term_code = t.term_code
    JOIN
        Account ac ON app.student_email = ac.student_email
    JOIN
        Course c ON c.term_code = t.term_code
    WHERE 
        app.student_email IS NOT NULL;
    """

    try:
        df = pd.read_sql(query, engine)
        return df
    except Exception as e:
        print(f"Query execution error: {e}")
        return None

def fetch_account_data():
    engine = create_connection()
    if engine is None:
        return None

    query = """
    SELECT
        account_id,
        name,
        dob,
        email,
        student_email,
        fee_waiver,
        level,
        program
    FROM
        Account;
    """

    try:
        df = pd.read_sql(query, engine)
        return df
    except Exception as e:
        print(f"Query execution error: {e}")
        return None

def fetch_application_data():
    engine = create_connection()
    if engine is None:
        return None

    query = """
    SELECT
        id,
        term_code,
        student_email,
        level
    FROM
        Application;
    """

    try:
        df = pd.read_sql(query, engine)
        return df
    except Exception as e:
        print(f"Query execution error: {e}")
        return None

def fetch_term_course_registration_data():
    engine = create_connection()
    if engine is None:
        return None

    query = """
    SELECT
        term_code,
        applying_level
    FROM
        TermCourseRegistrationApplication;
    """

    try:
        df = pd.read_sql(query, engine)
        return df
    except Exception as e:
        print(f"Query execution error: {e}")
        return None

def fetch_course_data():
    engine = create_connection()
    if engine is None:
        return None

    query = """
    SELECT
        id,
        course_code,
        course_name,
        full_fee,
        course_type,
        term_code
    FROM
        Course;
    """

    try:
        df = pd.read_sql(query, engine)
        return df
    except Exception as e:
        print(f"Query execution error: {e}")
        return None
