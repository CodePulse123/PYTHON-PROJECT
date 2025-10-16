
#FRAME02
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Import required modules
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox,ttk
import random
x = Tk()
x.geometry("10000x10000")
frame1 = Frame(x, background="#1A237E")
frame1.pack(side=LEFT, expand=True, fill=BOTH)
frame2 = Frame(x, background="#BBDEFB")
frame2.pack(side=RIGHT, expand=True, fill=BOTH)
Label(x,text="WELCOME TO HANDCRICKET PREMIER LEAGUE",fg='black',font=("Cooper",41)).place(x=80,y=10)
style = ttk.Style()
style.configure("Green.TButton", background="green", foreground="black", font=("Cooper", 20))
style.configure("Orange.TRadiobutton",background="orange",foreground="black",font=("Arial", 12))
style.configure("Blue.TButton",background="orange",foreground="black",font=("Arial", 12))
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def decide(j,z):
    score=0

    # Create label67 once so it's always available
    label67 = Label(frame2, text=score, bg="lightblue", font=("Arial", 10, "bold"))
    label67.place(x=450, y=400)
    def disable2():
        b1['state']='disable'
        b2['state']='disable'
        b3['state']='disable'
        b4['state']='disable'
        b5['state']='disable'
        b6['state']='disable'
    if (j=="THAT'S OUT"):
        compscore=z
        int(compscore)
        def p1():
            nonlocal score
            nonlocal compscore
            f=random.randint(1,6)
            if f==1:
                if compscore>score:
                    disable2()
                    messagebox._show(x,"OOPS...YOU LOST,AI WON THE MATCH")
                    x.destroy()
                if compscore==score:
                    disable2()
                    messagebox._show(x,"MATCH DRAWN")
                    x.destroy()
            else:
                score+=1
                label21=Label(frame2,text=score, bg="lightblue",font=("Arial", 10, "bold"))
                label21.place(x=450, y=400)
                if compscore<score:
                    messagebox._show(x,"YOU WON THE MATCH CONGRATULATIONS")
                    disable2()
                    
                    x.destroy()
                
        def p2():
            nonlocal score
            nonlocal compscore
            j=random.randint(1,6)
            if j==2:
                if compscore>score:
                    disable2()
                    messagebox._show(x,"OOPS...YOU LOST,AI WON THE MATCH")
                    x.destroy()
                if compscore==score:
                    disable2()
                    messagebox._show(x,"MATCH DRAWN")
                    x.destroy()
            else:
                score+=2
                label21=Label(frame2,text=score, bg="lightblue",font=("Arial", 10, "bold"))
                label21.place(x=450, y=400)
                if compscore<score:
                    messagebox._show(x,"YOU WON THE MATCH CONGRATULATIONS")
                    disable2()
                    x.destroy()
                
        def p3():
            nonlocal score
            nonlocal compscore
            p=random.randint(1,6)
            if p==3:
                if compscore>score:
                    disable2()
                    messagebox._show(x,"OOPS...YOU LOST,AI WON THE MATCH")
                    x.destroy()
                if compscore==score:
                    disable2()
                    messagebox._show(x,"MATCH DRAWN")
                    x.destroy()
            else:
                score+=3
                label21=Label(frame2,text=score, bg="lightblue",font=("Arial", 10, "bold"))
                label21.place(x=450, y=400)
                if compscore<score:
                    messagebox._show(x,"YOU WON THE MATCH CONGRATULATIONS")
                    disable2()
                    x.destroy()
                
        def p4():
            nonlocal score
            nonlocal compscore
            y=random.randint(1,6)
            if y==4:
                if compscore>score:
                    disable2()
                    messagebox._show(x,"OOPS...YOU LOST,AI WON THE MATCH")
                    x.destroy()
                if compscore==score:
                    disable2()
                    messagebox._show(x,"MATCH DRAWN")
                    x.destroy()
            else:
                score+=4
                label21=Label(frame2,text=score, bg="lightblue",font=("Arial", 10, "bold"))
                label21.place(x=450, y=400)
                if compscore<score:
                    messagebox._show(x,"YOU WON THE MATCH CONGRATULATIONS")
                    disable2()
                    x.destroy()
               
        def p5():
            nonlocal score
            nonlocal compscore
            b=random.randint(1,6)
            if b==5:
               if compscore>score:
                    disable2()
                    messagebox._show(x,"OOPS...YOU LOST,AI WON THE MATCH")
                    x.destroy()
               if compscore==score:
                    disable2()
                    messagebox._show(x,"MATCH DRAWN")
                    x.destroy()
            else:
                score+=5
                label21=Label(frame2,text=score, bg="lightblue",font=("Arial", 10, "bold"))
                label21.place(x=450, y=400)
                if compscore<score:
                    messagebox._show(x,"YOU WON THE MATCH CONGRATULATIONS")
                    disable2()
                    x.destroy()

        def p6():
            nonlocal score
            nonlocal compscore
            z=random.randint(1,6)
            if z==6:
                if compscore>score:
                    disable2()
                    messagebox._show(x,"OOPS...YOU LOST,AI WON THE MATCH")
                    x.destroy()
                if compscore==score:
                    disable2()
                    messagebox._show(x,"MATCH DRAWN")
                    x.destroy()
            else:
                score+=6
                label21=Label(frame2,text=score, bg="lightblue",font=("Arial", 10, "bold"))
                label21.place(x=450, y=400)
                if compscore<score:
                    messagebox._show(x,"YOU WON THE MATCH CONGRATULATIONS")
                    disable2()
                    x.destroy()
        b1=Button(frame2,text="1",command=p1,font=("Arial", 10), bg='teal', fg='white', activebackground="lightblue")
        b1.place(x=300,y=200)
        b2=Button(frame2,text="2",command=p2,font=("Arial", 10),  bg='teal', fg='white', activebackground="lightblue")
        b2.place(x = 340, y = 200)
        b3=Button(frame2,text="3",command=p3,font=("Arial", 10), bg='teal', fg='white', activebackground="lightblue")
        b3.place(x = 380, y = 200)
        b4=Button(frame2,text="4",command=p4,font=("Arial", 10),  bg='teal', fg='white', activebackground="lightblue")
        b4.place(x = 420, y = 200)
        b5=Button(frame2,text="5",command=p5,font=("Arial", 10),  bg='teal', fg='white', activebackground="lightblue")
        b5.place(x = 460, y = 200)
        b6=Button(frame2,text="6",command=p6,font=("Arial", 10), bg='teal', fg='white', activebackground="lightblue")
        b6.place(x = 500, y = 200)

