=====
Polls
=====

Polls is a Django application to conduct web based polls.
For each question, visitors can choose between a fixed number of answers.

Detailed documentation in "docs" directory.

Quick Start
-----------
1. Add "polls" to INSTALLED_APPS settings like this::

    INSTALLED_APPS = [
        ...
        'polls',
    ]

2. Include the polls URLConf in project urls.py like this::
    
    path('polls/', include('polls.urls')),

3. Configure the database engine in the settings.py file. SQLite3 can be used. This package is currently
   setup to use the sql database. On systemd linux, start the mysql database like this::
       
       $ sudo systemctl start mysqld

   please refer your distribution's documentation to install mysql if not present.

4. Run ``python manage.py migrate`` to create the polls models in the database.

5. Start the development server. Navigate to http://127.0.0.1:8000/admin and create a poll.

6. Visit http://127.0.0.1:8000/polls to list the polls and participate in one of them. The choices will be
   sent to admin who can collate the results.


