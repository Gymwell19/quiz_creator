# quiz creator in Python    
# simple greeting in intro
# uses the "=" character to create a border around the text
def display():
    print("====================================")   
    print("      Welcome to the quiz zes!")
    print("====================================\n")
    print("Let's create some quiz zestion!\n")

# for outro message
def exit():
    print("\n====================================")
    print("  Hope you enjoy using the Quiz zes!")
    print("  The questionnaire is in 'quiz-question.txt'.")
    print("====================================\n")

# function para mag-collect ng mga tanong at mga sagot mula sa user.
def get_quiz_input():
    question = input("write your question? ")
    options = {}
    for option in ['a', 'b', 'c', 'd']:
        options[option] = input(f"what wil be text the in choice {option}? ")
    while True:
        correct_answer = input("which is the correct answer (a/b/c/d)? ").strip()
        if correct_answer.lower() in options:
            break
        print("Invalid option. Pick one in a, b, c, or d.")
    return question, options, correct_answer.lower()

# dito papasok yung mga tanong at mga sagot sa text file
question_counter = 0
def write_quiz_data(question, options, correct_answer, filename="quiz-question.txt"):
    global question_counter
    question_counter += 1
    try:
        with open(filename, "a") as file:
            file.write("\n====================\n")
            file.write(f"{question_counter}. {question}\n")
            for option in ['a', 'b', 'c', 'd']:
                file.write(f"{option}. {options[option]}\n")
            file.write(f"Answer: {correct_answer}\n")
            file.write("====================\n")
        print("Tanong na-save sa file.\n")
    except Exception as e:
        # error handling kung may problema sa file
        print(f"Error saving to file: {e}")
            
# nagrecord ng mga tanong at sagot sa file
# loop part ng program
def main():
    display()
    while True:
        try:
            question, options, correct_answer = get_quiz_input()
            write_quiz_data(question, options, correct_answer)
            continue_input = input("Do you want to add another question? (only type y to continue)): ").strip().lower()
            if continue_input != "y":
                break

        # for interruption handling    
        except KeyboardInterrupt:
            print("\nUser interrupted the program.")
            break
    exit()

if __name__ == "__main__":
    main()