def decide2(k,y):
    compscore=0

    # Create label67 once so it's always available
    label67 = Label(frame2, text=compscore, bg="lightblue", font=("Arial", 10, "bold"))
    label67.place(x=450, y=450)
    def disable3():
        b1['state']='disable'
        b2['state']='disable'
        b3['state']='disable'
        b4['state']='disable'
        b5['state']='disable'
        b6['state']='disable'
    if (k=="THAT'S OUT"):
        score=y
        int(score)
        compscore=0
        def pl1():
            nonlocal compscore
            nonlocal score
            i = random.randint(1, 6)
    
            # Check if a wicket is taken
            if i == 1:
                if compscore < score:
                    messagebox._show(x, "YOU WON THE MATCH CONGRATULATIONS")
                    disable3()
                    x.destroy()
            elif compscore == score:
                messagebox._show(x, "MATCH DRAWN")
                disable3()
                x.destroy()
            else:
                compscore += i
                label21 = Label(frame2, text=compscore, bg="lightblue", font=("Arial", "10", "bold"))
                label21.place(x=450, y=450)
        
                if compscore > score:
                    messagebox._show(x, "OOPS...YOU LOST,AI WON THE MATCH")
                    disable3()
                    x.destroy()
        def pl2():
            nonlocal compscore
            nonlocal score
            i=random.randint(1,6)
            if i==2:
                if compscore<score:
                    messagebox._show(x,"YOU WON THE MATCH CONGRATULATIONS")
                    disable3()
                    x.destroy()
                if compscore==score:
                    messagebox._show(x,"MATCH DRAWN")
                    disable3()
                    x.destroy()
            else:
                compscore+=i
                label21=Label(frame2,text=compscore, bg="lightblue",font=("Arial", 10, "bold"))
                label21.place(x=450,y=450)
                if compscore>score:
                    messagebox._show(x,"OOPS...YOU LOST,AI WON THE MATCH")
                    disable3()
                    x.destroy()
        def pl3():
            nonlocal compscore
            nonlocal score
            i=random.randint(1,6)
            if i==3:
                if compscore<score:
                    messagebox._show(x,"YOU WON THE MATCH CONGRATULATIONS")
                    disable3()
                    x.destroy()
                if compscore==score:
                    messagebox._show(x,"MATCH DRAWN")
                    disable3()
                    x.destroy()
            else:
                compscore+=i
                label21=Label(frame2,text=compscore, bg="lightblue",font=("Arial", 10, "bold"))
                label21.place(x=450,y=450)
                if compscore>score:
                    messagebox._show(x,"OOPS...YOU LOST,AI WON THE MATCH")
                    disable3()
                    x.destroy()
        def pl4():
            nonlocal score
            nonlocal compscore
            i=random.randint(1,6)
            if i==4:
                if compscore<score:
                    messagebox._show(x,"YOU WON THE MATCH CONGRATULATIONS")
                    disable3()
                    x.destroy()
                if compscore==score:
                    messagebox._show(x,"MATCH DRAWN")
                    disable3()
                    x.destroy()
            else:
                compscore+=i
                label21=Label(frame2,text=compscore, bg="lightblue",font=("Arial", 10, "bold"))
                label21.place(x=450,y=450)
                if compscore>score:
                    messagebox._show(x,"OOPS...YOU LOST,AI WON THE MATCH")
                    disable3()
                    x.destroy()
        def pl5():
            nonlocal compscore
            nonlocal score
            i=random.randint(1,6)
            if i==5:
                if compscore<score:
                    messagebox._show(x,"YOU WON THE MATCH CONGRATULATIONS")
                    disable3()
                    x.destroy()
                if compscore==score:
                    messagebox._show(x,"MATCH DRAWN")
                    disable3()
                    x.destroy()
                
            else:
                compscore+=i
                label21=Label(frame2,text=compscore, bg="lightblue",font=("Arial", 10, "bold"))
                label21.place(x=450,y=450)
                if compscore>score:
                    messagebox._show(x,"OOPS...YOU LOST,AI WON THE MATCH")
                    disable3()
                    x.destroy()
        def pl6():
            nonlocal compscore
            nonlocal score
            i=random.randint(1,6)
            if i==6:
                if compscore<score:
                    messagebox._show(x,"YOU WON THE MATCH CONGRATULATIONS")
                    disable3()
                    x.destroy()
                if compscore==score:
                    messagebox._show(x,"MATCH DRAWN")
                    disable3()
                    x.destroy()
            else:
                compscore+=i
                label21=Label(frame2,text=compscore, bg="lightblue",font=("Arial", 10, "bold"))
                label21.place(x=450,y=450)
                if compscore>score:
                    messagebox._show(x,"OOPS...YOU LOST,AI WON THE MATCH")
                    disable3()
                    x.destroy()
        b1=Button(frame2,text="1",command=pl1,font=("Arial", 10), bg='teal', fg='white', activebackground="lightblue")
        b1.place(x=300,y=200)
        b2=Button(frame2,text="2",command=pl2,font=("Arial", 10),  bg='teal', fg='white', activebackground="lightblue")
        b2.place(x = 340, y = 200)
        b3=Button(frame2,text="3",command=pl3,font=("Arial", 10), bg='teal', fg='white', activebackground="lightblue")
        b3.place(x = 380, y = 200)
        b4=Button(frame2,text="4",command=pl4,font=("Arial", 10),  bg='teal', fg='white', activebackground="lightblue")
        b4.place(x = 420, y = 200)
        b5=Button(frame2,text="5",command=pl5,font=("Arial", 10),  bg='teal', fg='white', activebackground="lightblue")
        b5.place(x = 460, y = 200)
        b6=Button(frame2,text="6",command=pl6,font=("Arial", 10), bg='teal', fg='white', activebackground="lightblue")
        b6.place(x = 500, y = 200)    
