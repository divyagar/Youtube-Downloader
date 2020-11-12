import tkinter as tk
import tkinter.filedialog
from tkcalendar import DateEntry
from tkinter import messagebox

class GuiApp(tk.Frame):
    def __init__(self, master):
        self.master = master
        tk.Frame.__init__(self, master)

        f1 = Frame1(self)
        f1.grid(row=2,column=0)
        f2 = Frame2(self)
        f2.grid(row=2,column=0)
        f3 = Frame3(self)
        f3.grid(row=2,column=0)

        self.f = []
        self.f.append(f1)
        self.f.append(f2)
        self.f.append(f3)

        tf = TopFrame(self)
        tf.grid(row=0, column=0)

        self.show_frame(0);

    def show_frame(self, idx):
        frm = self.f[idx]
        frm.tkraise()


class TopFrame(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        tk.Frame.__init__(self, self.parent)
        self.b1 = tk.Button(self, text = "Video", command = lambda : parent.show_frame(0), width=10)
        self.b1.grid(row=0, column=1, padx=15, pady=10)
        self.b2 = tk.Button(self, text = "Audio", command = lambda : parent.show_frame(1), width=10)
        self.b2.grid(row=0, column=2, padx=15, pady=10)
        self.b3 = tk.Button(self, text = "Playlist", command = lambda : parent.show_frame(2), width=10)
        self.b3.grid(row=0, column=3, padx=15, pady=10)
        canvas = tk.Canvas(self.master, width=750, height=4)
        canvas.create_line(0, 2, 750, 2, fill="gray", tags="line")
        canvas.grid(row=1, column=0)


class Frame1(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        tk.Frame.__init__(self, self.parent, width = 800, height = 500, borderwidth = 1)
        self.grid_propagate(0)

        # Frame for checkboxes and their respective entry widgets
        checkBoxFrame = tk.Frame(self, width = 758, height = 120, borderwidth = 1)
        # checkBoxFrame['bg'] = 'red'
        checkBoxFrame.grid_propagate(0)
        checkBoxFrame.grid(row=0, column=0, padx=20, pady=5)

        # portion of checkboxes
        self.var = tk.StringVar()
        r1 = tk.Radiobutton(checkBoxFrame, text = "Youtube link", variable = self.var, value = "1")
        r1.grid(row=0, column=0, sticky = tk.W, padx=10, pady=10)
        r2 = tk.Radiobutton(checkBoxFrame, text = "File Path", variable = self.var, value = "2")
        r2.grid(row=0, column=1, sticky = tk.W, padx=10, pady=10)
        self.var.set("1")
        #-----------------------------

        # portion of entry widgets
        e1 = tk.Text(checkBoxFrame, width = 42, height=3)
        e1.grid(row=1, column=0, sticky = tk.W, padx=10, pady=5)
        e2 = tk.Text(checkBoxFrame, width = 42, height=3)
        e2.grid(row=1, column=1, sticky = tk.W, padx=10, pady=5)
        #-----------------------------------
        # First frame ends

        # second frame to get custom name, file directory location and dropdown
        secFrame = tk.Frame(self, width = 758, height = 70)
        # secFrame['bg'] = 'green'
        secFrame.grid_propagate(0)
        secFrame.grid(row=1, column=0, padx=20)

        ## row 1 of second frame
        customNameLabel = tk.Label(secFrame, text = "Provide custom name : ")
        customNameLabel.grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)

        fileLocLabel = tk.Label(secFrame, text = "Choose file location : ", width=23, anchor='w')
        fileLocLabel.grid(row=0, column=1, sticky=tk.W, padx=10, pady=5)

        chooseQualityLabel = tk.Label(secFrame, text = "Choose Quality : ")
        chooseQualityLabel.grid(row=0, column=2, sticky=tk.W, padx=10, pady=5)
        ##---------------------------------

        # row2 of second frame
        customName = tk.StringVar()
        customNameEntry = tk.Entry(secFrame, width=55, textvariable = customName)
        customNameEntry.grid(row=1, column=0, sticky = tk.W, padx=10)

        askDirectoryBtn = tk.Button(secFrame, text = "select folder", command = self.getDir)
        askDirectoryBtn.grid(row=1, column=1, sticky=tk.W, padx=10)

        self.qualities = ['best video, best audio', 'best video, worst audio', 'worst video, best audio', 'worst video, worst audio']
        self.quality = tk.StringVar()
        self.quality.set("best video, best audio")
        qualitySelection = tk.OptionMenu(secFrame, self.quality, *self.qualities, command=self.getQuality)
        qualitySelection.grid(row=1, column=2, sticky=tk.W, padx=10)
        #----------------------------------
        #second frame ends

        # third frame
        additionalData = tk.Frame(self, width = 758, height = 50)
        # additionalData['bg'] = 'yellow'
        additionalData.grid_propagate(0)
        additionalData.grid(row=2, column=0, padx=20)

        self.des = tk.IntVar()
        self.meta = tk.IntVar()
        self.annot = tk.IntVar()
        self.sub = tk.IntVar()
        self.thumb = tk.IntVar()

        description = tk.Checkbutton(additionalData, text = "Description", onvalue=1, offvalue=0, width=14)
        description.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)
        metadata = tk.Checkbutton(additionalData, text = "Metadata", onvalue=1, offvalue=0, width=14)
        metadata.grid(row=0, column=1, sticky=tk.W, padx=10, pady=10)
        annotation = tk.Checkbutton(additionalData, text = "Annotation", onvalue=1, offvalue=0, width=14)
        annotation.grid(row=0, column=2, sticky=tk.W, padx=10, pady=10)
        subtitle = tk.Checkbutton(additionalData, text = "Subtitle", onvalue=1, offvalue=0, width=14)
        subtitle.grid(row=0, column=3, sticky=tk.W, padx=10, pady=10)
        thumbnail = tk.Checkbutton(additionalData, text = "Thumbnail", onvalue=1, offvalue=0, width=14)
        thumbnail.grid(row=0, column=4, sticky=tk.W, padx=10, pady=10)
        #-------------------------------
        # third frame ends

        #fourth frame
        downloadFrame = tk.Frame(self, width=758, height=200)
        downloadFrame.grid(row=3, column=0, padx=20)

        self.downloadBtn = tk.Button(downloadFrame, text = "Download")
        self.downloadBtn.pack()
        helv36 = tk.font.Font(family='Helvetica', size=14, weight='bold')
        self.downloadBtn['font'] = helv36
        #fourth frame ends

        # fifth frame
        outputFrame = tk.Frame(self, width = 758, height = 200)
        # outputFrame['bg'] = 'orange'
        outputFrame.grid_propagate(0)
        outputFrame.grid(row=4, column=0, padx=20)

        outputWindow = tk.Text(outputFrame, width=90, height=10, state=tk.DISABLED)
        outputWindow.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)

        # fifth frame ends

    # testing function for directory selection
    def getDir(self):
        fileLoc = tk.filedialog.askdirectory()
        print(fileLoc)

    def getQuality(self, *qualitiesArgs):
        print(self.quality.get())

