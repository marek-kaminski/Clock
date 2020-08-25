
from tkinter import *
import time
import csv


# from PIL import ImageTk, Image

def Main():
    global root

    root = Tk()
    root.title("Stopwatch")
    width = 500
    height = 400

    # canvas = Canvas(root, width=300, height=160)
    # image = ImageTk.PhotoImage(Image.open("sky_image.png"))
    # canvas.create_image(0, 0, anchor=NW, image=image)
    # canvas.pack()
    # root.mainloop()

    # photo = PhotoImage(file="sky_image.png", )
    # label = Label(root, image=photo, width=900, height=450, bg="black")
    # label.pack()





    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))

    Top = Frame(root, width=600, bg="black")
    Top.pack(side=TOP)
    stopWatch = StopWatch(root)
    stopWatch.pack(side=TOP)

    Middle = Frame(root, width=600, bg="black")
    Middle.pack(side=TOP)

    Bottom = Frame(root, width=500, bg="black")
    Bottom.pack(side=BOTTOM)

    blank_line3 = Label(Bottom, text="", font=("arial", 18), fg="white", bg="black")
    blank_line3.pack(side=BOTTOM)
    blank_line4 = Label(Bottom, text="", font=("arial", 18), fg="white", bg="black")
    blank_line4.pack(side=TOP)

    Start = Button(Bottom, text='Start', command=stopWatch.Start, width=10, height=2)
    Start.pack(side=LEFT)
    Stop = Button(Bottom, text='Stop', command=stopWatch.Stop, width=10, height=2)
    Stop.pack(side=LEFT)
    Save = Button(Bottom, text='Save', command=stopWatch.Save, width=10, height=2)
    Save.pack(side=LEFT)
    Reset = Button(Bottom, text='Reset', command=stopWatch.Reset, width=10, height=2)
    Reset.pack(side=LEFT)

    blank_line = Label(Top, text=" ", font=("arial", 18), fg="white", bg="black")
    blank_line.pack(fill=X)

    Title = Label(Top, text="stoper", font=("arial", 18), fg="white", bg="black")
    Title.pack(fill=X)
    blank_line2 = Label(Middle, text="", font=("arial", 18), fg="white", bg="black")
    blank_line2.pack(side=TOP)

    Title2 = Label(Middle, text="Całkowity czas spędzony na programowaniu", font=("arial", 18), fg="white", bg="black")
    Title2.pack(side=TOP)

    #  ten try i excep ma tworzyc nowy plik albo zamieniać liczby z .txt na dane do wyświetlania
    try:
        with open('programming_time.txt', 'r') as file:
            reader = csv.reader(file)
            # print(reader)
            for row in reader:
                print(row)
            print(row)
            minutes_of_coding = float(row[0])//60
            hours_of_coding = minutes_of_coding//60
            
    except FileNotFoundError:
        f = open('programming_time.txt', "w+")
        f.write(str(0))
        f.close()
        minutes_of_coding = 0
        hours_of_coding = 0

    all_programming_time = Label(Middle, text="godziny: " + str(hours_of_coding) + " minuty: " + str(minutes_of_coding),
                                 font=("arial", 18), fg="white", bg="black")
    all_programming_time.pack(side=TOP)

    root.config(bg="black")
    root.mainloop()


class StopWatch(Frame):

    def save_csv(self):
        try:
            f = open("programming_time.txt", "w+")
            f.write(str(self.nextTime))
            f.close()
        except FileExistsError:
            f = open("programming_time.txt", "r+")
            f.write(str(self.nextTime))
            f.close()

    def __init__(self, parent=None, **kw):
        Frame.__init__(self, parent, kw)
        self.startTime = 0.0
        self.nextTime = 0.0
        self.onRunning = 0
        self.timestr = StringVar()
        self.MakeWidget()

    def MakeWidget(self):
        timeText = Label(self, textvariable=self.timestr, font=("arial", 50), fg="green", bg="black")
        self.SetTime(self.nextTime)
        timeText.pack(fill=X, expand=NO, pady=2, padx=2)

    def Updater(self):
        self.nextTime = time.time() - self.startTime
        self.SetTime(self.nextTime)
        self.timer = self.after(50, self.Updater)

    def SetTime(self, nextElap):
        minutes = int(nextElap / 60)
        seconds = int(nextElap - minutes * 60.0)
        miliSeconds = int((nextElap - minutes * 60.0 - seconds) * 100)
        self.timestr.set('%02d:%02d:%02d' % (minutes, seconds, miliSeconds))

    def Start(self):
        if not self.onRunning:
            self.startTime = time.time() - self.nextTime
            self.Updater()
            self.onRunning = 1

    def Save(self):
        #  poniższa linijka odwala jakąś magie 
        self.nextTime = time.time() - self.startTime
        self.SetTime(self.nextTime)

        with open('programming_time.txt', 'r+') as file:
            reader = csv.reader(file)
            for row in reader:
                all_time = self.nextTime + float(row[0])
                print(row)
                print(all_time)
                f = open('programming_time.txt', "w+")
                f.write(str(all_time))
                f.close()

        # try:
        #     with open('programming_time.txt', "w+") as file:
        #         reader = csv.reader(file)
        #         print(reader)
        #         for row in reader:
        #             print(row)
        #             all_time = self.nextTime + reader
        #             f.write(str(self.nextTime))
        #             f.close()
        #
        #
        # except FileExistsError:
        #     f = open('programming_time.txt', "r+")
        #     f.write(str(self.nextTime))
        #     f.close()

    def Stop(self):
        if self.onRunning:
            self.after_cancel(self.timer)
            self.onRunning = 0




    def Reset(self):
        self.startTime = time.time()
        self.nextTime = 0.0
        self.SetTime(self.nextTime)


if __name__ == '__main__':
    Main()
