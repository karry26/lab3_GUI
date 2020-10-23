from tkinter import *
from tkinter.filedialog import askopenfilename as opf
from PIL import ImageTk,Image  

from histogram import hist
from keyword_check import keyword_check

file_path = ""
keyword_path = ""
	
#load the file
def get_path(keyword):
	global file_path 
	global keyword_path 
	
	if keyword:
		keyword_path = opf()
	else:
		file_path = opf()
		
#open an editor to edit the file
def edit_file(path):
		window = Tk()
		window.title("Editor")
		text_area = Text(window, padx=5, pady=5)
		text_area.pack()
		
		if path == "":
			text_area.insert(END,"Please select the File")
			exit = Button(window, text="Exit", command=lambda: window.destroy()).pack()
			
		else:
			file = open(path)
			for line in file:
				text_area.insert(END,line)
			file.close()
				
			save = Button(window, text="Save", command=lambda: save()).pack()
			
			def save():
				file = open(path, "w")
				new = text_area.get(1.0,END)
				file.write(new)
				file.close()
				window.destroy()
		
#Function to print the histogram of words
def print_hist():
	
	global file_path	
	
	hist_box = Tk()
	hist_box.title("Histogram")
	
	if file_path == "":
		Label(hist_box, text = "Please select file first!").pack()
		exit = Button(hist_box, text="Exit", command=lambda: hist_box.destroy()).pack()
		
	else:
		ans=[]
		hist(ans,file_path)
		
		canvas = Canvas(hist_box, width = 680, height = 420)
		canvas.pack()
		
		
		img = ImageTk.PhotoImage(Image.open("./histogram.png"), master = canvas) 
		canvas.create_image(0,0, anchor=NW, image=img)

		text = "Most frequent used word is : "+str(ans[0][0])+"\n"+"Least frequent used word is : "+str(ans[0][1])+"\n"+"Number of lines used in file: "+str(ans[0][2])
		
		label=Label(hist_box,text=text).pack()
		
		exit = Button(hist_box, text="Exit", command=lambda: hist_box.destroy()).pack()
		
		mainloop()
	
#Function to print the lines with keyword
def print_lines():

	global file_path
	global keyword_path
	
	lines_box = Tk()
	lines_box.title("Lines with Keywords")
	
	
	if file_path == "" or keyword_path == "":
		if file_path == "":
			Label(lines_box, text = "Please select file first!").pack()
		if keyword_path =="":
			Label(lines_box, text = "Please select Keyword file first!").pack()
		exit = Button(lines_box, text="Exit", command=lambda: lines_box.destroy()).pack()
		
	else:
		ans = []
		keyword_check(ans,file_path,keyword_path)
		
		text = ""
		
		for i in range(0,len(ans[0])):
			text = text + str(ans[0][i]) + "\n"
			
		label=Label(lines_box,text=text).pack()
		
		exit = Button(lines_box, text="Exit", command=lambda: lines_box.destroy()).pack()
	
	
# main UI
def make_gui():

	box=Tk()
	box.title("LAP_LAB3")

	load_file = Button(box,    text="Load File                ", command=lambda: get_path(False))
	load_file.grid(column=0, row=0)
	
	load_keyword = Button(box, text="Load Keyword File", command=lambda:get_path(True))
	load_keyword.grid(column=0, row=1)
	
	editFile = Button(box, text="Edit File        ", command=lambda: edit_file(file_path))
	editFile.grid(column=1, row=0)
	
	editKeywords = Button(box, text="Edit Keyword", command=lambda: edit_file(keyword_path))
	editKeywords.grid(column=1, row=1)
	
	histogram = Button(box, text="Print Histogram", command=lambda: print_hist())
	histogram.grid(column=2, row=0)
	
	lines = Button(box, text="Keyword Check", command=lambda: print_lines())
	lines.grid(column=2, row=1)
	
	exit = Button(box, text="Exit", command=lambda: box.destroy())
	exit.grid(column=1)
	
	box.mainloop()
	
	
	
if __name__=="__main__":
	make_gui()
	
