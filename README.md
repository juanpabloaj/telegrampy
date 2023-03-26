# telegrampy

To send messages to Telegram from the command line

    echo "hello world" | python3 telegram.py
    python3 telegram.py "hello world"

Environment variables required

    TELEGRAM_CHANNEL_ID
    TELEGRAM_TOKEN

You can get the `TELEGRAM_TOKEN` from telegram [BotFather](https://core.telegram.org/bots/tutorial#obtain-your-bot-token).

Use case, receive notification from systemd when a service fails.

Create a service file, called `/etc/systemd/system/notify-telegram@.service`

    [Unit]
    Description=Sent telegram message

    [Service]
    Type=oneshot
    User=myUser
    WorkingDirectory=/home/myUser/src/telegrampy
    ExecStart=/usr/bin/bash -lc 'python3 telegram.py "%i failed"'

    [Install]
    WantedBy=multi-user.target

Add to systemd

    systemctl enable notify-telegram@.service

Add to other services

    [Unit]
    OnFailure=notify-telegram@%i.service

Reload the configuration

    systemctl daemon-reload

More details in [stackoverflow](https://serverfault.com/questions/694818/get-notification-when-systemd-monitored-service-enters-failed-state)