class Frame2(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        tk.Frame.__init__(self, self.parent, width = 800, height = 500, borderwidth = 1)
        self.grid_propagate(0)

        # Frame for checkboxes and their respective entry widgets
        checkBoxFrame = tk.Frame(self, width = 758, height = 120, borderwidth = 1)
        # checkBoxFrame['bg'] = 'red'
        checkBoxFrame.grid_propagate(0)
        checkBoxFrame.grid(row=0, column=0, padx=20, pady=5)

        # portion of checkboxes
        self.var = tk.StringVar()
        r1 = tk.Radiobutton(checkBoxFrame, text = "Youtube link", variable = self.var, value = "1")
        r1.grid(row=0, column=0, sticky = tk.W, padx=10, pady=10)
        r2 = tk.Radiobutton(checkBoxFrame, text = "File Path", variable = self.var, value = "2")
        r2.grid(row=0, column=1, sticky = tk.W, padx=10, pady=10)
        self.var.set("1")
        #-----------------------------

        # portion of entry widgets
        e1 = tk.Text(checkBoxFrame, width = 42, height=3)
        e1.grid(row=1, column=0, sticky = tk.W, padx=10, pady=5)
        e2 = tk.Text(checkBoxFrame, width = 42, height=3)
        e2.grid(row=1, column=1, sticky = tk.W, padx=10, pady=5)
        #-----------------------------------
        # First frame ends

        # second frame to get custom name, file directory location and dropdown
        secFrame = tk.Frame(self, width = 758, height = 70)
        # secFrame['bg'] = 'green'
        secFrame.grid_propagate(0)
        secFrame.grid(row=1, column=0, padx=20)

        ## row 1 of second frame
        customNameLabel = tk.Label(secFrame, text = "Provide custom name : ")
        customNameLabel.grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)

        fileLocLabel = tk.Label(secFrame, text = "Choose file location : ", width=23, anchor='w')
        fileLocLabel.grid(row=0, column=1, sticky=tk.W, padx=10, pady=5)
        ##---------------------------------

        # row2 of second frame
        customName = tk.StringVar()
        customNameEntry = tk.Entry(secFrame, width=55, textvariable = customName)
        customNameEntry.grid(row=1, column=0, sticky = tk.W, padx=10)

        askDirectoryBtn = tk.Button(secFrame, text = "select folder", command = self.getDir)
        askDirectoryBtn.grid(row=1, column=1, sticky=tk.W, padx=10)
        #----------------------------------
        #second frame ends

        #third frame
        downloadFrame = tk.Frame(self, width=758, height=200)
        downloadFrame.grid(row=3, column=0, padx=20)

        self.downloadBtn = tk.Button(downloadFrame, text = "Download")
        self.downloadBtn.pack()
        helv36 = tk.font.Font(family='Helvetica', size=14, weight='bold')
        self.downloadBtn['font'] = helv36
        #third frame ends

        # fourth frame
        outputFrame = tk.Frame(self, width = 758, height = 250)
        # outputFrame['bg'] = 'orange'
        outputFrame.grid_propagate(0)
        outputFrame.grid(row=4, column=0, padx=20)

        outputWindow = tk.Text(outputFrame, width=90, height=13, state=tk.DISABLED)
        outputWindow.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)

        # fourth frame ends

    # testing function for directory selection
    def getDir(self):
        fileLoc = tk.filedialog.askdirectory()
        print(fileLoc)

