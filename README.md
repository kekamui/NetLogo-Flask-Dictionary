# NetLogo-Flask-Dictionary
This is a documentation dictionary for NetLogo written in Python and Flask. This project was built with Umit Aslan as the supervisor.

## Installing
Enter `git clone https://github.com/kekamui/NetLogo-Flask-Dictionary.git` to get a copy of the project. You should install Python 3 and any packages to run the project if needed.

## Running
Enter `python3 app.py` to run it locally. You can also link your folder to a Heroku server to see it live. The server will update if connected properly and once you push to heroku master. The link to get started is here: [Heroku Tutorial](https://devcenter.heroku.com/articles/getting-started-with-python#introduction).

## app.py
app.py is the main file that contains all the page routes. `load_html` is the function that renders a standard layout of pages based on `conf` file data. You need to edit both app.py and the specific html page to call the rendering as shown below:

app.py
```
@app.route("/agentset")
def agentset():

    agentset_conf = ConfigFactory.parse_file('conf/agentset.conf')
    agentset_prim = agentset_conf.get_list('primitives')

    html = load_html(agentset_prim);

    return render_template('agentset.html',task=Markup(html))
```
agentset.html
```
<div class=agentset>
  {{task}}
</div>
```
## templates
All html files are located and should be placed in this folder.


## static
All css files, pictures, and icons are located and should be placed in this folder.

## conf
All conf files are located and should be placed in this folder. These files are similar to JSON files and contain data to be called from `load_html`.
