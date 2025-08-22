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


#DONE BY YOHANNIS
uiz = {
    "Maths": [
        {"q": "1. What is 12 × 8?", "options": ["a) 96", "b) 108", "c) 84", "d) 112"], "ans": "a"},
        {"q": "2. Solve: 15 + 27 = ?", "options": ["a) 32", "b) 42", "c) 40", "d) 52"], "ans": "d"},
        {"q": "3. Perimeter of a square = 40 cm. One side?", "options": ["a) 5", "b) 8", "c) 10", "d) 12"], "ans": "c"},
        {"q": "4. What is (3/4) × 16?", "options": ["a) 10", "b) 12", "c) 14", "d) 18"], "ans": "b"},
        {"q": "5. If x=5, find 2x² + 3.", "options": ["a) 28", "b) 45", "c) 53", "d) 60"], "ans": "c"},
    ],
    "English": [
        {"q": "1. Synonym of 'Happy'?", "options": ["a) Sad", "b) Angry", "c) Joyful", "d) Tired"], "ans": "c"},
        {"q": "2. Which is a noun?", "options": ["a) Run", "b) Beautiful", "c) Chair", "d) Quickly"], "ans": "c"},
        {"q": "3. Fill in: She ___ going to the market.", "options": ["a) is", "b) are", "c) were", "d) be"], "ans": "a"},
        {"q": "4. Which sentence is past tense?", "options": ["a) He eats an apple.", "b) She is eating.", "c) They will eat.", "d) He ate an apple."], "ans": "d"},
        {"q": "5. Correct spelling?", "options": ["a) Recieve", "b) Receive", "c) Recive", "d) Receeve"], "ans": "b"},
    ],
    "Biology": [
        {"q": "1. 'Powerhouse of the cell'?", "options": ["a) Nucleus", "b) Ribosome", "c) Mitochondrion", "d) Golgi"], "ans": "c"},
        {"q": "2. Basic unit of life?", "options": ["a) Organ", "b) Cell", "c) Tissue", "d) Organ system"], "ans": "b"},
        {"q": "3. Blood cells fighting infections?", "options": ["a) RBC", "b) WBC", "c) Platelets", "d) Plasma"], "ans": "b"},
        {"q": "4. DNA stores info in:", "options": ["a) Amino acids", "b) Nucleotides", "c) Fatty acids", "d) Polysaccharides"], "ans": "b"},
        {"q": "5. Photosynthesis occurs in:", "options": ["a) Nucleus", "b) Chloroplast", "c) Mitochondria", "d) Vacuole"], "ans": "b"},
    ],
    "Physics": [
        {"q": "1. SI unit of force?", "options": ["a) Watt", "b) Joule", "c) Newton", "d) Pascal"], "ans": "c"},
        {"q": "2. Energy change in bulb?", "options": ["a) Heat→Light", "b) Electrical→Light", "c) Chemical→Heat", "d) Light→Heat"], "ans": "b"},
        {"q": "3. Speed of light (vacuum)?", "options": ["a) 3×10⁸ m/s", "b) 3×10⁶ m/s", "c) 3×10⁵ m/s", "d) 3×10⁹ m/s"], "ans": "a"},
        {"q": "4. Who discovered gravitation?", "options": ["a) Einstein", "b) Galileo", "c) Newton", "d) Watt"], "ans": "c"},
        {"q": "5. Lens in magnifying glass?", "options": ["a) Concave", "b) Convex", "c) Plane", "d) Cylindrical"], "ans": "b"},
    ],
    "Chemistry": [
        {"q": "1. Symbol for Sodium?", "options": ["a) So", "b) Na", "c) S", "d) Sn"], "ans": "b"},
        {"q": "2. Gas for respiration?", "options": ["a) CO₂", "b) O₂", "c) N₂", "d) H₂"], "ans": "b"},
        {"q": "3. Water is made of:", "options": ["a) H + N", "b) O + C", "c) H + O", "d) C + H"], "ans": "c"},
        {"q": "4. pH of neutral solution?", "options": ["a) 0", "b) 7", "c) 14", "d) 10"], "ans": "b"},
        {"q": "5. Pencil 'lead' is actually:", "options": ["a) Graphite (C)", "b) Lead", "c) Zinc", "d) Copper"], "ans": "a"},
    ]
}

score = 0
total = sum(len(qs) for qs in quiz.values())

print("📘 Multi-Subject Quiz 📘")
print("------------------------")

for subject, questions in quiz.items():
    print(f"\n🔹 {subject} Section 🔹")
    for q in questions:
        print("\n" + q["q"])
        for option in q["options"]:
            print(option)
        user = input("Your answer (a/b/c/d): ").lower()
        if user == q["ans"]:
            print("✅ Correct!")
            score += 1
        else:
            correct_text = q["options"][ord(q["ans"]) - 97]
            print(f"❌ Wrong! Correct answer: {q['ans']}) {correct_text}")

print(f"\n🎯 Final Score: {score}/{total}")
