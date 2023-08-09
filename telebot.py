import telegram.ext
Token = "YOUR TOKEN ID"
updater = telegram.ext._updater("YOUR TOKEN ID", use_context = True)
dispatcher = updater.dispatcher
def start(update, context):
    update.message.reply_text("Hello")
def help(update, context):
    update.message.reply_text("""/start - welcome to chanell""")
dispatcher.add_handler(telegram.ext.CommandHandler('start', start))
dispatcher.add_handler(telegram.ext.CommandHandler('help', help))

updater.start_polling()
updater.idle()
