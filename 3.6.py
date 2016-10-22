class Exam:
    def __init__(self, examname, creditnumber, date, grade):
        self._examname = examname
        self._creditnumber = creditnumber
        self._date = date
        self._grade = grade

    def estimate_work(self):
        totalhours = self._creditnumber * 25
        x = int((totalhours * self._grade) / 30)
        return x
        
n = input("Name of the exam? ")
c = int(input("Credits of the exam? "))
d = input("Date of the exam (es. yyyy-mm-gg)? ")
g = int(input("Grade of the exam (from 18 to 30)? "))

if 18 <= g <= 30:
    e = Exam( n, c, d, g )
    print("Estimated hours of studying:", e.estimate_work())
else:
    print("Invalid grade for the exam")
          




    
