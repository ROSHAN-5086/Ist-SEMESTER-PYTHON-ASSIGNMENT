                                             #Question 1
from tkinter import *
root=Tk()
root.config(background="grey")
root.title("Roshan's GST Calculator")
root.geometry("900x740")
root.minsize(width=900,height=740)
root.maxsize(width=900,height=740)
#variable
original_cost_v=StringVar()
net_price_v=StringVar()
gst_v=StringVar()
value="" #Original Cost in string form
value2=""#Net price in string form
def GST():
    gst_rate=((float(value2)-float(value))*100)/float(value)
    r="{:.5f}".format(gst_rate)
    gst_v.set(str(r))
    gst = Label(gst_frame, bg="pink", textvariable=gst_v, font="bold 56",fg="black",
                width=7, relief="solid", bd=5)
    gst.grid(row=0, column=1, sticky="w")

#Number functions
def keyboard1():
    def fun1():
        global value
        value = value + "1"
        original_cost_v.set(value)

    def fun2():
        global value
        value = value + "2"
        original_cost_v.set(value)

    def fun3():
        global value
        value = value + "3"
        original_cost_v.set(value)

    def fun4():
        global value
        value = value + "4"
        original_cost_v.set(value)

    def fun5():
        global value
        value = value + "5"
        original_cost_v.set(value)

    def fun6():
        global value
        value = value + "6"
        original_cost_v.set(value)

    def fun7():
        global value
        value = value + "7"
        original_cost_v.set(value)

    def fun8():
        global value
        value = value + "8"
        original_cost_v.set(value)

    def fun9():
        global value
        value = value + "9"
        original_cost_v.set(value)

    def fun0():
        global value
        value = value + "0"
        original_cost_v.set(value)

    def fun_clear():
        global value
        value = ""
        original_cost_v.set(value)

    def fun_dot():
        global value
        value = value + "."
        original_cost_v.set(value)

    num = Frame(width=948, height=350, bg="green", relief="solid", bd=5)
    num.grid(row=4, column=0)

    # creating number button
    # column 0
    seven = Button(num, text="7", font="bold 35", bg="orange", fg="black", width=9, height=2, command=fun7)
    seven.grid(row=0, column=0)
    four = Button(num, text="4", font="bold 35", bg="orange", fg="black", width=9, height=2, command=fun4)
    four.grid(row=1, column=0)
    one = Button(num, text="1", font="bold 35", bg="orange", fg="black", width=9, height=2, command=fun1)
    one.grid(row=2, column=0)
    zero = Button(num, text="0", font="bold 35", bg="orange", fg="black", width=9, height=2, command=fun0)
    zero.grid(row=3, column=0)
    # column 1
    eight = Button(num, text="8", font="bold 35", bg="orange", fg="black", width=9, height=2, command=fun8)
    eight.grid(row=0, column=1)
    five = Button(num, text="5", font="bold 35", bg="orange", fg="black", width=9, height=2, command=fun5)
    five.grid(row=1, column=1)
    two = Button(num, text="2", font="bold 35", bg="orange", fg="black", width=9, height=2, command=fun2)
    two.grid(row=2, column=1)
    dot = Button(num, text=".", font="bold 35", bg="orange", fg="black", width=9, height=2, command=fun_dot)
    dot.grid(row=3, column=1)
    # column 2
    nine = Button(num, text="9", font="bold 35", bg="orange", fg="black", width=9, height=2, command=fun9)
    nine.grid(row=0, column=2)
    six = Button(num, text="6", font="bold 35", bg="orange", fg="black", width=9, height=2, command=fun6)
    six.grid(row=1, column=2)
    three = Button(num, text="3", font="bold 35", bg="orange", fg="black", width=9, height=2, command=fun3)
    three.grid(row=2, column=2)
    # column 3
    equal = Button(num, text="Calculate", font="bold 35", bg="orange", fg="blue", width=9, height=2,command=GST)
    equal.grid(row=3, column=2)
    # Clear
    clear = Button(gst_frame, text="Clear Original\nCost", font="bold 30", bg="orange", fg="red", width=9, height=2, command=fun_clear)
    clear.grid(row=0, column=2, sticky="w")

