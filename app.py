from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get('/')
def questions():
    """Render home page html, use story prompts from Story to fill form"""

    story_prompts = silly_story.prompts

    return render_template('questions.html', prompts=story_prompts)

@app.get('/results')
def results():
    """Render story page html, fill with completed story from Story.generate"""

    prompts_to_libs = request.args
    story = silly_story.generate(prompts_to_libs)

    return render_template('story.html', story=story)