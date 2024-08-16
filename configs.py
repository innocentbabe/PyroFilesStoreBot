# (c) @AbirHasan2005

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID", "0"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-100"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "1445283714"))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", None)
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
๏ 𝖳𝗁𝗂𝗌 𝖨𝗌 𝖯𝖾𝗋𝗆𝖺𝗇𝖾𝗇𝗍 𝖥𝗂𝗅𝖾 𝖲𝗍𝗈𝗋𝖾 𝖡𝗈𝗍.
➜ 𝖲𝖾𝗇𝖽 𝖬𝖾 𝖠𝗇𝗒 𝖥𝗂𝗅𝖾 𝖳𝗈 𝖦𝖾𝗍 𝖲𝗁𝖺𝗋𝖾𝖺𝖻𝗅𝖾 𝖫𝗂𝗇𝗄. 
➜ 𝖶𝗈𝗋𝗄𝗌 𝖨𝗇 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 𝖳𝗈𝗈.
➜ 𝖠𝗏𝗈𝗂𝖽 𝖢𝗈𝗉𝗒𝗋𝗂𝗀𝗁𝗍 𝖨𝗇𝖿𝗋𝗂𝗇𝗀𝖾𝗆𝖾𝗇𝗍.

★ 𝗔𝗯𝗼𝘂𝘁 𝗙𝗶𝗹𝗲 𝗦𝗮𝘃𝗲𝗿

**➜ 𝖬𝗒 𝖭𝖺𝗆𝖾 :** [𝖥𝗂𝗅𝖾 𝖲𝗍𝗈𝗋𝖾 𝖡𝗈𝗍](https://t.me/{BOT_USERNAME})
**➜ 𝖫𝗂𝖻𝗋𝖺𝗋𝗒 :** [𝖯𝗒𝗍𝗁𝗈𝗇3](https://www.python.org)
**🧑‍💻 𝖣𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋 :** @DRDIC
**𝖲𝗎𝗉𝗉𝗈𝗋𝗍 𝖦𝗋𝗈𝗎𝗉 🌥 :** [𝖨𝗇𝖿𝗂𝗇𝗂𝗍𝗒 𝖱𝗈𝖻𝗈𝗍𝗌](https://t.me/InfinityRobots)
**🌧 𝖴𝗉𝖽𝖺𝗍𝖾𝗌 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 :** [𝖨𝗇𝖿𝗂𝗇𝗂𝗍𝗒 𝖤𝖽𝗎𝖼𝖺𝗍𝗂𝗈𝗇](https://t.me/Infinity_Backup)
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **𝖣𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋 :** @DRDIC

➜ 𝖨 𝖶𝗂𝗅𝗅 𝖡𝖺𝗇 𝖸𝗈𝗎 𝖥𝗈𝗋𝖾𝗏𝖾𝗋 𝖨𝖿 𝖸𝗈𝗎 𝖲𝗍𝗈𝗋𝖾 𝖠𝖽𝗎𝗅𝗍 𝖢𝗈𝗇𝗍𝖾𝗇𝗍𝗌.
"""
	HOME_TEXT = """
𝖧𝗂𝗂 , [{}](tg://user?id={})\n\n𝖳𝗁𝗂𝗌 𝖨𝗌 𝖯𝖾𝗋𝗆𝖺𝗇𝖾𝗇𝗍 **𝖥𝗂𝗅𝖾 𝖲𝗍𝗈𝗋𝖾 𝖡𝗈𝗍**.

𝖲𝖾𝗇𝖽 𝖬𝖾 𝖠𝗇𝗒 𝖥𝗂𝗅𝖾 𝖨 𝖶𝗂𝗅𝗅 𝖦𝗂𝗏𝖾 𝖸𝗈𝗎 𝖠 𝖯𝖾𝗋𝗆𝖺𝗇𝖾𝗇𝗍 𝖲𝗁𝖺𝗋𝖾𝖺𝖻𝗅𝖾 𝖫𝗂𝗇𝗄. 𝖨 𝖲𝗎𝗉𝗉𝗈𝗋𝗍 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 𝖠𝗅𝗌𝗈 ! 𝖢𝗁𝖾𝖼𝗄 **𝖠𝖻𝗈𝗎𝗍 𝖡𝗈𝗍** 𝖡𝗎𝗍𝗍𝗈𝗇.
"""