def keyboard2():
    def fun1():
        global value2
        value2 = value2 + "1"
        net_price_v.set(value2)

    def fun2():
        global value2
        value2 = value2 + "2"
        net_price_v.set(value2)

    def fun3():
        global value2
        value2 = value2 + "3"
        net_price_v.set(value2)

    def fun4():
        global value2
        value2 = value2 + "4"
        net_price_v.set(value2)

    def fun5():
        global value2
        value2 = value2 + "5"
        net_price_v.set(value2)

    def fun6():
        global value2
        value2 = value2 + "6"
        net_price_v.set(value2)

    def fun7():
        global value2
        value2 = value2 + "7"
        net_price_v.set(value2)

    def fun8():
        global value2
        value2 = value2 + "8"
        net_price_v.set(value2)

    def fun9():
        global value2
        value2 = value2 + "9"
        net_price_v.set(value2)

    def fun0():
        global value2
        value2 = value2 + "0"
        net_price_v.set(value2)

    def fun_clear():
        global value2
        value2 = ""
        net_price_v.set(value2)

    def fun_dot():
        global value2
        value2 = value2 + "."
        net_price_v.set(value2)

    num = Frame(width=948, height=350, bg="green", relief="solid", bd=5)
    num.grid(row=4, column=0)

    # creating number button
    # column 0
    seven = Button(num, text="7", font="bold 35", bg="orange", fg="black", width=9, height=2, command=fun7)
    seven.grid(row=0, column=0)
    four = Button(num, text="4", font="bold 35", bg="orange", fg="black", width=9, height=2, command=fun4)
    four.grid(row=1, column=0)
    one = Button(num, text="1", font="bold 35", bg="orange", fg="black", width=9, height=2, command=fun1)
    one.grid(row=2, column=0)
    zero = Button(num, text="0", font="bold 35", bg="orange", fg="black", width=9, height=2, command=fun0)
    zero.grid(row=3, column=0)
    # column 1
    eight = Button(num, text="8", font="bold 35", bg="orange", fg="black", width=9, height=2, command=fun8)
    eight.grid(row=0, column=1)
    five = Button(num, text="5", font="bold 35", bg="orange", fg="black", width=9, height=2, command=fun5)
    five.grid(row=1, column=1)
    two = Button(num, text="2", font="bold 35", bg="orange", fg="black", width=9, height=2, command=fun2)
    two.grid(row=2, column=1)
    dot = Button(num, text=".", font="bold 35", bg="orange", fg="black", width=9, height=2, command=fun_dot)
    dot.grid(row=3, column=1)
    # column 2
    nine = Button(num, text="9", font="bold 35", bg="orange", fg="black", width=9, height=2, command=fun9)
    nine.grid(row=0, column=2)
    six = Button(num, text="6", font="bold 35", bg="orange", fg="black", width=9, height=2, command=fun6)
    six.grid(row=1, column=2)
    three = Button(num, text="3", font="bold 35", bg="orange", fg="black", width=9, height=2, command=fun3)
    three.grid(row=2, column=2)
    # column 3
    equal = Button(num, text="Calculate", font="bold 35", bg="orange", fg="blue", width=9, height=2,command=GST)
    equal.grid(row=3, column=2)
    # Clear
    clear = Button(gst_frame, text="Clear Net\n Price", font="bold 30", bg="orange", fg="red", width=9, height=2,
                   command=fun_clear)
    clear.grid(row=0, column=2, sticky="w")


gst_frame=Frame(width=948,height=10,bg="white",relief="solid",bd=2)
gst_frame.grid(row=3,column=0,pady=10)

#Heading
heading=Label(text="GST CALCULATOR",font="bold 55"
              ,bg="yellow",fg="black",relief="solid",bd=5,width=25)
heading.grid(row=0,column=0,padx=5)
#original cost
original_cost=Label(text="Original Cost",font="bold 45",bg="pink",width=10
         ,fg="black",relief="solid",bd=5)
original_cost.grid(row=1,column=0,sticky="w",padx=1,pady=1)
#Net price
net_price=Label(text="Net Price",font="bold 45",bg="pink",width=10
         ,fg="black",relief="solid",bd=5)
net_price.grid(row=2,column=0,sticky="w",padx=1,pady=1)
#Original cost entry
oc_entry=Entry(bd=5,textvariable=original_cost_v,bg="pink",
               font="bold 45",relief="sunken",fg="black",width=20)
