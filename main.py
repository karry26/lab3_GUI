from tkinter import *
from tkinter.filedialog import askopenfilename as opf

#from histgram import hist
#from keyword import keyword_check

global file_path 
global keyword_path 

file_path = ""
keyword_path = ""
	
def get_path(keyword):
	global file_path 
	global keyword_path 
	
	if keyword:
		keyword_path = opf()
	else:
		file_path = opf() 
		
	
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
		

	
def make_gui():

	box=Tk()
	box.title("LAP_LAB3")

		
	btn1 = Button(box, text="Load File", command=lambda: get_path(False))
	btn1.grid(column=0, row=0)
	btn2 = Button(box, text="Load Keyword File", command=lambda:get_path(True))
	btn2.grid(column=1, row=0)
	btn3 = Button(box, text="Edit File", command=lambda: edit_file(file_path))
	btn3.grid(column=2, row=0)
	btn4 = Button(box, text="Edit Keyword", command=lambda: edit_file(keyword_path))
	btn4.grid(column=3, row=0)
	
	btn5 = Button(box, text="Print Histogram", command=lambda: hist(file_path))
	btn5.grid(column=1, row=1)
	btn6 = Button(box, text="Keyword Check", command=lambda: keyword_check(file_path,keyword_path))
	btn6.grid(column=2, row=1)

	
	
	box.mainloop()
	
if __name__=="__main__":
	make_gui()
