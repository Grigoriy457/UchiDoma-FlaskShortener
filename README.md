# Flask shortener

Make long urls shorter.

## How to run

1. Clone repository 
    ```commandline
    git clone https://github.com/Grigoriy457/UchiDoma-FlaskShortener.git
    ```

2. Make and activate virtual environment
   - Windows:
    ```commandline
    python -m venv venv
    source venv/Scripts/activate
    ```
   - Ubuntu:
    ```commandline
    python -m venv venv
    source venv/bin/activate
    ```

3. Install all libs
    ```commandline
    pip install -r requirements.txt
    ```

4. Create .env file

5. Write settings in .env file
    ```dotenv
    SECRET_KEY=YOUR_SECRET_KEY
    SQLALCHEMY_DATABASE_URI=sqlite:///db.db
    SQLALCHEMY_TRACK_MODIFICATIONS=0
    SQLALCHEMY_COMMIT_ON_TEARDOWN=1
    ```

6. Run flask app
   - Development server:
    ```commandline
    flusk run
    ```
   - Production server ([more info](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04)):
   ```commandline
   gunicorn --bind 0.0.0.0:5000 app
   ```