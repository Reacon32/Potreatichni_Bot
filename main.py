from aiogram import Bot, Dispatcher, types, executor
from KeyBoards.InLine import get_keyboard_inline1, get_keyboard_inline2, get_keyboard_inline3, get_keyboard_inline4, get_keyboard_inline5, get_keyboard_inline6
TOKEN_API = '7437453983:AAHPdORfZEgcsOvCjxzXwP8k_8cWhCpVSnk'

bot = Bot(token= TOKEN_API)
dp = Dispatcher(bot)

async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command='/start', description='Команда для запуска бота'),
        types.BotCommand(command='/sv', description='Сухопутные войска'),
        types.BotCommand(command='/vvs', description='Военно воздушные силы'),
        types.BotCommand(command='/vmf', description='Военно морской флот'),
        types.BotCommand(command='/vdv', description='Воздушно десантные войска'),
        types.BotCommand(command='/rvsn', description='Ракетные войска стратегического назначения'),
        types.BotCommand(command='/vks', description='Воздушно-космические силы')
    ]

    await bot.set_my_commands(commands)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.reply('Привет! Я бот, который выводит общую информацию по военным силам России. Нажми на меню с лева, чтобы увидеть их.')

@dp.message_handler(commands='sv')
async def start(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://structure.mil.ru/images/SAVX9004.jpg', caption= 'Вид вооруженных сил Российской Федерации, предназначенный для отражения агрессии противника на континентальных театрах военных действий, защиты территориальной целостности и национальных интересов РФ.', reply_markup= get_keyboard_inline1())

@dp.message_handler(commands='vvs')
async def start(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://structure.mil.ru/images/military/military/photo/vvs_aviation.jpg', caption= 'Вид вооружённых сил Российской Федерации, предназначенный для самостоятельных действий при решении оперативно-стратегических задач и для совместных действий с другими видами вооружённых сил.', reply_markup= get_keyboard_inline2())

@dp.message_handler(commands='vmf')
async def start(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://structure.mil.ru/images/kfl-550.jpg', caption= 'Вид вооружённых сил Российской Федерации, предназначенный для обеспечения защиты национальных интересов Российской Федерации и ее союзников в Мировом океане военными методами.', reply_markup= get_keyboard_inline3())

@dp.message_handler(commands='vdv')
async def start(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://structure.mil.ru/images/vdv_centrtop.jpg', caption= 'Отдельный вид войск Вооружённых сил Российской Федерации, предназначенный для охвата противника по воздуху и выполнения задач в его тылу по нарушению управления войсками.', reply_markup= get_keyboard_inline4())

@dp.message_handler(commands='rvsn')
async def start(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://structure.mil.ru/images/IMG_0203.jpg', caption= 'Вид вооружённых сил Российской Федерации, предназначеный для ядерного сдерживания возможной агрессии и поражения в составе СЯС или самостоятельно массированными, групповыми или одиночными ракетно-ядерными ударами по стратегическим объектам', reply_markup= get_keyboard_inline5())

@dp.message_handler(commands='vks')
async def start(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://structure.mil.ru/images/vks_775.jpg', caption= 'Вид вооружённых сил Российской Федерации, предназначенный для ведения разведки воздушно-космической обстановки, вскрытия начала воздушного и ракетного воздушно-космического нападения и оповещения органов государственного и военного управления о нем.', reply_markup= get_keyboard_inline6())

async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup= on_startup)