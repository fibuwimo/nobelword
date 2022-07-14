import pandas as pd
import random
import tkinter as tk

def b1_click():
    count=0;
    word=e1.get()
    for w in words:
        if (word in w):
            count +=1
    t1.insert(tk.END,'{}:{}回\n'.format(word,count))
def b2_click():
    ans=e2.get()
    if(ans==titles_name[idx]):
        t2.insert(tk.END,'正解！\n')
    else:
        t2.insert(tk.END,'違うよ\n')

titles=[
    "ginga.csv",
    "sero.csv",
    "neko.csv",
    "tyuumon.csv",
    "kokoro.csv",
    "kumo.csv",
    "rasyou.csv",
]
titles_name=[
    "銀河鉄道の夜",
    "セロ弾きのゴーシュ",
    "吾輩は猫である",
    "注文の多い料理店",
    "こころ",
    "蜘蛛の糸",
    "羅生門",
]

print(len(titles))
idx=random.randint(0,len(titles)-1)
df = pd.read_csv(titles[idx])
words=df.iloc[:,3]

print(len(words))

root=tk.Tk()
root.title('クイズ')
root.geometry('1200x800')
canvas=tk.Canvas(root,width=1200,height=800,bg='skyblue')
canvas.pack()

l1=tk.Label(root,text='回数を調べたい単語を入力',font=('Arial',20))
l1.place(x=50,y=100)
t1=tk.Text(width=25,height=400,font=("Times New Roman", 16),bg='skyblue')
t1.place(x=400,y=100)
e1=tk.Entry(width=20,font=("Times New Roman", 16))
e1.place(x=50,y=150)
b1=tk.Button(width=10,height=3,text='回数を検索',command=b1_click)
b1.place(x=50,y=180)
l2=tk.Label(root,text='タイトルを入力',font=('Arial',20))
l2.place(x=50,y=270)
e2=tk.Entry(width=20,font=("Times New Roman", 16))
e2.place(x=50,y=320)
b2=tk.Button(width=10,height=3,text='回答',command=b2_click)
b2.place(x=50,y=360)
t3=tk.Text(width=20,height=400,font=('Arial',20),bg='skyblue')
t3.place(x=700,y=100)
t2=tk.Text(width=20,height=40,font=("Times New Roman", 16),bg='skyblue')
t2.place(x=50,y=420)

for t in titles_name:
    t3.insert(tk.END,f'{t}\n')


root.mainloop()