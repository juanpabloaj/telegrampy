#!/usr/bin/env python3
import os
import urllib.request
import urllib.parse
import sys

TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]
TELEGRAM_CHANNEL_ID = os.environ["TELEGRAM_CHANNEL_ID"]

telegram_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
telegram_url += f"?chat_id={TELEGRAM_CHANNEL_ID}"


def send_message(message):
    message = urllib.parse.quote(message)
    url = f"{telegram_url}&text={message}"
    urllib.request.urlopen(url)


if __name__ == "__main__":
    if not sys.stdin.isatty():
        for line in sys.stdin:
            send_message(line)

    if len(sys.argv) > 1:
        send_message(sys.argv[1])
