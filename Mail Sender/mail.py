import smtplib
import configparser

class Email:
    def __init__(self, sender, recipients, subject, body, attachments=None):
        # Initialize user variables
        self.sender = sender
        self.recipients = recipients
        self.subject = subject
        self.body = body
        self.attachments = attachments or []
        # Initialize config variables
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.server = config['DEFAULT']['server']
        self.port = config['DEFAULT']['port']
        self.password = config['DEFAULT']['password']

    def send(self):
        # Set up the SMTP server
        server = smtplib.SMTP(self.server, self.port)
        server.starttls()
        server.login(self.sender, self.password)
        # Send the email
        server.sendmail(self.sender, self.recipients, self.body)
        # Disconnect from the server
        server.quit()

    def add_attachment(self, attachment):
        self.attachment = attachment