def batAI():
    compscore=0

    # Create label67 once so it's always available
    label67 = Label(frame2, text=compscore, bg="lightblue", font=("Arial", 10, "bold"))
    label67.place(x=450, y=450)
    def c1():
        nonlocal compscore
        k=random.randint(1,6)
        if k==1:
            sc=compscore+1
            messagebox._show(x,f"THAT'S OUT,YOUR TARGET IS:{sc}")
            decide("THAT'S OUT",sc)
        if(k!=1):
            compscore+=k
            label21=Label(frame2,text=compscore, bg="lightblue",font=("Arial", 10, "bold"))
            label21.place(x=450, y=450)
            
    def c2():
        nonlocal compscore
        k=random.randint(1,6)
        if k==2:
            sc=compscore+1
            messagebox._show(x,f"THAT'S OUT,YOUR TARGET IS:{sc}")
            decide("THAT'S OUT",sc)
        if(k!=2):
            compscore+=k
            label21=Label(frame2,text=compscore, bg="lightblue",font=("Arial", 10, "bold"))
            label21.place(x=450, y=450)
    def c3():
        nonlocal compscore
        k=random.randint(1,6)
        if k==3:
            sc=compscore+1
            messagebox._show(x,f"THAT'S OUT,YOUR TARGET IS:{sc}")
            decide("THAT'S OUT",sc)
        if(k!=3):
            compscore+=k
            label21=Label(frame2,text=compscore, bg="lightblue",font=("Arial", 10, "bold"))
            label21.place(x=450, y=450)
    def c4():
        nonlocal compscore
        k=random.randint(1,6)
        if k==4:
            sc=compscore+1
            messagebox._show(x,f"THAT'S OUT,YOUR TARGET IS:{sc}")
            decide("THAT'S OUT",sc)
        if(k!=4):
            compscore+=k
            label21=Label(frame2,text=compscore, bg="lightblue",font=("Arial", 10, "bold"))
            label21.place(x=450, y=450)
    def c5():
        nonlocal compscore
        k=random.randint(1,6)
        if k==5:
            sc=compscore+1
            messagebox._show(x,f"THAT'S OUT,YOUR TARGET IS:{sc}")
            decide("THAT'S OUT",sc)
        if(k!=5):
            compscore+=k
            label21=Label(frame2,text=compscore, bg="lightblue",font=("Arial", 10, "bold"))
            label21.place(x=450, y=450)
    def c6():
        nonlocal compscore
        k = random.randint(1, 6)
        if k == 6:
            sc = compscore + 1
            messagebox.showinfo("OUT", f"THAT'S OUT, YOUR TARGET IS: {sc}")
            decide("THAT'S OUT",sc)
        else:
            compscore += k
            label21=Label(frame2,text=compscore, bg="lightblue",font=("Arial", 10, "bold"))
            label21.place(x=450, y=450)

    b1=Button(frame2,text="1",command=c1,font=("Arial", 10), bg='teal', fg='white', activebackground="lightblue")
    b1.place(x=300,y=200)
    b2=Button(frame2,text="2",command=c2,font=("Arial", 10),  bg='teal', fg='white', activebackground="lightblue")
    b2.place(x = 340, y = 200)
    b3=Button(frame2,text="3",command=c3,font=("Arial", 10), bg='teal', fg='white', activebackground="lightblue")
    b3.place(x = 380, y = 200)
    b4=Button(frame2,text="4",command=c4,font=("Arial", 10),  bg='teal', fg='white', activebackground="lightblue")
    b4.place(x = 420, y = 200)
    b5=Button(frame2,text="5",command=c5,font=("Arial", 10),  bg='teal', fg='white', activebackground="lightblue")
    b5.place(x = 460, y = 200)
    b6=Button(frame2,text="6",command=c6,font=("Arial", 10), bg='teal', fg='white', activebackground="lightblue")
    b6.place(x = 500, y = 200)      
