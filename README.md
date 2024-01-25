# API_URL_ADM

An url shortener microservice written on python using flask framework.


### First Steps:

- Clone this repository.
- CD to the application repository to create a virtual environment to run the app in development mode.
 
    **Linux:**
    ```
    1. cd api_url_adm/
    2. python3 -m venv venv
    ```

- Activate the new environment and install all the python dependences:

    **Linux:**
    ```
    1. source venv/bin/activate
    2. pip install --no-cache-dir --use-pep517 -r requirements.txt
    ```
    **Important:** The `--use-pep517` flag is used to prevent the "healthcheck" deprecated dependency alert, for more information visit [this link](https://github.com/pypa/pip/issues/8559). If this flag causes unexpected behavior, it should be removed from the integration process and the issue documented in this file so we are aware of the problem.

- Set the environment variables inside a `.env` file and run the application

    **Linux:**
    ```
    1. cp .env.example .env
    2. python3 start.py
    ```

### Minimum Requirements:

1. Python = 3.8.18
2. Mongo DB >= 4 