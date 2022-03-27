import tkinter as tk
from PIL import ImageTk, Image
from time import sleep
import pickle
from os.path import exists

row = 0

# Memorize the button state
buttonstatedaily = [False, False, False, False, False, False, False, False, False, False]
buttonstateweekly = [False, False, False, False, False, False, False, False, False, False]


def checkboxactdeact1(event=None):
    if button['image'] == 'pyimage18':
        if dailybutton['image'] == 'pyimage11':
            buttonstatedaily[0] = False
            imagereturndaily()
        if dailybutton['image'] == 'pyimage10':
            buttonstateweekly[0] = False
        button.config(image=checkboximageoff)
        text1['fg'] = '#93384f'
    else:
        button.config(image=checkboximageon)
        text1['fg'] = '#75d351'
        if dailybutton['image'] == 'pyimage11':
            buttonstatedaily[0] = True
        if dailybutton['image'] == 'pyimage10':
            buttonstateweekly[0] = True
    root.update()


def checkboxactdeact2(event=None):
    if button2['image'] == 'pyimage18':
        if dailybutton['image'] == 'pyimage11':
            buttonstatedaily[1] = False
            imagereturndaily()
        if dailybutton['image'] == 'pyimage10':
            buttonstateweekly[1] = False
        button2.config(image=checkboximageoff)
        text2['fg'] = '#93384f'
    else:
        button2.config(image=checkboximageon)
        text2['fg'] = '#75d351'
        if dailybutton['image'] == 'pyimage11':
            buttonstatedaily[1] = True
        if dailybutton['image'] == 'pyimage10':
            buttonstateweekly[1] = True
    root.update()


def checkboxactdeact3(event=None):
    if button3['image'] == 'pyimage18':
        if dailybutton['image'] == 'pyimage11':
            buttonstatedaily[2] = False
            imagereturndaily()
        if dailybutton['image'] == 'pyimage10':
            buttonstateweekly[2] = False
        button3.config(image=checkboximageoff)
        text3['fg'] = '#93384f'
    else:
        button3.config(image=checkboximageon)
        text3['fg'] = '#75d351'
        if dailybutton['image'] == 'pyimage11':
            buttonstatedaily[2] = True
        if dailybutton['image'] == 'pyimage10':
            buttonstateweekly[2] = True
    root.update()


def checkboxactdeact4(event=None):
    if button4['image'] == 'pyimage18':
        if dailybutton['image'] == 'pyimage11':
            buttonstatedaily[3] = False
            imagereturndaily()
        if dailybutton['image'] == 'pyimage10':
            buttonstateweekly[3] = False
        button4.config(image=checkboximageoff)
        text4['fg'] = '#93384f'
    else:
        button4.config(image=checkboximageon)
        text4['fg'] = '#75d351'
        if dailybutton['image'] == 'pyimage11':
            buttonstatedaily[3] = True
        if dailybutton['image'] == 'pyimage10':
            buttonstateweekly[3] = True
    root.update()


def checkboxactdeact5(event=None):
    if button5['image'] == 'pyimage18':
        if dailybutton['image'] == 'pyimage11':
            buttonstatedaily[4] = False
            imagereturndaily()
        if dailybutton['image'] == 'pyimage10':
            buttonstateweekly[4] = False
        button5.config(image=checkboximageoff)
        text5['fg'] = '#93384f'
    else:
        button5.config(image=checkboximageon)
        text5['fg'] = '#75d351'
        if dailybutton['image'] == 'pyimage11':
            buttonstatedaily[4] = True
        if dailybutton['image'] == 'pyimage10':
            buttonstateweekly[4] = True
    root.update()


