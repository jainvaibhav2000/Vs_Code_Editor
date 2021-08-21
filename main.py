from tkinter import*
from PIL import ImageTk
from tkinter import messagebox, filedialog
import subprocess
import os
class Vs_code:
    def __init__(self,root):
        self.root = root
        self.root.title("Untitle- VS Editor - Developed By Vaibhav")
        self.root.geometry("1200x700+0+0")

        self.path_name = ""
        self.color_theme = StringVar()
        self.color_theme.set('Light Default')
        self.font_size = 18
        self.file_name=""
        # ==============Menus Icons============
        self.new_icon = ImageTk.PhotoImage(file="icons/new.png")
        self.open_icon = ImageTk.PhotoImage(file="icons/Open-file-icon.png")
        self.save_icon = ImageTk.PhotoImage(file="icons/1save-icon.png")
        self.save_as_icon = ImageTk.PhotoImage(file="icons/2save-as-icon.png")
        self.exit_icon = ImageTk.PhotoImage(file="icons/exit-icon.png")

        self.light_default = ImageTk.PhotoImage(file="icons/default.jpg")
        self.light_plus = ImageTk.PhotoImage(file="icons/light_plus.jpg")
        self.dark = ImageTk.PhotoImage(file="icons/dark.jpg")
        self.red = ImageTk.PhotoImage(file="icons/red.jpg")
        self.monokai = ImageTk.PhotoImage(file="icons/monaki.jpg")
        self.night_blue = ImageTk.PhotoImage(file="icons/nightblue.jpg")

        #==============Menus============
        Mymenu=Menu(self.root)
        Filemenu=Menu(Mymenu, tearoff=False)
        Filemenu.add_command(label="New File", image=self.new_icon,compound=LEFT, accelerator="Ctl+N", command=self.new_file)
        Filemenu.add_command(label="Open File", image=self.open_icon,compound=LEFT, accelerator="Ctl+O", command=self.open_file)
        Filemenu.add_command(label="Save File", image=self.save_icon,compound=LEFT, accelerator="Ctl+S", command=self.save_file)
        Filemenu.add_command(label="Save As File", image=self.save_as_icon,compound=LEFT, accelerator="Ctl+Alt+S", command=self.save_as_file)
        Filemenu.add_command(label="Exit File", image=self.exit_icon,compound=LEFT, accelerator="Ctl+Q", command=self.exit_file)

        color_theme = Menu(Mymenu, tearoff=False)
        color_theme.add_radiobutton(label="Light Default", value='Light Default', variable=self.color_theme, image=self.light_default, compound=LEFT, command=self.color_change)
        color_theme.add_radiobutton(label="Light Plus", value='Light Plus', variable=self.color_theme, image=self.light_plus, compound=LEFT, command=self.color_change)
        color_theme.add_radiobutton(label="Dark", value='Dark', variable=self.color_theme, image=self.dark, compound=LEFT, command=self.color_change)
        color_theme.add_radiobutton(label="Red", value='Red', variable=self.color_theme, image=self.red, compound=LEFT, command=self.color_change)
        color_theme.add_radiobutton(label="Monokai", value='Monokai', variable=self.color_theme, image=self.monokai, compound=LEFT, command=self.color_change)
        color_theme.add_radiobutton(label="Night Blue", value='Night Blue', variable=self.color_theme, image=self.night_blue, compound=LEFT, command=self.color_change)

        Mymenu.add_cascade(label="File", menu=Filemenu)
        Mymenu.add_cascade(label="Color Theme", menu=color_theme)
        Mymenu.add_command(label="Clear", command=self.clear)
        Mymenu.add_separator()
        Mymenu.add_command(label="Run", command=self.run)
        self.root.config(menu=Mymenu)
        # =============== Menu End Here ===============

        # =========== Code Editor Frame ==========
        EditorFrame=Frame(self.root,bg="white")
        EditorFrame.place(x=0,y=0,relwidth=1,height=450)

        scrolly=Scrollbar(EditorFrame,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)

        self.text_editor=Text(EditorFrame,bg='white',font=("times new roman",self.font_size),yscrollcommand=scrolly.set)
        self.text_editor.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.text_editor.yview)

        # =========== Output Editor Frame ==========


        OutputFrame = LabelFrame(self.root,text="Output", bg="white", bd=3, font=("Arial",15))
        OutputFrame.place(x=0, y=450, relwidth=1, height=250)

        scrolly = Scrollbar(OutputFrame, orient=VERTICAL)
        scrolly.pack(side=RIGHT, fill=Y)

        self.text_output = Text(OutputFrame, bg='white', font=("times new roman", 17), yscrollcommand = scrolly.set)
        self.text_output.pack(fill=BOTH, expand=1)
        scrolly.config(command=self.text_output.yview)

    # ========================== shortcuts ========================
        self.root.bind('<Control-plus>',self.font_size_inc)
        self.root.bind('<Control-minus>', self.font_size_dec)
        self.root.bind('<Control-n>', self.new_file)
        self.root.bind('<Control-o>', self.open_file)
        self.root.bind('<Control-s>', self.save_file)
        self.root.bind('<Control-Alt-s>', self.save_as_file)
        self.root.bind('<Control-q>', self.exit_file)
