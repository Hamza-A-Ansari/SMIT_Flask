# Python Flask <br>
## Python Virual Environment:
Python, just like other modern programming languages, provides a huge
amount of third-party libraries and SDKs. Different applications might need
various specific versions of third-party modules, and it won’t be possible for
one Python installation to meet such requirements of every application. So,
in the world of Python, the solution for this problem is virtual environment,
which creates a separate self-contained directory tree containing a Python
installation of the required version alongside the required packages.<br>
## Installing flask windows:<br>
<b>firstly its neccessary to have python intalled in your machine<br></b> 
```pip install flask```<br>
for checking version:<br>
```pip show flask```<br><br>
When you install Flask, the following distributions are installed with
the main framework:<br>
* <b>Werkzeug</b>:Werkzeug implements WSGI(Web Server Gateway Interface), the standard Python
interface between the application and the server.<br>
* <b>Jinja</b>: Jinja is the templating engine in Flask which renders the pages for the application.<br>
* <b>MarkupSafe</b>:It protects API from injection attacks.<br>
* <b>ItsDangerous</b>:ItsDangerous is responsible for securely signing data to ensure data integrity and is used to protect Flask session cookies.<br>
* <b>Click</b>: Click is a framework to write CLI applications. It provides the “Flask” CLI command.<br>
## Environments in flask:
There are three types of Environment in flask:
 * <b>Production Environment</b>:production environments for online deployment
 * <b>Development Environment</b>:development environment that generally uses for local development environments
 * <b>Testing Environment</b>:testing environment for test environments, general for various test uses<br><br>
we can change flask enivronment by running the following command in window's shell/cmd:<br>
```set FLASK_ENV=development```<br>
```set FLASK_ENV=testing```<br>
```set FLASK_ENV=development```<br>