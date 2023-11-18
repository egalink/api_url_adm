# URLSHORTENER

An url shortener microservice written on python using flask framework.


### first steps:

- Clone this repository.
- CD to the application repository to create a virtual environment to run the app in development mode.
 
    **Linux:**
    ```
    1. cd urlshortener/
    2. python3 -m venv venv
    ```

- Activate the new environment and install all the python dependences:

    **Linux:**
    ```
    1. source venv/bin/activate
    2. pip install --no-cache-dir -r requirements.txt
    ```
- Set the environment variables inside a `.env` file and run the application

    **Linux:**
    ```
    1. cp .env.example .env
    2. python3 start.py
    ```

### Minimum Requirements:

1. Python = 3.8.18
2. Mongo DB >= 4 