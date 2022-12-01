# Moneyfest
A web app for tracking expenses and budgets.

## Features
  * Quick and bulk expensing
  * Budget creation and automatic tracking of expenses per budget
  * Custom spend categories
  * Dashboard with dynamic reporting
  * Detailed reports that break down spending
  * Add additional payers for tracking expenses across multiple people
  * Export your data directly into raw, CSV, and Excel
  * Responsive design - compatible with all major browsers and devices

## Built with
  * Back-end: [Flask](https://flask.palletsprojects.com)
  * Hosting: [Heroku](https://www.heroku.com)

## Run it locally (written for Windows and VSCode)
1) Create a directory and clone the repo in it:
```
git clone https://github.com/eddyharrington/Tendie-Tracker
```
2) Create your virtual environment:
```
python -m venv env
```
3) Activate your virtual environment:
```
env\Scripts\activate
```
4) Install the dependencies:
```
pip install -r requirements.txt
```
5) Create the DB in Postgres (schema in repo [here](./dbCreateStatements-Postgres.txt))

6) Set your environment variables in .env file (otherwise hard code the string ```app.secret_key``` in app.py and ```engine``` in all of the ```.py``` files):
```
# App variable
SECRET_KEY=someRandomStringOfText

# DB variable
DATABASE_URL=postgres://{user}:{password}@{hostname}:{port}/{database-name}
```
7) Build and run the Flask app in VSCode

