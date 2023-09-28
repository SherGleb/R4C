import smtplib


class EmailSender:
    # Для корректной работы нужно указать свой email и пароль
    sender = "your email"
    password = "your password"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    # Метод для отправки имейлов
    @classmethod
    def send_email(cls, email, model, version):
        try:
            cls.server.login(cls.sender, cls.password)
            message = f"Good afternoon! Recently you were interested in our robot model {model}, version {version}. " \
                      f"This robot is now available. If this option suits you, please contact us "
            cls.server.sendmail(cls.sender, email, message)
        except Exception as ex:
            print(ex)
