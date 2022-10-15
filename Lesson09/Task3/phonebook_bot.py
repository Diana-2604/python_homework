# Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.

from asyncore import dispatcher
from pickle import TRUE
from turtle import up
from config import token
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, ConversationHandler

#conversation constants
CHOICE, ADD_CONTACT, FIND_CONTACT, DELETE_CONTACT = range(4)

#start conversation
def start(update, _):
    update.message.reply_text(
        "Welcome to the phonebook! Choose which option you'd like to work with.\n"
        "Enter /cancel to stop the converation.\n\n")
    update.message.reply_text(
        "1 - to add new contact: \n2 - to find a contact: \n3 - to delete the contact: \n4 - to exit \n")
    return CHOICE

def choice(update, context):
    user_choice = update.message.text
    if user_choice in '1234':
        if user_choice == '1':
            update.message.reply_text('Enter ID, name, phone with SPACE to add a new contact: ')
            return ADD_CONTACT
        if user_choice == '2':
            context.bot.send_message(update.effective_chat.id, 'Enter the name to find a contact: ')
            return FIND_CONTACT
        if user_choice == '3':
            update.message.reply_text('Enter the name to delete the contact: ')
            return DELETE_CONTACT
    else:
        update.message.reply_text('Please choose option 1 - 4')


def add_csv(filename: str, data: list):
    with open(filename, 'a', encoding= 'utf-8') as fout:
        for i in range(len(data)-1, len(data)):
            s = ''
            for v in data[i].values():
                s += v + ','
            fout.write(f'{s[:-1]}\n')

def write_csv(filename: str, data: list):
    with open(filename, 'w', encoding= 'utf-8') as fout:
        for i in range(len(data)):
            s = ''
            for v in data[i].values():
                s += v + ','
            fout.write(f'{s[:-1]}\n')

def read_csv(filename: str) -> list:
    data = []
    fields = ["ID", "Name", "Phone"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data

def find_by_name(update, context):
    data = {}
    read_csv('Task3/phonebook.csv')
    name = update.message.text
    for el in data:
        if el.get("Name") == name:
            context.user_data['find_by_name'] = data[el]
            return el.get("Phone")
    return "The contact was not found"

def add_contact(update, context):
    data = {}
    contact_data = update.message.text
    fields = ["ID", "Name", "Phone"]
    new_contact = dict(zip(fields, contact_data.strip().split(',')))
    data.append(new_contact)
    add_csv('Task3/phonebook.csv', data)
    context.user_data['add_contact'] = new_contact
    update.message.reply_text(f'{new_contact} has been added')
    return ConversationHandler.END

def remove_contact(update, context):
    data = {}
    contact_name = update.message.text
    for el in data:
        if el.get("Name") == contact_name:
            index = data.index(el)
            data.remove(data[index])
            write_csv('Task3/phonebook.csv', data)
            context.user_data['remove_contact'] = index
            update.message.reply_text(f'{contact_name} has been deleted')
            return ConversationHandler.END

def cancel(update, _):
    user = update.message.from_user
    update.message.reply_text(f'Goodbye {user.first_name}, see you soon!')
    return ConversationHandler.END

if __name__ == '__main__':
    updater = Updater(token, update_queue=TRUE)
    dispatcher = updater.dispatcher

    conversation_handler = ConversationHandler(
        entry_points=CommandHandler('start', start),
        states={ 
            CHOICE: [MessageHandler(filters.text, choice)],
            ADD_CONTACT: [MessageHandler(filters.text, add_contact)],
            FIND_CONTACT: [MessageHandler(filters.text, find_by_name)],
            DELETE_CONTACT: [MessageHandler(filters.text, remove_contact)],
            },
        fallbacks=[CommandHandler('cancel', cancel)]
        )

dispatcher.add_handler(conversation_handler)

updater.start_polling()
updater.idle()
