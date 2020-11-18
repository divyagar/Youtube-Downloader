import tkinter as tk
import tkinter.filedialog
from urllib import request, parse
import re
from tkcalendar import DateEntry
from tkinter import messagebox
import os
import time

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
        self.checkBoxFrame = tk.Frame(self, width = 758, height = 120, borderwidth = 1)
        # checkBoxFrame['bg'] = 'red'
        self.checkBoxFrame.grid_propagate(0)
        self.checkBoxFrame.grid(row=0, column=0, padx=20, pady=5)

        # portion of checkboxes
        self.var = tk.StringVar()
        self.r1 = tk.Radiobutton(self.checkBoxFrame, text = "Youtube link", variable = self.var, value = "1", command = self.checkRadio)
        self.r1.grid(row=0, column=0, sticky = tk.W, padx=10, pady=10)
        self.r2 = tk.Radiobutton(self.checkBoxFrame, text = "File Path", variable = self.var, value = "2", command = self.checkRadio)
        self.r2.grid(row=0, column=1, sticky = tk.W, padx=10, pady=10)
        self.var.set("1")
        #-----------------------------

        # portion of entry widgets
        self.e1 = tk.Text(self.checkBoxFrame, width = 42, height=3)
        self.e1.grid(row=1, column=0, sticky = tk.W, padx=10, pady=5)
        self.e2 = tk.Text(self.checkBoxFrame, width = 42, height=3, state=tk.DISABLED)
        self.e2.grid(row=1, column=1, sticky = tk.W, padx=10, pady=5)
        #-----------------------------------
        # First frame ends

        # second frame to get custom name, file directory location and dropdown
        self.secFrame = tk.Frame(self, width = 758, height = 70)
        # secFrame['bg'] = 'green'
        self.secFrame.grid_propagate(0)
        self.secFrame.grid(row=1, column=0, padx=20)

        ## row 1 of second frame
        self.customNameLabel = tk.Label(self.secFrame, text = "Provide custom name : ")
        self.customNameLabel.grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)

        self.fileLocLabel = tk.Label(self.secFrame, text = "Choose file location : ", width=23, anchor='w')
        self.fileLocLabel.grid(row=0, column=1, sticky=tk.W, padx=10, pady=5)

        self.chooseQualityLabel = tk.Label(self.secFrame, text = "Choose Quality : ")
        self.chooseQualityLabel.grid(row=0, column=2, sticky=tk.W, padx=10, pady=5)
        ##---------------------------------

        # row2 of second frame
        self.customNameEntry = tk.Entry(self.secFrame, width=55)
        self.customNameEntry.grid(row=1, column=0, sticky = tk.W, padx=10)

        self.location = ""
        self.askDirectoryBtn = tk.Button(self.secFrame, text = "select folder", command = self.getDir)
        self.askDirectoryBtn.grid(row=1, column=1, sticky=tk.W, padx=10)

        self.qualities = ['bestvideo,bestaudio', 'bestvideo,worstaudio', 'worstvideo,bestaudio', 'worstvideo,worstaudio']
        self.quality = tk.StringVar()
        self.quality.set("bestvideo,bestaudio")
        self.qualitySelection = tk.OptionMenu(self.secFrame, self.quality, *self.qualities)
        self.qualitySelection.grid(row=1, column=2, sticky=tk.W, padx=10)
        #----------------------------------
        #second frame ends

        # third frame
        self.additionalData = tk.Frame(self, width = 758, height = 50)
        # additionalData['bg'] = 'yellow'
        self.additionalData.grid_propagate(0)
        self.additionalData.grid(row=2, column=0, padx=20)

        self.des = tk.IntVar()
        self.meta = tk.IntVar()
        self.annot = tk.IntVar()
        self.sub = tk.IntVar()
        self.thumb = tk.IntVar()

        self.desChecked = tk.IntVar()
        self.description = tk.Checkbutton(self.additionalData, text = "Description", onvalue=1, offvalue=0, width=14, variable=self.desChecked)
        self.description.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)
        self.metChecked = tk.IntVar()
        self.metadata = tk.Checkbutton(self.additionalData, text = "Metadata", onvalue=1, offvalue=0, width=14, variable=self.metChecked)
        self.metadata.grid(row=0, column=1, sticky=tk.W, padx=10, pady=10)
        self.annChecked = tk.IntVar()
        self.annotation = tk.Checkbutton(self.additionalData, text = "Annotation", onvalue=1, offvalue=0, width=14, variable=self.annChecked)
        self.annotation.grid(row=0, column=2, sticky=tk.W, padx=10, pady=10)
        self.subChecked = tk.IntVar()
        self.subtitle = tk.Checkbutton(self.additionalData, text = "Subtitle", onvalue=1, offvalue=0, width=14, variable=self.subChecked)
        self.subtitle.grid(row=0, column=3, sticky=tk.W, padx=10, pady=10)
        self.thuChecked = tk.IntVar()
        self.thumbnail = tk.Checkbutton(self.additionalData, text = "Thumbnail", onvalue=1, offvalue=0, width=14, variable=self.thuChecked)
        self.thumbnail.grid(row=0, column=4, sticky=tk.W, padx=10, pady=10)
        #-------------------------------
        # third frame ends

        #fourth frame
        self.downloadFrame = tk.Frame(self, width=758, height=200)
        self.downloadFrame.grid(row=3, column=0, padx=20)

        self.downloadBtn = tk.Button(self.downloadFrame, text = "Download", command = self.preprocess)
        self.downloadBtn.pack()
        helv36 = tk.font.Font(family='Helvetica', size=14, weight='bold')
        self.downloadBtn['font'] = helv36
        #fourth frame ends

        # fifth frame
        self.outputFrame = tk.Frame(self, width = 758, height = 200)
        # outputFrame['bg'] = 'orange'
        self.outputFrame.grid_propagate(0)
        self.outputFrame.grid(row=4, column=0, padx=20)

        self.outputWindow = tk.Text(self.outputFrame, width=90, height=10, state=tk.DISABLED)
        self.outputWindow.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)

        # fifth frame ends

    # testing function for directory selection
    def preprocess(self):
        self.insertValue('Pre-Processing starts... \n')
        checkedRad = self.var.get()
        links = {}
        options = ""
        if(checkedRad == "1"):
            link = self.e1.get('1.0', 'end-1c')
            if(len(link) != 43):
                messagebox.showerror("Error", "Invalid youtube link")
                return

            string = link[-11:-1]
            string += link[-1]
            links[string] = link
            custName = self.customNameEntry.get()
            if(len(custName.strip()) > 0):
                links.pop(string)
                links[custName] = link

        else:
            filename = self.e2.get('1.0', 'end-1c')
            if(len(filename.strip()) == 0):
                messagebox.showerror("Error", "Please provide file name")
                return

            links = self.readFileContents(filename)

        print(links)

        options += ' -f "' + self.quality.get() + '"'

        if(self.desChecked.get()):
            options += " --write-description"

        if(self.metChecked.get()):
            options += " --write-info-json"

        if(self.annChecked.get()):
            options += " --write-annotations"

        if(self.subChecked.get()):
            options += " --write-sub"

        if(self.thuChecked.get()):
            options += " --write-thumbnail"

        if(len(self.location) > 0):
            options += ' -o "' + self.location + '/'

        else:
            options += ' -o "'

        finalLinks = []
        print(links)
        for link in links:
            finalLinks.append("youtube-dl" + options + link + '.mp4" ' + links[link])

        print(finalLinks)
        self.insertValue("Pre-processing ends... \n")
        self.downloadVid(finalLinks)

    def insertValue(self, string):
        self.outputWindow.configure(state="normal")
        self.outputWindow.insert("end", string)
        self.outputWindow.configure(state="disabled")
        self.outputWindow.update()

    def readFileContents(self, filename):
        try:
            f = open(filename, "r")
            data = f.read()
            data = data.split('\n')
            print(data)
            links = {}
            for query in data:
                query = query.replace(" ", "%20")
                res = request.urlopen('https://www.youtube.com/results?search_query='+query)
                pattern = re.compile(r'\"videoId\":\"(.){11}\"')
                search_results = pattern.finditer(str(res.read()))
                print("search ", type(search_results))
                for result in search_results:
                    string = result.group()[11:-1]
                    link = "https://www.youtube.com/watch?v="+string
                    links[string] = link
                    break

            return links

        except Exception as ex:
            messagebox.showerror("Error", "File does not exists")
            return

    def downloadVid(self, finalLinks):
        self.insertValue("Downloading starts... \n")
        for link in finalLinks:
            self.insertValue("Executing "+link+ " \n")
            errorCode = os.system(link)
            if(errorCode == 0):
                self.insertValue("Command executed successfully... \n")
            else:
                self.insertValue("Error while downloading video... \n")

        self.insertValue("Downloading ends... \n")

    def checkRadio(self):
        checkedRad = self.var.get()
        if(checkedRad == "1"):
            self.e2.configure(state="disabled")
            self.e1.configure(state="normal")
            self.customNameEntry.configure(state="normal")
        if(checkedRad == "2"):
            self.e2.configure(state="normal")
            self.e1.configure(state="disabled")
            self.customNameEntry.configure(state="disabled")


    def getDir(self):
        self.location = tk.filedialog.askdirectory()

