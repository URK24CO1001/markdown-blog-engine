from flask import Flask, render_template
import markdown
import os

app = Flask(__name__)

POSTS_DIR = "posts"

@app.route("/")
def home():
    posts = []

    for filename in os.listdir(POSTS_DIR):
        if filename.endswith(".md"):
            posts.append(filename[:-3])

    return render_template("index.html", posts=posts)

@app.route("/post/<name>")
def post(name):
    filepath = os.path.join(POSTS_DIR, f"{name}.md")

    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()

    html = markdown.markdown(content)

    return render_template(
        "post.html",
        title=name,
        content=html
    )

if __name__ == "__main__":
    app.run(debug=True)