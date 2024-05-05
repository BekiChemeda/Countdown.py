
import telebot
from datetime import datetime
from telebot import types

# Initialize the bot
bot = telebot.TeleBot("6578767571:AAF_fHqNsH8adldWqV9S_kDAd8CxhqhDM8Q")

# Exam start times
natural_science_start = datetime(2024, 7, 16, 8, 0, 0)
social_science_start = datetime(2024, 7, 10, 8, 0, 0)

# Watermark text
watermark = "Created by @Euee_Tips"

# Countdown calculation function
def calculate_countdown(exam_start):
    current_time = datetime.now()
    time_remaining = exam_start - current_time
    days = time_remaining.days
    hours, remainder = divmod(time_remaining.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return days, hours, minutes, seconds

# Command to start the bot
@bot.message_handler(commands=['start','Start','START'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    natural_btn = types.InlineKeyboardButton(text='Natural Science', callback_data='natural')
    social_btn = types.InlineKeyboardButton(text='Social Science', callback_data='social')
    markup.row(natural_btn, social_btn)

    more_info_btn = types.InlineKeyboardButton(text='More Information ℹ️', callback_data='info')
    markup.add(more_info_btn)

    bot.send_message(message.chat.id, "Select which exam's countdown you want to see:", reply_markup=markup)

# Callback query handling
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    chat_id = call.message.chat.id
    if call.data == 'natural':
        days, hours, minutes, seconds = calculate_countdown(natural_science_start)
        countdown_message = f"✅Entrance Exam For Natural Science is scheduled on 9-11/11/2016 E.C Or 16-18/7/2024 G.C. \n \n 👉This means {days} days, {hours} hours, {minutes} minutes, {seconds} seconds left\n👉This Countdown is calculated as the exam will start on 8:00 AM \nhelp For Help \n\n{watermark}"
    elif call.data == 'social':
        days, hours, minutes, seconds = calculate_countdown(social_science_start)
        countdown_message = f"✅Entrance Exam For Social Science is scheduled on 3/11/2016 E.C or 10/7/2024 G.C.\n\n  👉This means {days} days, {hours} hours, {minutes} minutes, {seconds} seconds left\n👉This Countdown is calculated as the exam will start on 8:00 AM\n/help For Help \n\n{watermark}"
    elif call.data == 'info':
        info_message = "For More Educational Information:\n\n✅ Join these Channels:\n ✅ To get Past Entrance Questions  Join \n👉 @Euee_Tips\n✅ To get Educational Information Specially about Entrance in Amharic Join \n 👉 @Ethio_Educational_News\n✅ To get Educational Information Specially about Entrance in Afaan Oromoo Join \n 👉 @Oromia_Educational_Channel"
        bot.send_message(chat_id, info_message)
        return
    bot.send_message(chat_id, countdown_message)

# New handler for text messages
@bot.message_handler(func=lambda message: True)
def handle_text(message):
    if message.text.lower() == '/info':
        info = "About Bot \n This bot provides countdowns for entrance exams in Natural Science and Social Science. \n\n About Entrance Questions Channel \n  Our Channel(@Euee_Tips)  offers educational informations and Past Entrance Questions Daily for those who are preparing them selves for Entrance Exam. \n Also we have Q&A program where we ask questions and give prize for those Who answered it. \n For More Join Our Channel \n @EUEE_TIPS"
        bot.reply_to(message, info)
    elif message.text.lower() == '/help':
        help_message = "To use this bot, you can:\n\n- Use /start to start the bot or see the exam countdowns\n- Use /info to get information about the bot and our channel\n- Use /help to get help on how to use the bot"
        bot.reply_to(message, help_message)
    else:
        bot.reply_to(message, "Hmm, that looks like I can't respond to this. Please use the following commands:\n\n/Start - restart the bot\n/Info - about us\n/Help - help")

# Start the bot
bot.polling()
