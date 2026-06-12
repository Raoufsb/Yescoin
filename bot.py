import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# إعدادات الـ Logging لمراقبة الأخطاء
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

TOKEN = "tokbot"
QUIZ_URL = "https://t.me/bem4_bot/Chatai"

async def send_quiz_response(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """الدالة الموحدة للرد على أي رسالة أو أمر"""
    # التحقق من وجود رسالة نصية أو أي محتوى آخر لمنع الأخطاء في الحالات النادرة
    if not update.message:
        return

    welcome_text = (
        "👋 أهلاً بك في بوت كويز التعليمي للسنة الرابعة متوسط!\n\n"
        "اضغط على الزر أدناه لفتح الكويز وبدء الدراسة والاستعداد للمتحانات."
    )

    keyboard = [
        [
            InlineKeyboardButton(text="🚀 ابدأ الكويز الآن", url=QUIZ_URL)
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(text=welcome_text, reply_markup=reply_markup)

def main() -> None:
    """تشغيل البوت"""
    application = Application.builder().token(TOKEN).build()

    # معالج لأمر /start
    application.add_handler(CommandHandler("start", send_quiz_response))

    # معالج شامل (filters.ALL) لالتقاط أي رسالة أخرى (نص، صورة، صوت، إلخ) والرد عليها بنفس الدالة
    application.add_handler(MessageHandler(filters.ALL, send_quiz_response))

    print("البوت يعمل الآن ويستقبل كل الرسائل...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
