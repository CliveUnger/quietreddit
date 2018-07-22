from flask import Flask, render_template, request, redirect, url_for,session
import praw, config, pprint

app = Flask(__name__)
app.secret_key = config.secret_key

@app.route("/")
def index():
    auth_link = reddit.auth.url(['identity','read'],'...','permanent')
    
    posts = []
    for submission in reddit.front.hot(limit = 30):
        posts.append(submission)

    return render_template("layout.html", link=auth_link, posts=posts)

@app.route("/authorize")
def authorize():
    code = request.args.get('code', '')
    reddit.auth.authorize(code)
    session['username'] = str(reddit.user.me())
    session['authd'] = True
    return redirect("/")

@app.route("/logout")
def logout():
    reddit.read_only = True
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    reddit = praw.Reddit(client_id = config.client_id,
                    client_secret = config.client_secret,
                    redirect_uri=config.redirect_uri+'/authorize',
                    user_agent = config.user_agent)
    app.run()
