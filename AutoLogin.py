from tkinter import *
from login_details import auto_login_details

def auto_login():
	"""Build an auto login page using GUI"""
	
	screen = Tk()
	screen.title("User Login Page")
	screen.geometry("300x250")
	
	Label(screen, text="Please enter login details").pack()
	Label(screen, text="").pack()
	
	#Declaring type of variable for entry.
	username = StringVar()
	password = StringVar()
	
	Label(screen, text="Username").pack()
	Entry(screen, textvariable = username).pack() #Creating entry widget to take value.
	Label(screen, text = "").pack()
	

	Label(screen, text = "Password").pack()
	Entry(screen, textvariable = password,show="*").pack()
	Label(screen, text = "").pack()
	
	#Creating button to call auto_login_details function.
	Button(screen, text = "Auto fill username and password",command = auto_login_details).pack()
	
	
	screen.mainloop()

auto_login()
