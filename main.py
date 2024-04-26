from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, Poll, Contact, Location
import json


with open('config.json') as file:
    config = json.load(file)
BOT_TOKEN: str = config['BOT_TOKEN']


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь и в ответ '
        'я пришлю тебе твое сообщение'
    )


async def send_photo_echo(message: Message):
    await message.reply_photo(message.photo[0].file_id)


async def send_audio_echo(message: Message):
    await message.reply_audio(message.audio.file_id)


async def send_video_echo(message: Message):
    await message.reply_video(message.video.file_id)


async def send_document_echo(message: Message):
    await message.reply_document(message.document.file_id)


async def send_sticker_echo(message: Message):
    await message.reply_sticker(message.sticker.file_id)


async def send_video_note_echo(message: Message):
    await message.reply_video_note(message.video_note.file_id)


async def send_voice_echo(message: Message):
    await message.reply_voice(message.voice.file_id)


async def send_animation(message: Message):
    await message.reply_animation(message.animation.file_id)


async def send_dice(message: Message):
    await message.reply_dice(message.dice.emoji)


async def send_poll(message: Message):
    poll: Poll = message.poll
    questions: list[str] = list(map(lambda x: x.text, poll.options))
    await message.reply_poll(poll.question, questions, poll.is_anonymous, poll.type, poll.allows_multiple_answers,
                             poll.correct_option_id, poll.explanation, explanation_entities=poll.explanation_entities,
                             open_period=poll.open_period, close_date=poll.close_date, is_closed=poll.is_closed)


async def send_contact(message: Message):
    contact: Contact = message.contact
    await message.reply_contact(contact.phone_number, contact.first_name, contact.last_name, contact.vcard)


async def send_location(message: Message):
    location: Location = message.location
    await message.reply_location(location.latitude, location.longitude, location.horizontal_accuracy,
                                 location.live_period, location.heading, location.proximity_alert_radius)


async def send_echo(message: Message):
    print(message.model_dump_json(indent=4, exclude_none=True))
    await message.reply(text=message.text)


dp.message.register(process_start_command, Command(commands='start'))
dp.message.register(process_help_command, Command(commands='help'))
dp.message.register(send_photo_echo, F.photo)
dp.message.register(send_audio_echo, F.audio)
dp.message.register(send_video_echo, F.video)
dp.message.register(send_document_echo, F.document)
dp.message.register(send_sticker_echo, F.sticker)
dp.message.register(send_video_note_echo, F.video_note)
dp.message.register(send_voice_echo, F.voice)
dp.message.register(send_animation, F.animation)
dp.message.register(send_dice, F.dice)
dp.message.register(send_poll, F.poll)
dp.message.register(send_contact, F.contact)
dp.message.register(send_location, F.location)
dp.message.register(send_echo)


if __name__ == '__main__':
    dp.run_polling(bot)
