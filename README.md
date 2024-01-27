# Mail Sender Project

This project is centered around the creation and management of email-related tasks. Currently, it supports sending emails, with plans to expand its capabilities to include features such as checking for new incoming emails and more sophisticated mailing operations.

## Features

- **Email Sending**: Send emails using a specified Google account with the help of `send_mail.py` which utilizes a template for email content.

## Upcoming Features

- **Email Receiving**: Check for new incoming emails.
- Additional mailing functionalities.

## Configuration

The project uses a configuration file named `client_secret.json`, which is generated from the Google Developer Console. This file contains the necessary credentials to authenticate with the Google API and perform operations on behalf of a Google account.

## Usage

- `service.py` is responsible for the login process by leveraging `Google.py` for authentication and session management using the OAuth 2.0 protocol. It references `client_secret.json` to log in to the specific Google account.
- `send_mail.py` is responsible for sending emails based on a template.

## Getting Started

To begin using this project, follow these steps:

1. Obtain your `client_secret.json` file by setting up a project in the [Google Developer Console](https://console.developers.google.com/).
2. Place the `client_secret.json` file in the appropriate directory.
3. Use `service.py` in conjunction with `Google.py` to handle authentication.
4. Start sending emails through `send_mail.py`.

For detailed instructions on how to set up your credentials and use the Gmail API, refer to the [Gmail API Python Quickstart](https://developers.google.com/gmail/api/quickstart/python) and the official [Google documentation](https://developers.google.com/gmail/api).

## Contributions

Contributions are welcome! If you have ideas for new features or improvements, feel free to fork the repository and submit a pull request.

---

_This README is a work in progress and will be updated as the project evolves._
