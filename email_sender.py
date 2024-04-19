import aiosmtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailSender:
    def __init__(
            self, 
            username: str, 
            password: str,
            server: str = "smtp.gmail.com", 
            port: int = 465,
        ) -> None:
        self.server = server
        self.port = port
        self.username = username
        self.password = password

    def _create_message(self, subject: str, body: str, to: str) -> MIMEMultipart:
        message = MIMEMultipart()
        message["From"] = self.username
        message["To"] = to
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))
        return message

    async def send_mail(self, subject: str, body: str, to: str) -> None:
        message = self._create_message(subject, body, to)

        await aiosmtplib.send(
            message,
            hostname=self.server,
            port=self.port,
            username=self.username,
            password=self.password,
            use_tls=True,
        )

