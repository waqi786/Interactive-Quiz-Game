class QuizGame:
    def __init__(self):
        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["Paris", "London", "Berlin", "Madrid"],
                "answer": "Paris"
            },
            {
                "question": "Who wrote 'Romeo and Juliet'?",
                "options": ["Charles Dickens", "William Shakespeare", "Jane Austen", "Leo Tolstoy"],
                "answer": "William Shakespeare"
            },
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Venus", "Mars", "Jupiter", "Saturn"],
                "answer": "Jupiter"
            },
            {
                "question": "Which country is known as the 'Land of the Rising Sun'?",
                "options": ["China", "Japan", "India", "Korea"],
                "answer": "Japan"
            },
            {
                "question": "Who painted the Mona Lisa?",
                "options": ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Michelangelo"],
                "answer": "Leonardo da Vinci"
            },
            {
                "question": "What is the tallest mountain in the world?",
                "options": ["K2", "Mount Everest", "Kangchenjunga", "Makalu"],
                "answer": "Mount Everest"
            },
            {
                "question": "Which planet is known as the 'Red Planet'?",
                "options": ["Mars", "Venus", "Jupiter", "Mercury"],
                "answer": "Mars"
            },
            {
                "question": "Who discovered gravity when an apple fell on his head?",
                "options": ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Stephen Hawking"],
                "answer": "Isaac Newton"
            },
            {
                "question": "What is the chemical symbol for water?",
                "options": ["H2O", "CO2", "O2", "NaCl"],
                "answer": "H2O"
            },
            {
                "question": "Which instrument is used to measure earthquakes?",
                "options": ["Thermometer", "Barometer", "Seismograph", "Hygrometer"],
                "answer": "Seismograph"
            }

        ]
        self.score = 0

    def display_question(self, question):
        print(f"Question: {question['question']}")
        for idx, option in enumerate(question['options'], start=1):
            print(f"{idx}. {option}")
        user_answer = input("Your answer (enter option number): ")
        return user_answer

    def play_quiz(self):
        print("Welcome to the Quiz Game!")
        for question in self.questions:
            user_answer = self.display_question(question)
            if user_answer.isdigit() and 1 <= int(user_answer) <= len(question['options']):
                selected_option = question['options'][int(user_answer) - 1]
                if selected_option == question['answer']:
                    self.score += 1
                    print("Correct!")
                else:
                    print(f"Wrong! Correct answer is: {question['answer']}")
            else:
                print("Invalid input. Skipping question.")

        print(f"\nQuiz completed! Your score is: {self.score}/{len(self.questions)}")

def main():
    game = QuizGame()
    game.play_quiz()

if __name__ == '__main__':
    main()
