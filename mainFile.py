import tkinter as tk
import tkinter.filedialog
# from tkcalendar import DateEntry

class GuiApp(tk.Frame):
    def __init__(self, master):
        self.master = master
        # print(type(self))
        tk.Frame.__init__(self, master)

        f1 = Frame1(self)
        f1.grid(row=1,column=0)
        f2 = Frame2(self)
        f2.grid(row=1,column=0)
        f3 = Frame3(self)
        f3.grid(row=1,column=0)

        self.f = []
        self.f.append(f1)
        self.f.append(f2)
        self.f.append(f3)

        tf = TopFrame(self)
        tf.grid(row=0, column=0)


    def show_frame(self, idx):
        print("function called")
        frm = self.f[idx]
        frm.tkraise()


class TopFrame(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        tk.Frame.__init__(self, self.parent)
        self.b1 = tk.Button(self, text = "button1", command = lambda : parent.show_frame(0))
        self.b1.pack(side = "left")
        self.b2 = tk.Button(self, text = "button2", command = lambda : parent.show_frame(1))
        self.b2.pack(side = "left")
        self.b3 = tk.Button(self, text = "button3", command = lambda : parent.show_frame(2))
        self.b3.pack(side = "left")

class Frame1(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        tk.Frame.__init__(self, self.parent, width = 800, height = 600, borderwidth = 1)
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

        # fourth frame
        outputFrame = tk.Frame(self, width = 758, height = 200)
        # outputFrame['bg'] = 'orange'
        outputFrame.grid_propagate(0)
        outputFrame.grid(row=3, column=0, padx=20)

        outputWindow = tk.Text(outputFrame, width=90, height=10, state=tk.DISABLED)
        outputWindow.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)

        # fourth frame ends

    # testing function for directory selection
    def getDir(self):
        fileLoc = tk.filedialog.askdirectory()
        print(fileLoc)

    def getQuality(self, *qualitiesArgs):
        print(self.quality.get())

class Frame2(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        tk.Frame.__init__(self, self.parent, width = 800, height = 600, borderwidth = 1)
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

        # fourth frame
        outputFrame = tk.Frame(self, width = 758, height = 250)
        # outputFrame['bg'] = 'orange'
        outputFrame.grid_propagate(0)
        outputFrame.grid(row=3, column=0, padx=20)

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
        tk.Frame.__init__(self, self.parent, width = 800, height = 600, borderwidth = 1)
        self.grid_propagate(0)

        # first row
        firstFrame = tk.Frame(self, bg = 'red', width = 758, height = 80)
        firstFrame.grid_propagate(0)
        firstFrame.grid(row=0, column=0, padx=20, pady=20)

        label = tk.Label(firstFrame, text = "Youtube playlist link :")
        label.grid(row = 0, column = 0, sticky = tk.W, padx = 20, pady=5)

        e1 = tk.Text(firstFrame, width = 42, height=2)
        e1.grid(row=1, column=0, sticky = tk.NW, padx=20, pady=5)
        # first row ends

        # second row
        secondFrame = tk.Frame(self, width=758, height=50)
        secondFrame['bg'] = "green"
        secondFrame.grid_propagate(0)
        secondFrame.grid(row=1, column=0, padx=20)

        criteria = tk.StringVar();

        sizeLabel = tk.Radiobutton(secondFrame, text = "Size Criteria")
        sizeLabel.grid(row=0, column=0, sticky=tk.W, padx=20, pady=5)

        minSize = tk.Checkbutton(secondFrame, text = "Minimum : ", onvalue=1, offvalue=0, width=14)
        minSize.grid(row=0, column=1, sticky=tk.W, padx=(20,5), pady=10)

        minimum = tk.Entry(secondFrame, width = 10, state = tk.DISABLED)
        minimum.grid(row=0, column=2, sticky=tk.W, padx = (5,0), pady=10)

        self.sizes = ['KB', 'MB', 'GB']
        self.size = tk.StringVar()
        self.size.set('KB')
        sizeSelection = tk.OptionMenu(secondFrame, self.size, *self.sizes)
        sizeSelection.grid(row=0, column=3, sticky=tk.W, padx = (2,20))
        sizeSelection.configure(state="disabled")

        maxSize = tk.Checkbutton(secondFrame, text = "Maximum", onvalue=1, offvalue=0, width=14)
        maxSize.grid(row=0, column=4, sticky=tk.W, padx=(20,5), pady=10)

        maximum = tk.Entry(secondFrame, width = 10, state = tk.DISABLED)
        maximum.grid(row=0, column=5, sticky=tk.W, padx = (5,0), pady=10)

        self.size2 = tk.StringVar()
        self.size2.set('KB')
        sizeSelection2 = tk.OptionMenu(secondFrame, self.size2, *self.sizes)
        sizeSelection2.grid(row=0, column=6, sticky=tk.W, padx=(2,20))
        sizeSelection2.configure(state="disabled")
        # second row ends

    def getCriteria(self, *criterias):
        pass


root = tk.Tk()
root.geometry("800x500")
f1 = Frame3(root)
f1.grid(row=0, column=0)

root.mainloop()


# root = tk.Tk()
# print(type(root))
# app = GuiApp(root)
# app.pack(side = "left", fill = "both", expand = True)
# root.mainloop()




