import asyncio
from email_sender import EmailSender


async def main() -> None:
    email_sender = EmailSender("config.ini")
    await email_sender.send_mail("測試郵件", "test body", "doveliu0516@gmail.com")


if __name__ == "__main__":
    asyncio.run(main())
