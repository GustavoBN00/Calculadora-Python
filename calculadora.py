from tkinter import *
from tkinter import ttk

#cor
cinza1='#e3e3e3'#claro
cinza2='#2f3e40'#escuro
branco='white'
preto='black'
laranja='#e6952c'

#home
home=Tk()
home.title("Calculadora")
home.geometry('235x310+900+300')
home.resizable(False,False)

#frames
frame_display=Frame(home, width=235, height=50, bg=cinza2)
frame_display.grid(row=0, column=0)

frame_body=Frame(home, width=235, height=268, bg=cinza1)
frame_body.grid(row=1, column=0)

#funções
valorALL=''

def entrada(valor):
    global valorALL
    valorALL=valorALL+str(valor)
    result_texto.set(valorALL)

def calc():
    global valorALL
    result=eval(valorALL)
    result_texto.set(result)

def clear():
    global valorALL
    valorALL=""
    result_texto.set("")

#labels
result_texto=StringVar()
result_label=Label(frame_display, textvariable=result_texto, width=16, height=2, padx=7, relief=FLAT, anchor='e', justify='right', font=('Ivy 17 bold'), bg=cinza2, fg=branco)
result_label.place(x=1,y=0)


#botão linha 1
btclean=Button(frame_body, command=clear,text="C", width=11, height=2, bg=laranja, fg=branco, font=('Ivy 13 bold'), overrelief=RIDGE)
btclean.place(x=0,y=0)

btpercent=Button(frame_body, command=lambda:entrada('%'), text="%", width=5, height=2, bg=laranja, fg=branco, font=('Ivy 13 bold'), overrelief=RIDGE)
btpercent.place(x=120,y=0)
btdivisao=Button(frame_body, command=lambda:entrada('/'), text="/", width=5, height=2, bg=laranja, fg=branco, font=('Ivy 13 bold'), overrelief=RIDGE)
btdivisao.place(x=180,y=0)

#botão linha 2
btsete=Button(frame_body, command=lambda:entrada('7'), text="7", width=5, height=2, bg=cinza1, fg=preto, font=('Ivy 13 bold'), overrelief=RIDGE)
btsete.place(x=0,y=52)
btoito=Button(frame_body, command=lambda:entrada('8'), text="8", width=5, height=2, bg=cinza1, fg=preto, font=('Ivy 13 bold'), overrelief=RIDGE)
btoito.place(x=60,y=52)
btnove=Button(frame_body, command=lambda:entrada('9'), text="9", width=5, height=2, bg=cinza1, fg=preto, font=('Ivy 13 bold'), overrelief=RIDGE)
btnove.place(x=120,y=52)
btmulti=Button(frame_body, command=lambda:entrada('*'), text="*", width=5, height=2, bg=laranja, fg=branco, font=('Ivy 13 bold'), overrelief=RIDGE)
btmulti.place(x=180,y=52)

#botão linha 3
btquatro=Button(frame_body, command=lambda:entrada('4'), text="4", width=5, height=2, bg=cinza1, fg=preto, font=('Ivy 13 bold'), overrelief=RIDGE)
btquatro.place(x=0,y=104)
btcinco=Button(frame_body, command=lambda:entrada('5'), text="5", width=5, height=2, bg=cinza1, fg=preto, font=('Ivy 13 bold'), overrelief=RIDGE)
btcinco.place(x=60,y=104)
btseis=Button(frame_body, command=lambda:entrada('6'), text="6", width=5, height=2, bg=cinza1, fg=preto, font=('Ivy 13 bold'), overrelief=RIDGE)
btseis.place(x=120,y=104)
btmenos=Button(frame_body, command=lambda:entrada('-'), text="-", width=5, height=2, bg=laranja, fg=branco, font=('Ivy 13 bold'), overrelief=RIDGE)
btmenos.place(x=180,y=104)

#botão linha 4
btum=Button(frame_body, command=lambda:entrada('1'), text="1", width=5, height=2, bg=cinza1, fg=preto, font=('Ivy 13 bold'), overrelief=RIDGE)
btum.place(x=0,y=156)
btdois=Button(frame_body, command=lambda:entrada('2'), text="2", width=5, height=2, bg=cinza1, fg=preto, font=('Ivy 13 bold'), overrelief=RIDGE)
btdois.place(x=60,y=156)
bttres=Button(frame_body, command=lambda:entrada('3'), text="3", width=5, height=2, bg=cinza1, fg=preto, font=('Ivy 13 bold'), overrelief=RIDGE)
bttres.place(x=120,y=156)
btmais=Button(frame_body, command=lambda:entrada('+'), text="+", width=5, height=2, bg=laranja, fg=branco, font=('Ivy 13 bold'), overrelief=RIDGE)
btmais.place(x=180,y=156)

#botão linha 5
btzero=Button(frame_body, command=lambda:entrada('0'), text="0", width=11, height=2, bg=cinza1, fg=preto, font=('Ivy 13 bold'), overrelief=RIDGE)
btzero.place(x=0,y=208)

btponto=Button(frame_body, command=lambda:entrada('.'), text=".", width=5, height=2, bg=cinza1, fg=preto, font=('Ivy 13 bold'), overrelief=RIDGE)
btponto.place(x=120,y=208)
btigual=Button(frame_body, command=calc , text="=", width=5, height=2, bg=laranja, fg=branco, font=('Ivy 13 bold'), overrelief=RIDGE)
btigual.place(x=180,y=208)

home.mainloop()