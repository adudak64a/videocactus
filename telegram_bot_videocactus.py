#!/bin/python3

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

import json
from os import path
import random

TOKEN = "TOKEN"

chat_stat = {
    "hate": "on"
}

list_dirt_phrase = [
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
    "Піду гляну якийсь фільм жахів...нехай психіка відпочине",
    "Ти свої відео відправляєш сюди щоб перевірити хто першим лівне з чату?",
    "Ти як Людина Ікс, а твоя суперсила - викликати огиду в інших"
]

start_text = """Привіт. Я бот який ненавидить усіх хто посилає відео-повідомлення у телеграмі...

/videohate_off
/videohate_on
"""

def rand_mess():
    return random.choice(list_dirt_phrase)


async def start_work(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(start_text)


async def winter_2023_comming(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Pong")


def load_data():
    with open(chatfile, 'r') as f:
        return json.load(f)


def save_data(data):
    with open(chatfile, 'w') as f:
        json.dump(data, f, indent=4)


async def new_member(update: Update, context: ContextTypes.DEFAULT_TYPE):

    data = load_data()

    chats = str(update.effective_chat.id)

    data["chats_id"][chats] = chat_stat

    save_data(data)

    await update.message.reply_text("OK")


async def video_hate(update: Update, context: ContextTypes.DEFAULT_TYPE):

    chats = str(update.effective_chat.id)

    data = load_data()

    try:

        if data["chats_id"][chats]["hate"] == "on":

            await update.message.reply_text(
                rand_mess(),
                reply_to_message_id=update.message.message_id
            )

    except KeyError:

        await new_member(update, context)

        await video_hate(update, context)


async def hate_off(update: Update, context: ContextTypes.DEFAULT_TYPE):

    chats = str(update.effective_chat.id)

    data = load_data()

    try:

        data["chats_id"][chats]["hate"] = "off"

        save_data(data)

    except KeyError:

        await new_member(update, context)


async def hate_on(update: Update, context: ContextTypes.DEFAULT_TYPE):

    chats = str(update.effective_chat.id)

    data = load_data()

    try:

        data["chats_id"][chats]["hate"] = "on"

        save_data(data)

    except KeyError:

        await new_member(update, context)


def main():

    app = Application.builder().token(TOKEN).build()

    app.add_handler(
        MessageHandler(filters.VIDEO_NOTE, video_hate)
    )

    app.add_handler(CommandHandler("videohate_off", hate_off))

    app.add_handler(CommandHandler("videohate_on", hate_on))

    app.add_handler(CommandHandler("start", start_work))

    app.add_handler(CommandHandler("ping", winter_2023_comming))

    app.run_polling()


if __name__ == '__main__':

    chatfile = path.dirname(__file__)

    chatfile = path.join(chatfile, "chatfile.json")

    if not path.exists(chatfile):

        with open(chatfile, 'w') as f:
            f.write('{"chats_id": {}}')

    main()
