# NPTEL Course Registration Data Web Application

This project is about web application built using Flask to fetch and display course registration data from a MySQL database. It features a clean and responsive design, showcasing important details about course registrations.


## Features
- Connects to a MySQL database to retrieve course registration data.
- Features a user-friendly design that works well on all devices.
- Supports environment variables for secure database connection management.
- Includes an ER diagram to visualize the database structure.
- Implements error handling for database connections and query execution.


## Technologies Used
- **Backend**: Python, Flask, SQLAlchemy, Pandas
- **Database**: MySQL
- **Frontend**: HTML, CSS
- **Environment Management**: dotenv for managing environment variables
- **Virtual Environment**: venv for Python package management

## Project Structure

### File Descriptions

- **`app/db.py`**: Contains the database connection logic.
- **`app/queries.py`**: Contains functions for fetching course registration data from the database **(MySQL)**.
- **`app/er_diagram/`**: Contains the Entity-Relationship diagram for the database schema.
- **`static/`**: Contains static files such as CSS and images.
- **`templates/`**: Contains HTML templates for rendering views.
- **`.env`**: Environment variables for database configuration.
- **`main.py`**: Main file to initialize and run the Flask application.
- **`requirements.txt`**: Lists the required Python packages.
- **`.gitignore`**: Specifies files and directories to be ignored by Git.

## Setup Instructions
1. Detailed steps for cloning the repository, creating a virtual environment, activating it, installing requirements, setting up environment variables, and running the application.
2. **Clone the repository:**
   ```bash
   git clone https://github.com/Elilchandran/NPTEL.git
   cd <repository-directory>

## Create a virtual environment:
- **python -m venv venv**

- On Windows command prompt:
**venv\Scripts\activate**

## Install required packages:
- **pip install -r requirements.txt**

    --Set up your environment variables: Create a **.env** file in the root directory of the project and add your database credentials:

- **env**

  **`DB_HOST=127.0.0.1`**

  **`DB_PORT=3306`**

  **`DB_USER=*********`**

  **`DB_PASSWORD=*********`**
 
  **`DB_NAME=registration`**

## Run the application:

**cmd:**
- python main.py

- Access the application: Open your web browser and navigate to **http://127.0.0.1:5000**.
  
- It contains/ **Display the individual table details** of Account, Application, TermCourseRegistration, course along with Course Registration Data Details from MySql (database)


## Enhancement:
- Deploy the web application using Render for better performance and scalability.
- Utilize AWS services to improve data management and add features like notifications for course updates.

## ER Diagram:
- **Project Structure:** Included an `er_diagram/` section for your ER diagram as part of the project structure.


<img src="https://github.com/Elilchandran/NPTEL/blob/master/er_diagram/ER_diagram.png?raw=true" alt="ER Diagram" width="500" style="display: block; margin: auto;">
