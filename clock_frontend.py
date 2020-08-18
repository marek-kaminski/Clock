
from tkinter import *
import time
import csv
# from PIL import ImageTk, Image

def Main():
    global root

    root = Tk()
    root.title("Stopwatch")
    width = 500
    height = 500

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
    Top = Frame(root, width=600)
    Top.pack(side=TOP)
    stopWatch = StopWatch(root)
    stopWatch.pack(side=TOP)
    Bottom = Frame(root, width=500)
    Bottom.pack(side=BOTTOM)
    Start = Button(Bottom, text='Start', command=stopWatch.Start, width=10, height=2)
    Start.pack(side=LEFT)
    Stop = Button(Bottom, text='Stop', command=stopWatch.Stop, width=10, height=2)
    Stop.pack(side=LEFT)
    Reset = Button(Bottom, text='Reset', command=stopWatch.Reset, width=10, height=2)
    Reset.pack(side=LEFT)
    
    Title = Label(Top, text="stoper", font=("arial", 18), fg="white", bg="black")
    Title.pack(fill=X)

    # bottom_table = Label(root, text="całkowity czas spędzony na programowaniu   ", font="times 15 bold")
    # bottom_table.grid(row=3, column=2)


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


    def Stop(self):
        if self.onRunning:
            self.after_cancel(self.timer)
            self.nextTime = time.time() - self.startTime
            self.SetTime(self.nextTime)
            self.onRunning = 0
            # to poniżej printuje obecny czas, teraz wystarczy zrobić csv który będzie zapisywał czas
            print(self.nextTime)
            self.save_csv()
            with open('programming_time.txt', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row)

    def Reset(self):
        self.startTime = time.time()
        self.nextTime = 0.0
        self.SetTime(self.nextTime)




if __name__ == '__main__':
    Main()
