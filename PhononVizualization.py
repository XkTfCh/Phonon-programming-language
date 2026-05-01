import tkinter as tk
from PhononInterpreter import run_code

window = tk.Tk()
window.title('Phonon')

tk.Label(window, text="Code:").pack(anchor=tk.W)
code_input = tk.Text(window, height=5, width=60)
code_input.pack()
code_input.insert('1.0', 'Put your code here')

tk.Label(window, text="User Input (for ',' command):").pack(anchor=tk.W)
user_input_field = tk.Entry(window, width=60)
user_input_field.pack()
user_input_field.insert(0, "Put your input here")

tk.Label(window, text="Output:").pack(anchor=tk.W)
output_text = tk.Text(window, height=10, width=60)
output_text.pack()

def run_program():
    code = code_input.get('1.0', tk.END).strip()
    user_input = user_input_field.get()
    
    result = run_code(code, user_input)
    
    output_text.insert(tk.END, f'> {result}\n')
    output_text.see(tk.END)

tk.Button(window, text='Run code', command=run_program).pack(pady=5)

window.mainloop()
