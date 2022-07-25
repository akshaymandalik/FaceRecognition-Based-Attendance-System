import csv
from tkinter import *
import tkinter.messagebox as Mes
from tkinter import ttk
from PIL import ImageTk, Image
import cv2
import os
import numpy as np
import mysql.connector as Mysql
from playsound import playsound
import random
import pandas as pd
import datetime
import time

############################################# FUNCTIONS ################################################

def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)


##################################################################################

def tick():
    time_string = time.strftime('%H:%M:%S')
    time.clock.config(text=time_string)
    clock.after(200, tick)


###################################################################################

def contact():
    mess._show(title='Contact us', message="Please contact us on : 'shubhamkumar8180323@gmail.com' ")


###################################################################################

def check_haarcascadefile():
    exists = os.path.isfile("haarcascade_frontalface_default.xml")
    if exists:
        pass
    else:
        mess._show(title='Some file missing', message='Please contact us for help')
        window.destroy()


###################################################################################

def save_pass():
    assure_path_exists("TrainingImageLabel/")
    exists1 = os.path.isfile("TrainingImageLabel\psd.txt")
    if exists1:
        tf = open("TrainingImageLabel\psd.txt", "r")
        key = tf.read()
    else:
        master.destroy()
        new_pas = tsd.askstring('Old Password not found', 'Please enter a new password below', show='*')
        if new_pas == None:
            mess._show(title='No Password Entered', message='Password not set!! Please try again')
        else:
            tf = open("TrainingImageLabel\psd.txt", "w")
            tf.write(new_pas)
            mess._show(title='Password Registered', message='New password was registered successfully!!')
            return
    op = (old.get())
    newp = (new.get())
    nnewp = (nnew.get())
    if (op == key):
        if (newp == nnewp):
            txf = open("TrainingImageLabel\psd.txt", "w")
            txf.write(newp)
        else:
            mess._show(title='Error', message='Confirm new password again!!!')
            return
    else:
        mess._show(title='Wrong Password', message='Please enter correct old password.')
        return
    mess._show(title='Password Changed', message='Password changed successfully!!')
    master.destroy()


###################################################################################

def change_pass():
    global master
    master = tk.Tk()
    master.geometry("400x160")
    master.resizable(False, False)
    master.title("Change Password")
    master.configure(background="white")
    lbl4 = tk.Label(master, text='    Enter Old Password', bg='white', font=('times', 12, ' bold '))
    lbl4.place(x=10, y=10)
    global old
    old = tk.Entry(master, width=25, fg="black", relief='solid', font=('times', 12, ' bold '), show='*')
    old.place(x=180, y=10)
    lbl5 = tk.Label(master, text='   Enter New Password', bg='white', font=('times', 12, ' bold '))
    lbl5.place(x=10, y=45)
    global new
    new = tk.Entry(master, width=25, fg="black", relief='solid', font=('times', 12, ' bold '), show='*')
    new.place(x=180, y=45)
    lbl6 = tk.Label(master, text='Confirm New Password', bg='white', font=('times', 12, ' bold '))
    lbl6.place(x=10, y=80)
    global nnew
    nnew = tk.Entry(master, width=25, fg="black", relief='solid', font=('times', 12, ' bold '), show='*')
    nnew.place(x=180, y=80)
    cancel = tk.Button(master, text="Cancel", command=master.destroy, fg="black", bg="red", height=1, width=25,
                       activebackground="white", font=('times', 10, ' bold '))
    cancel.place(x=200, y=120)
    save1 = tk.Button(master, text="Save", command=save_pass, fg="black", bg="#3ece48", height=1, width=25,
                      activebackground="white", font=('times', 10, ' bold '))
    save1.place(x=10, y=120)
    master.mainloop()


#####################################################################################

def psw():
    assure_path_exists("TrainingImageLabel/")
    exists1 = os.path.isfile("TrainingImageLabel\psd.txt")
    if exists1:
        tf = open("TrainingImageLabel\psd.txt", "r")
        key = tf.read()
    else:
        new_pas = tsd.askstring('Old Password not found', 'Please enter a new password below', show='*')
        if new_pas == None:
            mess._show(title='No Password Entered', message='Password not set!! Please try again')
        else:
            tf = open("TrainingImageLabel\psd.txt", "w")
            tf.write(new_pas)
            mess._show(title='Password Registered', message='New password was registered successfully!!')
            return
    password = tsd.askstring('Password', 'Enter Password', show='*')
    if (password == key):
        TrainImages()
    elif (password == None):
        pass
    else:
        mess._show(title='Wrong Password', message='You have entered wrong password')


