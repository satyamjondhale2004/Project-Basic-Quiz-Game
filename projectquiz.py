questions = [
    {
        "question": "In which game the Manu bhakar won his 1st  olympic medal ?",
        "options": ["A. Football", "B. Shooting", "C. Running", "D. Hockey"],
        "answer": "B"
    },
    {
        "question": "what is the value of the pi ?",
        "options": ["A. 3.14", "B. 4", "C. 3.5", "D. 6"],
        "answer": "A"
    },
    {
        "question": "The National sport of india?",
        "options": ["A. cricket", "B.badminton", "C. hockey", "D. boxing"],
        "answer": "C"
    },
    {
        "question": "who is the current PM of india ?",
        "options": ["A. Narendra modi", "B. rahul gadhi", "C. yogi adityanath", "D. nitin gadakari"],
        "answer": "A"
    },
    {
        "question": "Neeraj chopara won his 1st gold medal in olympic in which year ?",
        "options": ["A.2012", "B.2024", "C.2020", "D.2016"],
        "answer": "C"
    }
]

def run_quiz(questions):
    score = 0
    for q in questions:
        print(q["question"])
        for opt in q["options"]:
            print(opt)
        
        user_answer = input("Your answer (A, B, C, D): ").upper()
        while user_answer not in ["A", "B", "C", "D"]:
            print("Invalid input. Please choose A, B, C, or D.")
            user_answer = input("Your answer (A, B, C, D): ").upper()
        
        if user_answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['answer']}.\n")
    
    print(f"Your final score is {score}/{len(questions)}")

run_quiz(questions)