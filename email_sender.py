import aiosmtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders


class EmailSender:
    def __init__(
        self,
        username: str,
        password: str,
        hostname: str = "smtp.gmail.com",
        port: int = 465,
    ) -> None:
        self.username = username
        self.password = password
        self.hostname = hostname
        self.port = port

    def _create_message(
        self, subject: str, body: str, recipient: str, file_path: str = None
    ) -> MIMEMultipart:
        message = MIMEMultipart()
        message["From"] = self.username
        message["To"] = recipient
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        if file_path:
            with open(file_path, "rb") as file:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(file.read())
                encoders.encode_base64(part)
                part.add_header("Content-Disposition", f"attachment; filename={file_path.split('/')[-1]}")
                message.attach(part)

        return message

    async def send_mail(
        self, subject: str, body: str, recipient: str, file_path: str = None
    ) -> None:
        message = self._create_message(subject, body, recipient, file_path)

        await aiosmtplib.send(
            message,
            hostname=self.hostname,
            port=self.port,
            username=self.username,
            password=self.password,
            use_tls=True,
        )
