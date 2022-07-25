# Author: Akshay Haribhau Mandalik
# Last Updated: 13/07/2022
############################################# IMPORTING ################################################

# Install all these libraries:
# For CV2: install opencv-config-python library.
import random
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mess
import tkinter.simpledialog as tsd
import cv2
import os
import csv
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time
from playsound import playsound
import pywhatkit

############################################# FUNCTIONS ################################################


def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)


##################################################################################

def tick():
    time_string = time.strftime('%H:%M:%S')
    clock.config(text=time_string)
    clock.after(200, tick)


###################################################################################

def contact():
    mess._show(title='Contact us',
               message="Please contact us on : 'akshaymandalik829@gmail.com' 'pritam.deore2273@gmail.com'")


###################################################################################

def check_haarcascadefile():
    exists = os.path.isfile("haarcascade_frontalface_default.xml")
    if exists:
        pass
    else:
        mess._show(title='Some file missing',
                   message='Please contact us for help')
        root.destroy()


###################################################################################

def save_pass():
    assure_path_exists("TrainingImageLabel/")
    exists1 = os.path.isfile("TrainingImageLabel\psd.txt")
    if exists1:
        tf = open("TrainingImageLabel\psd.txt", "r")
        key = tf.read()
    else:
        master.destroy()
        new_pas = tsd.askstring('Old Password not found',
                                'Please enter a new password below', show='*')
        if new_pas == None:
            mess._show(title='No Password Entered',
                       message='Password not set!! Please try again')
        else:
            tf = open("TrainingImageLabel\psd.txt", "w")
            tf.write(new_pas)
            mess._show(title='Password Registered',
                       message='New password was registered successfully!!')
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
        mess._show(title='Wrong Password',
                   message='Please enter correct old password.')
        return
    mess._show(title='Password Changed',
               message='Password changed successfully!!')
    master.destroy()


###################################################################################

