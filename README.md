# PROJECT-X

## Setup

1. Install python backend dependencies by running the following in the root of the project:

```shell
pip install -r requirements.txt
```

2. Install javascript dependencies by first changing directories to the client folder then instaling them with:

```shell
cd client
npm install
```

3. Set up the database tables with the following command from the root of the project:

```shell
PYTHONPATH=. python create_tables.py
```

## Running for development

1. Start the flask server by running the following in the root of the project:

```shell
PYTHONPATH=. FLASK_ENV=development FLASK_APP=main.py flask run
```

2. Then in a seperate terminal window or tab start the react development server by changing directories to the client folder then starting the script:

```shell
cd client
npm run start
```

The app should now be accesable through your localhost on port 3000. Both development servers should hot reload anytime changes are made.

## Production set up

1. To deploy you must first build a production build of the react application with the following commands:

```shell
cd client
npm run build
```

The flask app will now serve the react application to the client via the '/' route
