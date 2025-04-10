from flask import Flask, render_template, request, redirect
import json
import os
from datetime import date

app = Flask(__name__)
DATA_FILE = 'performances1.json'

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

@app.route('/', methods=['GET', 'POST'])
def form():
    data = load_data()

    if request.method == 'POST':
        venue = request.form['venue'].strip()
        event = request.form['event'].strip()
        genre = request.form['genre'].strip()
        date_input = request.form['date'].strip() or str(date.today())

        new_entry = {
            "date": date_input,
            "event": event,
            "genre": genre
        }

        if venue in data:
            data[venue].append(new_entry)
        else:
            data[venue] = [new_entry]

        save_data(data)
        return redirect('/')  # Prevent form re-submission on refresh

    return render_template('form2.html', entries=data)

if __name__ == '__main__':
    app.run(debug=True)
