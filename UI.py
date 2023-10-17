import tkinter as tk
import tkinter.font as tkFont


class App:
    def __init__(self, root):
        # various fonts used in the app
        title_font = tkFont.Font(family="Helvetica", size=20, weight="bold")
        input_font = tkFont.Font(family="Helvetica", size=12)
        output_font = tkFont.Font(family="Helvetica", size=15, weight="bold")

        # Setting title
        root.title("")

        # Setting window size
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        # Setting the icon to the transparent PNG
        icon = tk.PhotoImage(file="Icons/morse-code.png")
        root.iconphoto(False, icon)

        # Setting background color of app
        root.configure(bg="#E1AA74")

        # Create a frame with the desired border color (this will act as the border)
        border_frame = tk.Frame(root, bg="#FFFFFF")
        border_frame.pack(pady=5, padx=5)

        # Place the title label inside the frame
        title_label = tk.Label(border_frame, text="Text to Morse Converter",
                               font=title_font,
                               bg="#3876BF", fg="#FFFFFF", highlightthickness=0)
        title_label.pack(padx=3, pady=3)  # padding to define the width of the border

        # Frame to act as the border for the Text widget
        text_border_frame = tk.Frame(root, bg="#FFFFFF")
        text_border_frame.pack(pady=10, padx=20, fill=tk.X)

        # Text entry for user input placed inside the frame
        self.input_text = tk.Text(text_border_frame, height=10, wrap=tk.WORD, relief="solid", borderwidth=0,
                                  font=input_font,
                                  bg="#3876BF",  # background color
                                  fg="#FFFFFF")  # text color
        self.input_text.pack(padx=3, pady=3)  # padding to define the width of the border
        self.input_text.insert(tk.END, "Type the text you want converted here")
        self.input_text.bind("<FocusIn>", self.clear_default_text)

        # Frame to act as the border for the button
        button_border_frame = tk.Frame(root, bg="#FFFFFF")
        button_border_frame.pack(pady=5)

        # Convert button placed inside the frame
        convert_button = tk.Button(button_border_frame, text="Convert", command=self.convert_text,
                                   font=title_font, bg="#3876BF", fg="white",
                                   borderwidth=0, highlightthickness=0, relief="flat",
                                   activebackground="#3876BF", activeforeground="white", padx=2, pady=2, cursor="hand2")
        convert_button.pack(padx=3, pady=3)  # Padding determines border thickness
        # switch between the default and hover button backgrounds
        convert_button.bind("<Enter>", lambda e: convert_button.config(bg="#192655"))
        convert_button.bind("<Leave>", lambda e: convert_button.config(bg="#3876BF"))

        # Frame to act as the border for the Text widget
        output_text_border_frame = tk.Frame(root, bg="#FFFFFF")
        output_text_border_frame.pack(pady=10, padx=20, fill=tk.X)

        # Text widget for results placed inside the frame
        self.output_text = tk.Text(output_text_border_frame, height=10, wrap=tk.WORD, relief="solid", borderwidth=0,
                                   font=output_font, bg="#3876BF", fg="#FFFFFF")
        self.output_text.pack(padx=3, pady=3)  # padding to define the width of the border

        # Load both speaker icons
        speaker_image = tk.PhotoImage(file='Icons/speaker.png')
        speaker_hover_image = tk.PhotoImage(file='Icons/speaker_hover.png')

        speaker_label = tk.Label(root, image=speaker_image, text=" Sound", compound="left", cursor="hand2",
                                 bg="#E1AA74",
                                 fg="#FFFFFF", font=output_font)
        speaker_label.image = speaker_image
        speaker_label.hover_image = speaker_hover_image

        speaker_label.bind("<Button-1>", self.play_sound)

        # switch between the default and hover images and label backgrounds
        speaker_label.bind("<Enter>", lambda e: speaker_label.config(image=speaker_hover_image, fg="#192655"))
        speaker_label.bind("<Leave>", lambda e: speaker_label.config(image=speaker_image, fg="#FFFFFF"))

        speaker_label.place(x=10, y=268)  # Places it at the specified coordinates

    def clear_default_text(self, event=None):
        pass

    def convert_text(self, event=None):
        pass

    def play_sound(self, event=None):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
