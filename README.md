# Quantify Skill By The Evidence
### Description
This is a python django application where users are given a platform to showcase their skill by posting some of the projects to be rated/ reviewed by other programmers.

## author's Information
This code was done and compiled by Jeff Owuor

## user story- - 
- View posted projects and their details
- Post a project to be rated/reviewed
- Rate/ review other users' projects
- Search for projects 
- View projects overall score
- View  profile page


## BEHAVIOUR DRIVEN DEVELOPMENT
| Behaviour  | input  |output   |
| :------------: | :------------: | :------------: |
|Sign in| enter credentials in the login page | profile is made |
|Upload project| Enter the required details e.g project_description | The project is displayed on the home page |
|Rate project| Select from the choices(design,usability,content)| displayed on the single_project page |



## SETUP INSTRUCTIONS
To get the application ...
1. Clone the repo
2. Open the folder with your favorite IDE
3. Create a virtual environment and activate it

4.  Install all the requirements listed in the requirements.txt file.
  $ pip install -r requirements.txt


5. Running the application
    python3 manage.py runserver

6. Testing the application
    python3 manage.py test 

## API Endpoints
- https://skillrating.herokuapp.com/api/posts/
- https://skillrating.herokuapp.com/api/profile/
- https://skillrating.herokuapp.com/api/users/


### Known bugs 
No known bugs but if you find any feel free to reach me at Xavierjeff451@gmail.com
### Technologies used
Python
Heroku
Django
Postgresql