def checkboxactdeact6(event=None):
    if button6['image'] == 'pyimage18':
        if dailybutton['image'] == 'pyimage11':
            buttonstatedaily[5] = False
            imagereturndaily()
        if dailybutton['image'] == 'pyimage10':
            buttonstateweekly[5] = False
        button6.config(image=checkboximageoff)
        text6['fg'] = '#93384f'
    else:
        button6.config(image=checkboximageon)
        text6['fg'] = '#75d351'
        if dailybutton['image'] == 'pyimage11':
            buttonstatedaily[5] = True
        if dailybutton['image'] == 'pyimage10':
            buttonstateweekly[5] = True
    root.update()


def checkboxactdeact7(event=None):
    if button7['image'] == 'pyimage18':
        if dailybutton['image'] == 'pyimage11':
            buttonstatedaily[6] = False
            imagereturndaily()
        if dailybutton['image'] == 'pyimage10':
            buttonstateweekly[6] = False
        button7.config(image=checkboximageoff)
        text7['fg'] = '#93384f'
    else:
        button7.config(image=checkboximageon)
        text7['fg'] = '#75d351'
        if dailybutton['image'] == 'pyimage11':
            buttonstatedaily[6] = True
        if dailybutton['image'] == 'pyimage10':
            buttonstateweekly[6] = True
    root.update()


def checkboxactdeact8(event=None):
    if button8['image'] == 'pyimage18':
        if dailybutton['image'] == 'pyimage11':
            buttonstatedaily[7] = False
            imagereturndaily()
        if dailybutton['image'] == 'pyimage10':
            buttonstateweekly[7] = False
        button8.config(image=checkboximageoff)
        text8['fg'] = '#93384f'
    else:
        button8.config(image=checkboximageon)
        text8['fg'] = '#75d351'
        if dailybutton['image'] == 'pyimage11':
            buttonstatedaily[7] = True
        if dailybutton['image'] == 'pyimage10':
            buttonstateweekly[7] = True
    root.update()


def checkboxactdeact9(event=None):
    if button9['image'] == 'pyimage18':
        if dailybutton['image'] == 'pyimage11':
            buttonstatedaily[8] = False
            imagereturndaily()
        if dailybutton['image'] == 'pyimage10':
            buttonstateweekly[8] = False
        button9.config(image=checkboximageoff)
        text9['fg'] = '#93384f'
    else:
        button9.config(image=checkboximageon)
        text9['fg'] = '#75d351'
        if dailybutton['image'] == 'pyimage11':
            buttonstatedaily[8] = True
        if dailybutton['image'] == 'pyimage10':
            buttonstateweekly[8] = True
    root.update()


def checkboxactdeact10(event=None):
    if button10['image'] == 'pyimage18':
        if dailybutton['image'] == 'pyimage11':
            buttonstatedaily[9] = False
            imagereturndaily()
        if dailybutton['image'] == 'pyimage10':
            buttonstateweekly[9] = False
        button10.config(image=checkboximageoff)
        text10['fg'] = '#93384f'
    else:
        button10.config(image=checkboximageon)
        text10['fg'] = '#75d351'
        if dailybutton['image'] == 'pyimage11':
            buttonstatedaily[9] = True
        if dailybutton['image'] == 'pyimage10':
            buttonstateweekly[9] = True
    print(buttonstatedaily)
    root.update()


def rollover(event=None):
    if dailybutton['image'] == 'pyimage11':
        for c in range(0, len(buttons)):
            buttonstatedaily[c] = False
        imagereturndaily()
    if dailybutton['image'] == 'pyimage10':
        for c in range(0, len(buttons)):
            buttonstateweekly[c] = False
        imagereturnweekly()
    resetbutton['image'] = logoreset2
    root.update()
    sleep(0.1)
    resetbutton['image'] = logoreset


