from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

challenges = [
    {
        "id": 1,
        "name": "First Flag",
        "description": "Find the hidden flag in the HTML source.",
        "flag": "shadowroot{inspect_source}"
    },
    {
        "id": 2,
        "name": "Linux Basics",
        "description": "What command lists files in Linux?",
        "flag": "ls"
    }
]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/learn')
def learn():
    return render_template('learn.html')


@app.route('/challenges')
def challenges_page():
    return render_template('challenges.html', challenges=challenges)


@app.route('/submit_flag', methods=['POST'])
def submit_flag():
    try:
        challenge_id = int(request.form.get('challenge_id', 0))
        user_flag = request.form.get('flag', '')
    except ValueError:
        return "Invalid input", 400

    for challenge in challenges:
        if challenge['id'] == challenge_id:
            if user_flag == challenge['flag']:
                return "Correct Flag!"
            else:
                return "Wrong Flag."

    return "Challenge not found", 404


if __name__ == '__main__':
    app.run(debug=True)