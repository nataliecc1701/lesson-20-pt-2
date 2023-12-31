from flask import Flask, request, render_template
from stories import Story

app = Flask(__name__)
story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)


@app.route('/')
def show_form():
    '''Home page shows the madlibs beginning form'''
    return render_template("form.html", story=story)

@app.route('/story')
def show_story():
    '''shows the constructed madlibs story'''
    words = request.args
    text = story.generate(words)
    return render_template("story.html", story_text = text)