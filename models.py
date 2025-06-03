from datetime import datetime

# User model (simplified)
def create_user(username, email, password, image_url=None):
    user = {
        'username': username,
        'email': email,
        'password': password,  
        'created_at': datetime.utcnow(),
        'image_url': image_url  
    }
    return db.users.insert_one(user)

# Post model
def create_post(title, content, author_id, tags=[], image_url=None):
    post = {
        'title': title,
        'content': content,
        'author_id': author_id,
        'tags': tags,
        'created_at': datetime.utcnow(),
        'image_url': image_url  # Optional image URL field for the post
    }
    return db.posts.insert_one(post)
