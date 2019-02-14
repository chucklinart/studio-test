import os
import requests
import json
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def studio_test():
    uri = 'https://xkcd.now.sh'
    try:
        uResponse = requests.get(uri)
    except requests.ConnectionError as ex:
        return "Connection Error:" + ex
    Jresponse = uResponse.text
    data = json.loads(Jresponse)
    # return str(data)
    return render_template('xkcd.html', latest=data)

# since the XKCD API does not have an endpoint that delivers all comics, we will write a longer list 
# to a local file by hitting this endpoint with a cron job

@app.route('/write-local-json/blahblahsupertopsecret')
def get_all_comics():
    # a bit of repetition but only a few lines and this will be the last time. not worth abstracting
    uri = 'https://xkcd.now.sh'
    try:
      uResponse = requests.get(uri)
    except requests.ConnectionError as ex:
      return "Connection Error:" + ex
    Jresponse = uResponse.text
    data = json.loads(Jresponse)
    # we need the second one in the list so we'll offset by one
    num = data['num'] -1
    pagerange = num - 100
    comiclist = []
    # this will allow a second button click (but not a third -- already spent too much time on this)
    if not comiclist:
      num = num
    else:
      num = pagerange -1
      # reset pagerange or the arithmetic doesn't work
      pagerange = num -10
    for i in range(num, pagerange, -1):
        # need json 'out of the box' in loop so use different endpoint
        pagedata = requests.get('https://xkcd.com/'+str(i)+'/info.0.json').json()
        comiclist.append(pagedata)
    comiclist
    with open(os.path.dirname(__file__)+'/static/tmp/json/all.json', 'w') as outfile:
        json.dump(comiclist, outfile)
    return

@app.route('/full-list')
def full_list():
    # get json from local file to take load off api server
    local_data = open(os.path.dirname(__file__)+'/static/tmp/json/all.json', 'r').read()
    data = json.loads(local_data)
    ret = json.dumps(data)
    return ret
    # return render_template('full-list.html', comics=ret)

@app.route('/single-pane/<number>')
def single_pane(number):
    return render_template('single.html', number=number)

@app.route('/favorites')
def list_favorites():
    # get favorites from cookie
    cookie = request.cookies.get('favecomics')
    if cookie:
      faves = json.loads(cookie)
    else: 
      faves = ''
    return render_template('favorites.html', faves=faves)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

