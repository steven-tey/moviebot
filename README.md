# Moviebot
Code repository for Moviebot – an NLP-powered movie recommendation chatbot, written in Python, HTML/CSS and JavaScript & hosted on Vercel + AWS Lambda.

![](https://github.com/steven-tey/moviebot/blob/master/static/assets/thumbnail.png)

This is a group project for my IL181 Practical Data Science tutorial (group members are Dennis, Pedro, and Ahmed).

To run this locally, follow these steps:

1. Download the repo with `git clone https://github.com/steven-tey/moviebot.git`
2. Create a virtual environment with `python3 -m venv venv`
3. Activate your virtual environment with `source venv/bin/activate`
4. Then, install all the required libraries with `pip install -r requirements.txt`
5. Next, export the Flask app route with `export FLASK_APP=index.py`
6. You will also need to export the Flask environment with `export FLASK_ENV=development`
7. Lastly, execute `flask run` and your program should be running at `http://127.0.0.1:5000/`

Feel free to contact me at [stey@minerva.kgi.edu](mailto:stey@minerva.kgi.edu) for more information about this project.
