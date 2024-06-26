import contextlib
import asyncio 
from aiogram.types import ChatJoinRequest, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import Bot, Dispatcher, types, F
import logging

# Bot 1 configuration
BOT_TOKEN = '6427870841:AAGC7wKTWNgT14wxxLCovMl9h7t2HqiUZZE'
CHANNEL1_ID = -1001419655243
CHANNEL2_ID = -1001819624357
ADMIN_ID = 2136559110


# Logic for approving request for channel 1
async def approve_request_bot1(chat_join: ChatJoinRequest, bot: Bot):
    msg = "Ваша заявка одобрена!\n\nВступить в канал: https://t.me/+-NJYzNqw7YQ4NjMy"
    button = InlineKeyboardButton(text='ВСТУПИТЬ', url='https://t.me/+-NJYzNqw7YQ4NjMy', disable_web_page_preview=True)
    markup = InlineKeyboardMarkup(inline_keyboard=[[button]])
    await bot.send_message(chat_id=chat_join.from_user.id, text=msg, reply_markup=markup, disable_web_page_preview=True)

# Logic for approving request for channel 2
async def approve_request_bot2(chat_join: ChatJoinRequest, bot: Bot):
    msg = "Ваша заявка одобрена!\n\nВступить в канал: https://t.me/+5TDzGQl2kYswYmEy"
    button = InlineKeyboardButton(text='ВСТУПИТЬ', url='https://t.me/+5TDzGQl2kYswYmEy', disable_web_page_preview=True)
    markup = InlineKeyboardMarkup(inline_keyboard=[[button]])
    await bot.send_message(chat_id=chat_join.from_user.id, text=msg, reply_markup=markup, disable_web_page_preview=True)

async def handle_chat_join_request(chat_join: ChatJoinRequest, bot: Bot):
    if chat_join.chat.id == CHANNEL1_ID:
        await approve_request_bot1(chat_join, bot)
    elif chat_join.chat.id == CHANNEL2_ID:
        await approve_request_bot2(chat_join, bot)

async def start():
    logging.basicConfig(level=logging.DEBUG,
                        format="%(asctime)s - [%(levelname)s] - %(name)s -"
                               "(%(filename)s.%(funcName)s(%(lineno)d) - %(message)s"
                        )
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.chat_join_request.register(handle_chat_join_request, F.chat.id.in_([CHANNEL1_ID, CHANNEL2_ID]))

    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    except Exception as ex:
        logging.error(exc_info=True)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    with contextlib.suppress(KeyboardInterrupt, SystemExit):
        asyncio.run(start())
