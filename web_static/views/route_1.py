#!/usr/bin/env python
""" Blueprint routes"""

from web_static.views import app_views
from flask import render_template, request


@app_views.route('/home/', methods=['GET', 'POST'], strict_slashes=False)
def home():
    """ Handles all paths """
    generated_posts = []
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')  # Replace 'user_input' with the actual name attribute of your form input

        print(f"Title: {title}")  # Debugging output
        print(f"Content: {content}")

        generated_post = generate_post(title, content)  # Placeholder function for text generation

        # Store the generated post (you could use a list or dictionary depending on your requirements)
        generated_posts.append(generated_post)  # Assuming generated_posts is a list

        return render_template('index11.html', posts=generated_posts)

    return render_template('index11.html')


# Placeholder function for text generation
def generate_post(title, content):
    # For now, just return the user input; replace this with your AI generation logic later
    return f"Generated blog post titled {title}: {content}"
