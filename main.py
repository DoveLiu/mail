import asyncio
import configparser
from email_sender import EmailSender


async def main() -> None:
    config = configparser.ConfigParser()
    config.read("config.ini")
    username = config["EmailSettings"]["username"]
    password = config["EmailSettings"]["password"]
    server = config["EmailSettings"]["server"]
    port = config.getint("EmailSettings", "port")

    email_sender = EmailSender(
        username=username, password=password, hostname=server, port=port
    )

    await email_sender.send_mail(
        "測試郵件", "test body", "doveliu0516@gmail.com", "D:\\011.jpg"
    )


if __name__ == "__main__":
    asyncio.run(main())
