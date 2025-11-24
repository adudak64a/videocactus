#!/bin/python3
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
# pip3 install python-telegram-bot

import json
from os import path
import random

tokens = "TOKEN"
test = 1
botik = Updater(tokens, use_context=True)
dispatcher = botik.dispatcher
chat_stat = {
        "hate":"on"
}
list_dirt_phrases = [
    "Тебе по голові часто били?! Нєхуй свої відео сюди слати!",
    "Оааайййй бляяя, пробнік ти оператора невдалий...",
    "Ееееее.......фууу!",
    "Зайнятися нічим чи просто мозгів немає?",
    "Слиш, ти, вакуумна насадка, досить це робити",
    "Навіть кращі фіксери Найт сіті тебе б не пофіксили...",
    "Ну чого як знімати відеоповідомлення ти знаєш, а те що вони нахуй нікому не потрібні не знаєш",
    "Та я вірю що в тебе сорок сім хромосом, вірю",
    "Вже всі зрозуміли що ти не вмієш друкувати, досить нагадувати",
    "Чергова байда, можна не дивитися",
    "Буває...мізки є не у всіх",
    "Я готовий повірити в бога якщо він вилікує тебе",
    "Адмін, ну видали з групи ОЦЕ",
    "Коли вже твій телефон подасть заяву на звільнення?",
    "Хтось знову натиснув кнопку 'соромно', але відправилося відео…",
    "Твої дії породжують восьмий смертний гріх - Крінж!",
    "Ум, ну так, писати ж важко...",
    "Пряма трансляція з місцевої помийки!",
    "Коли нарешті стемніє, ти напевно будеш виглядати краще!",
    "Ахтунг! Відеодрочери онлайн",
    "Тобі пора покинути цей чат",
    "Нуууу йоообааане обличчя цього повідомлення",
    "Піздуй звідси зі своїми відосaми куди подалі",
    "Хто навчив цю макаку знімати відео?",
    "Таким повідомленням місце в зоні відчуження",
    "Що це? Я думав, що зоопарк закривається на ніч!",
    "Ах ти гуманоїд червонодупий, знову за старе -_-",
    "Навіть псевдособака і та гарніша за тебе",
    "Кадри з громадського туалету?",
    "Ще трохи і підеш вслід за рускім кораблем",
    "Блять, відоси??? А ти часом не дурко?!",
    "Викликайте відьмака, є замовлення на одну відео-потвору",
    "Може спробуй кнопковий телефон, рано тобі ще сенсорним користуватися",
    "Твої відео — це як реклама, яку не можна пропустити. Тільки гірше",
    "Кожен твій кружечок — доказ, що фронтальна камера теж може страждати",
    "Піду гляну якийсь фільм жахів...нехай психіка відпочине"
]
start_text = "Привіт. Я бот який ненавидить усіх хто посилає відео-повідомлення у телеграмі, тому я буду принижувати таких персонажів по максимуму! 😎\n\nАле, раптом, якщо дуже буде потрібно, навіть не знаю при яких умовах, хейт можна ввимкнути командою /videohate_off...Навіть не знаю навіщо тобі це.\n\nВвімкнути назад можна командою /videohate_on\n\nДля активування задійте будь-яку з двох вищеперечислених команд."

def main():
    dispatcher.add_handler(MessageHandler(Filters.video_note, video_hate))
    dispatcher.add_handler(CommandHandler("videohate_off", hate_off))
    dispatcher.add_handler(CommandHandler("videohate_on", hate_on))
    dispatcher.add_handler(CommandHandler("start", start_work))
    dispatcher.add_handler(CommandHandler("ping", winter_2023_comming))
    botik.start_polling(timeout = 30)

def start_work(update, context):
    context.bot.send_message(update.effective_message.chat_id, text=start_text)

def winter_2023_comming(update, context):
    context.bot.send_message(update.effective_message.chat_id, text="Pong")

def rand_mess():
    return list_dirt_phrases[random.randint(0,len(list_dirt_phrases)-1)]

def new_member(update, context):
    with open(chatfile,'r+') as fi:
        data = json.load(fi)
        fi.close()
    update.message.reply_text('OK')
    chats = str(update.effective_message.chat_id)
    data["chats_id"][chats] = chat_stat
    file = open(chatfile,'w')
    json.dump(data, file, indent = 4)
    file.close()

def video_hate(update, context):
    chats = str(update.effective_message.chat_id)
    with open(chatfile,'r+') as fi:
        data = json.load(fi)
        fi.close()
    try:
        if data["chats_id"][chats]["hate"] == "on":
            context.bot.send_message(update.effective_message.chat_id, reply_to_message_id = update.message.message_id, text=rand_mess())
    except KeyError:
        new_member(update, context)
        video_hate(update, context)

def hate_off(update, context):
    chats = str(update.effective_message.chat_id)
    with open(chatfile,'r+') as fi:
        data = json.load(fi)
        fi.close()
    try:
        data["chats_id"][chats]["hate"] = "off"
        file = open(chatfile,'w+')
        json.dump(data, file, indent = 4)
        file.close()
    except KeyError:
        new_member(update, context)

def hate_on(update, context):
    chats = str(update.effective_message.chat_id)
    with open(chatfile,'r+') as fi:
        data = json.load(fi)
        fi.close()
    try:
        data["chats_id"][chats]["hate"] = "on"
        file = open(chatfile,'w+')
        json.dump(data, file, indent = 4)
        file.close()
    except KeyError:
        new_member(update, context)

#update.message.reply_to_message(text = "dsfgfdgffd")

if __name__ == '__main__':
    chatfile = path.dirname(__file__)
    chatfile = path.join(chatfile, "chatfile.json")
    if path.exists(chatfile) != True:
        with open(chatfile, 'w') as f:
            f.write('{\"chats_id\": {} }')
        f.close()
    main()
