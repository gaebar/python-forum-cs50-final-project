# python-forum-cs50-final-project
Forum / social website project built with Python, Django, SQLite and Bootstrap

## Installation Requirements

`pip install django`

`pip install pillow`

`pip install django_crispy_forms`

## Run the app
1. Activate the virtual environment running `source myvirtualenv/bin/activate`
2. go on the social_site folder
3. run `python3 manage.py runserver` and open the localhost port `http://127.0.0.1:8000/`



## Server
Django version 3.0.8, using settings 'social_site.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

## access to the database
To access to the database you can use the built-in [Django Admin site](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Admin_site#:~:text=To%20login%20to%20the%20site,'ve%20entered%20your%20details).
- run `python3 manage.py runserver`
- To login to the site, open the /admin URL (e.g. http://127.0.0.1:8000/admin)


## Future Improvements

The next stage of this project would be adding these features, for example:
 * user profile picture
 * edit option
 * link preview
 * Private messages functionality
 * Language translator to let the user choose the prefer reading language.
 * A night mode, based on the latest browsers API, which allow to determine whether the user has chosen a dark for their OS.
