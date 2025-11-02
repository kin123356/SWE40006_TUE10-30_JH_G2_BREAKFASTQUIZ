from flask import Flask, render_template, request, redirect, url_for, send_from_directory

app = Flask(__name__, static_folder='.', static_url_path='')


@app.route('/')
def home():
   
    return send_from_directory('.', 'homepage.html')


@app.route('/quiz', methods=['GET'])
def quiz():
    
    return send_from_directory('.', 'Quiz Page.html')


@app.route('/result', methods=['POST'])
def result():
   
    q1 = request.form.get('q1')  
    q2 = request.form.get('q2')  
    q3 = request.form.get('q3')  
    q4 = request.form.get('q4')  
    print('[DEBUG] Received answers:', {'q1': q1, 'q2': q2, 'q3': q3, 'q4': q4})

    
    scores = {"egg": 0, "croissant": 0}

  
    if q1 in ('A', 'C'):
        scores['croissant'] += 1
    elif q1 in ('B', 'D'):
        scores['egg'] += 1

   
    if q2 in ('A', 'D'):  
        scores['croissant'] += 1
    elif q2 in ('B', 'C'):  
        scores['egg'] += 1

   
    if q3 in ('A', 'B'):
        scores['croissant'] += 1
    elif q3 in ('C', 'D'):
        scores['egg'] += 1

    
    if q4 in ('A', 'D'):
        scores['croissant'] += 1
    elif q4 in ('B', 'C'):
        scores['egg'] += 1

   
    winner = max(scores, key=scores.get)
    print('[DEBUG] Scores:', scores, '-> winner:', winner)
    if winner == 'egg':
        return send_from_directory('.', 'Result page (Egg).html')
    else:
        return send_from_directory('.', 'Result page (Croissant).html')


if __name__ == '__main__':
  
    app.run(debug=True)
