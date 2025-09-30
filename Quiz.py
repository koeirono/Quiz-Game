import random

questions = [
    {
        "question": "What year did Kenya gain independence?",
        "choices": {"A": "1963", "B": "1964", "C": "1952", "D": "1978"},
        "answer": "A"
    },
    {
        "question": "Who was the first President of Kenya?",
        "choices": {"A": "Jomo Kenyatta", "B": "Daniel arap Moi", "C": "Mwai Kibaki", "D": "Uhuru Kenyatta"},
        "answer": "A"
    },
    {
        "question": "Which is the largest lake in Kenya?",
        "choices": {"A": "Lake Naivasha", "B": "Lake Victoria", "C": "Lake Turkana", "D": "Lake Baringo"},
        "answer": "C"
    },
    {
        "question": "What is the currency of Kenya?",
        "choices": {"A": "Shilling", "B": "Dollar", "C": "Pound", "D": "Rupee"},
        "answer": "A"
    },
    {
        "question": "Which Kenyan athlete is famous for marathon records?",
        "choices": {"A": "Eliud Kipchoge", "B": "David Rudisha", "C": "Paul Tergat", "D": "Catherine Ndereba"},
        "answer": "A"
    },
    {
        "question": "Which Kenyan town is known as the 'green city under the sun'?",
        "choices": {"A": "Kisumu", "B": "Nairobi", "C": "Nakuru", "D": "Eldoret"},
        "answer": "B"
    },
    {
        "question": "What is Kenya’s national language?",
        "choices": {"A": "Swahili", "B": "English", "C": "Kikuyu", "D": "Maasai"},
        "answer": "A"
    },
    {
        "question": "Mount Kenya is the ____ highest mountain in Africa?",
        "choices": {"A": "1st", "B": "2nd", "C": "3rd", "D": "4th"},
        "answer": "B"
    }
]

random.shuffle(questions)

score = 0
print(" Welcome to the Quiz! Answer with A, B, C, or D.\n")

for i, q in enumerate(questions, start=1):
    print(f"Q{i}: {q['question']}")
    for option, text in q["choices"].items():
        print(f"  {option}. {text}")
    
    while True:
        try:
            user_answer = input("Your answer: ").strip().upper()
            if user_answer not in q["choices"]:
                raise ValueError("Invalid choice! Please pick A, B, C, or D.")
            break
        except ValueError as e:
            print(e)

    if user_answer == q["answer"]:
        print(" Correct!\n")
        score += 1
    else:
        print(f" Wrong! Correct answer was {q['answer']}\n")

print(f"Your total score: {score}/{len(questions)}")

if score == len(questions):
    print(" Excellent! Perfect score!")
elif score >= len(questions) // 2:
    print(" Good job! You passed.")
else:
    print(" Try again, you’ll do better next time!")
