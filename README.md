# Bot for Гагарин.Хакатон

## Вы можете узнать как продвигаются дела непосредственно в боте: https://t.me/gagarin_hackathon_bot

Это пока минимальная часть работы над проектом, но мы стремимся к большему

___
## Table of contents

- [Quick start](#quick-start)
    - [Clone Repository](#1-clone-repository)
    - [Setup and activate VirtualEnv](#2-setup-and-activate-virtualenv)
    - [Get Bot token](#3-get-bot-token)
    - [Start the server](#4-start-the-server)
- [Creators](#creators)

## Quickstart
For a quick start, you need to do the following:

> **NOTE**: The project was written in python version **3.11.4** 

### 1. Clone Repository

```bash
$ git clone https://github.com/FaVaKu/Gagarin_hackaton.git
```

Change your directory to a cloned repository using:

``` bash
$ cd Gagarin_hackaton
```

### 2. Setup and activate VirtualEnv

Inside your cloned repository directory, run following commands:

``` bash
$ python3 -m venv venv
```
``` bash
$ source venv/bin/activate
```
``` bash
$ pip install -r requirements.txt
```

After create `.env` file in the main directory based on the `.env.shared` file
### 3. Setup Bot

#### Get Bot token:

- You can get a bot token from [@BotFather](https://t.me/BotFather)

- After receiving the bot token, enter it into the BOT_TOKEN variable in the `.env` file

#### Setup Bot from @BotFather:

- Send /setinlinegeo to the BotFather chat.
- On the keyboard, select your bot.
- Next, select Enable


> **NOTE**: You can use [billing plans](https://home.openweathermap.org/subscriptions) for large volumes of requests

### 4. Start the server

Once all dependencies are installed, you can start your app via terminal using `main.py` script.

``` bash
$ python main.py
```
and kill the app close application window 

> **Note:** Make sure you create a `.env` file in the main directory and change environment variables as specified in `.env.shared`.


## Creators

    
### Developed by **LimeFox**:
- ***Telegram:*** [@LimeFox](https://t.me/LimeFox)
- ***GitHub:*** [LimeFox16](https://github.com/LimeFox16)
