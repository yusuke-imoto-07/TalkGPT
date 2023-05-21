import tkinter as tk
from tkinter import ttk
from gpt_api import get_answer

history = []

def main():
    root = tk.Tk()
    root.title('Talk GPT (gpt-4)')

    widgets = {}

    top_frame = tk.Frame(root)
    top_frame.pack(side="top", fill="x")

    # Add a new chat button
    def new_chat():
        clear_question(widgets)
        clear_answer(widgets)
        clear_history(widgets)

    new_chat_button = tk.Button(top_frame, text='New Chat', command=new_chat)
    new_chat_button.pack(side="left")

    frame = tk.Frame(root, padx=20, pady=20)
    frame.pack(side="left")

    question_frame = tk.Frame(frame)
    question_frame.pack(fill="x")

    question_label = tk.Label(question_frame, text="Question")
    question_label.pack(side="left")

    question_text = tk.Text(frame, width=70, height=20)
    question_text.pack()
    widgets["question_text"] = question_text

    clear_question_button = tk.Button(question_frame, text='Clear question', command=lambda: clear_question(widgets))
    clear_question_button.pack(side="right")

    submit_button = tk.Button(frame, text='Send question', command=lambda: ask_question(widgets))
    submit_button.pack(pady=20)

    result_frame = tk.Frame(frame)
    result_frame.pack(fill="x")

    result_label = tk.Label(result_frame, text="Answer from GPT")
    result_label.pack(side="left")

    result_text = tk.Text(frame, width=70, height=30)
    result_text.pack()
    widgets["result_text"] = result_text

    clear_answer_button = tk.Button(result_frame, text='Clear answer', command=lambda: clear_answer(widgets))
    clear_answer_button.pack(side="right")

    history_frame = tk.Frame(root, padx=20, pady=20)
    history_frame.pack(side="right")

    history_label_frame = tk.Frame(history_frame)
    history_label_frame.pack(fill="x")

    history_label = tk.Label(history_label_frame, text="History")
    history_label.pack(side="left")

    clear_history_button = tk.Button(history_label_frame, text='Clear history', command=lambda: clear_history(widgets))
    clear_history_button.pack(side="right")

    history_text = tk.Text(history_frame, width=70, height=60)
    history_text.pack()
    widgets["history_text"] = history_text

    root.mainloop()

def ask_question(widgets):
    result_text = widgets["result_text"]
    question_text = widgets["question_text"]

    global history
    result_text.delete("1.0", "end")
    question = question_text.get("1.0", tk.END).strip()

    # Prepare past messages to be passed to the chat model
    messages = [{"role": "user", "content": q} if i % 2 == 0 else {"role": "assistant", "content": a} for i, (q, a) in
                enumerate(history)]

    # Add the current question
    messages.append({"role": "user", "content": question})
    answer = get_answer(messages)
    result_text.insert(tk.END, answer + "\n")

    # Update the history of questions and answers
    history.append((question, answer))
    update_history(widgets)

    question_text.delete("1.0", "end")

def clear_question(widgets):
    question_text = widgets["question_text"]
    question_text.delete("1.0", "end")

def clear_answer(widgets):
    result_text = widgets["result_text"]
    result_text.delete("1.0", "end")

def clear_history(widgets):
    history_text = widgets["history_text"]
    global history
    history_text.delete("1.0", "end")
    history = []

def update_history(widgets):
    history_text = widgets["history_text"]
    history_text.delete("1.0", "end")
    for question, answer in history:
        history_text.insert(tk.END, f"Q: {question}\nA: {answer}\n\n")

if __name__ == "__main__":
    main()