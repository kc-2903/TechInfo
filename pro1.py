import tkinter as tk
import mysql.connector
from tkinter import ttk 
from tkinter import messagebox as tk1
from PIL import Image, ImageTk
win=tk.Tk()

win.minsize(height=600,width=600)
win.configure(bg='#8C78FF')
style = ttk.Style() 
style2=ttk.Style()
style.configure('W.TButton', font =
               ('Trebuchet MS', 10, 'bold'), 
                foreground = '#35424a') 
style2.configure("BW.TLabel", foreground='magenta', background="white",
                 font=('sans-serif', 19, 'bold'))
                #font=('Times New Roman',25,'bold'))
style.map("W.TButton",
    foreground=[('pressed', 'orange'), ('active', 'magenta')],
    background=[('pressed', '!disabled', 'black'), ('active', 'black')]
    )

var1=tk.StringVar()
#FF2E0B
#FF7A0B
#8A97FF
#8C78FF
#FF7FC2

#lang func variables
synv1=tk.IntVar()
synv2=tk.IntVar()
synv3=tk.IntVar()
supv1=tk.IntVar()
supv2=tk.IntVar()
supv3=tk.IntVar()
feav1=tk.IntVar()
feav2=tk.IntVar()
feav3=tk.IntVar()


#tech func variables
demv1=tk.IntVar()
demv2=tk.IntVar()
demv3=tk.IntVar()
yofv=tk.IntVar()
comv=tk.StringVar()

#comp func variables
avgv=tk.IntVar()
tecv=tk.StringVar()
lanv=tk.StringVar()
langs=""
techs=""
coms=""

c1=0
c2=0
c3=0

out1=0
out2=0
out3=0
def outputl():
    global synv1
    global synv2
    global synv3
    global supv1
    global supv2
    global supv3
    global feav1
    global feav2
    global feav3
    l=[synv1.get(),synv2.get(),synv3.get(),supv1.get(),supv2.get(),supv3.get(),feav1.get(),feav2.get(),feav3.get()]
    print(l)
    try:
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="password",database='s')
        myc=mydb.cursor()
        s='select lang from proglang where '
        syn="syntax in ("
        sup="support in ("
        fea="features in ("
        c=0
        if(any(l)==0):
            myc.execute("select * from proglang;")
            s=myc.fetchall()
            s=str(s)
            tk1.showinfo('language',s)
            myc.close()
        else:
            
            if l[0]==1 or l[1]==1 or l[2]==1:
    
                k=0
                c+=1
                s=s+syn
                if l[0]==1:
                    s=s+"\'easy\'"
                    k+=1
                if l[1]==1:
                    if k==0:
                        s=s+"\'medium\'"
                        k+=1
                    else:
                        s=s+','
                        s=s+"\'medium\'"
                        k+=1
                if l[2]==1:
                    if k==0:
                        s=s+"\'difficult'"
                        k+=1
                    else:
                        s=s+','
                        s=s+"\'difficult'"
                        k+=1
                s=s+')'
            if l[3]==1 or l[4]==1 or l[5]==1:
                if c>0:
                    s=s+' and '
                c+=1
                s=s+sup
                k=0
                if l[3]==1:
                    s=s+"\'less\'"
                    k+=1
                if l[4]==1:
                    if k==0:
                        s=s+"\'medium\'"
                        k+=1
                    else:
                        s=s+','
                        s=s+"\'medium\'"
                        k+=1
                if l[5]==1:
                    if k==0:
                        s=s+"\'high'"
                        k+=1
                    else:
                        s=s+','
                        s=s+"\'high'"
                        k+=1
                c+=1
                s=s+')'
    
            if l[6]==1 or l[7]==1 or l[8]==1:
                if c>0:
                    s=s+' and '
                c+=1
                s=s+fea
                k=0
                if l[6]==1:
                    s=s+"\'low\'"
                    k+=1
                if l[7]==1:
                    if k==0:
                        s=s+"\'moderate\'"
                        k+=1
                    else:
                        s=s+','
                        s=s+"\'moderate\'"
                        k+=1
                if l[8]==1:
                    if k==0:
                        s=s+"\'more'"
                        k+=1
                    else:
                        s=s+','
                        s=s+"\'more'"
                        k+=1
                c+=1  
                s=s+')'        
            s=s+";"
            print(s)
            myc.execute(s)
            s=myc.fetchall()
            s=str(s)
            print(s)
            #s=str(list(set(s)))
            tk1.showinfo('language',s)
            myc.close()
    except Exception as e:
        print(e)
