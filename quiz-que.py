import random

# ====================
#   QUIZ GAME PART
# ====================

def display_quiz_intro():
    print("====================================")
    print("      Welcome to the Quiz Game!     ")
    print("====================================")
    print("  Answer the question correctly!    \n")

# Function para basahin ang quiz file
def load_quiz_questions(filename="quiz-question.txt"):
    questions = []
    current_question = {}
    
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            
            for line in lines:
                line = line.strip()
                if line.startswith("===================="):
                    if current_question:
                        questions.append(current_question)
                        current_question = {}
                elif line.startswith(tuple(str(i) for i in range(1, 100))):
                    current_question['question'] = line.split('. ', 1)[1]
                    current_question['options'] = {}
                elif line.lower().startswith(('a.', 'b.', 'c.', 'd.')):
                    option = line[0].lower()
                    text = line[3:]
                    current_question['options'][option] = text
                elif line.startswith("Answer:"):
                    current_question['answer'] = line.split(': ')[1].lower()
                    
        return questions
    except Exception as e:
        print(f"\nError loading quiz file: {e}")
        return []

# Function para magaapear yung tanong at sagot
def show_question(question_data):
    print("\n====================================")
    print(f"  {question_data['question']}")
    print("====================================")
    for option in ['a', 'b', 'c', 'd']:
        print(f"{option}. {question_data['options'][option]}")
    print("====================================")

# Main quiz logic
def run_quiz():
    display_quiz_intro()
    questions = load_quiz_questions()
    
    if not questions:
        print("Walang mga tanong na nakita sa file!")
        return
    
    # Pumili ng random na tanong
    selected_question = random.choice(questions)
    
    show_question(selected_question)
    
    # Kumuha ng sagot sa user
    while True:
        user_answer = input("\nAnong sagot mo (a/b/c/d)? ").strip().lower()
        if user_answer in ['a', 'b', 'c', 'd']:
            break
        print("Invalid option. Pili lang ng a, b, c, or d.")
    
    # Check kung tama ang sagot
    if user_answer == selected_question['answer']:
        print("\n====================================")
        print("   Tamang sagot! Good job! 🎉")
        print("====================================")
    else:
        print("\n====================================")
        print(f"  Mali. Ang tamang sagot ay {selected_question['answer'].upper()}.")
        print("====================================")

# Para sa pagtakbo ng program
if __name__ == "__main__":
    run_quiz()
    print("\nSalamat sa paglalaro! Balik ka ulit! 😊\n")
