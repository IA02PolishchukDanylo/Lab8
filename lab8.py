import logging
from telegram.ext import Updater, CommandHandler,MessageHandler,Filters
from prometheus_client import start_http_server, Counter

message_counter = Counter('telegram_messages_total', 'Total number of messages received')

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Lab7 Grafana')

def handle_message(update, context):
    message_counter.inc()

def main():
    updater = Updater(token='6191130254:AAH5yCH0XWUYBuSNw-XCaQGX3RDJ4p1v920', use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))

    dispatcher.add_handler(MessageHandler(Filters.text, handle_message))

    updater.start_polling()

    start_http_server(9091)

    updater.idle()
if __name__ == '__main__':
    main()