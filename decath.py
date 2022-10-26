
import requests
from bs4 import BeautifulSoup
import pandas as pd
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename,asksaveasfilename

root=Tk()
root.geometry("700x300")
root.config(bg="#87BDD8")

def Search():
    file=asksaveasfilename(defaultextension=('csv', '*.csv',"*xlsx"))
    b=value.get("1.0","end-1c")
    page = requests.get(f"https://www.decathlon.in/search?query={b}").text
    a=f"https://www.decathlon.in/search?query={b}"
    soup = BeautifulSoup(page,"html.parser")
    # av=val.get("1.0","end-1c")

    df=pd.DataFrame(columns=["Name","Price","Rating","Link"])

    datas=soup.find_all("li",class_="ais-Hits-item")
    for data in datas:
        bottle_name=data.find("div",class_="mb-1 _1cXrNZvG3X card-title").text.replace("\n","")
        price=data.find("span",class_="_3wHKeni9X- mr-3").text.replace("\n","")
        rating=data.find("span", class_="_3zbbi0Uj7u").text.replace("\n","")
        link=data.find("a",class_="").get('href')
        

        df=df.append({"Name":bottle_name,"Price":price,"Rating":rating,"Link":a+link},ignore_index=True)
    df.to_csv(file,index=False)





value=Text(root, height=2, width=40)
value.place(x=200,y=20)
# val=Text(root, height=2, width=40)
# val.place(x=200,y=75)


hi=Label(root,text="Product Name:",bg="#87BDD8",font=("ariel 17 bold"), width=12)
hi.place(x=20,y=20)
# hi2=Label(root,text="File Name:",bg="#87BDD8",font=("ariel 17 bold"), width=8)
# hi2.place(x=45,y=75)
hi3=Label(root,text="Note:Enter '%20' insteed of space",bg="#87BDD8",font=("ariel 17 bold"), width=50)
hi3.place(x=10,y=270)

comment= Button(root, height=3, width=10, text="Generate File",fg='Red', command=lambda: Search())

#command=get_input() will wait for the key to press and displays the entered text
comment.place(x=300,y=200)

root.mainloop()