def weekly(event=None):
    imagereturnweekly()
    weeklybutton['image'] = buttonweeklypressed
    dailybutton['image'] = buttondaily
    text1['text'] = 'Weekly Task 1'
    logo_label['image'] = logoweekly
    text2['text'] = 'Weekly Task 2'
    logo_label2['image'] = logoweekly
    text3['text'] = 'Weekly Task 3'
    logo_label3['image'] = logoweekly
    text4['text'] = 'Abysses'
    logo_label4['image'] = logoabyssdg
    text5['text'] = 'Abyss Raid Argos'
    logo_label5['image'] = logoargos
    text6['text'], text6['font'] = 'Sylmael Bloodstone', ("Raleway", 26)
    logo_label6['image'] = logobloodstone
    text7['text'] = 'Pirate Vendor'
    logo_label7['image'] = logoslaves
    text8['text'], text8['font'] = 'Chaos Dungeon Vendor', ("Raleway", 25)
    logo_label8['image'] = logochaos
    text9['text'] = 'Ghostship'
    logo_label9['image'] = logoghost
    text10['text'] = 'Tickets'
    logo_label10['image'] = logotickets


def daily(event=None):
    imagereturndaily()
    dailybutton['image'] = buttondailypressed
    weeklybutton['image'] = buttonweekly
    text1['text'] = "Una's Task 1"
    logo_label['image'] = logouna
    text2['text'] = "Una's Task 2"
    logo_label2['image'] = logouna
    text3['text'] = "Una's Task 3"
    logo_label3['image'] = logouna
    text4['text'] = 'Chaos Dungeon 1'
    logo_label4['image'] = logochaos
    text5['text'] = 'Chaos Dungeon 2'
    logo_label5['image'] = logochaos
    text6['text'], text6['font'] = 'Guardian Raid 1', ("Raleway", 28)
    logo_label6['image'] = logoguardian
    text7['text'] = 'Guardian Raid 2'
    logo_label7['image'] = logoguardian
    text8['text'], text8['font'] = 'Kalthertz Slaves', ("Raleway", 28)
    logo_label8['image'] = logoslaves
    text9['text'] = 'Guild Donation'
    logo_label9['image'] = logosguild
    text10['text'] = 'Guild Research Support'
    logo_label10['image'] = logosguild


def imagereturndaily(event=None):
    for c in range(0, len(buttons)):
        if buttonstatedaily[c] == False:
            buttons[c]['image'] = checkboximageoff
            texts[c]['fg'] = '#93384f'
        else:
            buttons[c]['image'] = checkboximageon
            texts[c]['fg'] = '#75d351'


def imagereturnweekly(event=None):
    for c in range(0, len(buttons)):
        if buttonstateweekly[c] == False:
            buttons[c]['image'] = checkboximageoff
            texts[c]['fg'] = '#93384f'
        else:
            buttons[c]['image'] = checkboximageon
            texts[c]['fg'] = '#75d351'


def on_closing():
    with open("save", "wb") as fp:
        pickle.dump(buttonstatedaily, fp)
    with open("weekly", "wb") as fp:
        pickle.dump(buttonstateweekly, fp)
    root.destroy()


def on_init():
    global buttonstatedaily, buttonstateweekly
    if exists("save"):
        with open("save", "rb") as fp:  # Unpickling
            buttonstatedaily = pickle.load(fp)
    else:
        with open("save", "wb") as fp:
            pickle.dump(buttonstatedaily, fp)
    if exists("weekly"):
        with open("weekly", "rb") as fp:  # Unpickling
            buttonstateweekly = pickle.load(fp)
    else:
        with open("weekly", "wb") as fp:
            pickle.dump(buttonstateweekly, fp)

# Window setup
root = tk.Tk()
root.geometry("700x760")
root.configure(bg='#2a303c')
root.resizable(False, False)
root.iconbitmap('Logo\\Unastask.ico')
root.title('Lost Ark Dailies')
on_init()

# Configure columns
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=4)
root.columnconfigure(2, weight=1)

# Set canvas size and the number of rows and columns
canvas = tk.Canvas(root, width=1000, height=600)
canvas.grid(columnspan=3, row=11)

# List of functions
functions = [checkboxactdeact1, checkboxactdeact2, checkboxactdeact3, checkboxactdeact4, checkboxactdeact5,
             checkboxactdeact6, checkboxactdeact7, checkboxactdeact8, checkboxactdeact9, checkboxactdeact10]

