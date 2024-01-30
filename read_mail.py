from service import service
from googleapiclient.discovery import build
import time


def get_unread_messages():
    # Get the list of all unread messages
    results = (
        service.users()
        .messages()
        .list(
            userId="me",
            q="in:inbox is:unread category:primary",
        )
        .execute()
    )
    messages = results.get("messages", [])
    print(results.get("resultSizeEstimate"))
    if not messages:
        print("No unread messages found.")
    else:
        print("Unread messages:")
        print("-----------------")
        print(len(messages), "unread messages found.")
        for message in messages:
            # to check if the msg is read or not
            # print(message["labelIds"])
            msg = (
                service.users().messages().get(userId="me", id=message["id"]).execute()
            )

            # Get the headers
            headers = msg["payload"]["headers"]

            # Initialize variables
            date = None
            sender = None
            subject = None
            for header in headers:
                name = header["name"]
                if name == "Date":
                    date = header["value"]
                elif name == "From":
                    sender = header["value"]
                elif name == "Subject":
                    subject = header["value"]

            # Get the body
            body = msg["payload"]["body"].keys()

            # Log the information
            print("Date:", date)
            print("Sender:", sender)
            print("Subject:", subject)
            # print("Body:", body)
            print("Keys:", body)
            print(
                msg["snippet"],
                msg["payload"]["body"]["data"],
                "\n",
            )


if __name__ == "__main__":
    get_unread_messages()
