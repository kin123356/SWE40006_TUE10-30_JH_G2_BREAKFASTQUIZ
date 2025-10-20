from flask import Flask, render_template, request, redirect, url_for, send_from_directory

# Serve current project root as static so existing paths like images/* and styles.css still work
app = Flask(__name__, static_folder='.', static_url_path='')


@app.route('/')
def home():
    # Serve homepage.html from the project root (it's not under templates/)
    return send_from_directory('.', 'homepage.html')


@app.route('/quiz', methods=['GET'])
def quiz():
    # Serve your existing quiz page from the project root
    return send_from_directory('.', 'Quiz Page.html')


@app.route('/result', methods=['POST'])
def result():
    # Collect answers from the four on-screen questions
    q1 = request.form.get('q1')  # A/B/C/D
    q2 = request.form.get('q2')  # A/B/C/D
    q3 = request.form.get('q3')  # A/B/C/D
    q4 = request.form.get('q4')  # A/B/C/D
    print('[DEBUG] Received answers:', {'q1': q1, 'q2': q2, 'q3': q3, 'q4': q4})

    # Score only between croissant and egg using a simple heuristic
    scores = {"egg": 0, "croissant": 0}

    # Q1: Wake-up feeling
    if q1 in ('A', 'C'):
        scores['croissant'] += 1
    elif q1 in ('B', 'D'):
        scores['egg'] += 1

    # Q2: Favourite season
    if q2 in ('A', 'D'):  # Summer, Spring
        scores['croissant'] += 1
    elif q2 in ('B', 'C'):  # Autumn, Winter
        scores['egg'] += 1

    # Q3: Exercise frequency
    if q3 in ('A', 'B'):
        scores['croissant'] += 1
    elif q3 in ('C', 'D'):
        scores['egg'] += 1

    # Q4: Holiday type
    if q4 in ('A', 'D'):
        scores['croissant'] += 1
    elif q4 in ('B', 'C'):
        scores['egg'] += 1

    # Decide winner and serve existing static result pages
    winner = max(scores, key=scores.get)
    print('[DEBUG] Scores:', scores, '-> winner:', winner)
    if winner == 'egg':
        return send_from_directory('.', 'Result page (Egg).html')
    else:
        return send_from_directory('.', 'Result page (Croissant).html')


if __name__ == '__main__':
    # Run the Flask development server
    app.run(debug=True)
