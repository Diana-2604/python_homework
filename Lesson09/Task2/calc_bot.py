# Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему логирования

from asyncore import dispatcher
import logging
from pickle import TRUE
from turtle import up
from config import token
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, ConversationHandler

#start logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

#conversation constants
CHOICE, RATIONAL_ONE, RATIONAL_TWO, OPERATIONS_RATIONAL, OPERATIONS_COMPLEX, COMPLEX_ONE, COMPLEX_TWO = range(7)

#start conversation
def start(update, _):
    update.message.reply_text(
        "Welcome to the calculator! Choose which number you'd like to work with.\n"
        "Enter /cancel to stop the converation.\n\n")
    update.message.reply_text(
        "1 - to work with rational numbers: \n2 - to work with complex numbers \n3 - to exit \n")
    return CHOICE

def choice(update, context):
    user = update.message.from_user
    logger.info("Выбор операции: %s: %s", user.first_name, update.message.text)
    user_choice = update.message.text
    if user_choice in '123':
        if user_choice == '1':
            update.message.reply_text('Enter first rational number')
            return RATIONAL_ONE
        if user_choice == '2':
            context.bot.send_message(update.effective_chat.id, 'Enter Re & Im of the 1st number with SPACE: ')
            return COMPLEX_ONE
    else:
        update.message.reply_text('Please choose option 1 - 3')

def rational_one(update, context):
    user = update.message.from_user
    logger.info("Пользователь ввел число: %s: %s", user.first_name, update.message.text)
    get_rational = update.message.text
    if get_rational.isdigit():
        get_rational = float(get_rational)
        context.user_data['rational_one'] = get_rational
        update.message.reply_text('Enter second rational number')
        return RATIONAL_TWO

    else:
        update.message.reply_text('Please enter a number')

def rational_two(update, context):
    user = update.message.from_user
    logger.info("Пользователь ввел число: %s: %s", user.first_name, update.message.text)
    get_rational = update.message.text
    if get_rational.isdigit():
        get_rational = float(get_rational)
        context.user_data['rational_two'] = get_rational
        update.message.reply_text('Choose operation: \n\n+ : addition, \n- : subtraction, \n* : multiplication, \n/ : division')
        return OPERATIONS_RATIONAL

def operations_rational(update, context):
    user = update.message.from_user
    logger.info("Пользователь ввел число: %s: %s", user.first_name, update.message.text)
    rational_one = context.user_data.get('rational_one')
    rational_two = context.user_data.get('rational_two')
    user_choice = update.message.text
    if user_choice in '+-/*':
        if user_choice == '+':
            result = rational_one + rational_two
        if user_choice == '-':
            result = rational_one - rational_two
        if user_choice == '*':
            result = rational_one * rational_two
        if user_choice == '/':
            try:
                result = rational_one / rational_two
            except:
                update.message.reply_text('Деление на ноль запрещено')
        update.message.reply_text(f'Result: {rational_one} {user_choice} {rational_two} = {result}')
        return ConversationHandler.END
    else:
        update.message.reply_text('Please enter an operation: + - * /')

def complex_one(update, context):
    user = update.message.from_user
    logger.info("Пользователь ввел число: %s: %s", user.first_name, update.message.text)
    user_choice = update.message.text
    test = user_choice.replace('-', '')
    if ' ' in test and (test.replace('-', '')).isdigit():
        user_choice = user_choice.split(' ')
        complex_one = complex(int(user_choice[0]), int(user_choice[1]))
        context.user_data['complex_one'] = complex_one
        update.message.reply_text(f'1st number {complex_one}, enter Re & Im of the 2nd number with SPACE: ')
        return COMPLEX_TWO
    else:
        update.message.reply_text('Please enter Re & Im of the 2nd number with SPACE: ')

def complex_two(update, context):
    user = update.message.from_user
    logger.info("Пользователь ввел число: %s: %s", user.first_name, update.message.text)
    user_choice = update.message.text
    test = user_choice.replace('-', '')
    if ' ' in test and (test.replace('-', '')).isdigit():
        user_choice = user_choice.split(' ')
        complex_two = complex(int(user_choice[0]), int(user_choice[1]))
        context.user_data['complex_two'] = complex_two
        update.message.reply_text(f'2nd number {complex_two}, choose operation: \n\n+ : addition, \n- : subtraction, \n* : multiplication, \n/ : division')
        return OPERATIONS_COMPLEX
    else:
        update.message.reply_text('Please enter Re & Im of the 2nd number with SPACE: ')

def operations_complex(update, context):
    user = update.message.from_user
    logger.info("Пользователь выбрал операцию: %s: %s", user.first_name, update.message.text)
    complex_one = context.user_data.get('complex_one')
    complex_two = context.user_data.get('complex_two')
    user_choice = update.message.text
    if user_choice in '+-/*':
        if user_choice == '+':
            result = complex_one + complex_two
        if user_choice == '-':
            result = complex_one - complex_two
        if user_choice == '*':
            result = complex_one * complex_two
        if user_choice == '/':
            try:
                result = complex_one / complex_two
            except:
                update.message.reply_text('Деление на ноль запрещено')
        update.message.reply_text(f'Result: {complex_one} {user_choice} {complex_two} = {result}')
        return ConversationHandler.END
    else:
        update.message.reply_text('Please enter an operation: + - * /')

def cancel(update, _):
    user = update.message.from_user
    logger.info("Пользователь %s отменил разговор.", user.first_name)
    update.message.reply_text(f'Goodbye {user.first_name}, see you soon!')
    return ConversationHandler.END

if __name__ == '__main__':
    updater = Updater(token, update_queue=TRUE)
    dispatcher = updater.dispatcher

    conversation_handler = ConversationHandler(
        entry_points=CommandHandler('start', start),
        states={ 
            CHOICE: [MessageHandler(filters.text, choice)],
            RATIONAL_ONE: [MessageHandler(filters.text, rational_one)],
            RATIONAL_TWO: [MessageHandler(filters.text, rational_two)],
            OPERATIONS_RATIONAL: [MessageHandler(filters.text, operations_rational)],
            OPERATIONS_COMPLEX: [MessageHandler(filters.text, operations_complex)],
            COMPLEX_ONE: [MessageHandler(filters.text, complex_one)],
            COMPLEX_TWO: [MessageHandler(filters.text, complex_two)]
            },
        fallbacks=[CommandHandler('cancel', cancel)]
        )

dispatcher.add_handler(conversation_handler)

updater.start_polling()
updater.idle()
