questions=[
        ["Who is Shah Rukh Khan?","WWE Wrestler","Indian Actor","Cricketer","Politician",2],
        ["What is the capital of India?","New Delhi","Mumbai","Chennai","Kolkata",1],
        ["What is the currency of japan?","dollar","euro","peso","yen",4],
        ["What is the capital of USA?","Washington Dc","New York","Los Angeles","Chicago",1],
        ["What is the capital of UK?","Sarigamo","London","Birmingham","Liverpool",2],
        ["Who is known as the Father of India?","Subhash Chandra Bose","Mahatma Gandhi","Bhagat Singh","Jawaharlal Nehru",2],
        ["Which planet is known as the Red Planet?","Earth","Mars","Venus","Jupiter",2],
        ["Which language is used for AI and Machine Learning most commonly?","Python","HTML","CSS","C",1],
        ["What is 5 + 7?","10","11","12","13",3],
        ["Which is the largest ocean in the world?","Atlantic Ocean","Indian Ocean","Arctic Ocean","Pacific Ocean",4],
        ["Which animal is known as the King of the Jungle?","Tiger","Lion","Elephant","Leopard",2],
        ["How many continents are there in the world?","5","6","7","8",3],
        ["Which is the fastest land animal?","Cheetah","Lion","Horse","Tiger",1],
        ["Which country invented Pizza?","France","Italy","USA","Spain",2],
        ["Which device is used to input text into a computer?","Monitor","Keyboard","Printer","Speaker",2]
] 


prize_money=[1000,3000,5000,10000,50000]
i=0

for question in questions:
 
    print(question[0])
    print(f"a.{question[1]}")
    print(f"b.{question[2]}")
    print(f"c.{question[3]}")
    print(f"d.{question[4]}")

    a=int(input("Enter Your Answer : "))
    if(question[5]==a):
        print("Your Answer is Correct")
    else:
        print(f"Incorrect, The Correct Answer is option {question[5]}")
        print("Better Luck Next Time")
        break
    print(f"You Won {prize_money[i]}")
    i+=1