class Frame3(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        tk.Frame.__init__(self, self.parent, width = 800, height = 500, borderwidth = 1)
        self.grid_propagate(0)

        # first row
        self.firstFrame = tk.Frame(self, width = 758, height = 80)
        # firstFrame['bg'] = 'red'
        self.firstFrame.grid_propagate(0)
        self.firstFrame.grid(row=0, column=0, padx=20, pady=(20,0))

        self.label = tk.Label(self.firstFrame, text = "Youtube playlist link :")
        self.label.grid(row = 0, column = 0, sticky = tk.W, padx = 20, pady=5)

        self.playListEntry = tk.Text(self.firstFrame, width = 42, height=2)
        self.playListEntry.grid(row=1, column=0, sticky = tk.NW, padx=20, pady=5)
        # first row ends

        # second row
        self.secondFrame = tk.Frame(self, width=758, height=50)
        # secondFrame['bg'] = "green"
        self.secondFrame.grid_propagate(0)
        self.secondFrame.grid(row=1, column=0, padx=20)

        self.criteria = tk.StringVar();
        self.criteria.set("1")
        self.sizeLabel = tk.Radiobutton(self.secondFrame, text = "Size Criteria", variable=self.criteria, value="1", command = self.checkRadioBut)
        self.sizeLabel.grid(row=0, column=0, sticky=tk.W, padx=20, pady=5)

        self.subFrame = tk.Frame(self.secondFrame)
        self.subFrame.grid(row=0, column=1)

        self.minChecked = tk.IntVar()
        self.minSize = tk.Checkbutton(self.subFrame, text = "Minimum : ", onvalue=1, offvalue=0, width=14, variable = self.minChecked)
        self.minSize.grid(row=0, column=0, sticky=tk.W, padx=(20,2), pady=10)

        self.minimum = tk.Entry(self.subFrame, width = 10)
        self.minimum.grid(row=0, column=1, sticky=tk.W, padx = (2,0), pady=10)

        self.sizes = ['KB', 'MB', 'GB']
        self.size = tk.StringVar()
        self.size.set('KB')
        self.sizeSelection = tk.OptionMenu(self.subFrame, self.size, *self.sizes)
        self.sizeSelection.grid(row=0, column=3, sticky=tk.W, padx = (2,20))

        self.maxChecked = tk.IntVar()
        self.maxSize = tk.Checkbutton(self.subFrame, text = "Maximum :", onvalue=1, offvalue=0, width=14, variable = self.maxChecked)
        self.maxSize.grid(row=0, column=4, sticky=tk.W, padx=(20,2), pady=10)

        self.maximum = tk.Entry(self.subFrame, width = 10)
        self.maximum.grid(row=0, column=5, sticky=tk.W, padx = (2,0), pady=10)

        self.size2 = tk.StringVar()
        self.size2.set('KB')
        self.sizeSelection2 = tk.OptionMenu(self.subFrame, self.size2, *self.sizes)
        self.sizeSelection2.grid(row=0, column=6, sticky=tk.W, padx=(2,20))
        # second row ends

        #third row
        self.thirdFrame = tk.Frame(self, width=758, height=50)
        # thirdFrame['bg'] = "yellow"
        self.thirdFrame.grid_propagate(0)
        self.thirdFrame.grid(row=2, column=0, padx=20)

        self.dateLabel = tk.Radiobutton(self.thirdFrame, text = "Date Criteria", variable=self.criteria, value="2", command = self.checkRadioBut)
        self.dateLabel.grid(row=0, column=0, sticky=tk.W, padx=20, pady=5)

        self.subFrame2 = tk.Frame(self.thirdFrame)
        self.subFrame2.grid(row=0, column=1)

        self.dates = ['On this date', 'Before this date', 'After this date', 'After and before these dates']
        self.date = tk.StringVar()
        self.date.set('On this date')
        self.dateSelection = tk.OptionMenu(self.subFrame2, self.date, *self.dates)
        self.dateSelection.configure(width=25)
        self.dateSelection.grid(row=0, column=0, sticky=tk.W, padx = 20)

        self.date1 = DateEntry(self.subFrame2, width=12)
        self.date1.grid(row=0, column=1, sticky = tk.W, padx = 10)

        self.date2 = DateEntry(self.subFrame2, width=12)
        self.date2.grid(row=0, column=2, sticky = tk.W, padx = 10)

        #third row ends

        #fourth row
        self.fourthFrame = tk.Frame(self, width=758, height=50)
        # fourthFrame['bg'] = "Orange"
        self.fourthFrame.grid_propagate(0)
        self.fourthFrame.grid(row=3, column=0, padx=20)

        self.specificCriteria = tk.Radiobutton(self.fourthFrame, text = "Specific videos", variable=self.criteria, value="3", command = self.checkRadioBut)
        self.specificCriteria.grid(row=0, column=0, padx=20, sticky=tk.W)

        self.subFrame3 = tk.Frame(self.fourthFrame)
        self.subFrame3.grid(row=0, column=1)

        self.specifics = ['Mention indices(separated by commas)', 'Mention start and end of playlist(separated by space']
        self.specifc = tk.StringVar()
        self.specifc.set('Mention indices(separated by commas)')
        self.videoSelection = tk.OptionMenu(self.subFrame3, self.specifc, *self.specifics)
        self.videoSelection.configure(width=50)
        self.videoSelection.grid(row=0, column=0, sticky=tk.W, padx=10)

        self.selectionValue = tk.Entry(self.subFrame3, width=20, state=tk.DISABLED)
        self.selectionValue.grid(row=0, column=1, sticky=tk.W, padx=10)

        #fourth row ends

        #fourth row
        downloadFrame = tk.Frame(self, width=758, height=200)
        downloadFrame.grid(row=4, column=0, padx=20)

        self.downloadBtn = tk.Button(downloadFrame, text = "Download", command = self.downloadVide)
        self.downloadBtn.pack()
        helv36 = tk.font.Font(family='Helvetica', size=14, weight='bold')
        self.downloadBtn['font'] = helv36
        #fourth row ends

        #fifth row
        self.outputFrame = tk.Frame(self, width=758, height=250)
        # outputFrame['bg'] = "pink"
        self.outputFrame.grid_propagate(0)
        self.outputFrame.grid(row=5, column=0, padx=20)

        self.outputWindow = tk.Text(self.outputFrame, width=90, height=13, state=tk.DISABLED)
        self.outputWindow.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)

        self.disableSub2()
        self.disableSub3()

        #fifth row ends

    def downloadVide(self):
        link = self.playListEntry.get('1.0', 'end-1c')
        link = " " + link
        if(len(link) == 0):
            messagebox.showerror("Error", "Provide Link")
            return

        options = ""

        criteriaVal = self.criteria.get()
        if(criteriaVal == "1"):
            if(self.minChecked.get()):
                try:
                    minVal = self.minimum.get()
                    minVal = int(minVal)

                except Exception as ex:
                    messagebox.showerror("Error", "Minimum value should be an integer")
                    return

                size = self.size.get()
                options += " --min-filesize " + str(minVal) + size[0]

            if (self.maxChecked.get()):
                try:
                    maxVal = self.maximum.get()
                    maxVal = int(maxVal)

                except Exception as ex:
                    messagebox.showerror("Error", "Maximum value should be an integer")
                    return

                size = self.size2.get()
                options += " --max-filesize " + str(maxVal) + size[0]

            print(options)
        elif(criteriaVal == "2"):
            date = self.date.get()
            date1 = self.date1.get()
            date1 = date1.split('/')
            date2 = self.date2.get()
            date2 = date2.split('/')

            for i in range(2):
                if(len(date1[i]) == 1):
                    date1[i] = "0" + date1[i]
                if(len(date2[i]) == 1):
                    date2[i] = "0" + date2[i]

            if(date == "On this date"):
                options += " --date 20" + date1[2] + date1[0] + date1[1]

            elif(date == "Before this date"):
                options += " --datebefore 20" + date1[2] + date1[0] + date1[1]

            elif(date == "After this date"):
                options += " --dateafter 20" + date1[2] + date1[0] + date1[1]

            else:
                options += " --datebefore 20" + date1[2] + date1[0] + date1[1] + " --dateafter 20" + date2[2] + date2[0] + date2[1]

            print(options)

        else:
            specific = self.specifc.get()
            values = self.selectionValue.get()
            valuesList = values.split(",")
            for value in valuesList:
                try:
                    value = int(value)
                except:
                    messagebox.showerror("Error", "Values should be integer")
                    return

            if(specific == "Mention indices(separated by commas)"):
                options += " --playlist-items " + values
            else:
                values = values.split(",")
                if(len(values) >= 1 and len(values[0]) >= 1):
                    options += " --playlist-start " + values[0]

                    if(len(values) > 1 and len(values[0]) >= 1):
                        options += " --playlist-end " + values[1]

                else:
                    messagebox.showerror("Error", "Options box cannot be empty")

            print(options)

        command = "youtube-dl" + options + link
        print(command)

    def checkRadioBut(self):
        value = self.criteria.get()
        if(value == "1"):
            self.enableSub()
            self.disableSub2()
            self.disableSub3()

        elif(value == "2"):
            self.enableSub2()
            self.disableSub()
            self.disableSub3()

        else:
            self.enableSub3()
            self.disableSub()
            self.disableSub2()

    def disableSub(self):
        for child in self.subFrame.winfo_children():
            child.configure(state = 'disable')

    def disableSub2(self):
        for child in self.subFrame2.winfo_children():
            child.configure(state = 'disable')

    def disableSub3(self):
        for child in self.subFrame3.winfo_children():
            child.configure(state = 'disable')

    def enableSub(self):
        for child in self.subFrame.winfo_children():
            child.configure(state = 'normal')

    def enableSub2(self):
        for child in self.subFrame2.winfo_children():
            child.configure(state = 'normal')

    def enableSub3(self):
        for child in self.subFrame3.winfo_children():
            child.configure(state = 'normal')

    def radiobut(self):
        print("pressed")

    def getCriteria(self, *criterias):
        pass


root = tk.Tk()
app = GuiApp(root)
app.pack(side = "left", fill = "both", expand = True)
root.mainloop()




