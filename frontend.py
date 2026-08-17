import customtkinter as ctk
from backend import review_code
import re

app = ctk.CTk()
app.title("AI Code Review Assistant")
app.geometry("1000x1000")

# Label above the input box
input_label = ctk.CTkLabel(app, text="Paste your code below:")
input_label.pack(pady=(10, 0))

# Text box for pasting code
code_input = ctk.CTkTextbox(app, width=700, height=300)
code_input.pack(pady=10)


# Removes common Markdown symbols so plain text displays cleanly
def clean_markdown(text):
    text = re.sub(r"```[a-zA-Z]*\n?", "", text)   # code block markers
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)   # bold **text**
    text = re.sub(r"#{1,6}\s*", "", text)          # headers
    text = re.sub(r"^\s*[-*]\s+", "- ", text, flags=re.MULTILINE)  # bullet points
    text = re.sub(r"\$(.*?)\$", r"\1", text)       # LaTeX math notation like $O(1)$
    text = text.replace("\\mathcal{O}", "O")       # LaTeX big-O notation
    text = text.replace(""", '"').replace(""", '"')  # smart double quotes
    text = text.replace("'", "'").replace("'", "'")  # smart single quotes
    return text


# Runs when the "Review Code" button is clicked
def on_review_click():
    code = code_input.get("1.0", "end")
    result = review_code(code)
    result = clean_markdown(result)

    output_box.configure(state="normal")
    output_box.delete("1.0", "end")
    output_box.insert("1.0", result)
    output_box.configure(state="disabled")


# Review button
review_button = ctk.CTkButton(app, text="Review Code", command=on_review_click)
review_button.pack(pady=10)

# Label above the output box
output_label = ctk.CTkLabel(app, text="Review:")
output_label.pack(pady=(10, 0))

# Output box to display Gemini's review
output_box = ctk.CTkTextbox(app, width=700, height=700)
output_box.pack(pady=10)
output_box.configure(state="disabled")

app.mainloop()