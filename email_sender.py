import aiosmtplib
import configparser
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailSender:
    def __init__(self, config_path: str) -> None:
        config = configparser.ConfigParser()
        config.read(config_path)
        self.server = config["EmailSettings"]["server"]
        self.port = config.getint("EmailSettings", "port")
        self.username = config["EmailSettings"]["username"]
        self.password = config["EmailSettings"]["password"]

    def _create_message(self, subject: str, body: str, to: str) -> None:
        message = MIMEMultipart()
        message["From"] = self.username
        message["To"] = to
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))
        return message

    async def send_mail(self, subject: str, body: str, to: str) -> None:
        message = self._create_message(subject, body, to)

        try:
            await aiosmtplib.send(
                message,
                hostname=self.server,
                port=self.port,
                username=self.username,
                password=self.password,
                use_tls=True,
            )
        except aiosmtplib.SMTPException as e:
            print(f"send mail error: {e}")
