#!/usr/bin/env python
""" Blueprint routes"""

from web_static.views import app_views
from flask import render_template, request, url_for, redirect
from web_static.a_i_database import generate_blog_post, load_model
from models.post import Post
from models import storage

model, tokenizer = load_model()


@app_views.route('/home/', methods=['GET', 'POST'], strict_slashes=False)
@app_views.route('/', methods=['GET', 'POST'], strict_slashes=False)
# @app_views.route('/generate/', methods=['POST'], strict_slashes=False)
def home():
    """ Handles all paths """
    generated_posts = []
    if request.method == 'POST':
        title = request.form.get('title')
        prompt = request.form.get('content')  # Replace 'user_input' with the actual name attribute of your form input

        print(f"Title: {title}")  # Debugging output
        print(f"Content: {prompt}")

        content = generate_blog_post(prompt, model, tokenizer)
        print(content)

        new_post = Post(title=title, body=content)
        storage.new(new_post)
        storage.save()  # Placeholder function for text generation

        # Store the generated post (you could use a list or dictionary depending on your requirements)
        posts = storage.all(Post).values()
        # generate_post(title, content)
        for post in posts:
            if post.id == new_post.id:
                return render_template('index.html', posts=[post.format_for_display()])

    return render_template('index.html')


# Placeholder function for text generation
@app_views.route('/view_post/', methods=['GET'], strict_slashes=False)
def view_post():
    """ view all generated posts"""
    if request.method == 'GET':
        posts = storage.all(Post).values()
        print(posts)
        return render_template('view_post.html', posts=[post.format_for_display() for post in posts])
    return render_template('view_post.html')


@app_views.route('/delete_post/<post_id>', methods=['POST'], strict_slashes=False)
def delete_post(post_id):
    """Delete a post by ID."""
    # print(Post)
    # print(post_id)  # Debugging output
    post = storage.get(Post, post_id)  # Fetch post from storage by ID
    print(post)
    if post:
        storage.delete(post)  # Remove the post from the database
        storage.save()        # Save changes to persist deletion
        return redirect(url_for('app_views.view_post'))  # Redirect to home page or post list
    else:
        return "Post not found", 404  # Handle case where the post doesn't exist

