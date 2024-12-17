import re
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import nltk
from nltk.corpus import words

nltk.download("words")

class SpellingChecker:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Spelling Checker")
        self.root.geometry("600x600")
        
        self.text = ScrolledText(self.root, font=("Arial", 14))
        self.text.bind("<KeyRelease>", self.check)
        self.text.pack(expand=True, fill='both')

        self.root.mainloop()

    def check(self, event):
        content = self.text.get("1.0", tk.END).strip()
        for tag in self.text.tag_names():
            self.text.tag_delete(tag)

        words_list = content.split()
        for word in words_list:
            cleaned_word = re.sub(r"[^\w]", "", word.lower())
            if cleaned_word and cleaned_word not in words.words():
                start_idx = "1.0"
                while True:
                    start_idx = self.text.search(word, start_idx, stopindex=tk.END)
                    if not start_idx:
                        break
                    end_idx = f"{start_idx.split('.')[0]}.{int(start_idx.split('.')[1]) + len(word)}"
                    self.text.tag_add("misspelled", start_idx, end_idx)
                    start_idx = end_idx
                
        self.text.tag_config("misspelled", background="red")

SpellingChecker()
