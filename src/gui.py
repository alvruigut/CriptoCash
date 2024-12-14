import tkinter as tk
from tkinter import ttk
from bank import Bank
from user import User
from merchant import Merchant
from database import Database

class CryptoCashApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CryptoCash - Sistema de Monedas Electrónicas")
        self.root.geometry("1100x770")

        self.bank = Bank()
        self.merchant = Merchant("Comercio A", self.bank)
        self.db = Database()

        self.user = None
        self.user_coin = None

        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(self.root, text="Sistema CryptoCash", font=("Arial", 16))
        title.pack(pady=10)

        user_frame = tk.Frame(self.root)
        user_frame.pack(pady=10)
        self.user_id_label = tk.Label(user_frame, text="Ingrese su ID de Usuario:")
        self.user_id_label.pack(side=tk.LEFT)
        self.user_id_entry = tk.Entry(user_frame)
        self.user_id_entry.pack(side=tk.LEFT)

        receiver_frame = tk.Frame(self.root)
        receiver_frame.pack(pady=10)
        self.receiver_user_id_label = tk.Label(receiver_frame, text="Seleccione el Usuario Destino:")
        self.receiver_user_id_label.pack(side=tk.LEFT)
        self.receiver_user_id_combobox = ttk.Combobox(receiver_frame, state="readonly")
        self.receiver_user_id_combobox['values'] = ("Comercio A", "Comercio B", "Comercio C")
        self.receiver_user_id_combobox.pack(side=tk.LEFT)

        self.withdraw_button = tk.Button(self.root, text="Retirar Moneda", compound="left", command=self.withdraw_coin, bg="lightgreen")
        self.withdraw_button.pack(pady=10)

        self.pay_button = tk.Button(self.root, text="Hacer Pago", command=self.send_coin, state=tk.DISABLED, bg="lightblue")
        self.pay_button.pack(pady=10)

        self.deposit_button = tk.Button(self.root, text="Depositar Moneda", command=self.deposit_coin, state=tk.DISABLED, bg="lightcoral")
        self.deposit_button.pack(pady=10)

        self.history_label = tk.Label(self.root, text="Historial de Transacciones:", font=("Arial", 12))
        self.history_label.pack(pady=10)

        self.transaction_tree = ttk.Treeview(self.root)
        self.transaction_tree["columns"] = ("ID", "Usuario Origen", "Usuario Destino", "ID de Moneda")
        self.transaction_tree.heading("ID", text="ID")
        self.transaction_tree.heading("Usuario Origen", text="Usuario Origen")
        self.transaction_tree.heading("Usuario Destino", text="Usuario Destino")
        self.transaction_tree.heading("ID de Moneda", text="ID de Moneda")
        self.transaction_tree.pack(pady=20)

        self.public_key_label = tk.Label(self.root, text=f"Clave Pública del Banco: {self.bank.get_public_key()}", font=("Arial", 8), wraplength=300)
        self.public_key_label.pack(pady=10)

        self.status_label = tk.Label(self.root, text="Bienvenido al sistema CryptoCash", font=("Arial", 10))
        self.status_label.pack(pady=20)

    def withdraw_coin(self):
        user_id = self.user_id_entry.get()
        if user_id:
            self.user = User(user_id, self.bank)
            self.user_coin = self.user.withdraw_coin()
            self.status_label.config(text="Moneda retirada exitosamente", fg="green")
            self.withdraw_button.config(state=tk.DISABLED)  # Deshabilitar el botón
            self.pay_button.config(state=tk.NORMAL)  # Habilitar el botón de pago
        else:
            self.show_error("Por favor, ingrese un ID de usuario.")



    def send_coin(self):
        if self.user_coin:
            receiver_user_id = self.receiver_user_id_combobox.get()  
            if receiver_user_id:
                is_valid, payment_message = self.bank.verify_coin(self.user_coin)
                if not is_valid:
                    self.show_error(payment_message)  
                    return
                payment_message = self.user.send_coin(self.user_coin, self.merchant, receiver_user_id)
                self.status_label.config(text=payment_message, fg="green") 
                self.deposit_button.config(state=tk.NORMAL)  # Habilitar el botón de depósito
                self.pay_button.config(state=tk.DISABLED)   # Deshabilitar el botón de pago
            else:
                self.show_error("Por favor, seleccione un Usuario Destino.")
        else:
            self.show_error("No se ha retirado ninguna moneda.")

    def deposit_coin(self):
        if self.user_coin:
            receiver_user_id = self.receiver_user_id_combobox.get() 
            deposit_message = self.merchant.deposit_coin(self.user_coin, self.user.user_id, receiver_user_id)
            self.status_label.config(text=deposit_message, fg="green")  
            self.deposit_button.config(state=tk.DISABLED)  # Deshabilitar el botón de depósito

            # Reactivar botones de "Retirar Moneda" y "Hacer Pago"
            self.withdraw_button.config(state=tk.NORMAL)
            self.pay_button.config(state=tk.NORMAL)

            self.update_transaction_history()
        else:
            self.show_error("No hay moneda para depositar.")




    def show_error(self, message):
        """Muestra un mensaje de error en la etiqueta de estado con color rojo."""
        self.status_label.config(text=message, fg="red")  
    def update_transaction_history(self):
        transactions = self.db.get_all_transactions()
        for row in self.transaction_tree.get_children():
            self.transaction_tree.delete(row)

        for transaction in transactions:
            self.transaction_tree.insert("", "end", values=transaction)

def run_app():
    root = tk.Tk()
    app = CryptoCashApp(root)
    root.mainloop()

if __name__ == "__main__":
    run_app()