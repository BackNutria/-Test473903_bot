import telebot
from telebot import types

bot = telebot.TeleBot('###')


@bot.message_handler(commands=['website'])
def open_website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Перейти на сайт", url="https://store.playstation.com/ru-ru/latest"))
    bot.send_message(message.chat.id, "Нажмите на кнопку ниже и ознакомьтесь со всей актуальной информацией на оф.сайте",
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.InlineKeyboardButton('Шутеры')
    btn2 = types.InlineKeyboardButton('Гонки')
    btn3 = types.InlineKeyboardButton('Приключения')
    btn4 = types.InlineKeyboardButton('Для детей')
    btn5 = types.InlineKeyboardButton('Сетевые')
    markup.add(btn1, btn2, btn3, btn4, btn5)
    send_mess = f"<b>Привет {message.from_user.first_name} {message.from_user.last_name}</b>!\nКакое игровое направление тебя интересует?"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip().lower()

    if get_message_bot == "заново":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.InlineKeyboardButton('Шутеры')
        btn2 = types.InlineKeyboardButton('Гонки')
        btn3 = types.InlineKeyboardButton('Приключения')
        btn4 = types.InlineKeyboardButton('Для детей')
        btn5 = types.InlineKeyboardButton('Сетевые')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        final_message = "Решил попробовать что-то ещё? \nВыбери какое направление тебя интересует:"

    elif get_message_bot == "шутеры":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Одиночные')
        btn2 = types.KeyboardButton('Мультиплеер')
        btn3 = types.KeyboardButton('Кооператив')
        btn4 = types.KeyboardButton('Начать заново')
        markup.add(btn1, btn2, btn3,btn4)
        final_message = "Шутеры отличный жанр, а какой конкретно?"
    elif get_message_bot == "одиночные":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Открыть страницу в PSN - DOOM ETERNAL", url="https://store.playstation.com/ru-ru/product/EP1003-CUSA13275_00-DOOMETERNALBUNDL"))
        final_message = "Мне кажется тебе подойдет новый проект от Id Software - <b>DOOM ETERNAL </b>!\nМожете просмотреть страницу проекта ниже"
    elif get_message_bot == "мультиплеер":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Открыть страницу в PSN - Call of Duty",url="https://store.playstation.com/ru-ru/product/EP0002-CUSA24267_00-CODCWSTANDARD001"))
        final_message = "Самый популярный сетевой шутер на данный момент - <b>COD BO Cold War </b>\nМожете просмотреть страницу проекта ниже"
    elif get_message_bot == "кооператив":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Открыть страницу в PSN - BORDERLANDS 3",url="https://store.playstation.com/ru-ru/product/EP1001-PPSA01463_00-0000000OAKNGSIEE"))
        final_message = "<b>BORDERLANDS 3</b> - отличный варинт для прохождения со своими верными товарищами.\nМожете просмотреть страницу проекта ниже"
    elif get_message_bot == "начать заново":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.InlineKeyboardButton('Шутеры')
        btn2 = types.InlineKeyboardButton('Гонки')
        btn3 = types.InlineKeyboardButton('Приключения')
        btn4 = types.InlineKeyboardButton('Для детей')
        btn5 = types.InlineKeyboardButton('Сетевые')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        final_message = "Решил попробовать что-то ещё? \nВыбери какое направление тебя интересует:"
    elif get_message_bot == "гонки":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Аркада')
        btn2 = types.KeyboardButton('Симулятор')
        btn3 = types.KeyboardButton('Начать заново')
        markup.add(btn1, btn2, btn3,)
        final_message = "Погонять все любят,но что именно тебе по душе?"
    elif get_message_bot == "аркада":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Открыть страницу в PSN - Burnout™ Paradise", url="https://store.playstation.com/ru-ru/product/EP0006-CUSA10851_00-STELLARPARADISE0"))
        final_message = "Можно сказать,уже живая классика. Одна из самых драйвовых гонок - <b>Burnout™ Paradise </b>!\nМожете просмотреть страницу проекта ниже"
    elif get_message_bot == "симулятор":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Открыть страницу в PSN - Gran Turismo™ Sport",url="https://store.playstation.com/ru-ru/product/EP9001-CUSA02168_00-GTSPORT000000000"))
        final_message = "Присмотрись к <b>Gran Turismo™ Sport</b>, сражения не реальных треках с живыми игроками. \nМожете просмотреть страницу проекта ниже"
    elif get_message_bot == "начать заново":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.InlineKeyboardButton('Шутеры')
        btn2 = types.InlineKeyboardButton('Гонки')
        btn3 = types.InlineKeyboardButton('Приключения')
        btn4 = types.InlineKeyboardButton('Для детей')
        btn5 = types.InlineKeyboardButton('Сетевые')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        final_message = "Решил попробовать что-то ещё? \nВыбери какое направление тебя интересует:"
    elif get_message_bot == "приключения":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Uncharted 4')
        btn2 = types.KeyboardButton('Resident Evil 2')
        btn3 = types.KeyboardButton('God of War')
        btn4 = types.KeyboardButton('Начать заново')
        markup.add(btn1, btn2, btn3,btn4)
        final_message = "Если тебе по нраву дух приключений. Эти проекты тебя точно не разочаруют и подарят отличный игровой опыт."
    elif get_message_bot == "uncharted 4":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Открыть страницу в PSN - Uncharted 4", url="https://store.playstation.com/ru-ru/product/EP9000-CUSA04529_00-UNCHARTED4000000"))
        final_message = "<b>Последняя глава приключений Нэйтана Дрейка.</b>!\nМожете просмотреть страницу проекта ниже"
    elif get_message_bot == "resident evil 2":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Открыть страницу в PSN - Resident Evil 2",url="https://store.playstation.com/ru-ru/product/EP0102-CUSA09171_00-BH2R000000000001"))
        final_message = "<b>Resident Evil 2 </b>- холодящее кровь приключение в зараженном зомби городе. \nМожете просмотреть страницу проекта ниже"
    elif get_message_bot == "god of war":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Открыть страницу в PSN - God of War", url="https://store.playstation.com/ru-ru/product/EP9000-CUSA07412_00-0000000GODOFWARN"))
        final_message = "<b>God of War.</b>Обладатель премии игра года 2018 по версии игроков.\nМожете просмотреть страницу проекта ниже"
    elif get_message_bot == "начать заново":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.InlineKeyboardButton('Шутеры')
        btn2 = types.InlineKeyboardButton('Гонки')
        btn3 = types.InlineKeyboardButton('Приключения')
        btn4 = types.InlineKeyboardButton('Для детей')
        btn5 = types.InlineKeyboardButton('Сетевые')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        final_message = "Решил попробовать что-то ещё? \nВыбери какое направление тебя интересует:"
    elif get_message_bot == "для детей":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Bugsnax')
        btn2 = types.KeyboardButton('Spyro')
        btn3 = types.KeyboardButton('Dreams')
        btn4 = types.KeyboardButton('Начать заново')
        markup.add(btn1, btn2, btn3,btn4)
        final_message = "Следующие проекты понравятся как детям так и взрослым,имеют интересный игровой процесс и завораживающее графическое оформление."
    elif get_message_bot == "bugsnax":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Открыть страницу в PSN - Bugsnax", url="https://www.playstation.com/ru-ru/games/bugsnax/"))
        final_message = "В игре <b>Bugsnax</b> вы отправитесь в необычайное приключение на Остров Закусок, родину легендарных полубутербродов-полужуков или просто — Bugsnax!\nМожете просмотреть страницу проекта ниже"
    elif get_message_bot == "spyro":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Открыть страницу в PSN - Spyro Reignited Trilogy",url="https://www.playstation.com/ru-ru/games/spyro-reignited-trilogy/"))
        final_message = "<b>Spyro Reignited Trilogy</b>-  испепеляющая все на своем пути, воссоздает три величайших приключения серии – Spyro the Dragon, Spyro 2: Ripto's Rage! и Spyro: Year of the Dragon – и поражает своими визуальными эффектами в потрясающем HD-качестве. \nМожете просмотреть страницу проекта ниже"
    elif get_message_bot == "dreams":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Открыть страницу в PSN - Dreams", url="https://www.playstation.com/ru-ru/games/dreams/"))
        final_message = "<b>Dreams.</b>необычная, непрерывно расширяющаяся игровая вселенная от известной студии Media Molecule, выпустившей игры LittleBigPlanet и «Сорванец».\nМожете просмотреть страницу проекта ниже"
    elif get_message_bot == "начать заново":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.InlineKeyboardButton('Шутеры')
        btn2 = types.InlineKeyboardButton('Гонки')
        btn3 = types.InlineKeyboardButton('Приключения')
        btn4 = types.InlineKeyboardButton('Для детей')
        btn5 = types.InlineKeyboardButton('Сетевые')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        final_message = "Решил попробовать что-то ещё? \nВыбери какое направление тебя интересует:"
    elif get_message_bot == "сетевые":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('R6 Siege')
        btn2 = types.KeyboardButton('APEX')
        btn3 = types.KeyboardButton('BattleField 5')
        btn4 = types.KeyboardButton('Destiny 2')
        btn5 = types.KeyboardButton('Начать заново')
        markup.add(btn1, btn2, btn3,btn4,btn5)
        final_message = "Здесь собраны самые популярные сетевые проекты, которые способны завлечь на тясячи часов."
    elif get_message_bot == "r6 siege":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Открыть страницу в PSN - R6 Siege", url="https://www.playstation.com/ru-ru/games/tom-clancys-rainbow-six-siege/"))
        final_message = "<b>Tom Clancy's Rainbow Six Siege.</b>Участвуйте в жарких перестрелках 5 на 5 в этом шутере от первого лица, где вам доступны оперативники с разными специализациями.\nМожете просмотреть страницу проекта ниже"
    elif get_message_bot == "apex":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Открыть страницу в PSN - APEX",url="https://www.playstation.com/ru-ru/games/apex-legends/"))
        final_message = "<b>APEX Legends</b>- Сразитесь в новой королевской битве от Respawn Entertainment — опытных разработчиков, подаривших нам серию Titanfall. \nМожете просмотреть страницу проекта ниже \nИгра является бесплатной для всех пользователейю"
    elif get_message_bot == "battlefield 5":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Открыть страницу в PSN", url="https://www.playstation.com/ru-ru/games/battlefield-v/"))
        final_message = "<b>Battlefield V.</b>Участвуйте в крупнейшем конфликте: серия возвращается к своим корням — Второй мировой — изображая её в новом свете.\nМожете просмотреть страницу проекта ниже"
    elif get_message_bot == "destiny 2":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Открыть страницу в PSN",url="https://www.playstation.com/ru-ru/games/destiny-2/"))
        final_message = "Погрузитесь в мир Destiny 2, чтобы исследовать тайны Солнечной системы и испытать на себе возможности потрясающего шутера от первого лица. \n Можете просмотреть страницу проекта ниже"
    elif get_message_bot == "начать заново":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.InlineKeyboardButton('Шутеры')
        btn2 = types.InlineKeyboardButton('Гонки')
        btn3 = types.InlineKeyboardButton('Приключения')
        btn4 = types.InlineKeyboardButton('Для детей')
        btn5 = types.InlineKeyboardButton('Сетевые')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        final_message = "Решил попробовать что-то ещё? \nВыбери какое направление тебя интересует:"

    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.InlineKeyboardButton('Шутеры')
        btn2 = types.InlineKeyboardButton('Гонки')
        btn3 = types.InlineKeyboardButton('Приключения')
        btn4 = types.InlineKeyboardButton('Для детей')
        btn5 = types.InlineKeyboardButton('Сетевые')
        markup.add(btn1, btn2, btn3, btn4, btn5,)
        final_message = "Что-то не так.Я умею работаь только с кнопками.\nПредлагаю тебе пользоваться этими самыми кнопками - ниже."
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)

bot.polling(none_stop=True)
