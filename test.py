import os

password_key = os.getenv("PASSWORD_KEY")

if password_key is not None:
    print("La variable de entorno 'PASSWORD_KEY' está configurada.")
    print(f"Valor de 'PASSWORD_KEY': {password_key}")
else:
    print("La variable de entorno 'PASSWORD_KEY' no está configurada.")

EMAIL_SENDER = os.getenv("EMAIL_SENDER")

if EMAIL_SENDER is not None:
    print("La variable de entorno 'EMAIL_SENDER' está configurada.")
    print(f"Valor de 'EMAIL_SENDER': {EMAIL_SENDER}")
else:
    print("La variable de entorno 'EMAIL_SENDER' no está configurada.")


EMAIL_RECE = os.getenv("EMAIL_RECE")

if EMAIL_RECE is not None:
    print("La variable de entorno 'EMAIL_RECE' está configurada.")
    print(f"Valor de 'EMAIL_RECE': {EMAIL_RECE}")
else:
    print("La variable de entorno 'EMAIL_RECE' no está configurada.")