def clearl():
    synv1.set(0)
    synv2.set(0)
    synv3.set(0)
    supv1.set(0)
    supv2.set(0)
    supv3.set(0)
    feav1.set(0)
    feav2.set(0)
    feav3.set(0)
    
    
def ln():

    win2=tk.Toplevel() 
    win2.minsize(height=600,width=600) 
    win2.configure(bg='#8C78FF')
    title=tk.Label(win2,text="Choose the programming language you want.......")
    title.grid(row=1,column=1)
    syn=tk.Label(win2,text="syntax")
    syn.grid(row=2,column=1)

    sup=tk.Label(win2,text="support")
    sup.grid(row=4,column=1)

    fea=tk.Label(win2,text="features")
    fea.grid(row=6,column=1)

    sync1=tk.Checkbutton(win2,text='easy',variable=synv1,onvalue=1)
    sync1.grid(row=2,column=2,sticky='E')

    sync2=tk.Checkbutton(win2,text='medium',variable=synv2,onvalue=1)
    sync2.grid(row=2,column=3,sticky='E')

    sync3=tk.Checkbutton(win2,text='difficult',variable=synv3,onvalue=1)
    sync3.grid(row=2,column=4,sticky='E')

    supc1=tk.Checkbutton(win2,text='low',variable=supv1,onvalue=1)
    supc1.grid(row=4,column=2,sticky='E')

    supc2=tk.Checkbutton(win2,text='medium',variable=supv2,onvalue=1)
    supc2.grid(row=4,column=3,sticky='E')

    supc3=tk.Checkbutton(win2,text='high',variable=supv3,onvalue=1)
    supc3.grid(row=4,column=4,sticky='E')
 
    feac1=tk.Checkbutton(win2,text='less',variable=feav1,onvalue=1)
    feac1.grid(row=6,column=2,sticky='E')

    feac2=tk.Checkbutton(win2,text='moderate',variable=feav2,onvalue=1)































    feac2.grid(row=6,column=3,sticky='E')
 
    feac3=tk.Checkbutton(win2,text='more',variable=feav3,onvalue=1)
    feac3.grid(row=6,column=4,sticky='E')
        
    bt=ttk.Button(win2,style = 'W.TButton',text="submit",command=outputl)
    bt.grid(row=8,column=1)
    bt1=ttk.Button(win2,style = 'W.TButton',text="back",command=win2.destroy)
    bt1.grid(row=8,column=3)
    sub2=ttk.Button(win2,style = 'W.TButton',text="clear",command=clearl)
    sub2.grid(row=8,column=5)
    

def te():
    win2=tk.Toplevel()
    win2.minsize(height=500,width=500)
    win2.configure(bg='#8C78FF')
    titletech=tk.Label(win2,text="choose the technology you want......")
    titletech.grid(row=1,column=1)

    dem=tk.Label(win2,text='demand')
    dem.grid(row=2,column=1)

    dem1=tk.Checkbutton(win2,text="low",variable=demv1)
    dem1.grid(row=2,column=2)

    dem1=tk.Checkbutton(win2,text="medium",variable=demv2)
    dem1.grid(row=2,column=3)

    dem1=tk.Checkbutton(win2,text="high",variable=demv3)
    dem1.grid(row=2,column=4)

    yof=tk.Label(win2,text="year of fame")
    yof.grid(row=4,column=1)
    lst=range(1970,2020)
    yofl=tk.OptionMenu(win2,yofv,*lst)
    yofl.grid(row=4,column=2)

    com=tk.Label(win2,text="company")
    com.grid(row=6,column=1)
    l=['microsoft','google','apple','facebook','cisco','wallmart','amazon','netflix','JP morgan','nvidia','ibm','ea']
    coml=tk.OptionMenu(win2,comv,*l)
    coml.grid(row=6,column=2)
    
    bu3=tk.Button(win2,text="enter",command=enter3)
    bu3.grid(row=6,column=3)

    sub=ttk.Button(win2,style = 'W.TButton',text="submit",command=outputt)
    sub.grid(row=8,column=1)

    sub1=ttk.Button(win2,style = 'W.TButton',text="back",command=win2.destroy)
    sub1.grid(row=8,column=3)
    sub2=ttk.Button(win2,style = 'W.TButton',text="clear",command=cleart)
    sub2.grid(row=8,column=5)
    
def enter3():
    global coms
    global c3
    if(c3==0):
        coms=coms+"\""+comv.get()+"\""
        c3=c3+1
    else:
        coms=coms+","+"\""+comv.get()+"\""
        c3=c3+1
    comv.set(0)
