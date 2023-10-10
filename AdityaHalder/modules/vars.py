import os

from os import getenv
from dotenv import load_dotenv
from pyrogram import filters


if os.path.exists("Internal"):
  load_dotenv("Internal")


class Config(object):
    # REQUIRED VARIABLES
    API_ID = int(getenv("API_ID","11107466"))
    API_HASH = getenv("API_HASH","303837af39dfd53ff9b60a56f6ca3bc6")
    BOT_TOKEN = getenv("BOT_TOKEN","6652949143:AAFmXmYdM484jgo217X8CPxwNHmd4M7zbxk")
    STRING_SESSION = getenv("STRING_SESSION","BQCpfIoAxv3PTQ6Hpf9uFesBOIjcmDghd6As2qpfqrCTN_Pktvzd5HkrBoc5mQmCP34wRK_P783D9_7FLGMmDaeIICvZ47Vmu_bU43iCwv678sUlmfDUvS8uA_SU3cdr3mO0CvSPB5ZnArSbYjyNeOXiG_yKUXxIuso1BiYT8suXQGcrfhmu8XDiZADY_6YUTbHuchYj6aHfeM0Vq3nLYLNrDzqXVGo-ggvFIGqBtDlmCbtwaxzeluDLL0KpEzFvLaNgibj5pAPSFkXcAaPt6xc-27ZQY1eEYMDod_o477kcvQU_D44PPIPMfYKqm0Qxnpj5sRRlMVU2j32hWbHlsqSFvkb5xAAAAAGEsRkqAA")
    MONGO_DATABASE = getenv("MONGO_DATABASE","mongodb+srv://devilop:devilop123@devilserver.bhep18a.mongodb.net/?retryWrites=true&w=majority")
  
    # OPTIONAL VARIABLES
    SESSION_STRING = getenv("SESSION_STRING", None)
    COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", ". ! > *").split())
    USERBOT_PICTURE = getenv("USERBOT_PICTURE","https://graph.org/file/e332ff3f78ea32aaf6685.jpg")
    LOG_GROUP_ID = int(getenv("LOG_GROUP_ID","-1001919006105"))
    PMPERMIT = getenv("PMPERMIT", "True")
    PERMIT_MSG = getenv("PERMIT_MSG", None)
    PERMIT_LIMIT = int(getenv("PERMIT_LIMIT", 6))
  
  
    # do not edit these variables
    COMMAND_HANDLERS = []
    PLUGINS = {}
    SUPUSER = filters.me
    SUDOERS = filters.user([])
    CRAIDUB = filters.user([])
    LRAIDUB = filters.user([])
    RRAIDUB = filters.user([])
    GDELSUB = filters.user([])
    GBANSUB = filters.user([])
    GMUTEUB = filters.user([])
    #######################################
    for x in COMMAND_PREFIXES:
        COMMAND_HANDLERS.append(x)
    COMMAND_HANDLERS.append('')
    #######################################


# get all config variables in a list
all_vars = [i for i in Config.__dict__.keys()]
all_vals = [i for i in Config.__dict__.values()]

