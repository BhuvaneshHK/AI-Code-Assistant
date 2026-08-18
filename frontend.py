import customtkinter as ctk
from backend import review_code
from tkinter import filedialog
import re

from database import init_db, save_review

app = ctk.CTk()
app.title("AI Code Review Assistant")
app.geometry("800x750")

init_db()

# Label above the input box
input_label = ctk.CTkLabel(app, text="Paste your code below:")
input_label.pack(pady=(10, 0))

# Text box for pasting code
code_input = ctk.CTkTextbox(app, width=700, height=300)
code_input.pack(pady=10)


# Opens a file picker, reads the selected file, and loads it into the code box
def upload_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Code files", "*.py *.java *.cpp *.js *.cs *.txt"), ("All files", "*.*")]
    )
    if file_path:
        with open(file_path, "r") as f:
            content = f.read()
        code_input.delete("1.0", "end")
        code_input.insert("1.0", content)


# Upload button
upload_button = ctk.CTkButton(app, text="Upload File", command=upload_file)
upload_button.pack(pady=(0, 10))

# Language dropdown
language_menu = ctk.CTkOptionMenu(app, values=["Python", "Java", "C++", "JavaScript", "C#"])
language_menu.pack(pady=(0, 10))

# Status label (shows loading/progress messages)
status_label = ctk.CTkLabel(app, text="")
status_label.pack(pady=(0, 5))


# Removes common Markdown symbols so plain text displays cleanly
def clean_markdown(text):
    text = re.sub(r"```[a-zA-Z]*\n?", "", text)
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    text = re.sub(r"#{1,6}\s*", "", text)
    text = re.sub(r"^\s*[-*]\s+", "- ", text, flags=re.MULTILINE)
    text = re.sub(r"\$(.*?)\$", r"\1", text)
    text = text.replace("\\mathcal{O}", "O")
    text = text.replace(""", '"').replace(""", '"')
    text = text.replace("'", "'").replace("'", "'")
    return text


# Runs when the "Review Code" button is clicked
def on_review_click():
    status_label.configure(text="Reviewing... please wait")
    app.update()

    code = code_input.get("1.0", "end")
    language = language_menu.get()
    result = review_code(code, language=language)
    result = clean_markdown(result)

    output_box.configure(state="normal")
    output_box.delete("1.0", "end")
    output_box.insert("1.0", result)
    output_box.configure(state="disabled")

    save_review(code, language, result)

    status_label.configure(text="")


# Review button
review_button = ctk.CTkButton(app, text="Review Code", command=on_review_click)
review_button.pack(pady=10)

# Label above the output box
output_label = ctk.CTkLabel(app, text="Review:")
output_label.pack(pady=(10, 0))

# Output box to display Gemini's review
output_box = ctk.CTkTextbox(app, width=700, height=350)
output_box.pack(pady=10)
output_box.configure(state="disabled")

app.mainloop()