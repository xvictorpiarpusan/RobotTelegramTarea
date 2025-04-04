from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ParseMode
from telegram.ext import Application, CommandHandler, ContextTypes
from textos import textos
import json


bot_name = "Metodologías de desarrollo"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton('ÚNETE GRATIS AQUÍ', url = "https://google.com")]])

    message = await update.effective_chat.send_message(text = textos["Bienvenida"].format(bot_name, "https://google.com"), reply_markup = reply_markup, parse_mode = ParseMode.HTML, disable_web_page_preview=True)

    #Registro de información de usuarios nuevos

    new_user = {}
    new_user.update({"from_user.username":message.from_user.username, "from_user.id":message.from_user.id, "chat.first_name":message.chat.first_name, "chat.username":message.chat.username, "chat.id":message.chat.id})
    json_new_user = json.dumps(new_user, indent=4)

    registro_nuevos = -1002238369077 #ID Del canal donde se enviará la información y se almacenará

    await context.bot.send_message(chat_id = registro_nuevos, text = json_new_user, parse_mode = ParseMode.HTML)

async def ayuda(update: Update, context: ContextTypes.DEFAULT_TYPE):

    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton('Solicita más ayuda', url = "https://ayuda.com")],[InlineKeyboardButton('📤 ASISTENCIA PERSONALIZADA 🆘', url = "https://t.me/AyudaAdmin")]])

    await update.effective_chat.send_message(text = textos["Ayuda"], reply_markup = reply_markup, parse_mode = ParseMode.HTML)

async def contacto(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.effective_chat.send_message(text = textos["Contactanos"], parse_mode = ParseMode.HTML)

def main() -> None:
    application = Application.builder().token("8186738195:AAGV68G2ZUlPJPkJ7BS83W1kl87WJtLUREU").build()


    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("ayuda", ayuda))
    application.add_handler(CommandHandler("contacto", contacto))


    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()