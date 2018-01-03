# PYTHON Flask REST-API
  It is Python RESTful API application program interface (API), build with the Flask framework,  that uses <b>HTTP</b> requests to <b>GET</b>, <b>PUT</b>, <b>POST</b> and <b>DELETE</b> data. A RESTful API -- also referred to as a RESTful web service. Its main goal is to act as a middleman in project in order   to transfer data from Data Store to the GUI and vise versa.  
  
## Getting Started
  The Instructions below, will help you get started with a copy on your local machine and will equally give you an understanding of the project structure.
  
### Requirements
 In other to run this application, you will need a set of tools or components installed on your local machine.
  #### Tools Required
  <div>
    <ul>
      <li>Install Python 3.5 and above, you can get it from here <b>download</b>: https://www.python.org/downloads/</li>
      <li>Install python PIP liabrary, <b>command:</b> <i>python install pip/pip3</i></li>
      <li>Install Flask, <b>pip install flask</b></li>
      <li>Install Flask-SQLAlchemy, Flask-Marshmallow, Flask-CORS, Flask-Classy, Flask-WTF for example: <b>commnad: </b> <i>pip install         Flask-CORS</i></li> 
    </ul>
  </div>
  <h4>Setting up Database</h4>
  The project uses SQLAlchemy to link to the database <span><b style="color:red">Note*</b> You need to have a SQL local server installed and running on your machine. In this case MySQL is good you can equally use others database which are SQL. Create a SQL database and name it <b>todos</b>, access the config folder in the application and open base_config in your text editor change the path of <b>SQLALCHEMY_DATABASE_URI</b> to that of your database in your local machine. Finally luanch the app using the command line <b>command: </b> <i>python run.py</i> while inside the main application directory.</span>
<h4>Creating tables</h4>
Once the databse set up properly to create already designed tables using SQLAlchmey, access http://127.0.0.1:5000/api/. A page will open then you will have a create tables button click on it and the table <b>tasks</b> will be created in your database.

<h3>Built with</h3><hr/>
<ul>
  <li>Python Flask</li>
</ul>

<h3> Acknowledgments </h3>
<ol>
  <li>Pretty Printed by Anthony for past training. https://prettyprinted.com</li>
  <li>Inspiration</li>
</ol>

<h3>Authors</h3><hr/>
<ul>
  <li>Mbu Atang Junior Gerald: Built to support my ReactJS Todos application. https://github.com/mbugerald/react-redux-todo </li>
</ul>
