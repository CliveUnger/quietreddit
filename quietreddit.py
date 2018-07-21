from flask import Flask, render_template, request, redirect, url_for
import praw, config, pprint

app = Flask(__name__)

reddit = praw.Reddit(client_id = config.client_id,
                client_secret = config.client_secret,
                redirect_uri=config.redirect_uri+'/authorize',
                user_agent = config.user_agent)

auth_link = reddit.auth.url(['identity','read'],'...','permanent')

@app.route("/")
def index():
    posts = []
    for submission in reddit.front.hot(limit = 30):
        posts.append(submission)
    return render_template("layout.html", link=auth_link, posts=posts)

@app.route("/authorize")
def authorize():
    state = request.args.get('state', '')
    code = request.args.get('code', '')
    print(state)
    print(code)
    print(reddit.auth.authorize(code))
    print(reddit.user.me())
    return redirect("/")

if __name__ == "__main__":
    app.run()
