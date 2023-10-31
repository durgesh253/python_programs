class QuizGame:
    def __init__(self):
        self.quiz = []  # List to store quiz questions and answers
        self.score = 0

    def add_question(self, question, options, correct_option):
        # Add a new question to the quiz
        self.quiz.append({
            'question': question,
            'options': options,
            'correct_option': correct_option
        })

    def delete_question(self, question_number):
        if 1 <= question_number <= len(self.quiz):
            deleted_question = self.quiz.pop(question_number - 1)
            print(f"Deleted the following question:\n{deleted_question['question']}")
        else:
            print("Invalid question number. No question was deleted.")

    def display_quiz(self):
        # Display the quiz questions and options
        for idx, question_data in enumerate(self.quiz, start=1):
            print(f"Question {idx}: {question_data['question']}")
            for i, option in enumerate(question_data['options'], start=1):
                print(f"{i}. {option}")

    def play_quiz(self):
        # Start the quiz and allow the user to answer questions
        for question_data in self.quiz:
            self.display_quiz()
            user_answer = int(input("Select an option: "))
            if user_answer == question_data['correct_option']:
                print("Correct!")
                self.score += 1
            else:
                print("Incorrect!")

    def run(self):
        while True:
            print("Menu:")
            print("1. Add a new question")
            print("2. Delete a question")
            print("3. Play the quiz")
            print("4. Exit")
            choice = int(input("Select an option: "))
            if choice == 1:
                question = input("Enter the question: ")
                options = [input(f"Enter option {i}: ") for i in range(1, 5)]
                correct_option = int(input("Enter the correct option (1-4): "))
                self.add_question(question, options, correct_option)
            elif choice == 2:
                self.display_quiz()
                question_number = int(input("Enter the question number to delete: "))
                self.delete_question(question_number)
            elif choice == 3:
                self.play_quiz()
                print(f"Your score: {self.score}/{len(self.quiz)}")
            elif choice == 4:
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == '__main__':
    quiz_game = QuizGame()
    quiz_game.run()