def batUS():

    score = 0  

    # Create label67 once so it's always available
    label67 = Label(frame2, text=score, bg="lightblue", font=("Arial", 10, "bold"))
    label67.place(x=450, y=400)

    def play1():
        nonlocal score
        k = random.randint(1, 6)
        if k != 1:
            score += 1
            label67.config(text=score)   # update existing label
        else:
            txt = score + 1
            messagebox._show(x, f"THAT'S OUT,OPPONENT TARGET IS:{txt}")
            decide2("THAT'S OUT",txt)     # label67 is defined now

    def play2():
        nonlocal score
        k = random.randint(1, 6)
        if k != 2:
            score += 2
            label67.config(text=score)
        else:
            txt = score + 1
            messagebox._show(x, f"THAT'S OUT,OPPONENT TARGET IS:{txt}")
            decide2("THAT'S OUT",txt)

    def play3():
        nonlocal score
        k = random.randint(1, 6)
        if k != 3:
            score += 3
            label67.config(text=score)
        else:
            txt = score + 1
            messagebox._show(x, f"THAT'S OUT,OPPONENT TARGET IS:{txt}")
            decide2("THAT'S OUT",txt)

    def play4():
        nonlocal score
        k = random.randint(1, 6)
        if k != 4:
            score += 4
            label67.config(text=score)
        else:
            txt = score + 1
            messagebox._show(x, f"THAT'S OUT,OPPONENT TARGET IS:{txt}")
            decide2("THAT'S OUT",txt)

    def play5():
        nonlocal score
        k = random.randint(1, 6)
        if k != 5:
            score += 5
            label67.config(text=score)
        else:
            txt = score + 1
            messagebox._show(x, f"THAT'S OUT,OPPONENT TARGET IS:{txt}")
            decide2("THAT'S OUT",txt)

    def play6():
        nonlocal score
        k = random.randint(1, 6)
        if k != 6:
            score += 6
            label67.config(text=score)
        else:
            txt = score + 1
            messagebox._show(x, f"THAT'S OUT,OPPONENT TARGET IS:{txt}")
            decide2("THAT'S OUT",txt)

                
    b1=Button(frame2,text="1",command=play1,font=("Arial", 10), bg='teal', fg='white', activebackground="lightblue")
    b1.place(x=300,y=200)
    b2=Button(frame2,text="2",command=play2,font=("Arial", 10),  bg='teal', fg='white', activebackground="lightblue")
    b2.place(x = 340, y = 200)
    b3=Button(frame2,text="3",command=play3,font=("Arial", 10), bg='teal', fg='white', activebackground="lightblue")
    b3.place(x = 380, y = 200)
    b4=Button(frame2,text="4",command=play4,font=("Arial", 10),  bg='teal', fg='white', activebackground="lightblue")
    b4.place(x = 420, y = 200)
    b5=Button(frame2,text="5",command=play5,font=("Arial", 10),  bg='teal', fg='white', activebackground="lightblue")
    b5.place(x = 460, y = 200)
    b6=Button(frame2,text="6",command=play6,font=("Arial", 10), bg='teal', fg='white', activebackground="lightblue")
    b6.place(x = 500, y = 200)      

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
opt=['Heads','Tails']
def Tosswin():
    # Load coin images
    heads_img = ImageTk.PhotoImage(Image.open("HEAD (2).png").resize((130,130)))
    tails_img = ImageTk.PhotoImage(Image.open("TAIL (2).png").resize((130,130)))

    # Keep references so images don't disappear
    frame2.heads_img = heads_img
    frame2.tails_img = tails_img

    img_label = Label(frame2, image=heads_img)
    img_label.place(x=50, y=100)


    def coin_result(choice):
        play_btn2['state']='disable'
        play_btn1['state']='disable'
        global bt1,bt2
        result = random.choice(['Heads','Tails'])
        Label(frame2, text=result, font=("Arial", 12)).place(x=200, y=50)
        if choice == result:
            img_label = Label(frame2, image=heads_img)
            img_label.place(x=50, y=100)
            Label(frame2, text="YOU WON THE TOSS!", font=("Arial", 14, "bold")).place(x=200, y=80)
            bt1=ttk.Button(frame2, text="Bat first", command=lambda: [bt1.config(state="disabled"),bt2.config(state="disabled"),Label(frame2, text=bt1.cget("text"), font=("Arial", 14, "bold")).place(x=450, y=80),batUS()])
            bt1.place(x=200, y=150)
            bt2=ttk.Button(frame2, text="Bowl first", command=lambda: [bt2.config(state="disabled"),bt1.config(state="disabled"),Label(frame2, text=bt2.cget("text"), font=("Arial", 14, "bold")).place(x=450, y=80),batAI()])
            bt2.place(x=300, y=150)
            
        else:
            img_label = Label(frame2, image=tails_img)
            img_label.place(x=50, y=100)
            Label(frame2, text="YOU LOST THE TOSS,OPPONENT CHOSE TO", font=("Arial", 14, "bold")).place(x=200, y=80)
            ai_choice = random.choice(['Bat','Bowl'])
            label110=Label(frame2, text= ai_choice, font=("Arial", 14,"bold"))
            label110.place(x=600, y=80)
            if(label110.cget('text')=="Bat"):
                hd['state']='disable'
                tl['state']='disable'
                bt1=ttk.Button(frame2, text="PLAY", command=lambda: [bt1.config(state="disabled"), batAI()])
                bt1.place(x=200, y=150)
            if(label110.cget('text')=="Bowl"):
                hd['state']='disable'
                tl['state']='disable'
                bt1=ttk.Button(frame2, text="PLAY", command=lambda: [bt1.config(state="disabled"),batUS()])
                bt1.place(x=200, y=150)
    hd=ttk.Button(frame2, text="HEADS", style="Blue.TButton",command=lambda: coin_result("Heads"))
    hd.place(x=50, y=250)
    tl=ttk.Button(frame2, text="TAILS",style="Blue.TButton", command=lambda: coin_result("Tails"))
    tl.place(x=300, y=250)


