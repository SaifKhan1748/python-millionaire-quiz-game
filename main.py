questions=[
        ["Who is Shah Rukh Khan?","WWE Wrestler","Indian Actor","Cricketer","Politician",2],
        ["What is the capital of India?","New Delhi","Mumbai","Chennai","Kolkata",1],
        ["What is the currency of japan?","dollar","euro","peso","yen",4],
        ["What is the capital of USA?","Washington Dc","New York","Los Angeles","Chicago",1],
        ["What is the capital of UK?","Sarigamo","London","Birmingham","Liverpool",2]
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
