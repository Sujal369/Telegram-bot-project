import telegram.ext
Token = "6120682729:AAHaaGDiUefqPFPop5D-ZERXWwjOvYI0mR4"
updater = telegram.ext._updater("6120682729:AAHaaGDiUefqPFPop5D-ZERXWwjOvYI0mR4", use_context = True)
dispatcher = updater.dispatcher
def start(update, context):
    update.message.reply_text("Hello")
def help(update, context):
    update.message.reply_text("""/start - welcome to chanell""")
dispatcher.add_handler(telegram.ext.CommandHandler('start', start))
dispatcher.add_handler(telegram.ext.CommandHandler('help', help))

updater.start_polling()
updater.idle()