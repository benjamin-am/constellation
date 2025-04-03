# bcs-hacks-roots

BCS Hacks Project

## Set up

### To Set Up Conda Env

windows:

```
conda env create -f environment.yml
```

macOS:

```
conda env create -f environment-mac.yml

```

### Set up docker

Download docker from http://docker.com/get-started/

Create the .ENV file inside `/bcs-hacks-roots/backend`

### Set up the database with docker and postgres

In terminal naviage to `/bcs-hacks-roots/backend`:

`docker-compose up -d`

### Push the test data to the database

Run `data_push.ipynb` to push the test data from the repo to the database.

You can switch the path in the file to other test folders if you want to push more test data to the database.

You can also upload or crate more test data into the resources folder. Just make sure to update the file path.

### useful SQL command

check number of rows in the note_data table
` select count(*) from note_data`

wipe the table and reset the auto-increment ID counter
`TRUNCATE TABLE note_data RESTART IDENTITY;`

see all title values from the note_data table
`select title from note_data;`

# Start the app

In one terminal:

- Navigate to the backend directory `/bcs-hacks-roots/backend`
- Type `conda activate stack` (if not already in stack), `python manage.py runserver`
  In another terminal:
- Navigate to the frontend directory `/bcs-hacks-roots/frontend`
- Type `conda activate stack`(if not already in stack), `npm install`, then `npm start`
  You should be able to access the app at (http://localhost:3000)
