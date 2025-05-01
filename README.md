# Flask Server

This project is a simple Flask server that uses Gunicorn or Waitress for production deployment and `python-dotenv` for storing configuration variables.

## Requirements

Make sure you have Python 3.7 or newer installed on your system.

## Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/your-project-name.git
   cd your-project-name

python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python run.py
python wsgi.py
