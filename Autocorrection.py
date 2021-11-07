import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="grad"
)


def new_question(question, keywords):
    sql = "INSERT INTO questions VALUES ('',%s,%s)"
    val = (question, keywords)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

mycursor = mydb.cursor()

print("Type: ")
type = input()


if(type == "1"):
    print("Question:")
    question = input()

    print("Keywords (separated by commas):")
    keywords = input()
    new_question(question,keywords)


def get_questions():
    sql = "SELECT * FROM questions"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    i=0
    for x in myresult:
        i+=1
        print(x[0], "-", x[1])


def answer_question(_id, answer):
    sql = "INSERT INTO answers VALUES ('',%s,%s)"
    val = (_id, answer)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

if(type =="2"):
    get_questions()
    print("Please select question number")
    q_n = input()
    print("Please answer the question")
    answer = input()
    answer_question(q_n,answer)

def show_results(_id):
    sql = "SELECT q.*,a.* FROM questions q, answers a WHERE q.id=%s AND a.question_id = q.id"
    mycursor.execute(sql,(_id,))
    myresult = mycursor.fetchall()
    keywords = myresult[0][2]
    answers = []
    filter_keywords = [',',".",":",";","?","!","'",'"',
    " is "," a "," that "," the "," of "," and "," there "," this "," those "," these "," are "," was "," were "," which "," in "]
    
    for x in myresult:
        answer = x[5]
        for i in filter_keywords:
            answer = answer.replace(i," ")
        answer = answer.replace("  ", " ")
        answers.append(answer.strip().split(' '))
    mark = [0,0]
    print(len(answers))
    student_count = 0
    
    for j in answers:
        for i in keywords.split(','):
            for k in j:
                if(k == i):
                    mark[student_count] += 0.5
        student_count += 1
    answer_results = []
    for index,item in enumerate(mark):
        arr = [item,myresult[index][5]]
        answer_results.append(arr)
    print(answer_results)

if(type == "3"):
    print("Enter q_id")
    q_n = input()
    show_results(q_n)