oc_entry.grid(row=1,column=0,sticky="e",pady=5)
#Net price entry box
np_entry=Entry(bd=5,textvariable=net_price_v,bg="pink",
               font="bold 45",relief="sunken",fg="black",width=20)
np_entry.grid(row=2,column=0,sticky="e",pady=5)
#GST label
gst=Label(gst_frame,bd=5,text="GST % ",bg="yellow",font="bold 56",relief="solid",
          fg="black",width=5)
gst.grid(row=0,column=0,sticky="w",)
# GST output
gst = Label(gst_frame, bg="pink", textvariable=gst_v, font="bold 56", width=7, relief="solid", bd=5)
gst.grid(row=0, column=1, sticky="w")

#keyboard 1 button
key1=Button(text="Keyboard",font="bold 15",command=keyboard1)
key1.grid(row=1,column=0,sticky="e")
#keyboard 2 button
key2=Button(text="Keyboard",font="bold 15",command=keyboard2)
key2.grid(row=2,column=0,sticky="e")

root.mainloop()


                                          #Question 2
from tkinter import *
import calendar
root=Tk()
root.title("Roshan's  Calender")
def print_calender():
    year_value=int(year.get())
    year_formatted=calendar.month(year_value,1)
    m1=Label(frame_2,text=year_formatted,font="bold 18",bg="orange",fg="black",relief="solid",bd=8,height=10)
    m1.grid(row=0,column=0,pady=10,padx=5)

    year_formatted=calendar.month(year_value,2)
    m2=Label(frame_2,text=year_formatted,font="bold 18",bg="orange",fg="black",relief="solid",bd=8,height=10)
    m2.grid(row=0,column=1,padx=5)

    year_formatted=calendar.month(year_value,3)
    m3=Label(frame_2,text=year_formatted,font="bold 18",bg="white",fg="black",relief="solid",bd=8,height=10)
    m3.grid(row=0,column=2,padx=5)

    year_formatted=calendar.month(year_value,4)
    m4=Label(frame_2,text=year_formatted,font="bold 18",bg="white",fg="black",relief="solid",bd=8,height=10)
    m4.grid(row=0,column=3,padx=5)

    year_formatted=calendar.month(year_value,5)
    m5=Label(frame_2,text=year_formatted,font="bold 18",bg="green",fg="black",relief="solid",bd=8,height=10)
    m5.grid(row=0,column=4,padx=5)

    year_formatted=calendar.month(year_value,6)
    m6=Label(frame_2,text=year_formatted,font="bold 18",bg="green",fg="black",relief="solid",bd=8,height=10)
    m6.grid(row=0,column=5,padx=5)

    year_formatted=calendar.month(year_value,7)
    m7=Label(frame_2,text=year_formatted,font="bold 18",bg="orange",fg="black",relief="solid",bd=8,height=10)
    m7.grid(row=1,column=0,padx=5)

    year_formatted=calendar.month(year_value,8)
    m8=Label(frame_2,text=year_formatted,font="bold 18",bg="orange",fg="black",relief="solid",bd=8,height=10)
    m8.grid(row=1,column=1,padx=5)

    year_formatted=calendar.month(year_value,9)
    m9=Label(frame_2,text=year_formatted,font="bold 18",bg="white",fg="black",relief="solid",bd=8,height=10)
    m9.grid(row=1,column=2,padx=5)

    year_formatted=calendar.month(year_value,10)
    m10=Label(frame_2,text=year_formatted,font="bold 18",bg="white",fg="black",relief="solid",bd=8,height=10)
    m10.grid(row=1,column=3,padx=5)

    year_formatted=calendar.month(year_value,11)
    m11=Label(frame_2,text=year_formatted,font="bold 18",bg="green",fg="black",relief="solid",bd=8,height=10)
    m11.grid(row=1,column=4,padx=5)

    year_formatted=calendar.month(year_value,12)
    m12=Label(frame_2,text=year_formatted,font="bold 18",bg="green",fg="black",relief="solid",bd=8,height=10)
    m12.grid(row=1,column=5,padx=5)

#fixing window size
root.geometry("1420x640")
root.minsize(width=1420, height=640)
root.maxsize(width=1420, height=640)

