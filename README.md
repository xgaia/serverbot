# ServerBot

Telegram Bot to manage a server.

## Installation


### Get a Telegram bot

First, you will need a telegram bot. Ask this to [BotFather](https://t.me/botfather) by sending him the `/newbot` command.

Configure it with `/setcommands` and sent this:

```
/hello - say hello
/disk - show hard drives usage
/uptime - uptime
/memory - show memory and swap usage
/wakeonlan - wake machines
/shutdown - shutdown server
/cmd - run custom commands
```

### Install, configure and run ServerBot

Install depandancies:

```bash
# Debian/Ubuntu
sudo apt install python3 python3-pip python3-venv
```

Clone the repo

```bash
git clone https://github.com/xgaia/serverbot.git
cd serverbot
```

Create a config file with the template and edit it

```bash
cp config.ini.template config.ini
vim config.ini # Edit the file
```

Create and source a Python virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

Install bot and run

```bash
python3 setup.py install
```
