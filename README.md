# Squirrel Tracker Project

<img src = "https://images.squarespace-cdn.com/content/5b834741f407b4df429d791a/1561681623533-A7X6X0H2FW9A9OIJW79J/Acorn_Starburst_Name_Blue.png?content-type=image%2Fpng">

# Project Description:
Squirrels are everywhere in NYC's Central Park. We are helping out to keep track of all known squirrels. This is an application that can import the 2018 Central Park Squirrel Census data and allow his team to add, update, and view squirrel data. Leverage Django, we coded backend files with python and front end files with html. 

# Group Name and Section
Project Group 38, Section 1
Benjamin Byeon and Matthew Hamati

# UNIs
[bb3037, mnh2128]

# Link to the Server
In order to run this interface it's imperative to follow the steps below:

At the command line:
git clone https://github.com/hamats423/Squirrel_Project.git

To install the dependencies in the requirements.txt file:
pip install -r requirements.txt

After these steps you should be able to launch the webpage using the command below:
sudo /home/USERNAME/DIRECTORY/env/bin/python manage.py runserver 0.0.0.0:80

# Different views
To access the list of all squirrels: sightings/

To access a map of squirrel sightings: map/

To access some stats about the sightings: sightings/stats/

To view/update information about a specific squirrel: sightings/<unique-squirrel-id>

To add data for a new sightings: sightings/add/

Note: All sites have a drop down menu at the top to help navigate between pages!