def cleart():
    global coms,c3
    coms=""
    comv.set(0)
    demv1.set(0)
    demv2.set(0)
    demv3.set(0)
    yofv.set(0)
    c3=0    
    
def outputt():
    global demv1
    global demv2
    global demv3
    global yofv
    global comv
    l=[demv1.get(),demv2.get(),demv3.get(),yofv.get(),comv.get()]
    try:
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="password",database='s')
        myc=mydb.cursor()
        s='select t1.tech from technology t1 '
        s2=',company t2'
        s1="t1.demand in ("
        c=0
        k=0
        l1=['microsoft','google','apple','facebook','cisco','wallmart','amazon','netflix','JP morgan','nvidia','ibm','ea']
        if(any(l)==0 and coms==""):
            myc.execute("select * from technology;")
            s=myc.fetchall()
            s=str(s)
            tk1.showinfo('language',s)
            myc.close()
        else:
            
            if coms!="":
                s=s+s2+' where '
                s=s+' t2.company in ('+coms+') and t1.tech=t2.tech'
                k+=1
            else:
                s=s+ ' where ' 
            if l[0]==1 or l[1]==1 or l[2]==1:
                if k!=0:
                    s=s+' and '
                s=s+s1
                if l[0]==1:
                    if c==0:
                        s=s+"\'low\'"
                        c+=1
                    else:
                        s=s+','
                        s=s+"\'low\'"
                        c+=1
                if l[1]==1:
                    if c==0:
                        s=s+"\'medium\'"
                        c+=1
                    else:
                        s=s+','
                        s=s+"\'medium\'"
                        c+=1
                if l[2]==1:
                    if c==0:
                        s=s+"\'high\'"
                        c+=1
                    else:
                        s=s+','
                        s=s+"\'high\'"
                        c+=1
                s=s+')'
            if yofv.get()==0:
                pass
            else:
                s=s+ 'and t1.year>='+str(yofv.get())
    
            s=s+';'
            print(s)
            myc.execute(s)
            s=myc.fetchall()
            print(s)
            #s=str(list(set(s)))
            tk1.showinfo("tech",str(s))
            myc.close()
    except Exception as e:
        print(e)
def enter1():
    global langs
    global c1
    if(c1==0):
        langs=langs+"\""+lanv.get()+"\""
        c1=c1+1
    else:
        langs=langs+","+"\""+lanv.get()+"\""
        c1=c1+1
    lanv.set(0)
def enter2():
    global techs
    global c2
    if(c2==0):
        techs=techs+"\""+tecv.get()+"\""
        c2=c2+1
    else:
        techs=techs+","+"\""+tecv.get()+"\""
        c2=c2+1
    tecv.set(0)
def clearc():
    global techs
    global langs
    global c1,c2
    techs=""
    langs=""
    avgv.set(0)
    lanv.set(0)
    tecv.set(0)
    c1=0
    c2=0
    
    
def outputc():
    global avgv
    global tecv
    global lanv
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="password",database='s')
    myc=mydb.cursor()
    l1=['ai','bigdata','kernel design','os design','data science','blockchain','iOS apps','networking','web apps','android apps','devops','iot','compiler design','e-business','gui design','hardware design','games','web backend','ar/vr','cloud computing']
    l2=['python','java','c','r','rust','c++','swift','java script','ruby','kotlin','scala','arduino','cobol','c#','go','dart','fortran','assembly','perl','basic']
    s='select company from company where '
    if(langs=="" and techs=="" and avgv.get()==0):
        myc.execute("select * from technology;")
        s=myc.fetchall()
        s=str(s)
        tk1.showinfo('language',s)
        myc.close()
    else:
        if avgv.get()!=0:
            s=s+'avgpay>='+str(avgv.get())
        elif techs!= "":
            s=s+'tech in ('+techs+')'
            
        elif langs!="":
            s=s+'lang in ('+langs+')'
            s=s+';'
        print(s)
        myc.execute(s)
        s=myc.fetchall()
        s=str(s)
        print(s)
        #s=str(list(set(s)))
        tk1.showinfo("company",s)
        myc.close()
