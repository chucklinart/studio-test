#Studio job interview test

This is just a silly little app designed to show that I know how to code.  It reaches out to the XKCD API and gets data.  
The challenge here was that the API has not endpoints that deliver all comics or filters of any kind.  So you couldn't, for 
example, just `$ curl "https://xkcd.api/?year=2017` to retrieve all comics from 2017.  

What I did was create an endpoint on my end that will be hit by a cron job every couple hours.  It takes a load off the API 
because to get any kind of list, multiple requests have to be made. So we do this every couple hours and store the list 
locally as a JSON file.

There were also some limitations regarding the data itself. For example, the spec I received showed a date being displayed, 
but the API does not deliver the date of publication, just a year, so this was a total no-go.

The main TODO that remains is to make the styling of the pressed "favorites" button persist upon page reload.  Right now it only 
persists if you hit the browser's "back" button.

If this were a real app, I would have implemented a Login/Register scheme and database and all that.  I also would have done the 
insertion of the "More" comics differently, with a Python Flask child template and lazy load scroll.  But I was having fun with 
the JS click function and just kind of went down that road.

##To run locally:

1) Clone the repo
2) Set up a Python environment at Python 3.4x+ I usually put all my environments in a directory one level above my projects.  This 
   one was called "studioenv" so you could `$ python3 venv studioenv -env`
3) Activate the environment `$ source studioenv/bin/activate` and navigate to the project root where the studio_test.py is located
4) Define the Flask app `$ export FLASK_APP=studio_test.py`
5) Run the app `$ flask run`

The app will be visible in your browser at http://127.0.0.1:5000
6) navigate to http://127.0.0.1:5000/write-local-json/blahblahsupertopsecret to load the local data.  This takes a few minutes due
   to the API

**In its current state, the app will not persist the state of your favorited "Favorite" buttons.  The favorites themselves will be 
visible**


In the "production" environment it runs on a proper gunicorn/nginx stack.
:wq
