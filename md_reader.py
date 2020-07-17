import os
import mistune
from flask import Flask, render_template
import yaml

app = Flask(__name__)

POSTS_DIR = 'posts/'
posts = []
post_files = [f for f in os.listdir(POSTS_DIR) if os.path.isfile(os.path.join(POSTS_DIR, f))]

for pf in post_files:
    fname = os.path.splitext(pf)[0]
    posts.append({
        'title': ' '.join(fname.split('_')),
        'url': os.path.join(POSTS_DIR, pf)
    })


@app.route('/')
def all_posts():
    return render_template('posts.html', posts=posts)


@app.route('/<path:md_file>')
def single_post(md_file):
    with open(md_file) as file_handle:
        markdown_data = file_handle.read()
    md = mistune.markdown(markdown_data)
    return render_template("single_post.html", content=md)


@app.errorhandler(500)
def page_not_found(e):
    # note that we set the 500 status explicitly
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(
        debug=False,
        host='127.0.0.1',
        port=5000
    )
