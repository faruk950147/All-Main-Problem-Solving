import threading
import time


class MailSender(threading.Thread):
    def __init__(self, email):
        threading.Thread.__init__(self)
        self.email = email

    def run(self):
        print(f"Sending email to {self.email}")
        time.sleep(2)
        print(f"Email sent to {self.email}")

list1 = ["faruk950147@gmail.com", "faruk950147@outlook.com", "faruk950147@yahoo.com"]

for email in list1:
    t1 = MailSender(email)
    t1.start()
    t1.join()