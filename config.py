# Copyright (c) 2022 Itz-fork

import os


class Config(object):
    APP_ID = int(os.environ.get("APP_ID", 21636723))
    API_HASH = os.environ.get("API_HASH", "077c6885ffcc5b398cb8b662665247da")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6147217240:AAFXiOxNt7lWlz0rplBKi7DgwRXUnc2pZaQ")
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "5007354893").split())
    IS_PUBLIC_BOT = os.environ.get("IS_PUBLIC_BOT") in ["False", "false"]
    LOGS_CHANNEL = int(os.environ.get("LOGS_CHANNEL")) if os.environ.get("LOGS_CHANNEL") else None
    # DON'T CHANGE THESE 2 VARS
    DOWNLOAD_LOCATION = "./NexaBots"
    TG_MAX_SIZE = 2040108421
    # Mega User Account
    MEGA_EMAIL = os.environ.get("myp.c5.0.50@gmail.com")
    MEGA_PASSWORD = os.environ.get("mypc5050")
