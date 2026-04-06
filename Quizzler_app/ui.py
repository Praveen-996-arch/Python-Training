from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

class QuizInterface:

    def __init__(self, quiz_brain : QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler App")
        
        self.window.configure(bg = THEME_COLOR, padx = 20, pady = 20)

        self.canvas = Canvas(width = 300, height = 250, highlightbackground= THEME_COLOR)
        self.question = self.canvas.create_text(150,125,text = "Quote", font=FONT, fill = THEME_COLOR, width = 230)
        self.canvas.grid(row=1, column = 0, columnspan = 2,rowspan=2)

        self.right_image = PhotoImage(file = "/Users/manasapola/PycharmProjects/Basicsofpython/Quizzler_app/images/true.png")
        self.right_button = Button(image= self.right_image, highlightbackground= THEME_COLOR, command = self.true_button)
        self.right_button.grid(row=3,column=0)

        self.wrong_image = PhotoImage(file = "/Users/manasapola/PycharmProjects/Basicsofpython/Quizzler_app/images/false.png")
        self.wrong_button = Button(image=  self.wrong_image,highlightbackground= THEME_COLOR, command = self.false_button)
        self.wrong_button.grid(row=3,column=1)

        self.score = Label(text = "Score: 0", background=THEME_COLOR,foreground= 'white')
        self.score.grid(row=0, column = 1)

        self.is_next_question()

        self.window.mainloop()

    def is_next_question(self):
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text = f"Score: {self.quiz.score}")
            text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text = text)
        else:
            self.canvas.itemconfig(self.question, text = "You've reached the end of the quiz" )
            self.right_button.config(state = "disabled")
            self.wrong_button.config(state = "disabled")

        
    def true_button(self):
        
        self.give_feedback(self.quiz.check_answer(user_answer = "True"))
       
    def false_button(self):
       
        self.give_feedback(self.quiz.check_answer(user_answer = "False"))
        

    def give_feedback(self, is_right):
        if is_right == True:
            self.canvas.config(bg ="green")
        elif is_right == False:
            self.canvas.config(bg="red")
        self.window.after(1000, self.is_next_question)


  
        
        
      


