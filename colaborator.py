import random

# Question format: (question, options list, correct option)
quiz_data = {
    "Biology": [
        ("What is the powerhouse of the cell?", ["A) Nucleus", "B) Ribosome", "C) Mitochondria", "D) Golgi body"], "C"),
        ("Which organ pumps blood in the human body?", ["A) Brain", "B) Kidney", "C) Liver", "D) Heart"], "D"),
        ("DNA stands for?", ["A) Deoxyribonucleic Acid", "B) Dynamic Nuclear Acid", "C) Double Helix Acid", "D) None"], "A"),
        ("Which blood cells help in clotting?", ["A) RBC", "B) WBC", "C) Platelets", "D) Plasma"], "C")
    ],
    "Physics": [
        ("Unit of Force?", ["A) Pascal", "B) Newton", "C) Watt", "D) Joule"], "B"),
        ("What is used to measure temperature?", ["A) Thermometer", "B) Barometer", "C) Ammeter", "D) Voltmeter"], "A"),
        ("Speed of light is approximately?", ["A) 3x10^8 m/s", "B) 1x10^6 m/s", "C) 5x10^7 m/s", "D) 1x10^5 m/s"], "A"),
        ("Which law explains action-reaction?", ["A) Newton's First", "B) Newton's Second", "C) Newton's Third", "D) Hooke's Law"], "C")
    ],
    "Chemistry": [
        ("What is H2O?", ["A) Oxygen", "B) Hydrogen", "C) Water", "D) Salt"], "C"),
        ("NaCl is commonly called?", ["A) Sugar", "B) Salt", "C) Soda", "D) Lime"], "B"),
        ("Atomic number of Oxygen?", ["A) 6", "B) 7", "C) 8", "D) 9"], "C"),
        ("pH of a neutral substance?", ["A) 1", "B) 7", "C) 5", "D) 14"], "B")
    ],
    "Maths": [
        ("What is 9 * 9?", ["A) 81", "B) 72", "C) 91", "D) 99"], "A"),
        ("√64 = ?", ["A) 6", "B) 7", "C) 8", "D) 9"], "C"),
        ("π (pi) approximately equals?", ["A) 2.14", "B) 3.14", "C) 4.13", "D) 1.31"], "B"),
        ("What is the derivative of x^2?", ["A) 2x", "B) x", "C) x^2", "D) 1"], "A")
    ],
    "Aptitude": [
        ("What comes next: 2, 4, 8, 16, ...?", ["A) 20", "B) 24", "C) 32", "D) 30"], "C"),
        ("25% of 200 is?", ["A) 25", "B) 40", "C) 50", "D) 60"], "C"),
        ("If x = 5 and y = 2, then x^y = ?", ["A) 25", "B) 10", "C) 32", "D) 20"], "C"),
        ("What is 100/4 + 6?", ["A) 31", "B) 30", "C) 29", "D) 28"], "A")
    ]
}

# Select 4 random questions from each subject
selected_questions = []
for subject, qlist in quiz_data.items():
    selected_questions.extend(random.sample(qlist, 4))

# Shuffle the 20 questions
random.shuffle(selected_questions)

# Quiz logic
score = 0
print("🧠 Welcome to the 20-Question MCQ Quiz!\n")

for i, (question, options, correct) in enumerate(selected_questions, 1):
    print(f"Q{i}: {question}")
    for opt in options:
        print(opt)
    user_input = input("Your answer (A/B/C/D): ").strip().upper()

    if user_input == correct:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! Correct answer is {correct}\n")

# Final Score
print(f"🎉 Quiz Over! Your score: {score}/20")

