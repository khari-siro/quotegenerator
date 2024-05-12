from tkinter import*
import tkinter
import random

top=tkinter.Tk()
top.geometry("600x400+0+0")
top.config(bg='purple')


def game():
    quotes=['The sun never waits for no one','Never apologise for being unique','People will talk bad about you cause they really just wanna be you','If they ghost you, fine with it, respect the dead and move on','It is not the goodbyes that hurt but the flashbacks that follow','It takes one flame to light a fire','Regardless of how you feel,wake up and just do it','What I want only depends on me','Let no one ever tell you what you can or cannot do','Always remember people will only want you when it is convenient to them','Try your hardest not to act how you feel','Be useless so nobody can use you','Know your worth and do not care what others think','Call me mean but Imma just be myself','Never live to think WHAT IF , just do it','saying "thats crazy" and moving on will save you some unecessary stress','It is rather you hate me when alive than love me when I am dead','Live today like tomorrow does not exist','Life is more peaceful when no one knows about you or your life.','Later should never exist in your vocabulary']
    quote=random.randint(0,(len(quotes)-1))
    top=tkinter.Tk()
    top.title("Quote generator")
    top.geometry("600x400+0+0")
    top.config(bg="purple")
    top.resizable(True,False)
    L1=Label(top,text="random quote?",font="times 40")
    L1.place(x=70,y=100)
    L2=Label(top,text=quotes[quote],font="times 15")
    L2.place(x=50,y=300)


x1=Label(top,text="Wanna get a random quote?",font="Arial 26 bold")
x1.place(x=30,y=100)
b1=Button(top,text="Let's gooo...",command=game,width=16,bg="gray")
b1.place(x=200,y=200)



top.mainloop()