######################################################################################

def clear():
    txt.delete(0, 'end')
    res = "1)Take Images  >>>  2)Save Profile"
    message1.configure(text=res)


def clear2():
    txt2.delete(0, 'end')
    res = "1)Take Images  >>>  2)Save Profile"
    message1.configure(text=res)


#######################################################################################






























#############GUI##################################
#Window
root = Tk()
root.title('Registration Window')
root.geometry('1980x1024')
root.config(bg='white')
# Background Image
root.bg = ImageTk.PhotoImage(file='Images/bg.jpg')
background = Label(root, image=root.bg).place(x=250, y=0, relwidth=1, relheight=1)

# Attendance Image
root.left = ImageTk.PhotoImage(file='Images/leftbg.jpg')
left = Label(root, image=root.left).place(x=150, y=100, width=400, height=600)

#Frame
frame1 = Frame(root, bg="white")
frame1.place(x=550, y=100, width=800, height=600)
title = Label(frame1, text='FACULTY REGISTRATION', font=('poppins medium', 20, 'bold'), bg='white', fg='#2f3640').place(
    x=250, y=10)

# ===========================First Name
fname = Label(frame1, text='First Name', font=('poppins medium', 15, 'bold'), bg='white', fg='black').place(x=50, y=90)
root.txt_fname = Entry(frame1, font=('poppins medium', 14), bg='white', bd=1)
root.txt_fname.place(x=50, y=120, width='250')

# ===========================Last Name
lname = Label(frame1, text='Last Name', font=('poppins medium', 15, 'bold'), bg='white', fg='black').place(x=500, y=90)
root.txt_lname = Entry(frame1, font=('poppins medium', 14), bg='white', bd=1)
root.txt_lname.place(x=500, y=120, width='250')

# ===========================Contact
contact = Label(frame1, text='Contact No.', font=('poppins medium', 15, 'bold'), bg='white', fg='black').place(x=50,
                                                                                                               y=200)
root.txt_contact = Entry(frame1, font=('poppins medium', 14), bg='white', bd=1)
root.txt_contact.place(x=50, y=230, width='250')

# ===========================Enrollment
uid = Label(frame1, text='Id', font=('poppins medium', 15, 'bold'), bg='white', fg='black').place(
    x=500, y=200)
root.txt_uid = Entry(frame1, font=('poppins medium', 14), bg='white', bd=1)
root.txt_uid.place(x=500, y=230, width='250')

# ===========================Department
departments = ['', 'CM', 'CE', 'ME', 'IDFD']
department = Label(frame1, text='Department', font=('poppins medium', 15, 'bold'), bg='white', fg='black').place(x=50,
                                                                                                                 y=310)
root.deptcombo = ttk.Combobox(frame1, value=departments, font=('poppins medium', 13))
root.deptcombo.current(0)
root.deptcombo.place(x=50, y=340, width='250')

# ===========================Shift/Regular


# ==========================Buttons=============================

newwin = Button(root, text='View Records', font=('poppins medium', 15, 'bold'), bg="blue", fg='white', borderwidth=1,
                cursor='hand2').place(x=50, y=30, width=150)
Generateid = Button(frame1, text='Generate Id', font=('poppins medium', 15, 'bold'), bg='blue', fg='white',
                    borderwidth=1, cursor='hand2').place(x=500, y=330, width='250')

tkimages = Button(frame1, text='Take Sample Photo', font=('poppins medium', 15, 'bold'), bg='blue', fg='white',
                  borderwidth=1, cursor='hand2').place(x=50, y=420, width=250)

train = Button(frame1, text='Train System', font=('poppins medium', 15, 'bold'), bg='blue', fg='white', borderwidth=1,
               cursor='hand2').place(x=500, y=420, width=250)

submit = Button(frame1, text='Submit', font=('poppins medium', 15, 'bold'), bg="blue", fg='white', borderwidth=1,
                cursor='hand2').place(x=50, y=500, width=250)

update = Button(frame1, text='Update', font=('poppins medium', 15, 'bold'), bg="blue", fg='white', borderwidth=1,
                cursor='hand2').place(x=500, y=500, width=250)
root.mainloop()

