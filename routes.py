from flask import render_template, request, redirect, url_for
from app import app, db
from datetime import datetime
from bson.objectid import ObjectId

@app.route('/')
def index():
    posts = db.posts.find().sort('created_at', -1)
    return render_template('index.html', posts=posts)

@app.route('/create', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        image_url = request.form.get('image_url')  # Get the image URL from the form (optional)

        # Insert the post into the database, including the image URL
        db.posts.insert_one({
            'title': title,
            'content': content,
            'image_url': image_url,  # Store the image URL
            'created_at': datetime.utcnow()
        })
        return redirect(url_for('index'))
    
    return render_template('create.html')

@app.route('/post/<post_id>')
def view_post(post_id):
    post = db.posts.find_one({'_id': ObjectId(post_id)})
    if post:
        return render_template('post.html', post=post)
    return "Post not found", 404
