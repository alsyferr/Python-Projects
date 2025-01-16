from tkinter import *
from tkinter import ttk, messagebox
import googletrans
from textblob import TextBlob  # Import is case-sensitive

# Initialize main window
root = Tk()
root.title("Translator")
root.geometry("1080x400")

def label_change(event=None):
    c = combo1.get()
    c1 = combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)

def translate_now():
    global language
    try:
        text_ = text1.get(1.0, END).strip()
        c2 = combo1.get()
        c3 = combo2.get()
        if not text_:
            messagebox.showerror("Input Error", "Input text cannot be empty!")
            return
        if c3 == "SELECT LANGUAGE":
            messagebox.showerror("Selection Error", "Please select a target language!")
            return

        words = TextBlob(text_)
        detected_lang = words.detect_language()
        
        target_lang = None
        for key, value in language.items():
            if value == c3:
                target_lang = key
                break

        if not target_lang:
            messagebox.showerror("Language Error", "Invalid target language selected!")
            return

        translated_words = words.translate(from_lang=detected_lang, to=target_lang)
        text2.delete(1.0, END)
        text2.insert(END, translated_words)
    except Exception as e:
        messagebox.showerror("Translation Error", f"An error occurred: {e}")

# Initialize arrow image
arrow_image = PhotoImage(file="arrow.png")
image_label = Label(root, image=arrow_image, width=150)
image_label.place(x=460, y=50)

# Languages
language = googletrans.LANGUAGES
languageV = list(language.values())

# Combobox for source language
combo1 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="readonly")
combo1.place(x=110, y=20)
combo1.set("ENGLISH")

label1 = Label(root, text="ENGLISH", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label1.place(x=10, y=50)

# Frame for input text
f = Frame(root, bg="Black", bd=5)
f.place(x=10, y=118, width=440, height=210)

text1 = Text(f, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=430, height=200)

scrollbar1 = Scrollbar(f)
scrollbar1.pack(side="right", fill="y")
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# Combobox for target language
combo2 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="readonly")
combo2.place(x=730, y=20)
combo2.set("SELECT LANGUAGE")
combo2.bind("<<ComboboxSelected>>", label_change)

label2 = Label(root, text="SELECT LANGUAGE", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label2.place(x=620, y=50)

# Frame for translated text
f1 = Frame(root, bg="Black", bd=5)
f1.place(x=620, y=118, width=440, height=210)

text2 = Text(f1, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=430, height=200)

scrollbar2 = Scrollbar(f1)
scrollbar2.pack(side="right", fill="y")
scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

# Translate Button
translate = Button(root, text="Translate", font="Roboto 15 bold italic",
                   activebackground="purple", cursor="hand2", bd=5,
                   bg='red', fg="white", command=translate_now)
translate.place(x=480, y=250)

# Set background color
root.configure(bg="white")
root.mainloop()
