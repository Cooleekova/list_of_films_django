# Films list :movie_camera:
## A simple web application written in Python (Django framework)

The site represents a table containing a list of random films.  
Implemented pagination and the ability to search and sort by each of table fields.

Data in CSV format obtained from open sources.  
The command `load_from_csv`has been created to load data from a file:
 
`python manage.py load_from_csv films`

For a visual demonstration the project is deployed to Heroku web server,
[click here](https://list-of-films-django.herokuapp.com/) to open it.

CI/CD was set up using GitHub Actions.

### Used technologies:
- Python 3.9
- Django 3.2
- PostgreSQL 13.2
- Heroku cloud platform
- GitHub Actions
