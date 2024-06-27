import tkinter as tk
from tkinter import ttk, messagebox

from procesamiento_entrada.parsing import Parser
from procesamiento_entrada.lexema import Lexema
from procesamiento_entrada.tipo_token import TokenType


class AddLexeme(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.result = None

        # Configuración básica del diálogo
        self.title('Agregar lexema')
        self.geometry('400x300')

        # Variables para almacenar datos
        self.text = tk.StringVar()
        self.selected_token_type = tk.StringVar()
        self.weight = tk.IntVar()

        # Widgets del diálogo
        self.label = ttk.Label(self, text='Ingrese palabra o frase:')
        self.lineEdit = ttk.Entry(self, textvariable=self.text)

        self.label2 = ttk.Label(self, text='Token:')
        self.comboBox = ttk.Combobox(self, textvariable=self.selected_token_type)
        self.comboBox['values'] = [token_type.titulo for token_type in TokenType]
        self.comboBox.bind("<<ComboboxSelected>>", self.on_token_type_selected)

        self.label3 = ttk.Label(self, text='Seleccione un número del 0 al 5:')
        self.spinBox = ttk.Spinbox(self, from_=0, to=5, textvariable=self.weight)

        self.button_ok = ttk.Button(self, text='Aceptar', command=self.accept)
        self.button_cancel = ttk.Button(self, text='Cancelar', command=self.cancel)

        # Layout del diálogo
        self.label.pack(pady=5)
        self.lineEdit.pack(pady=5)
        self.label2.pack(pady=5)
        self.comboBox.pack(pady=5)
        self.label3.pack(pady=5)
        self.spinBox.pack(pady=5)
        self.button_ok.pack(pady=10, side=tk.LEFT, padx=10)
        self.button_cancel.pack(pady=10, side=tk.LEFT)

    def accept(self):
        try:
            # Obtén los datos ingresados por el usuario
            text = self.text.get()
            selected_title = self.selected_token_type.get()
            selected_token_type = next(token_type for token_type in TokenType if token_type.titulo == selected_title)
            weight = self.weight.get()
            parser = Parser(text)
            lexema = Lexema(parser.parse(), selected_token_type, weight)
            self.result = lexema
            self.destroy()
        except Exception as e:
            messagebox.showerror('Error', f'Error al procesar datos: {str(e)}')

    def on_token_type_selected(self, event):
        selected_token_title = self.selected_token_type.get()
        selected_token_type = next(
            (token_type for token_type in TokenType if token_type.titulo == selected_token_title), None)
        if selected_token_type:
            self.weight.set(selected_token_type.pesos_por_defecto())

    def cancel(self):
        self.result = None
        self.destroy()

    def get_data(self) -> Lexema:
        self.wait_window()
        return self.result