#-------------------------------------------------------------------------------
#FRAME01
a=StringVar()
ntbt=ttk.Button(frame1,text="NEXT",style="Green.TButton",command=Tosswin)
ntbt.place(x=500, y=500)
ntbt['state']='disable'
a=StringVar()
def Submit(y,z,x):
    play_btn2['state']='normal'
    k=z.get()
    str(k)
    l=y.cget("text")
    if(str(k)==l):
       messagebox._show("showinfo","invalid team selection")
    elif(str(k)==''):
       messagebox._show("showinfo","please select your team")
    elif(str(k)!=l):
        label20.config(text=k)
        global label99
        label99 = Label(frame2, text=k, font=("Cooper", 12))
        label99.place(x=100, y=400)   # moved inside visible area

        label100 = Label(frame2, text='(YOU)', font=("Arial", 10, "bold"))
        label100.place(x=50, y=400)

        label900 = Label(frame2, text=l, fg='black', font=('Cooper', 12))
        label900.place(x=100, y=450)

        label200 = Label(frame2, text='(AI)', font=("Arial", 10, "bold"))
        label200.place(x=50, y=450)
        x['state']='disable'
def frch():
        r2['state']='disable'
        tm=['Chennai Stingers','Hyderabad Hawks','Mumbai Legends','Bangalore Rockets','Gujarat Gladiators','Lucknow Nawabs','Punjab Kings','Kolkata Tigers','Delhi Capitals','Barbados Royals','Guyana Warriors','Perth Scorchers','Sydney Sixers']
        y=random.choice(tm)
        global label100
        label12=Label(frame1,text='Select your team',font=('Cooper',8))
        label12.place(x=150,y=130)
        label100=Label(frame1,text=y,font=('Cooper',21),fg='black')
        label100.place(x=500,y=400)
        r1['state']='disable'
        opt=OptionMenu(frame1,a,*tm)
        opt.place(x=200,y=170)
        r1['state']='disable'
        v=ttk.Button(frame1,text="Submit", style="Green.TButton",command=lambda:Submit(label100,a,v))
        v.place(x=10, y=500)
