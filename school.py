class school:
  def __init__ (self,questions):
    self.ques = questions
  def get_answer(self,ans):
    self.answer = ans
  def correction(self):
    self.final = {self.ques[i]:self.answer[i] for i in range(len(self.ques))}
  def generate_report(self,marks):
    print("------------------------------")
    print("Report Card")
    print("student name = sangee ")
    print("teacher name = rathna")
    self.marks = []
    sum = 0
    for j in marks:
      sum += j
      self.marks.append(sum)
    print("Total mark","=",sum,"out of",((len(marks))*5))
    if sum>= 10 and sum<=15:
      print("O grade")
    elif sum>=5 and sum<10:
      print("A grade")
    else:
      print("fail")

class teacher:
  def correction(self,final,quest):
    mark = []
    self.mark = mark
    for i,j in final.items():
      print("questions:\t"+i+"\nanswer:\t"+j)
      mark.append(float(input()))
    self.final_mark = {quest[i]:mark[i] for i in range(len(quest))}

class student:
  def write_answer(self,questions):
    self.answer = []
    for i in questions:
      print(i)
      self.answer.append(input())
  def get_mark(self,mark1):
    self.marks = mark1
    input("Parent Signature: ")
    print("------------------------------")

Ignatius = school(["1. what is python","2.what is data science","3.what is SQL"])
rathna = teacher()
sangee = student()

sangee.write_answer(Ignatius.ques)
Ignatius.get_answer(sangee.answer)
Ignatius.correction()
rathna.correction(Ignatius.final,Ignatius.ques)
Ignatius.generate_report(rathna.mark)
sangee.get_mark(Ignatius.marks)
