# Same as run.py
import mail

if __name__ == "__main__":
    sender = 'me@server.com'
    recipients = 'you@server.com'
    subject = 'Test mail'
    body = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
    mail.Email(sender, recipients, subject, body)