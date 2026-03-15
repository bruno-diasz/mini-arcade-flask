from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from .models import db, Question
from .services import NumberGuessingGame, DrawingChallenge, QuizGame

main = Blueprint('main', __name__)

# Initialize game services
number_game = NumberGuessingGame()
drawing_challenge = DrawingChallenge()

@main.route('/')
def index():
    return render_template('index.html')

# Number Guessing Game Routes
@main.route('/guess', methods=['GET', 'POST'])
def guess():
    if request.method == 'POST':
        guess_value = request.form.get('guess')
        message = number_game.guess(guess_value)
        correct = "Parabéns" in message
        return render_template('guess.html', message=message, correct=correct)
    return render_template('guess.html')

@main.route('/guess/reset')
def guess_reset():
    number_game.reset()
    return redirect(url_for('main.guess'))

# Quiz Game Routes
@main.route('/quiz', methods=['GET', 'POST'])
def quiz():
    questions = Question.query.all()
    if not questions:
        return render_template('quiz.html', message="Nenhuma pergunta cadastrada ainda.", finished=False)

    # Initialize quiz in session if not exists
    if 'quiz_game' not in session:
        quiz_game = QuizGame(questions)
        session['quiz_game'] = {
            'current_index': 0,
            'score': 0,
            'finished': False
        }

    quiz_data = session['quiz_game']
    quiz_game = QuizGame(questions)
    quiz_game.current_index = quiz_data['current_index']
    quiz_game.score = quiz_data['score']
    quiz_game.finished = quiz_data['finished']

    if request.method == 'POST':
        answer = request.form.get('answer')
        message = quiz_game.answer_question(answer)

        # Update session
        session['quiz_game'] = {
            'current_index': quiz_game.current_index,
            'score': quiz_game.score,
            'finished': quiz_game.finished
        }

        return render_template('quiz.html',
                             message=message,
                             finished=quiz_game.finished,
                             score=quiz_game.score,
                             total=len(questions))

    question = quiz_game.get_current_question()
    if quiz_game.finished:
        return render_template('quiz.html',
                             finished=True,
                             score=quiz_game.score,
                             total=len(questions))

    return render_template('quiz.html', question=question)

@main.route('/quiz/reset')
def quiz_reset():
    session.pop('quiz_game', None)
    return redirect(url_for('main.quiz'))

# Drawing Challenge Routes
@main.route('/draw')
def draw():
    challenge = drawing_challenge.get_random_challenge()
    return render_template('draw.html', challenge=challenge)

# Admin Routes
@main.route('/admin')
def admin():
    return render_template('admin.html')

@main.route('/admin/questions')
def questions():
    questions = Question.query.all()
    return render_template('questions.html', questions=questions)

@main.route('/admin/question/new', methods=['GET', 'POST'])
def new_question():
    if request.method == 'POST':
        question = Question(
            text=request.form['text'],
            option_a=request.form['option_a'],
            option_b=request.form['option_b'],
            option_c=request.form['option_c'],
            correct_answer=request.form['correct_answer']
        )
        db.session.add(question)
        db.session.commit()
        flash('Pergunta criada com sucesso!')
        return redirect(url_for('main.questions'))
    return render_template('question_form.html')

@main.route('/admin/question/<int:id>/edit', methods=['GET', 'POST'])
def edit_question(id):
    question = Question.query.get_or_404(id)
    if request.method == 'POST':
        question.text = request.form['text']
        question.option_a = request.form['option_a']
        question.option_b = request.form['option_b']
        question.option_c = request.form['option_c']
        question.correct_answer = request.form['correct_answer']
        db.session.commit()
        flash('Pergunta atualizada com sucesso!')
        return redirect(url_for('main.questions'))
    return render_template('question_form.html', question=question)

@main.route('/admin/question/<int:id>/delete')
def delete_question(id):
    question = Question.query.get_or_404(id)
    db.session.delete(question)
    db.session.commit()
    flash('Pergunta removida com sucesso!')
    return redirect(url_for('main.questions'))