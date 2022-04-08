from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


btnUrlChannel = InlineKeyboardButton(text="1.Подписаться👨‍💻", url=""# ссылка на приватный чат)
btnDoneSub = InlineKeyboardButton(text="Подписался✅", callback_data="subchanneldone")

checkSubMenu = InlineKeyboardMarkup(row_width=1)
checkSubMenu.insert(btnUrlChannel)
checkSubMenu.insert(btnDoneSub)
