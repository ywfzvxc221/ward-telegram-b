
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = 'YOUR_BOT_TOKEN'  # 馃攣 睾賷賾乇 賴匕丕 亘丕賱鬲賵賰賳 丕賱禺丕氐 亘賰
ADMIN_ID = 123456789       # 馃攣 睾賷賾乇 賴匕丕 亘賲毓乇賮賰 (丌賷丿賷賰 丕賱乇賯賲賷)
CHANNEL_USERNAME = '@your_channel'  # 馃攣 睾賷賾乇 賴匕丕 亘丕爻賲 賯賳丕鬲賰

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(
        InlineKeyboardButton("馃摙 丕胤賱亘 廿毓賱丕賳", callback_data='order'),
        InlineKeyboardButton("馃挵 丕賱亘丕賯丕鬲 賵丕賱兀爻毓丕乇", callback_data='prices'),
        InlineKeyboardButton("馃搳 廿丨氐丕卅賷丕鬲", callback_data='stats'),
        InlineKeyboardButton("馃摓 鬲賵丕氐賱 賲毓 丕賱廿丿丕乇丞", url="https://t.me/your_username")
    )
    bot.send_message(message.chat.id, "賲乇丨亘賸丕 亘賰 賮賷 亘賵鬲 鬲賲賵賷賱 丕賱賯賳賵丕鬲 馃捀\n丕禺鬲乇 賲賳 丕賱賯丕卅賲丞:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data == "order":
        msg = bot.send_message(call.message.chat.id, "馃摠 兀乇爻賱 丕賱丌賳 廿毓賱丕賳賰 (賳氐 兀賵 氐賵乇丞/賮賷丿賷賵 + 賳氐)...")
        bot.register_next_step_handler(msg, receive_ad)
    elif call.data == "prices":
        bot.send_message(call.message.chat.id, "馃挵 丕賱亘丕賯丕鬲:\n\n- 賲賳卮賵乇 毓丕丿賷: 5$\n- 賲賳卮賵乇 賲孬亘鬲: 10$\n- 賯氐丞: 15$")
    elif call.data == "stats":
        try:
            members = bot.get_chat_member_count(CHANNEL_USERNAME)
            bot.send_message(call.message.chat.id, f"馃搳 毓丿丿 兀毓囟丕亍 丕賱賯賳丕丞: {members}")
        except Exception as e:
            bot.send_message(call.message.chat.id, f"鉂� 丨丿孬 禺胤兀 兀孬賳丕亍 噩賱亘 丕賱廿丨氐丕卅賷丕鬲: {e}")

def receive_ad(message):
    ad_info = f"馃摜 胤賱亘 廿毓賱丕賳 噩丿賷丿 賲賳 {message.from_user.first_name} (@{message.from_user.username}):\n\n"
    if message.text:
        ad_info += message.text
    elif message.caption:
        ad_info += message.caption

    bot.send_message(ADMIN_ID, ad_info)
    if message.content_type != 'text':
        bot.forward_message(ADMIN_ID, message.chat.id, message.message_id)

    bot.send_message(message.chat.id, "鉁� 鬲賲 廿乇爻丕賱 廿毓賱丕賳賰 賱賱廿丿丕乇丞 賱賲乇丕噩毓鬲賴. 爻賷鬲賲 丕賱鬲賵丕氐賱 賲毓賰 亘毓丿 丕賱賲賵丕賮賯丞.")

print("馃 丕賱亘賵鬲 賷毓賲賱 丕賱丌賳...")
bot.infinity_polling()
