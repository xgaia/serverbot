# ServerBot

Telegram Bot to manage a server.

## Installation


### Get a Telegram bot

First, you will need a telegram bot. Ask this to [BotFather](https://t.me/botfather) by sending him the `/newbot` command.

Configure it with `/setcommands` and sent this:

```
hello - say hello
disk - show hard drives usage
uptime - uptime
memory - show memory and swap usage
wakeonlan - wake machines
shutdown - shutdown server
cmd - run custom commands
```

### Install

Install dependencies:

```bash
# Debian/Ubuntu
sudo apt install make python3 python3-pip python3-venv
```

Clone the repo

```bash
git clone https://github.com/xgaia/serverbot.git
cd serverbot
```

Install all python dependencies in a python virtual env

```bash
make install
```

### Configure

Create a config file with the template and edit it

```bash
make configure
vim config.ini # Edit the file
```

- [telegram]
    - token: the bot token
    - [telegram:authorized_users]: list of username who are authorized to use the bot. Example: `me = xgaiia`

- [server]
    - name: the name of the managed server
    - [server:disks]: disks path to manage. Example: `root = /`
    - [server:cmd]: list of shell command. Example: `ls = ls -l`

- [wakeonlan]: list of machine to wake. Example: `warmachine = 00:00:00:00:00:00 `


### Run


```bash
make build run
```

### Run as a service

Create a  `/etc/systemd/system/serverbot.service` file like:

```
[Unit]
Description=Telegram bot to manage a Linux server
After=network.target
[Service]
Type=simple
User=root
WorkingDirectory=/root
ExecStart=/path/to/serverbot -c /path/to/serverbot/config.ini
Restart=on-failure
[Install]
WantedBy=multi-user.target
```

Control the service

```bash
# Control whether bot start on boot
systemctl enable serverbot
systemctl disable serverbot

# Manual start and stop
systemctl start serverbot
systemctl stop serverbot

# Status
systemctl status serverbot
```