#frames
frame_1=Frame(width=100,height=70,bg="pink")
frame_1.pack(fill="x")
frame_2=Frame(height=710)
frame_2.pack(fill="x")
#welcome label
welcome=Label(frame_1,text="Welcome to CALENDER",font="bold 45",fg="black",bg="yellow",relief="solid",bd=4,)
welcome.grid(row=0,column=1)
#Variable
year=StringVar()
#Entry box and entry label
year_label=Label(frame_1,text="ENTER YEAR FOR THE CALENDER",font="bold 35",fg="black",bg="silver",relief="solid",bd=4,)
year_label.grid(row=1,column=0,sticky="w",pady=10,padx=10)
year_entry=Entry(frame_1,font="bold 35",fg="black",bg="silver",relief="sunken",bd=5,textvariable=year)
year_entry.grid(row=1,column=1,pady=10,sticky="w")
#Button
b1=Button(frame_1,text="ENTER",font="bold 45",fg="red",bg="silver",relief="solid",bd=3,command=print_calender)
b1.grid(row=1,column=2,sticky="w")




root.mainloop()


                                               #Question 3

from tkinter import *
from tkinter import ttk
root=Tk()
root.config(background="black")
root.title("Roshan's  Calculator")
#variable
input_given=StringVar()
output=StringVar()
#empty string
value=""
#Number functions
def fun1():
    global value
    value = value + "1"
    input_given.set(value)
def fun2():
    global value
    value = value + "2"
    input_given.set(value)
def fun3():
    global value
    value = value + "3"
    input_given.set(value)
def fun4():
    global value
    value = value + "4"
    input_given.set(value)
def fun5():
    global value
    value = value + "5"
    input_given.set(value)
def fun6():
    global value
    value = value + "6"
    input_given.set(value)
def fun7():
    global value
    value = value + "7"
    input_given.set(value)
def fun8():
    global value
    value = value + "8"
    input_given.set(value)
def fun9():
    global value
    value = value + "9"
    input_given.set(value)
def fun0():
    global value
    value = value + "0"
    input_given.set(value)
def fun_clear():
    global value
    value=""
    input_given.set(value)
#symbol functions
def fun_plus():
    global value
    value = value + " + "
    input_given.set(value)
def fun_multi():
    global value
    value = value + " X "
    input_given.set(value)
def fun_divide():
    global value
    value = value + " / "
    input_given.set(value)
def fun_minus():
    global value
    value = value + " - "
    input_given.set(value)
def fun_dot():
    global value
    value = value + "."
    input_given.set(value)
#calculating operation
def output_value():
    global value
    listv=value.split()
    listvc=listv.copy()
    if len(listv)>3:
        output.set("Enter two values only")
    elif len(listv)==3:
        n1 = listv[0]
        operation = listv[1]
        n2 = listv[2]
        c1=n1.isdigit() and n2.isdigit()
        if c1:
            if operation=="+":
                v=float(n1) + float(n2)
                output.set(f"{value} = {str(v)}")
            elif operation=="X":
                v=float(n1) * float(n2)
                output.set(f"{value} = {str(v)}")
            elif operation=="/":
                v=float(n1) / float(n2)
                output.set(f"{value} = {str(v)}")
            elif operation=="-":
                v=float(n1) - float(n2)
                output.set(f"{value} = {str(v)}")
        else:output.set("Error")
    else:
        output.set("Error")


