# StartWay
A platform for solving the problem of algerian startups

# Instructions
## Installation steps:
0. This python app was developed on python 3.12.2

1. Create a python virtual environement
- for a windows machine use the following:
```
python -m venv venv
```
- for a linux machine use the following:
```
python3 -m venv venv
```
2. Activate the virutal environment 
- for a windows machine use the following:
```
venv\Scripts\activate 
```
- for a linux machine use the following:
```
source venv/bin/activate
```
4. install dependencies 
```
pip install -r requirements.txt
```
5. Change the directory to 
## Running Steps:

1. change the directory to the "startWay" project directory then run the command 
```
python manage.py migrate
```
To run the migrations and create the db and tables
2. Run the local server . In the same directory do the command
```
python manage.py runserver
```
3. Go to localhost:8000 to acess the webapp