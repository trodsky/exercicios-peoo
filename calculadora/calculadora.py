import tkinter as tk

def press_key(key):
    current_expression = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_expression + str(key))

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Erro")

def clear():
    entry.delete(0, tk.END)

# Criando a janela principal
root = tk.Tk()
root.title("Calculadora")

# Entrada para exibir a expressão e o resultado
entry = tk.Entry(root, width=20, font=('Arial', 16), justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Botões
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, width=5, height=2, command=lambda b=button: press_key(b) if b != '=' else calculate()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Botão de limpar
tk.Button(root, text="C", width=5, height=2, command=clear).grid(row=row_val, column=col_val, columnspan=2)

# Iniciando a interface gráfica
root.mainloop()
