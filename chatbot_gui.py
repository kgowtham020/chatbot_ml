import nltk
from nltk.chat.util import Chat, reflections
import tkinter as tk
from tkinter import scrolledtext

# Define your chatbot patterns and responses
chatbot_pairs = [
    (r"hi|hello|hey", ["Hello!", "Hi there!", "Hey! How can I assist you?"]),
    (r"bye|goodbye", ["Goodbye!", "See you later!", "Take care!"]),
    (r"how are you|how's it going", ["I'm just a chatbot, but I'm here to help!", "I'm doing well, thanks!"]),
    (r"tell me a joke", ["Why did the programmer quit his job? Because he didn't get arrays!", "Sure, here's one: Why do programmers prefer dark mode? Because light attracts bugs!"]),
    (r"what is your name", ["I'm your friendly chatbot!", "I don’t have a name, but I'm here to assist you!"]),
    (r"(.*) (help|assist)", ["Sure, I'm here to help you with whatever I can!", "How can I assist you today?"]),
]

# Initialize chatbot
chatbot = Chat(chatbot_pairs, reflections)

# Define the function to process user input and display responses
def get_response():
    user_input = user_entry.get()
    if user_input.lower() == "quit":
        app.destroy()
    else:
        chat_output.config(state='normal')
        chat_output.insert(tk.END, f"You: {user_input}\n")
        response = chatbot.respond(user_input)
        chat_output.insert(tk.END, f"Chatbot: {response}\n\n")
        chat_output.config(state='disabled')
        chat_output.yview(tk.END)  # Scroll to the bottom
        user_entry.delete(0, tk.END)

# Set up the main Tkinter window
app = tk.Tk()
app.title("Chatbot")
app.geometry("400x500")
app.config(bg="#2c3e50")  # Dark background for a sleek look

# Chat output display
chat_output = scrolledtext.ScrolledText(app, wrap=tk.WORD, state='disabled', bg="#ecf0f1", fg="#2c3e50", font=("Helvetica", 11))
chat_output.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# Input frame
input_frame = tk.Frame(app, bg="#2c3e50")
input_frame.pack(pady=10)

# Entry field for user input
user_entry = tk.Entry(input_frame, width=30, font=("Helvetica", 12))
user_entry.pack(side=tk.LEFT, padx=10)

# Send button
send_button = tk.Button(input_frame, text="Send", command=get_response, bg="#3498db", fg="white", font=("Helvetica", 12, "bold"))
send_button.pack(side=tk.LEFT)

# Run the main Tkinter loop
app.mainloop()