# ========================== All Functions ========================
    def font_size_inc(self,event=None):
        self.font_size+=1
        self.text_editor.config(font=('times new roman',self.font_size))

    def font_size_dec(self,event=None):
        self.font_size-=1
        self.text_editor.config(font=('times new roman',self.font_size))

    def new_file(self,event=None):
        self.path_name=""
        self.file_name = ""
        self.root.title("Untitle- VS Editor - Developed By Vaibhav")
        self.text_editor.delete('1.0', END)
        self.text_output.delete('1.0', END)

    def open_file(self,event=None):
        path = filedialog.askopenfilename(filetype=[('Python Files', '*.py')], defaultextension=('.py'))
        if path!="":
            info = os.path.split(path)
            self.file_name = info[1]
            self.root.title(f"{self.file_name}- VS Editor - Developed By Vaibhav")
            self.path_name = path
            fp = open(self.path_name, "r")
            data=fp.read()
            self.text_editor.delete("1.0", END)
            self.text_editor.insert('1.0', data)
            fp.close()

    def save_file(self,event=None):
        if self.path_name=="" and self.file_name=="":
            self.save_as_file()
        else:
            fp=open(self.path_name, 'w')
            fp.write(self.text_editor.get('1.0',END))
            fp.close()

    def save_as_file(self,event=None):
        path = filedialog.asksaveasfilename(filetype=[('Python Files', '*.py')], defaultextension=('.py'))
        if path!="":
            info = os.path.split(path)
            self.file_name = info[1]
            self.root.title(f"{self.file_name}- VS Editor - Developed By Vaibhav")
            self.path_name = path
            fp = open(self.path_name, "w")
            fp.write(self.text_editor.get('1.0',END))
            fp.close()

    def exit_file(self,event=None):
        if messagebox.askokcancel('Confirm Exit','Are you sure want to exit Vs editor')==True:
            self.root.destroy()

    def color_change(self):
        if self.color_theme.get()=="Light Default":
            self.text_editor.config(bg='white', fg='black')
            self.text_output.config(bg='white', fg='black')
        elif self.color_theme.get()=="Light Plus":
            self.text_editor.config(bg='#e0e0e0', fg='#474747')
            self.text_output.config(bg='#e0e0e0', fg='#474747')
        elif self.color_theme.get()=="Dark":
            self.text_editor.config(bg='#2d2d2d', fg='#c4c4c4')
            self.text_output.config(bg='#2d2d2d', fg='#c4c4c4')
        elif self.color_theme.get()=="Red":
            self.text_editor.config(bg='#ffe8e8', fg='#2d2d2d')
            self.text_output.config(bg='#ffe8e8', fg='#2d2d2d')
        elif self.color_theme.get()=="Monokai":
            self.text_editor.config(bg='#d3b774', fg='#474747')
            self.text_output.config(bg='#d3b774', fg='#474747')
        elif self.color_theme.get()=="Night Blue":
            self.text_editor.config(bg='#6b9dc2', fg='#ededed')
            self.text_output.config(bg='#6b9dc2', fg='#ededed')

    def clear(self):
        self.text_editor.delete('1.0', END)
        self.text_output.delete('1.0', END)

    def run(self):
        if self.path_name=='':
            if messagebox.askokcancel('Error', 'Please save the file to execute the code',icon='error', parent=self.root)==True:
                self.save_file()
        else:

            command=f'python {self.path_name}'
            run_file=subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            #print(self.path_name,command)
            output, error=run_file.communicate()
            self.text_output.delete('1.0', END)
            self.text_output.insert('1.0',output)
            self.text_output.insert('1.0',error)

root=Tk()
obj=Vs_code(root)
root.mainloop()