def intn():
        r1['state']='disable'
        tm=['India','Australia','Pakistan','South Africa','New Zealand','USA','Sri Lanka','England','Ireland','Afghanistan','Bangladesh','Canada','Scotland']
        y=random.choice(tm)
        label12=Label(frame1,text='Select your team',font=('Cooper',13))
        label12.place(x=150,y=130)
        global label100
        label100=Label(frame1,text=y,font=('Cooper',21),fg='black')
        label100.place(x=500,y=400)
        options=['India','Australia','Pakistan','South Africa','New Zealand','USA','Sri Lanka','England','Ireland','Afghanistan','Bangladesh','Canada','Scotland']
        OptionMenu(frame1,a,*options).place(x=200,y=170)
        r2['state']='disable'
        v= ttk.Button(frame1, text="Submit", style="Green.TButton", command=lambda: Submit(label100,a,v))
        v.place(x=10, y=500)
def Reset():
    r1['state']='normal'
    r2['state']='normal'
    label20.config(text=" ")
    label99.config(text=" ")
    v= ttk.Button(frame1, text="Submit", style="Green.TButton", command=lambda: Submit(label100, a, v))
    v.place(x=10, y=500)
    play_btn = ttk.Button(frame1, text="Next", style="Green.TButton", command=Reset)
    play_btn.place(x=500, y=500)

