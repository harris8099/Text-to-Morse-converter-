import tkinter

FONT_NAME = "Courier"
BACKGROUND = "#FFE3CA"

window = tkinter.Tk()
window.title("Text to Morse convert")
window.geometry("470x300")
# window.minsize(width=600, height=300)
window.config(bg=BACKGROUND)


# label
label_1 = tkinter.Label(text="Text to morse convertor", font=(FONT_NAME, 24, "bold"))
label_1.grid(column=0, row=0, columnspan=2)
label_1.config(padx=15, pady=15, bg=BACKGROUND, foreground='white', background="#0C359E")

# for space
label_2 = tkinter.Label(text="", font=(FONT_NAME, 25))
label_2.grid(column=0, row=2, columnspan=2)
label_2.config(padx=5, pady=20, bg=BACKGROUND)

# label
label_3 = tkinter.Label(text="", font=(FONT_NAME, 15))
label_3.grid(column=0, row=3, columnspan=2)
label_3.config(padx=5, pady=5, bg=BACKGROUND, wraplength=300)

# Entry
entry = tkinter.Entry(width=50, takefocus=True)
entry.grid(column=0, row=2)
entry.config()


# button function
def button_clicked():
    label_3["text"] = text_morse(entry.get())
    entry.delete(0, tkinter.END)


# button
button = tkinter.Button(text="Convert", command=button_clicked)
button.grid(column=1, row=2)
button.config(cursor="cross", relief="groove", bg="#59D5E0")


# Main code
morse_code = {'A': '._', 'B': '_...', 'C': '_._.', 'D': '_..', 'E': '.', 'F': '.._.', 'G': '__.', 'H': '....',
              'I': '..', 'J': '.___', 'K': '_._', 'L': '._..', 'M': '__', 'N': '_.', 'O': '___', 'P': '.__.',
              'Q': '__._', 'R': '._.', 'S': '...', 'T': '_', 'U': '.._', 'V': '..._', 'W': '.__', 'X': '_.._',
              'Y': '_.__', 'Z': '__..', '0': '_____', '1': '.____', '2': '..___', '3': '...__', '4': '...._',
              '5': '.....', '6': '_....', '7': '__...', '8': '___..', '9': '____.'}


def text_morse(user_input):
    usr_input = user_input.upper().split()
    message = []
    try:
        for word in usr_input:
            for char in word:
                message.append(morse_code[char])
        return ' '.join(message)
    except KeyError:
        return "Please use Alphabet and number only!!"


window.mainloop()
