import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk

from procesamiento_entrada.parsing import Parser
from procesamiento_entrada.procesamiento_archivo import FileManager
from procesamiento_entrada.tokenizador_minimo import MinimalTokenizer
from win.agregar_lexema import AddLexeme
from win.editar_lexema import EditLexeme


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.word = None
        self.title("Speech Analytics - MNLPTK")
        self.attributes('-zoomed', True)
        self.text = ""
        self.tokenized_words = []
        self.non_tokenized_words = []

        # Frame para la columna izquierda (botones y evaluación)
        self.left_frame = tk.Frame(self, bg='white')
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y, expand=True)

        # Frame para la columna derecha (tablas)
        self.right_frame = tk.Frame(self, bg='white')
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Botón para editar lexema
        self.edit_button = tk.Button(self.right_frame, text="Editar Lexema", command=self.edit_selected_lexeme)
        self.edit_button.pack(side=tk.RIGHT, pady=10)

        # Botón para abrir el diálogo de agregar lexema
        self.open_dialog_button = tk.Button(self.right_frame, text="Agregar Lexema", command=self.open_dialog)
        self.open_dialog_button.pack(side=tk.RIGHT, pady=10)

        self.non_tokenized_table = ttk.Treeview(self.right_frame, columns=("Palabra",), show="headings")

        self.tokenized_table = ttk.Treeview(self.right_frame, columns=("Id", "Palabra", "Tipo", "Peso"),
                                            displaycolumns=("Palabra", "Tipo", "Peso"), show="headings")
        self.tokenized_table.column(column="Id")

        # Botón para abrir el archivo
        self.open_button = tk.Button(self.left_frame, text="Abrir Archivo", command=self.open_file)
        self.open_button.pack(pady=10)

        # Área de texto para mostrar la evaluación y resultados
        self.text_display = scrolledtext.ScrolledText(self.left_frame, wrap=tk.WORD, width=80, height=20)
        self.text_display.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # Título para palabras tokenizadas
        self.tokenized_label = tk.Label(self.right_frame, text="Palabras Tokenizadas", font=('Arial', 14, 'bold'),
                                        justify="center")
        self.tokenized_label.pack(pady=10)

        # Crear la tabla para palabras tokenizadas
        self.create_tokenized_table()

        # Título para palabras no tokenizadas
        self.non_tokenized_label = tk.Label(self.right_frame, text="Palabras No Tokenizadas",
                                            font=('Arial', 14, 'bold'), justify="center")
        self.non_tokenized_label.pack(pady=10)
        # Crear la tabla para palabras no tokenizadas
        self.create_non_tokenized_table()

    def create_tokenized_table(self):
        self.tokenized_table.heading("Id", text="")
        self.tokenized_table.heading("Palabra", text="Palabra")
        self.tokenized_table.heading("Tipo", text="Tipo")
        self.tokenized_table.heading("Peso", text="Peso")
        self.tokenized_table.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    def create_non_tokenized_table(self):
        self.non_tokenized_table.heading("Palabra", text="Palabra")
        self.non_tokenized_table.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    def edit_selected_lexeme(self):
        selected_item = self.tokenized_table.selection()
        if selected_item:
            item = selected_item[0]
            word = self.tokenized_table.item(item, "values")
            print(str(word[0]))
            if word:
                self.word = word
                self.edit_lexeme()

    def open_file(self):
        filepath = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if not filepath:
            return

        with open(filepath, "r") as file:
            self.text = file.read()

        self.display_results()

    def display_results(self):
        try:
            self.tokenized_words = None
            self.non_tokenized_words = None

            parser = Parser(self.text)
            minimal_tokenizer = MinimalTokenizer(parser.parse())

            minimal_tokenizer.buscar_lexemas()
            self.text_display.delete(1.0, tk.END)
            self.text_display.insert(tk.END, self.text + "\n\n")
            self.text_display.insert(tk.END, "\nEvaluación:\n\n")

            if minimal_tokenizer.tiene_saludo:
                self.text_display.insert(tk.END, "Posee palabras tokenizadas de saludo\n\n")
            else:
                self.text_display.insert(tk.END, "No Posee palabras tokenizadas de saludo\n\n")

            if minimal_tokenizer.tiene_despedida:
                self.text_display.insert(tk.END, "Posee palabras tokenizadas de despedida\n\n")
            else:
                self.text_display.insert(tk.END, "No posse palabras tokenizadas de despedida\n\n")

            message, score = minimal_tokenizer.evaluacion
            self.text_display.insert(tk.END, f"Evaluación final: {message}\n")
            self.text_display.insert(tk.END, f"({score})\n\n")

            self.tokenized_words = minimal_tokenizer.tokenized_lex
            print("Tokenized Lexemas:")
            for lex in self.tokenized_words:
                print(str(lex) + ", ")
            self.non_tokenized_words = minimal_tokenizer.no_tokenized_lex

            # Limpiar y llenar la tabla de palabras tokenizadas
            self.tokenized_table.delete(*self.tokenized_table.get_children())

            for word in self.tokenized_words:
                self.insert_tokenized_word(word)

            # Limpiar y llenar la tabla de palabras no tokenizadas
            self.non_tokenized_table.delete(*self.non_tokenized_table.get_children())
            for word in self.non_tokenized_words:
                self.non_tokenized_table.insert("", "end", values=(word,))

        except ValueError as ve:
            messagebox.showerror("Error", f"Error de valor: {str(ve)}")

    def insert_tokenized_word(self, word):
        self.tokenized_table.insert("", "end", values=(word.id, word.lexemas, word.token.value,
                                                       word.peso))

    def edit_lexeme(self):
        dialog = EditLexeme(self, self.word)
        lexema = dialog.get_data()
        elimino = dialog.elimino
        if lexema is not None:
            FileManager.eliminar_lexemas(lexema.id)
            FileManager.actualizar_dictlexemas(lexema)
            self.display_results()
        elif elimino:
            self.display_results()

    def open_dialog(self):
        dialog = AddLexeme(self)
        lexema = dialog.get_data()
        if lexema is not None:
            FileManager.actualizar_dictlexemas(lexema)
            self.display_results()


if __name__ == "__main__":
    app = App()
    app.mainloop()
