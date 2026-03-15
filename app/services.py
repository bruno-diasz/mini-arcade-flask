import random

class NumberGuessingGame:
    def __init__(self):
        self.reset()

    def reset(self):
        self.target_number = random.randint(1, 100)
        self.game_over = False

    def guess(self, number):
        if self.game_over:
            return "Jogo já terminado. Clique em 'Jogar Novamente'."

        try:
            guess_num = int(number)
            if guess_num < 1 or guess_num > 100:
                return "Por favor, digite um número entre 1 e 100."

            if guess_num < self.target_number:
                return "O número é maior!"
            elif guess_num > self.target_number:
                return "O número é menor!"
            else:
                self.game_over = True
                return "Parabéns! Você acertou!"
        except ValueError:
            return "Por favor, digite um número válido."

class DrawingChallenge:
    def __init__(self):
        self.challenges = [
            "Desenhe um robô",
            "Desenhe um gato astronauta",
            "Desenhe uma casa mágica",
            "Desenhe um dragão colorido",
            "Desenhe um super-herói",
            "Desenhe uma floresta encantada",
            "Desenhe um castelo no céu",
            "Desenhe animais da fazenda",
            "Desenhe seu animal favorito",
            "Desenhe uma nave espacial"
        ]

    def get_random_challenge(self):
        return random.choice(self.challenges)

class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.current_index = 0
        self.score = 0
        self.finished = False

    def get_current_question(self):
        if self.current_index < len(self.questions):
            return self.questions[self.current_index]
        return None

    def answer_question(self, answer):
        if self.finished:
            return "Quiz já finalizado."

        question = self.get_current_question()
        if not question:
            return "Nenhuma pergunta disponível."

        if answer.upper() == question.correct_answer:
            self.score += 1
            result = "Correto! 🎉"
        else:
            result = f"Incorreto. A resposta certa era {question.correct_answer}) {getattr(question, f'option_{question.correct_answer.lower()}')}"

        self.current_index += 1
        if self.current_index >= len(self.questions):
            self.finished = True

        return result

    def reset(self):
        self.current_index = 0
        self.score = 0
        self.finished = False
        random.shuffle(self.questions)