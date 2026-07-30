import customtkinter as ctk

app = ctk.CTk()
app.title("AI Code Review Assistant")
app.geometry("800x600")

# Label above the input box
input_label = ctk.CTkLabel(app, text="Paste your code below:")
input_label.pack(pady=(10, 0))

# Text box for pasting code
code_input = ctk.CTkTextbox(app, width=700, height=300)
code_input.pack(pady=10)

app.mainloop()