class Frame2(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        tk.Frame.__init__(self, self.parent, width = 800, height = 500, borderwidth = 1)
        self.grid_propagate(0)

        # Frame for checkboxes and their respective entry widgets
        self.checkBoxFrame = tk.Frame(self, width = 758, height = 120, borderwidth = 1)
        # checkBoxFrame['bg'] = 'red'
        self.checkBoxFrame.grid_propagate(0)
        self.checkBoxFrame.grid(row=0, column=0, padx=20, pady=5)

        # portion of checkboxes

        self.var = tk.StringVar()
        self.r1 = tk.Radiobutton(self.checkBoxFrame, text = "Youtube link", variable = self.var, value = "1", command = self.checkRadio)
        self.r1.grid(row=0, column=0, sticky = tk.W, padx=10, pady=10)
        self.r2 = tk.Radiobutton(self.checkBoxFrame, text = "File Path", variable = self.var, value = "2", command = self.checkRadio)
        self.r2.grid(row=0, column=1, sticky = tk.W, padx=10, pady=10)
        self.var.set("1")

        # portion of entry widgets
        self.e1 = tk.Text(self.checkBoxFrame, width = 42, height=3)
        self.e1.grid(row=1, column=0, sticky = tk.W, padx=10, pady=5)
        self.e2 = tk.Text(self.checkBoxFrame, width = 42, height=3)
        self.e2.grid(row=1, column=1, sticky = tk.W, padx=10, pady=5)
        #-----------------------------------
        # First frame ends

        # second frame to get custom name, file directory location and dropdown
        self.secFrame = tk.Frame(self, width = 758, height = 70)
        # secFrame['bg'] = 'green'
        self.secFrame.grid_propagate(0)
        self.secFrame.grid(row=1, column=0, padx=20)

        ## row 1 of second frame
        self.customNameLabel = tk.Label(self.secFrame, text = "Provide custom name : ")
        self.customNameLabel.grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)

        self.fileLocLabel = tk.Label(self.secFrame, text = "Choose file location : ", width=23, anchor='w')
        self.fileLocLabel.grid(row=0, column=1, sticky=tk.W, padx=10, pady=5)
        ##---------------------------------

        # row2 of second frame
        self.customName = tk.StringVar()
        self.customNameEntry = tk.Entry(self.secFrame, width=55, textvariable = self.customName)
        self.customNameEntry.grid(row=1, column=0, sticky = tk.W, padx=10)

        self.askDirectoryBtn = tk.Button(self.secFrame, text = "select folder", command = self.getDir)
        self.askDirectoryBtn.grid(row=1, column=1, sticky=tk.W, padx=10)
        #----------------------------------
        #second frame ends

        #third frame
        self.downloadFrame = tk.Frame(self, width=758, height=200)
        self.downloadFrame.grid(row=3, column=0, padx=20)

        self.downloadBtn = tk.Button(self.downloadFrame, text = "Download", command = self.preprocess)
        self.downloadBtn.pack()
        self.helv36 = tk.font.Font(family='Helvetica', size=14, weight='bold')
        self.downloadBtn['font'] = self.helv36
        #third frame ends

        # fourth frame
        self.outputFrame = tk.Frame(self, width = 758, height = 250)
        # outputFrame['bg'] = 'orange'
        self.outputFrame.grid_propagate(0)
        self.outputFrame.grid(row=4, column=0, padx=20)

        self.outputWindow = tk.Text(self.outputFrame, width=90, height=13, state=tk.DISABLED)
        self.outputWindow.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)

        # fourth frame ends

        self.checkRadio()
        self.location = ""

    # testing function for directory selection
    def preprocess(self):
        self.insertValue('Pre-Processing starts... \n')
        checkedRad = self.var.get()
        links = {}
        options = " -x"
        if(checkedRad == "1"):
            link = self.e1.get('1.0', 'end-1c')
            if(len(link) != 43):
                messagebox.showerror("Error", "Invalid youtube link")
                return

            string = link[-11:-1]
            string += link[-1]
            links[string] = link
            custName = self.customNameEntry.get()
            if(len(custName.strip()) > 0):
                links.pop(string)
                links[custName] = link

        else:
            filename = self.e2.get('1.0', 'end-1c')
            if(len(filename.strip()) == 0):
                messagebox.showerror("Error", "Please provide file name")
            links = self.readFileContents(filename)

        print(links)

        if(len(self.location) > 0):
            options += ' -o "' + self.location + '/'

        else:
            options += ' -o "'

        finalLinks = []
        for link in links:
            finalLinks.append("youtube-dl" + options + link + '.mp3" ' + links[link])

        print(finalLinks)
        self.insertValue('Pre-Processing ends... \n')
        self.downloadVid(finalLinks)


    def readFileContents(self, filename):
        try:
            f = open(filename, "r")
            data = f.read()
            data = data.split('\n')
            links = {}
            for query in data:
                query = query.replace(" ", "%20")
                res = request.urlopen('https://www.youtube.com/results?search_query='+query)
                pattern = re.compile(r'\"videoId\":\"(.){11}\"')
                search_results = pattern.finditer(str(res.read()))
                for result in search_results:
                    string = result.group()[11:-1]
                    link = "https://www.youtube.com/watch?v="+string
                    links[string] = link
                    break

            return links

        except Exception as ex:
            messagebox.showerror("Error", "File does not exists")

    def downloadVid(self, finallinks):
        self.insertValue("Downloading starts... \n")
        for link in finallinks:
            self.insertValue("Executing "+link+ " \n")
            errorCode = os.system(link)
            if(errorCode == 0):
                self.insertValue("Command executed successfully... \n")
            else:
                self.insertValue("Error while downloading video... \n")

        self.insertValue("Downloading ends... \n")

    def insertValue(self, string):
        self.outputWindow.configure(state="normal")
        self.outputWindow.insert("end", string)
        self.outputWindow.configure(state="disabled")
        self.outputWindow.update()

    def getDir(self):
        self.location = tk.filedialog.askdirectory()

    def checkRadio(self):
        checkedRad = self.var.get()
        if(checkedRad == "1"):
            self.e2.configure(state="disabled")
            self.e1.configure(state="normal")
            self.customNameEntry.configure(state="normal")
        if(checkedRad == "2"):
            self.e2.configure(state="normal")
            self.e1.configure(state="disabled")
            self.customNameEntry.configure(state="disabled")


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

        self.downloadBtn = tk.Button(downloadFrame, text = "Download", command = self.preProcess)
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

    def preProcess(self):
        self.insertValue('Pre-Processing starts... \n')
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

        command = "youtube-dl -cit " + options + link
        print(command)
        self.insertValue('Pre-Processing ends... \n')
        self.downloadVid(command)

    def downloadVid(self, command):
        self.insertValue("Downloading starts... \n")
        self.insertValue("Executing " + command + " \n")
        errorCode = os.system(command)
        if (errorCode == 0):
            self.insertValue("Command executed successfully... \n")
        else:
            self.insertValue("Error while downloading playlist... \n")

        self.insertValue("Downloading ends... \n")

    def insertValue(self, string):
        self.outputWindow.configure(state="normal")
        self.outputWindow.insert("end", string)
        self.outputWindow.configure(state="disabled")
        self.outputWindow.update()

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