def comp():
    win2=tk.Toplevel()
    win2.minsize(height=500,width=500)
    win2.configure(bg='#8C78FF')
    lab=tk.Label(win2,text="please select any one option to get the company you want....")
    lab.grid(row=1,column=1)
    avg=tk.Label(win2,text="avg pay")
    avg.grid(row=3,column=1)
    
    lst=range(90000,200000,10000)
    avgl=tk.OptionMenu(win2,avgv,*lst)
    avgl.grid(row=3,column=2)

    tec=tk.Label(win2,text="technology")
    tec.grid(row=5,column=1)

    lst1=['ai','bigdata','kernel design','os design','data science','blockchain','iOS apps','networking','web apps','android apps','devops','iot','compiler design','e-business','gui design','hardware design','games','web backend','ar/vr','cloud computing']
    tecl=tk.OptionMenu(win2,tecv,*lst1)
    tecl.grid(row=5,column=2)
    
    bu1=tk.Button(win2,text='enter',command=enter2)
    bu1.grid(row=5,column=3)

    lan=tk.Label(win2,text="language")
    lan.grid(row=7,column=1)
    lst2=['python','java','c','r','rust','c++','swift','java script','ruby','kotlin','scala','arduino','cobol','c#','go','dart','fortran','assembly','perl','basic']
    lanl=tk.OptionMenu(win2,lanv,*lst2)
    lanl.grid(row=7,column=2)
    bu1=tk.Button(win2,text='enter',command=enter1)
    bu1.grid(row=7,column=3)


    sub=ttk.Button(win2,style = 'W.TButton',text="SUBMIT",command=outputc)
    sub.grid(row=9,column=1)
    sub1=ttk.Button(win2,style = 'W.TButton',text="BACK",command=win2.destroy)
    sub1.grid(row=9,column=2)
    sub2=ttk.Button(win2,style = 'W.TButton',text="CLEAR",command=clearc)
    sub2.grid(row=9,column=3)


title=ttk.Label(text="TECH INFO",style='BW.TLabel')
title.place(x=200,y=20)


loadai = Image.open("ai.jfif").resize((50,50))
renderai = ImageTk.PhotoImage(loadai)

imgai = tk.Label( image=renderai)
imgai.image = renderai
imgai.place(x=125, y=130)

loadbg = Image.open("bigdata.png").resize((50,50))
renderbg = ImageTk.PhotoImage(loadbg)

imgbg = tk.Label( image=renderbg)
imgbg.image = renderbg
imgbg.place(x=40, y=190)
loadk = Image.open("kernal.png").resize((50,50))
renderk = ImageTk.PhotoImage(loadk)

imgk = tk.Label( image=renderk)
imgk.image = renderk
imgk.place(x=210, y=190)
loadd = Image.open("datas.jfif").resize((50,50))
renderd = ImageTk.PhotoImage(loadd)

imgd = tk.Label( image=renderd)
imgd.image = renderd
imgd.place(x=125, y=260)

tech=ttk.Button(win,style = 'W.TButton',text='TECHNOLOGY',command=te)
tech.place(x=102,y=200,height =40,width=100)
loadg = Image.open("google.png").resize((50,50))
renderg = ImageTk.PhotoImage(loadg)

imgg = tk.Label( image=renderg)
imgg.image = renderg
imgg.place(x=385, y=130)
loadf = Image.open("facebook.png").resize((50,50))
renderf = ImageTk.PhotoImage(loadf)

imgf = tk.Label( image=renderf)
imgf.image = renderf
imgf.place(x=300, y=190)
loada = Image.open("amazon.png").resize((50,50))
rendera = ImageTk.PhotoImage(loada)

imga = tk.Label( image=rendera)
imga.image = rendera
imga.place(x=470, y=190)
loadm = Image.open("microsoft.png").resize((50,50))
renderm = ImageTk.PhotoImage(loadm)

imgm = tk.Label( image=renderm)
imgm.image = renderm
imgm.place(x=385, y=260)

company=ttk.Button(win,style = 'W.TButton',text='COMPANY',command=comp)
company.place(x=362,y=200,height =40,width=100)

loadc = Image.open("c.png").resize((50,50))
renderc = ImageTk.PhotoImage(loadc)

imgc = tk.Label( image=renderc)
imgc.image = renderc
imgc.place(x=260, y=320)
loadr = Image.open("r.jfif").resize((50,50))
renderr = ImageTk.PhotoImage(loadr)

imgr = tk.Label( image=renderr)
imgr.image = renderr
imgr.place(x=175, y=380)
loadp = Image.open("python.jfif").resize((50,50))
renderp = ImageTk.PhotoImage(loadp)

imgp = tk.Label( image=renderp)
imgp.image = renderp
imgp.place(x=345, y=380)
loadj = Image.open("java.png").resize((50,50))
renderj = ImageTk.PhotoImage(loadj)

imgj = tk.Label( image=renderj)
imgj.image = renderj
imgj.place(x=260, y=440)

lang=ttk.Button(win,style = 'W.TButton',text='LANGUAGE',command=ln)
lang.place(x=237,y=390,height =40,width=100)






win.mainloop()