# Images
logouna = Image.open('Logo\\Unastask.png')
logouna = ImageTk.PhotoImage(logouna)
logochaos = Image.open('Logo\\Chaosdg.png')
logochaos = ImageTk.PhotoImage(logochaos)
logoguardian = Image.open('Logo\\Guardianraid.png')
logoguardian = ImageTk.PhotoImage(logoguardian)
logoslaves = Image.open('Logo\\Piratecoin.png')
logoslaves = ImageTk.PhotoImage(logoslaves)
logosguild = Image.open('Logo\\Guildhonor.png')
logosguild = ImageTk.PhotoImage(logosguild.resize((64, 64)))
logoreset = Image.open('Logo\\Reset.png')
logoreset = ImageTk.PhotoImage(logoreset.resize((64, 68)))
logoreset2 = Image.open('Logo\\Reset2.png')
logoreset2 = ImageTk.PhotoImage(logoreset2.resize((64, 68)))
buttonweekly = Image.open('Logo\\buttontab.png')
buttonweekly = ImageTk.PhotoImage(buttonweekly.resize((100, 50)))
buttonweeklypressed = Image.open('Logo\\buttontabpressed.png')
buttonweeklypressed = ImageTk.PhotoImage(buttonweeklypressed.resize((100, 50)))
buttondaily = Image.open('Logo\\buttontab2.png')
buttondaily = ImageTk.PhotoImage(buttondaily.resize((100, 50)))
buttondailypressed = Image.open('Logo\\buttontab2pressed.png')
buttondailypressed = ImageTk.PhotoImage(buttondailypressed.resize((100, 50)))
logoweekly = Image.open('Logo\\weekly.png')
logoweekly = ImageTk.PhotoImage(logoweekly)
logoabyssdg = Image.open('Logo\\Abyssdg.png')
logoabyssdg = ImageTk.PhotoImage(logoabyssdg)
logobloodstone = Image.open('Logo\\Bloodstone.png')
logobloodstone = ImageTk.PhotoImage(logobloodstone)
logoghost = Image.open('Logo\\Ghostship.png')
logoghost = ImageTk.PhotoImage(logoghost)
logoargos = Image.open('Logo\\Argos.png')
logoargos = ImageTk.PhotoImage(logoargos)
logotickets = Image.open('Logo\\Tickets.png')
logotickets = ImageTk.PhotoImage(logotickets)
checkboximageon = Image.open('Logo\\On.png')
checkboximageon = ImageTk.PhotoImage(checkboximageon.resize((138, 60)))
checkboximageoff = Image.open('Logo\\Off.png')
checkboximageoff = ImageTk.PhotoImage(checkboximageoff.resize((138, 60)))

# Creating texts
text1 = tk.Label(root, text="Una's Task 1", font=("Raleway", 28), bg='#2a303c', fg='#93384f')
text2 = tk.Label(root, text="Una's Task 2", font=("Raleway", 28), bg='#2a303c', fg='#93384f')
text3 = tk.Label(root, text="Una's Task 3", font=("Raleway", 28), bg='#2a303c', fg='#93384f')
text4 = tk.Label(root, text="Chaos Dungeon 1", font=("Raleway", 28), bg='#2a303c', fg='#93384f')
text5 = tk.Label(root, text="Chaos Dungeon 2", font=("Raleway", 28), bg='#2a303c', fg='#93384f')
text6 = tk.Label(root, text="Guardian Raid 1", font=("Raleway", 28), bg='#2a303c', fg='#93384f')
text7 = tk.Label(root, text="Guardian Raid 2", font=("Raleway", 28), bg='#2a303c', fg='#93384f')
text8 = tk.Label(root, text="Kalthertz Slaves", font=("Raleway", 28), bg='#2a303c', fg='#93384f')
text9 = tk.Label(root, text="Guild Donation", font=("Raleway", 28), bg='#2a303c', fg='#93384f')
text10 = tk.Label(root, text="Guild Research Support", font=("Raleway", 28), bg='#2a303c', fg='#93384f')
texts = [text1, text2, text3, text4, text5, text6, text7, text8, text9, text10]

