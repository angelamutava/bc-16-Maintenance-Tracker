# bc-16-Maintenance-Tracker

This is a web application that allows reporting of maintainance and repair requests, to track the maintenance process and escalate unusual delays.



##Basic functionalities.

1. User Registration
2. User signIn
3. User request maintainance/repair
4. Admin accept/reject a maintainance/repair. In case of a reject provide comment.
5. Admin assign maintainance/repair to relevant user
6. User get a notification once a repair/maintanance has been resolved
7. As admin, I should be able to add names and contacts (phone number) for the people doing maintenance.


##Installation To get the application up and running on your environment.

1.git clone the repository.



2.Configure the virtual environment.
3.In your virtual aenvironment run the command.

```pip -r requirements.txt```

4.Navigate to the folder bc-16-Maintanance-Tracker.
5.Initialize the database .
6.Run the application with the command.

  ```python manage.py runserver```


##Requirements
 1. Language python 2.7 or python 3.0 should be installed in your machine.<br/>
 2. To install the required dependencies for the application to run on your machine run the below command in the virtual environment.

```pip install -r requirements.txt on your machine.```

###Initialize the db with the command.

python manage.py db init

###Migrations

python manage.py db migrate

###Upgrading the database.

python manage.py db upgrade

###Run the server

python manage.py runserver


## Tasks not accomplished.