def change_pass():
    global master
    master = Tk()
    master.geometry("500x160")
    master.resizable(False, False)
    master.title("Change Password")
    master.configure(background="white")
    lbl4 = Label(master, text='    Enter Old Password',
                 bg='white', font=('times', 12, ' bold '))
    lbl4.place(x=10, y=10)
    global old
    old = Entry(master, width=25, fg="black", relief='solid',
                font=('times', 12, ' bold '), show='*')
    old.place(x=220, y=10)
    lbl5 = Label(master, text='   Enter New Password',
                 bg='white', font=('times', 12, ' bold '))
    lbl5.place(x=10, y=45)
    global new
    new = Entry(master, width=25, fg="black", relief='solid',
                font=('times', 12, ' bold '), show='*')
    new.place(x=220, y=45)
    lbl6 = Label(master, text='Confirm New Password',
                 bg='white', font=('times', 12, ' bold '))
    lbl6.place(x=10, y=80)
    global nnew
    nnew = Entry(master, width=25, fg="black", relief='solid',
                 font=('times', 12, ' bold '), show='*')
    nnew.place(x=220, y=80)
    cancel = Button(master, text="Cancel", command=master.destroy, fg="black", bg="red", height=1, width=25,
                    activebackground="white", font=('times', 10, ' bold '))
    cancel.place(x=200, y=120)
    save1 = Button(master, text="Save", command=save_pass, fg="black", bg="#3ece48", height=1, width=25,
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
        new_pas = tsd.askstring('Old Password not found',
                                'Please enter a new password below', show='*')
        if new_pas == None:
            mess._show(title='No Password Entered',
                       message='Password not set!! Please try again')
        else:
            tf = open("TrainingImageLabel\psd.txt", "w")
            tf.write(new_pas)
            mess._show(title='Password Registered',
                       message='New password was registered successfully!!')
            return
    password = tsd.askstring('Password', 'Enter Password', show='*')
    if (password == key):
        TrainImages()
    elif (password == None):
        pass
    else:
        mess._show(title='Wrong Password',
                   message='You have entered wrong password')


######################################################################################
def Generate_id():
    dept = root.deptcombo.get()
    root.txt_uid.delete(0, END)
    if dept == '':
        playsound('VoiceCommands/firstdepartment.mp3')
    else:
        ran = random.randint(2000, 2100)
        genrated_id = dept + str(ran)
        root.txt_uid.insert(0, genrated_id)


#######################################################################################

def TakeImages():
    first_name = txt.get()
    last_name = txt2.get()
    contac = root.txt_contact.get()
    u_id = root.txt_uid.get()
    dept = root.deptcombo.get()
    print(first_name, last_name, contac, u_id, dept)

    check_haarcascadefile()
    columns = ['SERIAL NO.', '', 'First Name', '', 'Last Name',
               '', 'Contact No.', '', 'UId', '', 'Department']
    assure_path_exists("FacultyDetails/")
    assure_path_exists("TrainingImage/")
    serial = 0
    exists = os.path.isfile("FacultyDetails\FacultyDetails.csv")
    if exists:
        with open("FacultyDetails\FacultyDetails.csv", 'r') as csvFile1:
            reader1 = csv.reader(csvFile1)
            for l in reader1:
                serial = serial + 1
        serial = (serial // 2)
        csvFile1.close()
    else:
        with open("FacultyDetails\FacultyDetails.csv", 'a+') as csvFile1:
            writer = csv.writer(csvFile1)
            writer.writerow(columns)
            serial = 1
        csvFile1.close()

    if first_name == '' or last_name == '' or contac == '' or u_id == '' or dept == '':
        playsound('VoiceCommands/Fill All Fields.mp3')
    else:
        cam = cv2.VideoCapture(0)
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0
        while (True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                # incrementing sample number
                sampleNum = sampleNum + 1
                # saving the captured face in the dataset folder TrainingImage
                cv2.imwrite(
                    "TrainingImage\ " + first_name + "" + last_name + "." + str(serial) + "." + u_id + '.' + str(
                        sampleNum) + ".jpg",
                    gray[y:y + h, x:x + w])
                # display the frame
                cv2.imshow('Taking Images', img)
                # wait for 100 miliseconds
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            # break if the sample number is morethan 100
            elif sampleNum > 100:
                break
        cam.release()
        playsound('VoiceCommands/samplephotos.mp3')
        cv2.destroyAllWindows()
        row = [serial, '', first_name, '', last_name,
               '', contac, '', u_id, '', dept]
        with open('FacultyDetails\FacultyDetails.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()


########################################################################################

def TrainImages():
    first_name = txt.get()
    contac = root.txt_contact.get()
    hrs = int(time.strftime("%H"))
    min = int(time.strftime("%M"))

    check_haarcascadefile()
    assure_path_exists("TrainingImageLabel/")
    recognizer = cv2.face_LBPHFaceRecognizer.create()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(harcascadePath)
    faces, ID = getImagesAndLabels("TrainingImage")
    try:
        recognizer.train(faces, np.array(ID))
    except:
        playsound('VoiceCommands/NotTrained.mp3')
        return
    recognizer.save("TrainingImageLabel\Trainner.yml")
    playsound('VoiceCommands/train.mp3')
    # pywhatkit.sendwhatmsg("+91"+contac,first_name+" Your registration to the Face recognition System is done! Thanks for you cooperation",hrs,min+2)


# 3

def getImagesAndLabels(path):
    # get the path of all the files in the folder
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    # create empth face list
    faces = []
    # create empty ID list
    Ids = []
    # now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:
        # loading the image and converting it to gray scale
        pilImage = Image.open(imagePath).convert('L')
        # Now we are converting the PIL image into numpy array
        imageNp = np.array(pilImage, 'uint8')
        # getting the Id from the image
        ID = int(os.path.split(imagePath)[-1].split(".")[1])
        # extract the face from the training image sample
        faces.append(imageNp)
        Ids.append(ID)
    return faces, Ids


###########################################################################################


######################################## USED STUFFS ############################################

global key
key = ''

ts = time.time()
date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
day, month, year = date.split("-")

mont = {'01': 'January',
        '02': 'February',
        '03': 'March',
        '04': 'April',
        '05': 'May',
        '06': 'June',
        '07': 'July',
        '08': 'August',
        '09': 'September',
        '10': 'October',
        '11': 'November',
        '12': 'December'
        }

######################################## GUI FRONT-END ###########################################
root = Tk()
root.title('Face Recognition Based Attendance System')
root.geometry('1980x1024')
root.config(bg='white')
# Background Image
root.bg = ImageTk.PhotoImage(file='Images/bg.jpg')
background = Label(root, image=root.bg).place(
    x=250, y=0, relwidth=1, relheight=1)
# Attendance Image
root.left = ImageTk.PhotoImage(file='Images/leftbg.jpg')
left = Label(root, image=root.left).place(x=150, y=150, width=400, height=600)

# root = tk.Tk()
# root.geometry("1280x720")
# root.resizable(True, False)
# root.title("Attendance System")
# root.configure(background='#262523')

frame2 = Frame(root, bg="white")
frame2.place(x=550, y=150, width=875, height=600)

# message3 = Label(root, text="Face Recognition Based Attendance System", fg="#262523", width=55,
#                  height=1, font=('times', 29, ' bold '))
# message3.place(x=150, y=10)

frame3 = Frame(root, bg="#c4c6ce")
frame3.place(x=900, y=50, relwidth=0.09, relheight=0.07)

frame4 = tk.Frame(root, bg="#c4c6ce")
frame4.place(x=600, y=50, relwidth=0.16, relheight=0.07)

datef = Label(frame4, text=day + "-" + mont[month] + "-" + year + "  |  ", fg="black", bg="white", width=55,
              height=1, font=('times', 22, ' bold '))
datef.pack(fill='both', expand=1)

clock = Label(frame3, fg="black", bg="white", width=55,
              height=1, font=('times', 22, ' bold '))
clock.pack(fill='both', expand=1)
tick()

head2 = Label(frame2, text='FACULTY REGISTRATION', font=('poppins medium', 20, 'bold'), bg='white', fg='#2f3640').place(
    x=250, y=10)
# First Name
lbl = Label(frame2, text='First Name', font=('poppins medium',
            15, 'bold'), bg='white', fg='black').place(x=50, y=90)
txt = Entry(frame2, font=('poppins medium', 14), bg='white', bd=1)
txt.place(x=50, y=120, width='250')
# Last Name
lbl2 = Label(frame2, text='Last Name', font=('poppins medium', 15,
             'bold'), bg='white', fg='black').place(x=500, y=90)
txt2 = Entry(frame2, font=('poppins medium', 14), bg='white', bd=1)
txt2.place(x=500, y=120, width='250')

# ===========================Contact
contact = Label(frame2, text='Contact No.', font=('poppins medium', 15, 'bold'), bg='white', fg='black').place(x=50,
                                                                                                               y=200)
root.txt_contact = Entry(frame2, font=('poppins medium', 14), bg='white', bd=1)
root.txt_contact.place(x=50, y=230, width='250')

# ===========================Enrollment
uid = Label(frame2, text='Id', font=('poppins medium', 15, 'bold'), bg='white', fg='black').place(
    x=500, y=200)
root.txt_uid = Entry(frame2, font=('poppins medium', 14), bg='white', bd=1)
root.txt_uid.place(x=500, y=230, width='250')

# ===========================Department
departments = ['', 'CM', 'CE', 'ME', 'IDFD']
department = Label(frame2, text='Department', font=('poppins medium', 15, 'bold'), bg='white', fg='black').place(x=330,
                                                                                                                 y=310)
root.deptcombo = ttk.Combobox(
    frame2, value=departments, font=('poppins medium', 13))
root.deptcombo.current(0)
root.deptcombo.place(x=290, y=340, width='250')

res = 0
exists = os.path.isfile("FacultyDetails\FacultyDetails.csv")
if exists:
    with open("FacultyDetails\FacultyDetails.csv", 'r') as csvFile1:
        reader1 = csv.reader(csvFile1)
        for l in reader1:
            res = res + 1
    res = (res // 2) - 1
    csvFile1.close()
else:
    res = 0


# Take Attendance
def takeAttendance():
    root1 = tk.Tk()
    root1.geometry("1280x720")
    root1.resizable(True, False)
    root1.title("Attendance System")
    root1.configure(background='#262523')
    frame1 = Frame(root1, bg="white")
    frame1.place(x=350, y=100, width=500, height=500)

    ################## TREEVIEW ATTENDANCE TABLE ####################

    tv = ttk.Treeview(frame1, height=13, columns=('name', 'date', 'time'))
    tv.column('#0', width=82)
    tv.column('name', width=130)
    tv.column('date', width=133)
    tv.column('time', width=133)
    tv.grid(row=2, column=0, padx=(0, 0), pady=(150, 0), columnspan=4)
    tv.heading('#0', text='ID')
    tv.heading('name', text='NAME')
    tv.heading('date', text='DATE')
    tv.heading('time', text='TIME')

    ###################### SCROLLBAR ################################

    scroll = ttk.Scrollbar(frame1, orient='vertical', command=tv.yview)
    scroll.grid(row=2, column=4, padx=(0, 100), pady=(150, 0), sticky='ns')
    tv.configure(yscrollcommand=scroll.set)

    def TrackImages():
        check_haarcascadefile()
        assure_path_exists("Attendance/")
        assure_path_exists("FacultyDetails/")
        for k in tv.get_children():
            tv.delete(k)
        msg = ''
        i = 0
        j = 0
        df = None
        attendance = []
        recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
        exists3 = os.path.isfile("TrainingImageLabel\Trainner.yml")
        if exists3:
            recognizer.read("TrainingImageLabel\Trainner.yml")
        else:
            mess._show(title='Data Missing',
                       message='System is not trained yet!')
            return
        harcascadePath = "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(harcascadePath)

        cam = cv2.VideoCapture(0)
        font = cv2.FONT_HERSHEY_SIMPLEX
        col_names = ['Id', '', 'Name', '', 'Date', '', 'Time']
        exists1 = os.path.isfile("FacultyDetails\FacultyDetails.csv")
        if exists1:
            df = pd.read_csv("FacultyDetails\FacultyDetails.csv")
        else:
            mess._show(title='Details Missing',
                       message='Students details are missing, please check!')
            cam.release()
            cv2.destroyAllWindows()
            root.destroy()
        while True:
            ret, im = cam.read()
            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gray, 1.2, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
                serial, conf = recognizer.predict(gray[y:y + h, x:x + w])
                if (conf < 50):
                    ts = time.time()
                    date = datetime.datetime.fromtimestamp(
                        ts).strftime('%d-%m-%Y')
                    timeStamp = datetime.datetime.fromtimestamp(
                        ts).strftime('%H:%M:%S')
                    aa = df.loc[df['SERIAL NO.'] ==
                                serial]['First Name'].values
                    ID = df.loc[df['SERIAL NO.'] == serial]['UId'].values
                    ID = str(ID)
                    ID = ID[1:-1]
                    bb = str(aa)
                    bb = bb[2:-2]
                    attendance = [str(ID), '', bb, '', str(
                        date), '', str(timeStamp)]

                else:
                    Id = 'Unknown'
                    bb = str(Id)
                cv2.putText(im, str(bb), (x, y + h),
                            font, 1, (255, 255, 255), 2)
            cv2.imshow('Taking Attendance', im)
            if cv2.waitKey(1) == ord('q'):
                break
        ts = time.time()
        date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
        exists = os.path.isfile("Attendance\Attendance_" + date + ".csv")
        if exists:
            with open("Attendance\Attendance_" + date + ".csv", 'a+') as csvFile1:
                writer = csv.writer(csvFile1)
                writer.writerow(attendance)
            csvFile1.close()
        else:
            with open("Attendance\Attendance_" + date + ".csv", 'a+') as csvFile1:
                writer = csv.writer(csvFile1)
                writer.writerow(col_names)
                writer.writerow(attendance)
            csvFile1.close()
        with open("Attendance\Attendance_" + date + ".csv", 'r') as csvFile1:
            reader1 = csv.reader(csvFile1)
            for lines in reader1:
                i = i + 1
                if (i > 1):
                    if (i % 2 != 0):
                        iidd = str(lines[0]) + '   '
                        tv.insert('', 0, text=iidd, values=(
                            str(lines[2]), str(lines[4]), str(lines[6])))
        csvFile1.close()
        cam.release()
        cv2.destroyAllWindows()

    head1 = tk.Label(frame1, text="                       For Already Registered                       ",
                     fg="black",
                     bg="#3ece48", font=('times', 17, ' bold '))
    head1.place(x=0, y=0)

    lbl3 = tk.Label(frame1, text="Attendance", width=20, fg="black", bg="#00aeff", height=1,
                    font=('times', 17, ' bold '))
    lbl3.place(x=100, y=115)

    ######################Buttons##########################################

    trackImg = tk.Button(frame1, text="Take Attendance", command=TrackImages, fg="black", bg="yellow", width=25,
                         height=1,
                         activebackground="white", font=('times', 15, ' bold '))
    trackImg.place(x=60, y=50)
    quitroot = tk.Button(frame1, text="Quit", command=root1.destroy, fg="black", bg="red", width=25, height=1,
                         activebackground="white", font=('times', 15, ' bold '))
    quitroot.place(x=60, y=450)
    root.mainloop()


##################### MENUBAR #################################

menubar = tk.Menu(root, relief='ridge')
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label='Change Password', command=change_pass)
filemenu.add_command(label='Exit', command=root.destroy)
menubar.add_cascade(label='Help', font=('times', 29, ' bold '), menu=filemenu)

###################### BUTTONS ##################################


takeImg = Button(frame2, text='Take Sample Photo', font=('poppins medium', 15, 'bold'), bg='blue', fg='white',
                 borderwidth=1, cursor='hand2', command=TakeImages).place(x=50, y=420, width=250)

trainImg = Button(frame2, text="Save Profile", command=psw, font=('poppins medium', 15, 'bold'), bg="blue", fg='white',
                  borderwidth=1,
                  cursor='hand2').place(x=50, y=500, width=250)

Generateid = Button(frame2, text='Generate Id', font=('poppins medium', 15, 'bold'), bg='blue', fg='white',
                    borderwidth=1, cursor='hand2', command=Generate_id).place(x=500, y=420, width='250')

attend = Button(frame2, text="Attendance", command=takeAttendance, font=('poppins medium', 15, 'bold'), bg='blue',
                fg='white', borderwidth=1,
                cursor='hand2').place(x=500, y=500, width=250)

##################### END ######################################

root.configure(menu=menubar)
root.mainloop()

####################################################################################################