# Creating buttons
button = tk.Label(root, image=checkboximageoff,
                  borderwidth=0, highlightthickness=0, bd=0)
button2 = tk.Label(root, image=checkboximageoff,
                   borderwidth=0, highlightthickness=0, bd=0)
button3 = tk.Label(root, image=checkboximageoff,
                   borderwidth=0, highlightthickness=0, bd=0)
button4 = tk.Label(root, image=checkboximageoff,
                   borderwidth=0, highlightthickness=0, bd=0)
button5 = tk.Label(root, image=checkboximageoff,
                   borderwidth=0, highlightthickness=0, bd=0)
button6 = tk.Label(root, image=checkboximageoff,
                   borderwidth=0, highlightthickness=0, bd=0)
button7 = tk.Label(root, image=checkboximageoff,
                   borderwidth=0, highlightthickness=0, bd=0)
button8 = tk.Label(root, image=checkboximageoff,
                   borderwidth=0, highlightthickness=0, bd=0)
button9 = tk.Label(root, image=checkboximageoff,
                   borderwidth=0, highlightthickness=0, bd=0)
button10 = tk.Label(root, image=checkboximageoff,
                    borderwidth=0, highlightthickness=0, bd=0)
resetbutton = tk.Label(root, image=logoreset,
                       borderwidth=0, highlightthickness=0, bd=0)
resetbutton.bind("<Button-1>", rollover)
resetbutton.grid(column=2, row=10)
dailybutton = tk.Label(root, image=buttondailypressed, borderwidth=0, highlightthickness=0, bd=0, bg='#2a303c')
dailybutton.bind("<Button-1>", daily)
dailybutton.grid(column=0, row=10, pady=15, padx=25)
weeklybutton = tk.Label(root, image=buttonweekly, borderwidth=0, highlightthickness=0, bd=0, bg='#2a303c')
weeklybutton.bind("<Button-1>", weekly)
weeklybutton.grid(column=1, row=10, pady=15)

# List of buttons
buttons = [button, button2, button3, button4, button5, button6, button7, button8, button9, button10]

# Applying logos
logo_label = tk.Label(image=logouna, bg='#2a303c')
logo_label.image = logouna
logo_label2 = tk.Label(image=logouna, bg='#2a303c')
logo_label2.image = logouna
logo_label3 = tk.Label(image=logouna, bg='#2a303c')
logo_label3.image = logouna
logo_label4 = tk.Label(image=logochaos, bg='#2a303c')
logo_label4.image = logochaos
logo_label5 = tk.Label(image=logochaos, bg='#2a303c')
logo_label5.image = logochaos
logo_label6 = tk.Label(image=logoguardian, bg='#2a303c')
logo_label6.image = logoguardian
logo_label7 = tk.Label(image=logoguardian, bg='#2a303c')
logo_label7.image = logoguardian
logo_label8 = tk.Label(image=logoslaves, bg='#2a303c')
logo_label8.image = logoslaves
logo_label9 = tk.Label(image=logosguild, bg='#2a303c')
logo_label9.image = logosguild
logo_label10 = tk.Label(image=logosguild, bg='#2a303c')
logo_label10.image = logosguild

# List of Logos
logos = [logo_label, logo_label2, logo_label3, logo_label4, logo_label5, logo_label6, logo_label7, logo_label8,
         logo_label9, logo_label10]
# Update state
imagereturndaily()

for c in range(0, (len(logos))):
    buttons[c].bind("<Button-1>", functions[c])
    buttons[c].grid(column=2, row=row)
    logos[c].grid(column=0, row=row)
    texts[c].grid(column=1, row=row)
    row += 1

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
