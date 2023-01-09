# Instagram (educational project)
It's a educational project. to learn django better...

## Requirements and Technologies
- Python 3.6.9 or maybe higher (hasn't test)
- PostgreSQL 10.12 or maybe higher (maybe MySQL 7.0.0+ work either but hasn't test)
- Django framework 2.2
- HTML5/CSS3
- Bootstrap 4

## Quick Start
- Create a directory and name it "instagram"
- Open a terminal in this directory
- Create a virtualenv:

    `virtualenv -p python3.6 venv`

- Activate virtualenv:

    `source venv/bin/activate`
    
- Clone this project:

    `git clone https://gitlab.com/7learn-py-web/step10/instagram.git instagram`

- Change directory to "instagram":

    `cd instagram`

- Install require packages:

    `pip install -r requirements.txt`
    
- Create a PostgreSQL Database and user:
    - Open postgresql terminal:
    
        `sudo -i -u postgres`

    - Enter root password and run this command to enter postgresql terminal:
    
        `psql`

    - Create database:
    
        `CREATE DATABASE instagram;`
        
    - Create user:
    
        `CREATE USER instagram WITH ENCRYPTED PASSWORD '1234567';`
        
    - Now, all we need to do is give our database user access rights to the database we created:

        `GRANT ALL PRIVILEGES ON DATABASE instagram TO instagram;`
        
    - Exit the SQL prompt to get back to the postgres user’s shell session:

        `\q`
        
    - Exit out of the postgres user’s shell session to get back to your regular user’s shell session:

        `exit`

- Run config_prject.py and enter project setting and PostgreSQL connection details:

    `python manage.py config_project.py`
