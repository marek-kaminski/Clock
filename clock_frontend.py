from tkinter import *
import time
import csv
from PIL import ImageTk, Image
# import ImageTk
# import Image

# import Image

def main():
    global root

    root = Tk()
    root.title("Stopwatch")
    width = 500
    height = 400

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))

    top = Frame(root, width=600, bg="black")
    top.pack(side=TOP)
    stop_watch = StopWatch(root)
    stop_watch.pack(side=TOP)

    middle = Frame(root, width=600, bg="black")
    middle.pack(side=TOP)

    bottom = Frame(root, width=500, bg="black")
    bottom.pack(side=BOTTOM)

    blank_line = Label(top, text=" ", font=("arial", 18), fg="white", bg="black")
    blank_line.pack(fill=X)

    title = Label(top, text="stoper", font=("arial", 18), fg="white", bg="black")
    title.pack(fill=X)

    blank_line2 = Label(middle, text="", font=("arial", 18), fg="white", bg="black")
    blank_line2.pack(side=TOP)
    blank_line3 = Label(bottom, text="", font=("arial", 18), fg="white", bg="black")
    blank_line3.pack(side=BOTTOM)
    blank_line4 = Label(bottom, text="", font=("arial", 18), fg="white", bg="black")
    blank_line4.pack(side=TOP)

    start = Button(bottom, text='Start', command=stop_watch.start, width=10, height=2)
    start.pack(side=LEFT)
    stop = Button(bottom, text='Stop', command=stop_watch.stop, width=10, height=2)
    stop.pack(side=LEFT)
    save = Button(bottom, text='Save/Reset', command=stop_watch.save_reset, width=10, height=2)
    save.pack(side=LEFT)

    title2 = Label(middle, text="Całkowity czas spędzony na programowaniu", font=("arial", 18), fg="white", bg="black")
    title2.pack(side=TOP)

    # this try/except will read the .txt file or create a new one
    try:
        with open('programming_time.txt', 'r') as file:
            reader = csv.reader(file)
            # the line below will make an object called 'row' from the time in .txt file
            for row in reader:
                pass
            # the row below takes the time from file, then converts it into float to make the
            # calculations and then to int to remove the unnecessary "0"
            minutes_of_coding = int(float(row[0])//60)
            hours_of_coding = minutes_of_coding//60
    except FileNotFoundError:
        f = open('programming_time.txt', "w+")
        f.write(str(0))
        f.close()
        minutes_of_coding = 0
        hours_of_coding = 0

    all_programming_time = Label(middle, text="godziny: " + str(hours_of_coding) + " minuty: " + str(minutes_of_coding),
                                 font=("arial", 18), fg="white", bg="black")
    all_programming_time.pack(side=TOP)

    root.config(bg="black")
    root.mainloop()
    # update the line

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
        timeText.pack(fill=X, expand=NO, pady=1, padx=1)

    def updater(self):
        self.nextTime = time.time() - self.startTime
        self.SetTime(self.nextTime)
        self.timer = self.after(50, self.updater)

    def SetTime(self, next_lap):
        minutes = int(next_lap / 60)
        seconds = int(next_lap - minutes * 60.0)
        miliSeconds = int((next_lap - minutes * 60.0 - seconds) * 100)
        self.timestr.set('%02d:%02d:%02d' % (minutes, seconds, miliSeconds))

    def start(self):
        if not self.onRunning:
            self.startTime = time.time() - self.nextTime
            self.updater()
            self.onRunning = 1

    def save_reset(self):

        with open('programming_time.txt', 'r+') as file:
            reader = csv.reader(file)
            for row in reader:
                all_time = self.nextTime + float(row[0])
                f = open('programming_time.txt', "w+")
                f.write(str(all_time))
                f.close()
                # this will reset the time
                self.startTime = time.time()
                self.nextTime = 0.0
                self.SetTime(self.nextTime)
                #  without the "break" the loop would go a second time after reaching 100 seconds and cause a bug
                break

    def stop(self):
        if self.onRunning:
            self.after_cancel(self.timer)
            self.onRunning = 0


if __name__ == '__main__':
    main()