#window size
root.geometry("948x568")
root.minsize(width=948,height=568)
root.maxsize(width=948,height=568)
#Frame in window
result=Frame(width=948,height=70,bg="blue",relief="sunken",bd=5)
result.pack(anchor="w")
num=Frame(width=948,height=350,bg="green",relief="solid",bd=5)
num.pack(anchor="w")
#creating number button
#column 0
seven=Button(num,text="7",font="bold 35",bg="orange",fg="black",width=9,height=2,command=fun7)
seven.grid(row=0,column=0)
four=Button(num,text="4",font="bold 35",bg="orange",fg="black",width=9,height=2,command=fun4)
four.grid(row=1,column=0)
one=Button(num,text="1",font="bold 35",bg="orange",fg="black",width=9,height=2,command=fun1)
one.grid(row=2,column=0)
zero=Button(num,text="0",font="bold 35",bg="orange",fg="black",width=9,height=2,command=fun0)
zero.grid(row=3,column=0)
#column 1
eight=Button(num,text="8",font="bold 35",bg="orange",fg="black",width=9,height=2,command=fun8)
eight.grid(row=0,column=1)
five=Button(num,text="5",font="bold 35",bg="orange",fg="black",width=9,height=2,command=fun5)
five.grid(row=1,column=1)
two=Button(num,text="2",font="bold 35",bg="orange",fg="black",width=9,height=2,command=fun2)
two.grid(row=2,column=1)
dot=Button(num,text=".",font="bold 35",bg="orange",fg="black",width=9,height=2,command=fun_dot)
dot.grid(row=3,column=1)
#column 2
nine=Button(num,text="9",font="bold 35",bg="orange",fg="black",width=9,height=2,command=fun9)
nine.grid(row=0,column=2)
six=Button(num,text="6",font="bold 35",bg="orange",fg="black",width=9,height=2,command=fun6)
six.grid(row=1,column=2)
three=Button(num,text="3",font="bold 35",bg="orange",fg="black",width=9,height=2,command=fun3)
three.grid(row=2,column=2)
divide=Button(num,text="/",font="bold 35",bg="orange",fg="red",width=9,height=2,command=fun_divide)
divide.grid(row=3,column=2)
#column 3
multiply=Button(num,text="X",font="bold 35",bg="orange",fg="red",width=9,height=2,command=fun_multi)
multiply.grid(row=0,column=3)
minus=Button(num,text="-",font="bold 35",bg="orange",fg="red",width=9,height=2,command=fun_minus)
minus.grid(row=1,column=3)
plus=Button(num,text="+",font="bold 35",bg="orange",fg="red",width=9,height=2,command=fun_plus)
plus.grid(row=2,column=3)
equal=Button(num,text="=",font="bold 35",bg="orange",fg="red",width=9,height=2,command=output_value)
equal.grid(row=3,column=3)

#add scroll bar
sb1_label=Label(result,text="Scroll bar",bg="yellow",fg="black",relief="solid",bd=3)
sb1_label.grid(row=2,sticky="w",padx=2,pady=3)
sb1=Scrollbar(result,orient="horizontal",bg="green",relief="solid",bd=3,width=17)
sb1.grid(row=2,sticky="w",padx=80,pady=2)

sb2=Scrollbar(result,orient="horizontal",bg="green",relief="solid",bd=3,width=17)
sb2.grid(row=2,sticky="w",padx=130,pady=2)
#type bar
type_space=Entry(result,width=37,bg="white",fg="black",font="bold 40",textvariable=input_given,xscrollcommand=sb1.set)
type_space.grid(row=0,column=0)
#clear button
clear=Button(result,text="CLEAR",font="bold 25",bg="orange",fg="Red",width=10,height=2,command=fun_clear)
clear.grid(row=1,column=0,sticky="e",padx=20,pady=5)
#Result space
result_space=Entry(result,width=31,bg="white",fg="black",font="bold 35",textvariable=output,xscrollcommand=sb2.set)
result_space.grid(row=1,column=0,sticky="w",padx=1)

sb2.config(command=result_space.xview)
sb1.config(command=type_space.xview)


root.mainloop()




                                             #Question 4

                                             

                                             #Question 5
print("Question 5\n")
#Que 5a

#Taking input from the user
list_input=list(map(int,input("Enter space separated integers:").split()))
#Defining sorting functions
def bubble_sort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
#printing sorted input
bubble_sort(list_input)
print(f"\nQue.5a\nThe Input list after sorting is: {list_input}")

#Que 5b
print("\nQue.5b")
#Defining binary search
def binary_search(list,search,l,u):
    global i
    m=(l+u)//2
    m_element=list[m]
    while l<=u:
        m = (l + u) // 2
        m_element = list[m]
        if m_element==search:
            return [True,list.index(search)]
        else:
            if m_element<search:
                l=m+1
            elif m_element>search:
                u=m-1
    return False,"random"
#Taking input of Integer to find
find=int(input("Enter number to search in list:"))
#Printing Output
if binary_search(list_input,find,0,len(list_input)-1)[0]:
    print(f"The integer {find} is present at Index "
          f"{binary_search(list_input,find,0,len(list_input)-1)[1]} in the list {list_input}")
else:
    print(f"Error\nInteger {find} is not present in the list")

#Que.5c
print("\nQue 5c\n")
count=0
for e in list_input:
    if e==find:
        count=count+1
print(f"Number of occurrences of {find} in the list is:{count}")






