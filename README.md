# Moviebot 🤖
Code repository for Moviebot – an NLP-powered movie recommendation chatbot, written in Python, HTML/CSS and JavaScript & hosted on Vercel + AWS Lambda.

![](https://github.com/steven-tey/moviebot/blob/master/static/assets/thumbnail.gif)

This is a group project for my IL181 Practical Data Science tutorial (group members are Dennis, Pedro, and Ahmed).

## Running this locally 🖥
To run this program locally, follow these steps:

1. Download the repo with `git clone https://github.com/steven-tey/moviebot.git`
2. Create a virtual environment with `python3 -m venv venv`
3. Activate your virtual environment with `source venv/bin/activate`
4. Then, install all the required libraries with `pip install -r requirements.txt`
5. Next, export the Flask app route with `export FLASK_APP=index.py`
6. You will also need to export the Flask environment with `export FLASK_ENV=development`
7. Lastly, execute `flask run` and your program should be running at `http://127.0.0.1:5000/`

## Deploying on Vercel ▲
To deploy this to vercel, all you gotta do is run `vercel --prod` in your terminal and follow through with the default setup criteria, as shown below:
```
? Set up and deploy “~/Desktop/username/moviebot”? [Y/n] y
? Which scope do you want to deploy to? vercel-username
? Link to existing project? [y/N] n
? What’s your project’s name? moviebot
? In which directory is your code located? ./
> Upload [====================] 98% 0.0sNo framework detected. Default Project Settings:
- Build Command: `npm run vercel-build` or `npm run build`
- Output Directory: `public` if it exists, or `.`
- Development Command: None
? Want to override the settings? [y/N] n
```
If you run into the error `zsh: command vercel not found`, you might need to run the following:

```
export PATH="/Users/steventey/.npm-global/bin/:$PATH"
```

## The AWS Lambda Function 💪
We are still making changes to the AWS Lambda function and will be publishing this soon!

## Question + Bug Fixes 🐞
Feel free to contact me at [stey@minerva.kgi.edu](mailto:stey@minerva.kgi.edu) for more information about this project.
