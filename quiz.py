questions = ["What is the capital of finland?", "Who is the founder of spaceX?", "Who is the first person to step on moon?"]
answers = ["Helsinki", "Elon Musk", "Neil Armstrong"]

addQuestions = int(input((f"There are {len(questions)} questions in the quiz. Do you want to add more?\n1. Yes 2. No ")))

def take_question ():
    question = input("Enter question: ")
    questions.append(question)

def take_answer ():
    answer = input("Enter answer: ")
    answers.append(answer)

def take_questions ():
    op = 1
    while op == 1:
        take_question()
        take_answer()
        op = int(input("Do you want to enter more questions?\n1. Yes 2. No: "))


def check_answer (index, input):
  if (input.lower() == answers[index].lower()):
    return True
  else:
    return False
  
if (addQuestions == 1):
  take_questions()
  
index = 0
user_score = 0
achievable_score = len(questions)

while index < len(questions):
  user_answer = input(questions[index])
  isCorrect = check_answer(index, user_answer)

  if (isCorrect):
    user_score += 1
    print("Correct answer")
  else: 
    print("Incorrect answer")

  index += 1 

print(f"Your score is {user_score}/{achievable_score}")
    