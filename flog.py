import os
import mistune
from flask import Flask, render_template
import yaml

app = Flask(__name__)

def load_yaml():
    if os.path.exists('config.yaml'):
        return yaml.load(open('config.yaml', 'r'), Loader=yaml.FullLoader)
    print('ERROR: Flog requires a config.yaml file in the root directory')
    return False

def load_posts():
    config = load_yaml()
    post_files = [f for f in os.listdir(config['POSTS_DIR']) if os.path.isfile(os.path.join(config['POSTS_DIR'], f))]
    config['posts'] = []

    for pf in post_files:
        fname = os.path.splitext(pf)[0]
        config['posts'].append({
            'title': ' '.join(fname.split('_')),
            'url': os.path.join(config['POSTS_DIR'], pf)
        })
    return config


@app.route('/')
def all_posts():
    config = load_posts()
    return render_template('posts.html', data={
        'blog_title': config['BLOG_TITLE'],
        'posts': config['posts']
    })


@app.route('/<path:md_file>')
def single_post(md_file):
    with open(md_file) as file_handle:
        markdown_data = file_handle.read()
    md = mistune.markdown(markdown_data)
    return render_template('single_post.html', content=md)


@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(
        debug=False,
        host='127.0.0.1',
        port=5000
    )
