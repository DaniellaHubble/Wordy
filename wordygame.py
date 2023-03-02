
"""
File: wordygame.py
Author: Daniella Hubble
Date: 5/12/22
Description: A Python/tkinter implementation of a game similar to the NYT Wordle.
"""

# Imports
import random
import tkinter as tk


class Wordy:
    def __init__(self):
        """ Initialize the game """
       
        # Constants
        self.i=0
        self.the_gueses={}
        self.start=False
        self.keybutton=[[]]
        self.guess_num=0
        self.curguess=""
        self.labels=[[]]
        self.curguess_letters=0
        self.secret_word=""
        self.done=False

        self.WORD_SIZE = 5  # number of letters in the hidden word
        self.NUM_GUESSES = 6  # number of guesses that the user gets
        self.LONG_WORDLIST_FILENAME = "long_wordlist.txt"
        self.SHORT_WORDLIST_FILENAME = "short_wordlist.txt"

        # Size of the frame that holds all guesses.  This is the upper left
        # frame in the window.
        self.PARENT_GUESS_FRAME_WIDTH = 750
        self.PARENT_GUESS_FRAME_HEIGHT = 500
        self.text2 = None
        
        # Parameters for an individual letter in the guess frame
        self.GUESS_FRAME_SIZE = 50  # the width and height of the guess box.
        self.GUESS_FRAME_PADDING = 3
        self.GUESS_FRAME_BG_BEGIN = 'white'  # background color of a guess box
       
        self.GUESS_FRAME_TEXT_BEGIN = 'black'  # color of text in guess box after the
        # user enters the letter, but before
        # the guess is entered.
        self.GUESS_FRAME_BG_WRONG = 'grey'  # background color of guess box
     
        self.GUESS_FRAME_BG_CORRECT_WRONG_LOC = 'orange'  # background color
        
        self.GUESS_FRAME_BG_CORRECT_RIGHT_LOC = 'green'  # background color
       
        self.GUESS_FRAME_TEXT_AFTER = 'white'  # color of text in guess box afterwards
        
        self.FONT_FAMILY = 'ariel'
        # Font size for letters in the guess boxes.
        self.FONT_SIZE_GUESS = 35

        self.on=True
        # Parameters for the keyboard frame
        self.KEYBOARD_FRAME_HEIGHT = 200
        self.KEYBOARD_BUTTON_HEIGHT = 2
        self.KEYBOARD_BUTTON_WIDTH = 3  # width of the letter buttons. 

        # width of the enter and back buttons.
        self.KEYBOARD_BUTTON_WIDTH_LONG = 5

       #color constants
        self.KEYBOARD_BUTTON_BG_BEGIN = 'white'
        self.KEYBOARD_BUTTON_TEXT_BEGIN = 'black'
        self.KEYBOARD_BUTTON_BG_WRONG = 'grey'
        self.KEYBOARD_BUTTON_BG_CORRECT_WRONG_LOC = 'orange'
        self.KEYBOARD_BUTTON_BG_CORRECT_RIGHT_LOC = 'green'
        self.KEYBOARD_BUTTON_TEXT_AFTER = 'white'

        self.KEYBOARD_BUTTON_NAMES = [
            ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
            ["A", "S", "D", "F", "G", "H", "J", "K", "L"],
            ["ENTER", "Z", "X", "C", "V", "B", "N", "M", "BACK"]]

        self.button_objs=self.KEYBOARD_BUTTON_NAMES[:]

        # Parameters for the control frame
        self.CONTROL_FRAME_HEIGHT = self.PARENT_GUESS_FRAME_HEIGHT + self.KEYBOARD_FRAME_HEIGHT
        self.CONTROL_FRAME_WIDTH = 300
      
        # Horizontal padding on either side of the widgets in
        self.USER_SELECTION_PADDING = 10
        # the parameter frame.

        self.MESSAGE_DISPLAY_TIME_SECS = 5  # Length of time the message should be
        # displayed.
        # When processing a guess 
        self.PROCESS_GUESS_WAITTIME = 1
       
       
       #methods for set up
        self.frames()
        self.keyboard_buttons()
        self.guess_frame_boxes()
        self.window.mainloop()

    def start_command(self):
        """handler for start button"""
        self.start=True
        #make sure user put in valid word
        if self.done==False:
            if self.specify_word.get() == True and len(self.entry_var.get()) != self.WORD_SIZE:
                self.screen_message_length()
                return
            elif self.specify_word.get() == True and (self.entry_var.get() not in self.shortlist):
                self.screen_message_not_word()
                return
            #get the word randomly
            elif self.specify_word.get() == False:
                self.secret_word = random.choice(self.longlist)
            
            #Start game based on user commands
            elif self.specify_word.get() == True:
                self.secret_word = self.entry_var.get()
            if self.specify_word.get() == True and len(self.secret_word) == self.WORD_SIZE and (self.secret_word in self.shortlist):
                self.entry_var.set("")
                self.guess_must_words_box['state'] = 'disabled'
                self.hard_mode_box['state'] = 'disabled'
                self.hidden_word_box['state'] = 'disabled'
            if self.show_word_parameter.get() == True:
                self.text2 = tk.Label(self.parameter_frame,
                                    text=self.secret_word)
                self.text2.grid(row=3, column=2)
            
        
            
                #disable boxes
            self.guess_must_words_box['state'] = 'disabled'
            self.hard_mode_box['state'] = 'disabled'
            self.hidden_word_box['state'] = 'disabled'
                

                #print values
            print("Hard mode=", self.hard_mode_parameter.get())
            print("Guesses must be words=", self.guess_must_words_parameter.get())
            print("Show word=", self.show_word_parameter.get())
            print("specify word= ", self.specify_word.get())
            print("Hidden word=", self.secret_word)
            

    def screen_message_length(self):
        """screen messages for bad input"""
        # bad length

        self.text1.destroy()
        if self.done==True:

            self.text1 = tk.Label(self.message_frame,
                                text="Incorrect specified word length")
            self.text1.grid(row=1, column=1, sticky=tk.W,
                            padx=self.USER_SELECTION_PADDING)
            self.message_frame.grid_rowconfigure(1, weight=1)
            self.window.after(self.MESSAGE_DISPLAY_TIME_SECS *
                            1000, self.text1.destroy)

    def screen_message_not_word(self):
        """For if word is not in list"""
       
        # bad word
        self.text1.destroy()
        self.text1 = tk.Label(self.message_frame,
                              text="Entry must be a valid word")
        self.text1.grid(row=1, column=1, sticky=tk.W,
                        padx=self.USER_SELECTION_PADDING)
        self.message_frame.grid_rowconfigure(1, weight=1)
        self.window.after(self.MESSAGE_DISPLAY_TIME_SECS *
                          1000, self.text1.destroy)

    def show_the_word(self):
        """handler for showng the word. can be toggled on and off"""
       
        #adjust based on if paremeter is true or not
        if self.show_word_parameter.get() == True:
            self.text2 = tk.Label(self.parameter_frame,
                                  text=self.secret_word)
            self.text2.grid(row=3, column=2)
        if self.show_word_parameter.get() == False:
            if self.text2 != None:
                self.text2.destroy()
            else:
                return

    def frames(self):
        """create frames"""
        self.window = tk.Tk()
        self.window.title("Wordy")

        # Create a frame.
        self.guess_frame = tk.Frame(self.window,
                                    borderwidth=1, relief='solid',
                                    height=self.PARENT_GUESS_FRAME_HEIGHT, width=self.PARENT_GUESS_FRAME_WIDTH)
        self.guess_frame.grid(row=1, column=1, sticky="")
        self.guess_frame.grid_propagate(False)

        # Put a frame to the right of it.
        self.keyboard_frame = tk.Frame(self.window,
                                       borderwidth=1, relief='solid',
                                       height=self.KEYBOARD_FRAME_HEIGHT, width=self.PARENT_GUESS_FRAME_WIDTH)
        self.keyboard_frame.grid(row=2, column=1)
        self.keyboard_frame.grid_propagate(False)

        # Put a frame below the top two.
        self.control_frame = tk.Frame(self.window,
                                      borderwidth=1, relief='solid',
                                      height=self.CONTROL_FRAME_HEIGHT, width=self.CONTROL_FRAME_WIDTH)
        self.control_frame.grid(row=1, column=2, rowspan=3)
        self.control_frame.grid_propagate(False)
        height_mult = 1/3

        #top control frame
        self.message_frame = tk.Frame(self.control_frame, borderwidth=1, relief='solid',
                                      height=height_mult * self.CONTROL_FRAME_HEIGHT, width=self.CONTROL_FRAME_WIDTH)
        self.message_frame.grid(row=1, column=1)
        self.message_frame.grid_rowconfigure(0, weight=1)
        self.message_frame.grid_rowconfigure(2, weight=1)
        self.message_frame.grid_columnconfigure(0, weight=1)
        self.message_frame.grid_columnconfigure(2, weight=1)
        self.message_frame.grid_propagate(False)

    #create the next frame below it
        self.parameter_frame = tk.Frame(self.control_frame, borderwidth=1, relief='solid',
                                        height=height_mult * self.CONTROL_FRAME_HEIGHT, width=self.CONTROL_FRAME_WIDTH)
        self.parameter_frame.grid(row=2, column=1)
        self.parameter_frame.grid_propagate(False)
    #create the botten right frame
        self.button_frame = tk.Frame(self.control_frame, borderwidth=1, relief='solid',
                                     height=height_mult * self.CONTROL_FRAME_HEIGHT, width=self.CONTROL_FRAME_WIDTH)
        self.button_frame.grid(row=3, column=1)
        self.button_frame.grid_propagate(False)

        self.boxes()
        self.start_stop()

    def boxes(self):
        """add widgets to the frames"""
        self.text1 = tk.Label(self.message_frame, text="")
        self.text1.grid(row=1, column=1, sticky=tk.W,
                        padx=self.USER_SELECTION_PADDING)
        self.message_frame.grid_rowconfigure(1, weight=1)

        # hard mode button
        self.hard_mode_parameter = tk.BooleanVar()
        self.hard_mode_parameter.set(False)
        self.hard_mode_box = tk.Checkbutton(self.parameter_frame, text="Hard mode",
                                            var=self.hard_mode_parameter)
        self.hard_mode_box.grid(
            row=1, column=1, sticky=tk.W, padx=self.USER_SELECTION_PADDING)

        # guess button
        self.guess_must_words_parameter = tk.BooleanVar()
        self.guess_must_words_parameter.set(True)
        self.guess_must_words_box = tk.Checkbutton(self.parameter_frame, text="Guess must be words",
                                                   var=self.guess_must_words_parameter)
        self.guess_must_words_box.grid(
            row=2, column=1, sticky=tk.W, padx=self.USER_SELECTION_PADDING)
        # show words button
        self.show_word_parameter = tk.BooleanVar()
        self.show_word_parameter.set(False)
        self.show_words_box = tk.Checkbutton(self.parameter_frame, text="Show word",
                                             var=self.show_word_parameter, command=self.show_the_word)
        self.show_words_box.grid(
            row=3, column=1, sticky=tk.W, padx=self.USER_SELECTION_PADDING)

        # hidden word
        self.specify_word = tk.BooleanVar()
        self.specify_word.set(False)
        self.hidden_word_box = tk.Checkbutton(self.parameter_frame, text="Specify word",
                                              var=self.specify_word)
        self.hidden_word_box.grid(
            row=4, column=1, sticky=tk.W, padx=self.USER_SELECTION_PADDING)

        self.configure()

    def configure(self):
        """space out buttons and create entry box"""
        # space buttons
        self.parameter_frame.grid_rowconfigure(0, weight=1)
        self.parameter_frame.grid_rowconfigure(1, weight=0)
        self.parameter_frame.grid_rowconfigure(2, weight=0)
        self.parameter_frame.grid_rowconfigure(3, weight=0)
        self.parameter_frame.grid_rowconfigure(4, weight=0)
        self.parameter_frame.grid_rowconfigure(5, weight=1)
        # entry
        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(self.parameter_frame,
                              textvariable=self.entry_var, width=5)
        self.entry.grid(row=4, column=2)

    def start_stop(self):
        """start/stop buttons and lists of the words"""
        self.longlist = []
        self.shortlist = []
        long_f = open('long_wordlist.txt')
        short_f = open('short_wordlist.txt')

        #create dictionaries
        for word in long_f:

            if len(word.strip()) == self.WORD_SIZE:
                self.longlist.append(word.strip())

        for word in short_f:
            if len(word.strip()) == self.WORD_SIZE:
                self.shortlist.append(word.strip())

        self.start = tk.Button(
            self.button_frame, text="Start Game", command=self.start_command)

        self.start.place(relx=.36, rely=.5, anchor=tk.CENTER)

        if self.show_word_parameter.get() == True:
            self.entry_var.set(self.secret_word)

        #quit button
        self.stop = tk.Button(self.button_frame, text="Quit",
                              command=self.stop_command)

        self.stop.place(relx=.64, rely=.5, anchor=tk.CENTER)

    def stop_command(self):
        """quit game"""
        self.window.destroy()

    def guess_frame_boxes(self):
        """boxes in guess frame"""

        #create boxes
        for r in range(self.NUM_GUESSES):
            for c in range(self.WORD_SIZE):
                frame = tk.Frame(self.guess_frame,
                                 bg=self.GUESS_FRAME_BG_BEGIN,
                                 height=self.GUESS_FRAME_SIZE,
                                 width=self.GUESS_FRAME_SIZE,
                                 relief="solid",
                                 borderwidth=1)

                frame.grid(row=r + 1, column=c + 1, padx=2, pady=2, sticky="")
        #put them in frames
                self.guess_frame.grid_rowconfigure(0, weight=1)
                self.guess_frame.grid_rowconfigure(7, weight=1)
                self.guess_frame.grid_columnconfigure(0, weight=1)
                self.guess_frame.grid_columnconfigure(6, weight=1)
                

    def keyboard_buttons(self):
        """buttons for keyboard"""
        self.buttons = {}

         # Create frames for the 3 keyboard rows
        self.row1=tk.Frame(self.keyboard_frame, height=self.KEYBOARD_FRAME_HEIGHT/3, width=self.PARENT_GUESS_FRAME_WIDTH)
        self.row1.grid(row=1,column=1)
        self.button_frame.grid_propagate(False)

        self.row2=tk.Frame(self.keyboard_frame, height=self.KEYBOARD_FRAME_HEIGHT/3, width=self.PARENT_GUESS_FRAME_WIDTH)
        self.row2.grid(row=2,column=1)
        self.button_frame.grid_propagate(False)

        self.row3=tk.Frame(self.keyboard_frame, height=self.KEYBOARD_FRAME_HEIGHT/3, width=self.PARENT_GUESS_FRAME_WIDTH)
        self.row3.grid(row=3,column=1)
        self.button_frame.grid_propagate(False)

        #create the button and connect to handlers
        for c in range(len(self.KEYBOARD_BUTTON_NAMES[0])):
            r=0
            def handler(key = self.KEYBOARD_BUTTON_NAMES[r][c]):
                self.button_handler(key)
            self.widthnum=self.KEYBOARD_BUTTON_WIDTH
                    
      

    def keyrows(self):
        """set up three rows of keys"""
            
        #first row
        button = tk.Button(self.row1,
                width = self.widthnum,
                text = self.KEYBOARD_BUTTON_NAMES[r][c],
                
                
                command = handler)
        button.grid(row = r + 1, column = c + 1)

            # Put the button in a dictionary of buttons
            # where the key is the button text, and the
            # value is the button object.
        self.buttons[self.KEYBOARD_BUTTON_NAMES[r][c]] = button
            
        #second row
        for c in range(len(self.KEYBOARD_BUTTON_NAMES[1])):
            r=1
            def handler(key = self.KEYBOARD_BUTTON_NAMES[r][c]):
                self.button_handler(key)
            self.widthnum=self.KEYBOARD_BUTTON_WIDTH
                    
            if self.KEYBOARD_BUTTON_NAMES[r][c]=="ENTER" or self.KEYBOARD_BUTTON_NAMES[r][c]=="BACK":
                self.widthnum=self.KEYBOARD_BUTTON_WIDTH_LONG


            button = tk.Button(self.row2,
                    width = self.widthnum,
                    text = self.KEYBOARD_BUTTON_NAMES[r][c],
                    
                
                    command = handler)
            button.grid(row = r + 1, column = c + 1)

                # Put the button in a dictionary of buttons
                # where the key is the button text, and the
                # value is the button object.
            self.buttons[self.KEYBOARD_BUTTON_NAMES[r][c]] = button
       
         #third row   
        for c in range(len(self.KEYBOARD_BUTTON_NAMES[2])):
            r=2
            def handler(key = self.KEYBOARD_BUTTON_NAMES[r][c]):
                self.button_handler(key)
            self.widthnum=self.KEYBOARD_BUTTON_WIDTH

            button = tk.Button(self.row3,
                    width = self.widthnum,
                    text = self.KEYBOARD_BUTTON_NAMES[r][c],
                   
                   
                    command = handler)
            button.grid(row = r + 1, column = c + 1)

               
            self.buttons[self.KEYBOARD_BUTTON_NAMES[r][c]] = button

   
            
        #configure
        self.keyboard_frame.rowconfigure(0, weight = 1)
        self.keyboard_frame.rowconfigure(len(self.KEYBOARD_BUTTON_NAMES) + 1, weight = 1)
        self.keyboard_frame.columnconfigure(0, weight = 1)
        self.keyboard_frame.columnconfigure(len(self.KEYBOARD_BUTTON_NAMES[0]) + 1, weight = 1)


        

        # Center the grid of buttons in the button frame
        self.keyboard_frame.grid_rowconfigure(0, weight=1)
        self.keyboard_frame.grid_rowconfigure(len(self.KEYBOARD_BUTTON_NAMES) + 1, weight=1)
        self.keyboard_frame.grid_columnconfigure(0, weight=1)
       
        self.keyboard_frame.grid_columnconfigure(len(self.KEYBOARD_BUTTON_NAMES[0]) + 1, weight=1)
   

    def configure(self):
        """space out buttons and create entry box"""
        # space buttons
        self.parameter_frame.grid_rowconfigure(0, weight=1)
        self.parameter_frame.grid_rowconfigure(1, weight=0)
        self.parameter_frame.grid_rowconfigure(2, weight=0)
        self.parameter_frame.grid_rowconfigure(3, weight=0)
        self.parameter_frame.grid_rowconfigure(4, weight=0)
        self.parameter_frame.grid_rowconfigure(5, weight=1)
       
        # entry
        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(self.parameter_frame,
                              textvariable=self.entry_var, width=5)
        self.entry.grid(row=4, column=2)

  

    def guess_frame_boxes(self):
        """make guess frame boxes"""
        self.wordboxes={}
        
        #boxes for specified size
        for r in range(self.NUM_GUESSES):
            for c in range(self.WORD_SIZE):
                frame = tk.Frame(self.guess_frame,
                                 bg=self.GUESS_FRAME_BG_BEGIN,
                                 height=self.GUESS_FRAME_SIZE,
                                 width=self.GUESS_FRAME_SIZE,
                                 relief="solid",
                                 borderwidth=1)

                frame.grid(row=r + 1, column=c + 1, padx=2, pady=2, sticky="")

                #configure
                self.guess_frame.grid_rowconfigure(0, weight=1)
                self.guess_frame.grid_rowconfigure(7, weight=1)
                self.guess_frame.grid_columnconfigure(0, weight=1)
                self.guess_frame.grid_columnconfigure(6, weight=1)
                self.wordboxes[(r,c)] = frame
              

    def keyboard_buttons(self):
        self.buttons = {}
       
        
         # Create frames for the keyboard rows
        self.row1=tk.Frame(self.keyboard_frame, height=self.KEYBOARD_FRAME_HEIGHT/3, width=self.PARENT_GUESS_FRAME_WIDTH)
        self.row1.grid(row=1,column=1)
        self.button_frame.grid_propagate(False)

        self.row2=tk.Frame(self.keyboard_frame, height=self.KEYBOARD_FRAME_HEIGHT/3, width=self.PARENT_GUESS_FRAME_WIDTH)
        self.row2.grid(row=2,column=1)
        self.button_frame.grid_propagate(False)

        self.row3=tk.Frame(self.keyboard_frame, height=self.KEYBOARD_FRAME_HEIGHT/3, width=self.PARENT_GUESS_FRAME_WIDTH)
        self.row3.grid(row=3,column=1)
        self.button_frame.grid_propagate(False)

        #handler and buttons
        for c in range(len(self.KEYBOARD_BUTTON_NAMES[0])):
            r=0
            def handler(key = self.KEYBOARD_BUTTON_NAMES[r][c]):
                self.button_handler(key)
            self.widthnum=self.KEYBOARD_BUTTON_WIDTH
                    
          

            button = tk.Button(self.row1,
                    width = self.widthnum,
                    text = self.KEYBOARD_BUTTON_NAMES[r][c],
                   
                    command = handler)
            button.grid(row = r + 1, column = c + 1)

                # Put the button in a dictionary of buttons
                # where the key is the button text, and the
                # value is the button object.
            self.buttons[self.KEYBOARD_BUTTON_NAMES[r][c]] = button
            

        for c in range(len(self.KEYBOARD_BUTTON_NAMES[1])):
            r=1
            def handler(key = self.KEYBOARD_BUTTON_NAMES[r][c]):
                self.button_handler(key)
            self.widthnum=self.KEYBOARD_BUTTON_WIDTH
                    
            if self.KEYBOARD_BUTTON_NAMES[r][c]=="ENTER" or self.KEYBOARD_BUTTON_NAMES[r][c]=="BACK":
                self.widthnum=self.KEYBOARD_BUTTON_WIDTH_LONG

            button = tk.Button(self.row2,
                    width = self.widthnum,
                    text = self.KEYBOARD_BUTTON_NAMES[r][c],
                    
                    #font=self.FONT,
                    command = handler)
            button.grid(row = r + 1, column = c + 1)

                # Put the button in a dictionary of buttons
                # where the key is the button text, and the
                # value is the button object.
            self.buttons[self.KEYBOARD_BUTTON_NAMES[r][c]] = button
            
        for c in range(len(self.KEYBOARD_BUTTON_NAMES[2])):
            r=2
            def handler(key = self.KEYBOARD_BUTTON_NAMES[r][c]):
                self.button_handler(key)
            self.widthnum=self.KEYBOARD_BUTTON_WIDTH
                    
            if self.KEYBOARD_BUTTON_NAMES[r][c]=="ENTER" or self.KEYBOARD_BUTTON_NAMES[r][c]=="BACK":
                self.widthnum=self.KEYBOARD_BUTTON_WIDTH_LONG


            button = tk.Button(self.row3,
                    width = self.widthnum,
                    text = self.KEYBOARD_BUTTON_NAMES[r][c],
                   
                  
                    command = handler)
            button.grid(row = r + 1, column = c + 1)

                # Put the button in a dictionary of buttons
                # where the key is the button text, and the
                # value is the button object.
            self.buttons[self.KEYBOARD_BUTTON_NAMES[r][c]] = button

   
        #configure
            
        self.keyboard_frame.rowconfigure(0, weight = 1)
        self.keyboard_frame.rowconfigure(len(self.KEYBOARD_BUTTON_NAMES) + 1, weight = 1)
        self.keyboard_frame.columnconfigure(0, weight = 1)
        self.keyboard_frame.columnconfigure(len(self.KEYBOARD_BUTTON_NAMES[0]) + 1, weight = 1)    
        self.buttons[self.KEYBOARD_BUTTON_NAMES[r][c]] = button

       
        # Center the grid of buttons in the button frame
        self.keyboard_frame.grid_rowconfigure(0, weight=1)
        self.keyboard_frame.grid_rowconfigure(len(self.KEYBOARD_BUTTON_NAMES) + 1, weight=1)
        self.keyboard_frame.grid_columnconfigure(0, weight=1)
       
        self.keyboard_frame.grid_columnconfigure(len(self.KEYBOARD_BUTTON_NAMES[0]) + 1, weight=1)
   
   
    def button_handler(self, texts):
        """
        handles keyboard press
        """
        if self.start==True and self.done==False:
            self.curguess=self.curguess.lower()
            themessage=""
            if self.on==True:
                #enter button
                if texts=="ENTER":
                    self.enter()
                    
                #deletes labels
                elif texts=="BACK":
                    if len(self.curguess)>=1:
                        self.curguess=self.curguess[0:-1]
                        self.curguess_letters-=1
                        temp=self.labels[self.guess_num].pop()
                        temp.destroy()
            
                #short word
                elif len(self.curguess)<self.WORD_SIZE:
                  
                    text1=tk.Label(self.wordboxes[(self.guess_num, self.curguess_letters)],text=texts,font=(self.FONT_FAMILY,self.FONT_SIZE_GUESS), bg="white",  width=2, padx=0, pady=2, height=0)
                
                    self.curguess=self.curguess+texts
                    self.curguess_letters+=1
                    self.labels[self.guess_num].append(text1)

                    text1.grid(row=1, column=1)
                    self.message_frame.grid_rowconfigure(1, weight = 1) 
        elif(self.done==True):
            themessage="Please quit, then restart."
        else:
            themessage="Please start the game."
            self.text1=tk.Label(self.message_frame,text=themessage )
            self.text1.grid(row=1, column=1, sticky=tk.W, padx=self.USER_SELECTION_PADDING)
            self.message_frame.grid_rowconfigure(1, weight = 1)
            self.window.after(self.MESSAGE_DISPLAY_TIME_SECS*1000, self.text1.destroy)
            

    def enter(self):
        """enter button actions"""
        themessage=""
        if len(self.curguess)<self.WORD_SIZE:
            themessage="Word not finished."
       
        #game over
        elif self.guess_num==self.NUM_GUESSES-1:
            self.process_guess()  
            themessage="Guesses used up. Word was "+self.secret_word+". Game over."
            self.the_gueses={}
            self.done=True
            tk.wind

            
        elif self.guess_num<self.NUM_GUESSES:
            themessage=self.checkword()
            #game is ended
        else:
            pass

        #centered messgae
        self.text1=tk.Label(self.message_frame,text=themessage )
        self.text1.grid(row=1, column=1, sticky=tk.W, padx=self.USER_SELECTION_PADDING)
        self.window.after(self.MESSAGE_DISPLAY_TIME_SECS*1000, self.text1.destroy)
        self.labels.append([])
  
    def checkword(self):
        """Check if the word is valid if guesses must be words and in general"""
        themessage=""
        #guesses must be words handler
        if len(self.curguess)==self.WORD_SIZE and self.guess_must_words_parameter.get()==True and (self.curguess not in self.longlist):
            self.text1=tk.Label(self.message_frame,text=" "+self.curguess+" is not in word list." )
            self.text1.grid(row=1, column=1, sticky=tk.W, padx=self.USER_SELECTION_PADDING)
            self.message_frame.grid_rowconfigure(1, weight = 1)
            self.window.after(self.MESSAGE_DISPLAY_TIME_SECS*1000, self.text1.destroy)

        #just clicking enter in a row
        elif len(self.curguess)==0:
            pass
        #True guess 
        elif len(self.curguess)==self.WORD_SIZE:
           
            
            if self.curguess==self.secret_word:
                self.curguess_letters=0                   
                self.process_guess()
                self.guess_num+=1
                self.lastguess=self.curguess
                self.curguess=""
                self.on==False
                themessage="Correct. Nice Job! Game Over."
                self.the_gueses={}
                self.curguess="      "
     

            else: 
                themessage="Valid guess"
                self.process_guess()
                    
                self.curguess_letters=0
                self.guess_num+=1
                self.curguess=""
        #self.curguess_letters=0 
        return themessage

        #if enter button
    def process_guess(self):
        """process completed guess"""
        self.count_letters=self.check_duplicates()
        self.i=0
        while self.i!=-1:
            self.window.after(self.PROCESS_GUESS_WAITTIME*1000, self.pros_word(self.i))
            self.window.update()
        self.count_letters=None
        self.i=0
        self.curguess=""
   

    def pros_word(self, i):
        """process each of the guess letters"""
      
        #correct letter and placing
        if self.curguess[i].lower()==self.secret_word[i]:
           
            self.buttons[self.curguess[i].upper()]["fg"]="green"
            self.labels[self.guess_num][i]["fg"]="green"
      
            
        #coreect letter but wrong placing
        elif (self.curguess[i].lower() in self.secret_word and self.count_letters[self.curguess[i].lower()]>0 and self.hard_mode_parameter.get()==False):
            self.window.update()
            self.labels[self.guess_num][i]["fg"]="orange"
            self.buttons[self.curguess[i].upper()]["fg"]="orange"
            self.count_letters[self.curguess[i].lower()]-=1
         
        else:
            
            self.labels[self.guess_num][i]["fg"]="gray"
            self.buttons[self.curguess[i].upper()]["fg"]="gray"
      
        if i+1<self.WORD_SIZE:    
            self.i=self.i+1
            
        else:
            self.i= -1


    def check_duplicates(self):
        """get dictionary of how many copies of the letters there are in a word"""
        count_letter={}

        #iterate through the secret word/guess word
        i=0
        for letter in self.secret_word:
            if letter not in count_letter.keys():
                count_letter[letter]=0

            #subtract 1 if the letter in the guess is in the correct spot  
            if self.curguess[i].lower()==self.secret_word[i]:
                count_letter[letter]-=1
              
            count_letter[letter]+=1
            i+=1
        
        return count_letter
                        
if __name__ == "__main__":
    Wordy()
