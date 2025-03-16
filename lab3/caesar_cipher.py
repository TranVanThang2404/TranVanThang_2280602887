import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.caesar import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)
    
    def call_api_encrypt(self):
        # Get the text and key input
        plain_text = self.ui.textEdit.toPlainText()  # This is the input field for plain text
        key = self.ui.textEdit_2.toPlainText()  # This is the key input field

        # Validate input text and key
        if not plain_text:
            self.show_error_message("Error", "Please enter the text to encrypt.")
            return

        if not key.isdigit():
            self.show_error_message("Error", "Key must be a valid integer.")
            return
        
        key = int(key)

        url = "http://127.0.0.1:5000/api/caesar/encrypt"
        payload = {
            "plain_text": plain_text,
            "key": key
        }

        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                # Update only the field for the encrypted message
                self.ui.textEdit_3.setText(data["encrypted_message"])  # This is the field for encrypted message

                self.show_info_message("Encrypted Successfully")
            else:
                self.show_error_message("Error", "Error while calling API.")
        except requests.exceptions.RequestException as e:
            self.show_error_message("Request Error", f"An error occurred: {e}")

    def call_api_decrypt(self):
        # Get the text and key input
        cipher_text = self.ui.textEdit_3.toPlainText()  # This is the input field for cipher text
        key = self.ui.textEdit_2.toPlainText()  # This is the key input field

        # Validate input text and key
        if not cipher_text:
            self.show_error_message("Error", "Please enter the text to decrypt.")
            return

        if not key.isdigit():
            self.show_error_message("Error", "Key must be a valid integer.")
            return
        
        key = int(key)

        url = "http://127.0.0.1:5000/api/caesar/decrypt"
        payload = {
            "cipher_text": cipher_text,
            "key": key
        }

        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                # Update only the field for the decrypted message
                self.ui.textEdit.setText(data["decrypted_message"])  # This is the field for decrypted message

                self.show_info_message("Decrypted Successfully")
            else:
                self.show_error_message("Error", "Error while calling API.")
        except requests.exceptions.RequestException as e:
            self.show_error_message("Request Error", f"An error occurred: {e}")

    def show_error_message(self, title, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle(title)
        msg.exec_()

    def show_info_message(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
