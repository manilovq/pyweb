from app import app
from flask import render_template, request 
from app.model.task import Task

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        Task.insert({'name': name
        })

        tasks = Task.select().get()
    return render_template('index.html', tasks=tasks)
