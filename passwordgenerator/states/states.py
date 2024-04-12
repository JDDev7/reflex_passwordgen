import reflex as rx
from constants import *
import random
import string
import pyperclip
import locale

class LanguageSelectState(rx.State):
    # Detects the system language, if it's not spanish, defaults to english.
    system_lang, _ = locale.getdefaultlocale()
    current_language = "ES" if system_lang.startswith('es') else "EN"
    def toggle_language(self):
        if self.current_language == "EN":
            self.current_language = "ES"
        else:
            self.current_language = "EN"
    @rx.var
    def heading_text(self) -> str:
        return HEADING_EN if self.current_language == "EN" else HEADING_ES
    
    @rx.var
    def help_text(self) -> str:
        return HELP_TEXT_EN if self.current_language == "EN" else HELP_TEXT_ES
    
    @rx.var
    def eight_button_text(self) -> str:
        return EIGHT_CHARACTERS_EN if self.current_language == "EN" else EIGHT_CHARACTERS_ES
    
    @rx.var
    def thirteen_button_text(self) -> str:
        return THIRTEEN_CHARACTERS_EN if self.current_language == "EN" else THIRTEEN_CHARACTERS_ES
    
    @rx.var
    def sixteen_button_text(self) -> str:
        return SIXTEEN_CHARACTERS_EN if self.current_language == "EN" else SIXTEEN_CHARACTERS_ES
    
    @rx.var
    def generated_password_text(self) -> str:
        return GENERATED_PASSWORD_EN if self.current_language == "EN" else GENERATED_PASSWORD_ES
    
    @rx.var
    def about_text(self) -> str:
        return ABOUT_EN if self.current_language == "EN" else ABOUT_ES
    @rx.var
    def footer_text(self) -> str:
        return FOOTER_TEXT_EN if self.current_language == "EN" else FOOTER_TEXT_ES
    
    @rx.var
    def change_language_text(self) -> str:
        return SPANISH_LANGUAGE if self.current_language == "EN" else ENGLISH_LANGUAGE
    
class PasswordGeneratorState(rx.State):
    password_length: int = 8  # Default password length
    generated_password: str = "Your new password will show here / Tu contraseña nueva aparecerá aquí."

    def generate_password(self):
        characters = string.ascii_letters + string.digits + string.punctuation
        self.generated_password = ''.join(random.choice(characters) for _ in range(self.password_length))
        
    def update_password_length(self, password_length):
        self.password_length = password_length
    
    def on_button_click(self, length):
        self.update_password_length(length)
        self.generate_password()
        pyperclip.copy(self.generated_password)
     