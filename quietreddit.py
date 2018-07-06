from flask import Flask, render_template
import praw, config

app = Flask(__name__)

reddit = praw.Reddit(client_id = config.client_id,
                client_secret = config.client_secret,
                user_agent = config.user_agent)

@app.route("/")

def index():
    posts_list  = []
    for submission in reddit.front.hot(limit = 30):
        posts_list.append(submission)
    return render_template("layout.html", posts=posts_list)


if __name__ == "__main__":
    app.run()
