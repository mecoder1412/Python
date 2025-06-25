import requests
import random
import html
#Educational focused categories(General Knowledge, Science, History, etc.)
EC_ID=9#General Knowledge category
API_URL=f"https://opentdb.com/api.php?amount=10&category={EC_ID}&type=multiple"
def get_educational_questions():
    response=requests.get(API_URL)
    if response.status_code==200:
        data=response.json()
        if data['response_code']==0 and data['results']:
            return data['results']
        return None
def run_quiz():
    questions=get_educational_questions()   
    if not questions:
        print("Failed to fetch educational questions") 
        return
    score=0
    print("welcome to the education Quiz!\n")
    for i, q in enumerate(questions,1):
        #Decode HTML entities and prepare options
        question=html.unescape(q['question'])
        correct=html.unescape(q['correct_answer'])
        incorrect=[html.unescape(a) for a in q['incorrect_answers']]
        #Create and shuffle options
        options=incorrect+[correct]
        random.shuffle(options)
        #Display question
        print(f"Question{i}:{question}")
        for idx, option in enumerate(options,1):
            print(f"{idx}.{option}")
        #get and validate answer
        while True:
            try:
                choice=int(input("\nYour answer (1-4):"))
                if 1<= choice <=4:
                    break
            except ValueError:
                pass
            print("Invalid input! Please enter 1-4")
            #Check answer
        if options[choice-1]==correct:
            print("Correct!☺️\n")
            score+=1
        else:
            print(f"Wrong answer!😔 Correct answer:{correct}\n")
        if score>=5:
               print(f"Final Score:{score}/{len(questions)}☺️")
               print(f"percentage:{score/len(questions)*100:.1f}%☺️") 
        else:
          print(f"Final Score:{score}/{len(questions)}😔")
          print(f"percentage:{score/len(questions)*100:.1f}%😔")
if __name__=="__main__":
    run_quiz()