# Make a style for ttk button
style = ttk.Style()
style.configure("Green.TButton", background="green", foreground="black", font=("Cooper", 20))
style.configure("Orange.TRadiobutton",background="orange",foreground="black",font=("Arial", 12))
style.configure("Blue.TButton",background="orange",foreground="black",font=("Arial", 12))

play_btn1 = ttk.Button(frame1, text="Reset", style="Green.TButton", command=Reset)
play_btn1.place(x=250, y=500)

play_btn2 = ttk.Button(frame1, text="Next", style="Green.TButton", command=Tosswin)
play_btn2.place(x=500, y=500)  
play_btn2['state']='disable'

r1 = ttk.Radiobutton(frame1, text="FRANCHISE", value="Franchise", style="Orange.TRadiobutton",command=frch)
r1.place(x=10,y=170)

r2 = ttk.Radiobutton(frame1, text="INTERNATIONAL",  value="International", style="Orange.TRadiobutton",command=intn)
r2.place(x=10,y=200)

label20=Label(frame1,text="",font = ('Cooper', 21))
label20.place(x=100,y=400)

label980=Label(frame1,text='VS',fg='black',font=('Cooper',18))
label980.place(x=350,y=400)

label300=Label(frame1,text="RULES--",fg='black',font=('Cooper',10))
label300.place(x=10,y=550)
label301=Label(frame1,text="1> BOTH USER AND AI WILL GET 1 WICKET EACH",fg='black',font=('Cooper',10))
label301.place(x=100,y=550)
label302=Label(frame1,text="2> AFTER TOSS,TEAM UPDATION IS NOT ALLOWED",fg='black',font=('Cooper',10))
label302.place(x=100,y=600)
label300=Label(frame1,text="3> THIS GAME CAN BE PLAYED ONCE.TO PLAY AGAIN PLS RE-RUN",fg='black',font=("Cooper",10))
label300.place(x=100,y=650)
label310=Label(frame1,text="4> CLICK THE PLAY BUTTON ONCE ONLY",fg='black',font=("Cooper",10))
label310.place(x=100,y=700)

x.mainloop()
