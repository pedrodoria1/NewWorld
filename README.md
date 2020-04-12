Flask on App Engine Project Template (Deprecated)
=================================================

IMPORTANT: This project is deprecated (primarily due to Python 2 end-of-life as of 1 Jan 2020) 
and has been supplanted by the following, which supports Flask in Python 3
on Google App Engine's second-generation runtimes...

https://github.com/kamalgill/cloud-starterkit-flask-appengine

Boilerplate project template for running a Flask-based application on
Google App Engine's Standard Python 2.7 Runtime

Similar boilerplate projects are listed below:

- [gae-init](https://github.com/gae-init/gae-init)
- [gae-boilerplate](https://github.com/coto/gae-boilerplate)


App Engine Flexible Environment
-------------------------------
This project does not currently support deployments on the App Engine Flexible environment,
although it could potentially work on App Engine Flexible with some modifications.

See the official [Quickstart for Python in the App Engine Flexible Environment][quickstart]
if you are looking to deploy Python 2.7 and 3.x applications on App Engine


About Flask
-----------
[Flask][flask] is a BSD-licensed microframework for Python based on
[Werkzeug][wz], [Jinja2][jinja2] and good intentions.

See <http://flask.pocoo.org> for more info.


Setup/Configuration
-------------------
1. Download this repository via
   `git clone https://github.com/kamalgill/flask-appengine-template.git`
   or download the tarball at
   <http://github.com/kamalgill/flask-appengine-template/tarball/master>
2. Copy the src/ folder to your application's root folder
3. Set the application id in `src/app.yaml`
4. Configure datastore models at `src/application/models.py`
5. Configure application views at `src/application/views/`
6. Configure URL routes at `src/application/urls.py`
7. Configure forms at `src/application/forms.py`
8. Add the secret keys for CSRF protection by running the `generate_keys.py`
   script at `src/application/generate_keys.py`, which will generate the
   secret keys module at src/application/secret_keys.py

Note: Copy the .gitignore file from the tarball folder's root to your git
repository root to keep the secret_keys module out of version control.

Or, add the following to your .(git|hg|bzr)ignore file

<pre class="console">
  # Keep secret keys out of version control
  secret_keys.py
</pre>


Install python dependencies
---------------------------
The local dev environment requires installation of Jinja2, PIL, and simplejson,
which can be installed via:

<pre class="console">
  pip install -r requirements_dev.txt
</pre>


Front-end Customization
-----------------------
1. Customize the main HTML template at
   `src/application/templates/base.html`
2. Customize CSS styles at `src/application/static/css/main.css`
3. Add custom JavaScript code at `src/application/static/js/main.js`
4. Customize favicon at `src/application/static/img/favicon.ico`
5. Customize 404 page at `src/application/templates/404.html`


Previewing the Application
--------------------------
To preview the application using App Engine's development server,
use [dev_appserver.py][devserver]

<pre class="console">
  dev_appserver.py src/
</pre>

Assuming the latest App Engine SDK is installed, the test environment is
available at <http://localhost:8080>


Admin Console
-------------
The admin console is viewable at http://localhost:8000 (note distinct port from dev app server)


Flask-Cache
-----------
The handy Flask-Cache extension is included, pre-configured for App Engine's Memcache API.
Use the "Flush Cache" button at http://localhost:8000/memcache to clear the cache.


Testing
-------
Place all your tests in src/tests directory. Test runner is placed in src directory. To run your tests simply go to src directory and do:

<pre class="console">
  python apptest.py path/to/your/googleappengine/installation
</pre>

Path to your local google app engine installation must be provided as first argument to the script. If the path is long and you don't like to type it each time you run the tests you can also hardcode it in apptest.py, just edit the variable SDK_PATH and set it to your google app engine folder. 

Before running tests set evironment variable FLASK_CONF to the value TEST. 

In Linux this is done by:

<pre class="console">
  export FLASK_CONF=TEST
</pre>

In Powershell:

<pre class="console">
  [Environment]::SetEnvironmentVariable("FLASK_CONF", "TEST", "User");
</pre>

Remember to restart Powershell. Change of environment variable will take place after restarting Powershell. 

You can specify your testing configuration (e.g. separate database for tests results) in src/application/settings.py.

To switch back to development configuration just set FLASK_CONF to DEV.

Deploying the Application
-------------------------
To deploy the application to App Engine, use [appcfg.py update][appcfg]
<pre class="console">
  appcfg.py update src/
</pre>

The application should be visible at http://{YOURAPPID}.appspot.com


Folder structure
----------------
The App Engine app's root folder is located at `src/`.

<pre class="console">
  src/
  |-- app.yaml (App Engine config file)
  |-- application (application code)
  |-- index.yaml (App Engine query index definitions)
  |-- lib/
  |   |-- blinker/ (library for event/signal support)
  |   |-- flask/ (Flask core)
  |   |-- flask_cache/  (Flask-Cache extension)
  |   |-- flask_debugtoolbar/  (Port of Django Debug Toolbar to Flask)
  |   |-- flaskext/ (Flask extensions go here)
  |   |-- gae_mini_profiler/ (Appstats-based profiler)
  |   |-- itsdangerous.py (required by Flask >= 0.10
  |   |-- werkzeug/ (WSGI utilities for Python-based web development)
  |   `-- wtforms/ (Jinja2-compatible web form utility)
  |-- tests/ (unit tests)
</pre>

The application code is located at `src/application`.

<pre class="console">
  application/
  |-- __init__.py (initializes Flask app)
  |-- decorators.py (decorators for URL handlers)
  |-- forms.py (web form models and validators)
  |-- models.py (App Engine datastore models)
  |-- settings.py (settings for Flask app)
  |-- static
  | |-- css
  | | |-- bootstrap-*.css (Twitter Bootstrap styles)
  | | |-- fontawesome-*.css (Fontawesome styles)
  | | `-- main.css (custom styles)
  | |-- font
  | | `various fontawesome font files
  | |-- img
  | | |-- favicon.ico
  | | |-- favicon.png
  | | `-- glyphicons-*.png (Twitter bootstrap icons sprite)
  | `-- js
  |   |-- main.js (site-wide JS)
  |   `-- lib/ (third-party JS libraries)
  |     |--bootstrap-*.js (Bootstrap jQuery plugins
  |     `--modernizer-*.js (HTML5 detection library)
  |-- templates
  | |-- includes/ (common include files)
  | |-- 404.html (not found page)
  | |-- 500.html (server error page)
  | |-- base.html (master template)
  | |-- list_examples.html (example list-based template)
  | `-- new_example.html (example form-based template)
  |-- urls.py (URL dispatch routes)
  |-- views
  |   |-- admin
  |     `-- *.py (Views which require authentication)
  |   |-- public
  |     `-- *.py (Public views)
</pre>



Licenses
--------
See licenses/ folder


Package Versions
----------------
- Blinker: 1.4
- Bootstrap: 3.0.0
- Click: 6.7
- Flask: 0.12.2
- Flask-Cache 0.13.1
- Flask-DebugToolbar: 0.10.1
- Flask-WTF: 0.14.2
- FontAwesome: 3.0
- itsdangerous: 0.24
- Jinja2: 2.6 (included in GAE)
- jQuery: 3.2.1 (set in base.html)
- Modernizr: 2.6.2
- Werkzeug: 0.12.2
- WTForms: 2.1


Credits
-------
Project template layout was heavily inspired by Francisco Souza's
[gaeseries Flask project][gaeseries]

Incorporates [Flask-DebugToolbar][debugtoolbar] by Matt Good et. al.
and [Flask-Cache][flaskcache] by Thadeus Burgess

Layout, form, table, and button styles provided by [Bootstrap][bootstrap]

[Font Awesome][fontawesome] by Dave Gandy

HTML5 detection provided by [Modernizr 2][modernizr] (configured with all features)


[appcfg]: http://code.google.com/appengine/docs/python/tools/uploadinganapp.html
[bootstrap]: http://twitter.github.com/bootstrap
[debugtoolbar]: https://readthedocs.org/projects/flask-debugtoolbar/
[devserver]: http://code.google.com/appengine/docs/python/tools/devserver.html
[flask]: http://flask.pocoo.org
[flaskcache]: http://pythonhosted.org/Flask-Cache/
[fontawesome]: http://fortawesome.github.com/Font-Awesome/
[html5]: http://html5boilerplate.com/
[jinja2]: http://jinja.pocoo.org/2/documentation/
[gaeseries]: http://github.com/franciscosouza/gaeseries/tree/flask
[modernizr]: http://www.modernizr.com/
[profiler]: http://packages.python.org/Flask-GAE-Mini-Profiler/
[quickstart]: https://cloud.google.com/appengine/docs/flexible/python/quickstart
[wz]: http://werkzeug.pocoo.org/
[wzda]: https://github.com/nshah/werkzeug-debugger-appengine
