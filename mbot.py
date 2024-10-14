import sqlite3
import telebot, random, os

bot = telebot.TeleBot("your_token")

conn = sqlite3.connect('db.db', check_same_thread=False)
cursor = conn.cursor()

def keyboard(where_call):
    a = telebot.types.InlineKeyboardMarkup()
    if where_call == 'teoria':
        a_1 = telebot.types.InlineKeyboardButton(text='Алгебра 2️⃣✖️2️⃣', callback_data='1')
        a.add(a_1)
        a_2 = telebot.types.InlineKeyboardButton(text='Геометрия 📐', callback_data='2')
        a.add(a_2)
        pl_eg = telebot.types.InlineKeyboardButton(text='Плюшки для ЕГЭ 🥨', callback_data='pl_eg')
        a.add(pl_eg)
        pr_1 = telebot.types.InlineKeyboardButton(text='Бонус -> (=^･^=)', callback_data='pr')
        a.add(pr_1)
        n_3 = telebot.types.InlineKeyboardButton(text='{ Закрыть меню }', callback_data='n_3')
        a.add(n_3)
        return a
    elif where_call == 'tema1':
        a_3 = telebot.types.InlineKeyboardButton(text='Производная', callback_data='3')
        a.add(a_3)
        a_4 = telebot.types.InlineKeyboardButton(text='Точки экстремума', callback_data='4')
        a.add(a_4)
        a_9 = telebot.types.InlineKeyboardButton(text='Вторая производная', callback_data='9')
        a.add(a_9)
        a_10 = telebot.types.InlineKeyboardButton(text='Точки перегиба', callback_data='10')
        a.add(a_10)
        a_11 = telebot.types.InlineKeyboardButton(text='Исследование функции', callback_data='11')
        a.add(a_11)
        a_12 = telebot.types.InlineKeyboardButton(text='Асимптоты графика функции', callback_data='12')
        a.add(a_12)
        a_18 = telebot.types.InlineKeyboardButton(text='Первообразная функции', callback_data='18')
        a.add(a_18)
        a_22 = telebot.types.InlineKeyboardButton(text='Дифференциал функции, \nнеопределённый интеграл', callback_data='22')
        a.add(a_22)
        a_23 = telebot.types.InlineKeyboardButton(text='Площадь криволинейной \nтрапеции', callback_data='23')
        a.add(a_23)
        a_24 = telebot.types.InlineKeyboardButton(text='Определённый интеграл', callback_data='24')
        a.add(a_24)
        n_1 = telebot.types.InlineKeyboardButton(text='<<Назад', callback_data='n_1')
        a.add(n_1)
        return a
    elif where_call == 'tema2':
        a_5 = telebot.types.InlineKeyboardButton(text='Конус', callback_data='5')
        a.add(a_5)
        a_6 = telebot.types.InlineKeyboardButton(text='Цилиндр', callback_data='6')
        a.add(a_6)
        a_7 = telebot.types.InlineKeyboardButton(text='Сфера и шар', callback_data='7')
        a.add(a_7)
        a_8 = telebot.types.InlineKeyboardButton(text='Усечённый конус', callback_data='8')
        a.add(a_8)
        a_13 = telebot.types.InlineKeyboardButton(text='Сфера и цилиндр', callback_data='13')
        a.add(a_13)
        a_14 = telebot.types.InlineKeyboardButton(text='Сфера и конус', callback_data='14')
        a.add(a_14)
        a_15 = telebot.types.InlineKeyboardButton(text='Многогранник, вписанный в сферу', callback_data='15')
        a.add(a_15)
        a_16 = telebot.types.InlineKeyboardButton(text='Призма, вписанная в сферу', callback_data='16')
        a.add(a_16)
        a_17 = telebot.types.InlineKeyboardButton(text='Пирамида, вписанная в сферу', callback_data='17')
        a.add(a_17)
        a_19 = telebot.types.InlineKeyboardButton(text='Сфера, вписанная в многогранник', callback_data='19')
        a.add(a_19)
        a_20 = telebot.types.InlineKeyboardButton(text='Сфера, вписанная в призму', callback_data='20')
        a.add(a_20)
        a_21 = telebot.types.InlineKeyboardButton(text='Сфера, вписанная в пирамиду', callback_data='21')
        a.add(a_21)
        n_2 = telebot.types.InlineKeyboardButton(text='<<Назад', callback_data='n_2')
        a.add(n_2)
        return a
    elif where_call == 'pl_eg':
        a_25= telebot.types.InlineKeyboardButton(text='Параметры. Часть 1', callback_data='25')
        a.add(a_25)
        a_27= telebot.types.InlineKeyboardButton(text='Параметры. Часть 2', callback_data='27')
        a.add(a_27)
        a_28= telebot.types.InlineKeyboardButton(text='Параметры. Часть 3', callback_data='28')
        a.add(a_28)
        a_26= telebot.types.InlineKeyboardButton(text='Произведение логарифмов', callback_data='26')
        a.add(a_26)
        n_4 = telebot.types.InlineKeyboardButton(text='<<Назад', callback_data='n_4')
        a.add(n_4)
        return a

def db_table_val(user_id: int, user_name: str, user_surname: str, username: str, k: int):
	cursor.execute('INSERT INTO test (user_id, user_name, user_surname, username, k) VALUES (?, ?, ?, ?, ?)', (user_id, user_name, user_surname, username, k))
	conn.commit()

def getName(conn, user_id: int):
    c = conn.cursor()
    c.execute("SELECT * FROM test WHERE user_id = ?", (user_id, ))
    result = c.fetchone()
    if result:
        return result[5], result[1]


@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == "Привет" or message.text == "/start":
        bot.send_message(message.from_user.id, "Салют! ✌️ \n Для нашего успешного сотрудничества тебе стоит знать всего две команды: \n1. /teoria (тут ты можешь найти интересующие тебя подсказки). \n2. /help (если вдруг возникли вопросы в плане общения с ботом, или же вопросы по менюшкам). \n3. Если вдруг забыл команды, то обрати внимание на меню, которое находится в левом нижнем углу около строки ввода.")
        us_id = message.from_user.id
        us_name = message.from_user.first_name
        us_sname = message.from_user.last_name
        username = message.from_user.username
        K=1
        db_table_val(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username, k=K)
        sql2 = """UPDATE test SET k=? WHERE user_id=?"""
        c=(1, getName(conn, message.chat.id)[1])
        cursor.execute(sql2, c)
        conn.commit()
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Вижу, тебе понадобилась помощь. Надеюсь, это поможет: \n  1️⃣ Найти подсказки довольно просто: напиши мне /teoria. \n  2️⃣  О значении менюшек: \n    a) Алгебра: теория по алгебре. \n    b) Геометрия... а как сам думаешь?)) Бинго! Это теория по геометрии! \n    c) Бонус: немного приколов и милоты. \n    d) Плюшки для ЕГЭ: штуки, которые действительно огут помочь сдать тебе экзамен успешно. \n  3️⃣  Если вдруг забыл команды, то обрати внимание на меню, которое находится в левом нижнем углу около строки ввода.")
    elif message.text == "/teoria" and getName(conn, message.chat.id)[0]==1:
        bot.send_message(message.from_user.id,
                         "Что ищешь? Теорему из геометрии, а может формулу из алгебры? Выбери предмет:", reply_markup=keyboard('teoria'))
        sql = """UPDATE test SET k=? WHERE user_id=?"""
        a=(0, getName(conn, message.chat.id)[1])
        cursor.execute(sql, a)
        conn.commit()
    elif message.text == "/teoria" and getName(conn, message.chat.id)[0]==0:
        bot.send_message(message.from_user.id,
                         "Вы уже открыли меню")
    else:
        bot.send_message(message.from_user.id, "К сожалению, я тебя не понимаю. Напиши /help, если нужна помощь.")

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == '1':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Окей, про Пифагора пока забудем. Теперь выбери интересующую тебя тему.', reply_markup=keyboard('tema1'))
        bot.answer_callback_query(call.id)
    elif call.data == '2':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='Надеюсь, у тебя хорошо развито пространственное мышление, потому что геометрия в 11 классе – это что-то жуткое. Но не будем отчаиваться, выбирай тему.', reply_markup=keyboard('tema2'))
        bot.answer_callback_query(call.id)
    elif call.data == 'pl_eg':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='Здесь собраны некоторые лайфхаки и просто полезные теоремы и формулы для успешной сдачи экзамена:', reply_markup=keyboard('pl_eg'))
        bot.answer_callback_query(call.id)
    if call.data == 'pr':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        photo = open('mbotpi/' + random.choice(os.listdir('mbotpi')), 'rb')
        bot.send_photo(call.message.chat.id, photo, caption=' Лови котейку) Meow')
        bot.send_message(call.message.chat.id,
                         "Что ищешь? Теорему из геометрии, а может формулу из алгебры? Выбери предмет:", reply_markup=keyboard('teoria'))
        bot.answer_callback_query(call.id)
    elif call.data == '3':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_photo(call.message.chat.id,
                       'https://i.ibb.co/RQyF6Ww/image.png', caption='Лови. Надеюсь, что смог помочь. Обращайся снова! '
                                                                     'Ссылка на фото: https://i.ibb.co/RQyF6Ww/image.png')
        bot.send_message(call.message.chat.id,
                         "Окей, про Пифагора пока забудем. Теперь выбери интересующую тебя тему.", reply_markup=keyboard('tema1'))

        bot.answer_callback_query(call.id)
    elif call.data == '4':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_photo(call.message.chat.id,
                       'https://i.ibb.co/mRvxWpZ/image.png', caption='Лови. Надеюсь, что смог помочь. Обращайся снова! '
                                                                     'Ссылка на фото: https://i.ibb.co/mRvxWpZ/image.png')
        bot.send_message(call.message.chat.id,
                         "Окей, про Пифагора пока забудем. Теперь выбери интересующую тебя тему.", reply_markup=keyboard('tema1'))
        bot.answer_callback_query(call.id)
    elif call.data == '5':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_photo(call.message.chat.id,
                       'https://i.ibb.co/88TGkH3/image.jpg', caption='Лови. Надеюсь, что смог помочь. Обращайся снова! '
                                                                     'Ссылка на фото: https://i.ibb.co/88TGkH3/image.jpg')
        bot.send_message(call.message.chat.id,
                         "Надеюсь, у тебя хорошо развито пространственное мышление, потому что геометрия в 11 классе – это что-то жуткое. Но не будем отчаиваться, выбирай тему.", reply_markup=keyboard('tema2'))
        bot.answer_callback_query(call.id)
    elif call.data == '6':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_photo(call.message.chat.id,
                       'https://i.ibb.co/W2F9mRH/image.jpg', caption='Лови. Надеюсь, что смог помочь. Обращайся снова! '
                                                                     'Ссылка на фото: https://i.ibb.co/W2F9mRH/image.jpg')
        bot.send_message(call.message.chat.id,
                         "Надеюсь, у тебя хорошо развито пространственное мышление, потому что геометрия в 11 классе – это что-то жуткое. Но не будем отчаиваться, выбирай тему.", reply_markup=keyboard('tema2'))
        bot.answer_callback_query(call.id)
    elif call.data == '7':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_photo(call.message.chat.id,
                       'https://i.ibb.co/Rgvg7bz/image.jpg', caption='Лови. Надеюсь, что смог помочь. Обращайся снова! '
                                                                     'Ссылка на фото: https://i.ibb.co/Rgvg7bz/image.jpg')
        bot.send_message(call.message.chat.id,
                         "Надеюсь, у тебя хорошо развито пространственное мышление, потому что геометрия в 11 классе – это что-то жуткое. Но не будем отчаиваться, выбирай тему.", reply_markup=keyboard('tema2'))
        bot.answer_callback_query(call.id)
    elif call.data == '8':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_photo(call.message.chat.id,
                       'https://i.ibb.co/sjTx1YD/image.jpg', caption='Лови. Надеюсь, что смог помочь. Обращайся снова! '
                                                                     'Ссылка на фото: https://i.ibb.co/sjTx1YD/image.jpg')
        bot.send_message(call.message.chat.id,
                         "Надеюсь, у тебя хорошо развито пространственное мышление, потому что геометрия в 11 классе – это что-то жуткое. Но не будем отчаиваться, выбирай тему.", reply_markup=keyboard('tema2'))
        bot.answer_callback_query(call.id)
    elif call.data == '9':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_photo(call.message.chat.id,
                       'https://i.ibb.co/27g8M3G/image.png', caption='Лови. Надеюсь, что смог помочь. Обращайся снова! '
                                                                     'Ссылка на фото: https://i.ibb.co/27g8M3G/image.png')
        bot.send_message(call.message.chat.id,
                         "Окей, про Пифагора пока забудем. Теперь выбери интересующую тебя тему.", reply_markup=keyboard('tema1'))
        bot.answer_callback_query(call.id)
    elif call.data == '10':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_photo(call.message.chat.id,
                       'https://i.ibb.co/HBqLq9f/image.png', caption='Лови. Надеюсь, что смог помочь. Обращайся снова! '
                                                                     'Ссылка на фото: https://i.ibb.co/HBqLq9f/image.png')
        bot.send_message(call.message.chat.id,
                         "Окей, про Пифагора пока забудем. Теперь выбери интересующую тебя тему.", reply_markup=keyboard('tema1'))
        bot.answer_callback_query(call.id)
    elif call.data == '11':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_photo(call.message.chat.id,
                       'https://i.ibb.co/19j5Rgm/image.png', caption='Лови. Надеюсь, что смог помочь. Обращайся снова! '
                                                                     'Ссылка на фото: https://i.ibb.co/19j5Rgm/image.png')
        bot.send_message(call.message.chat.id,
                         "Окей, про Пифагора пока забудем. Теперь выбери интересующую тебя тему.", reply_markup=keyboard('tema1'))
        bot.answer_callback_query(call.id)
    elif call.data == '12':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_photo(call.message.chat.id,
                       'https://i.ibb.co/VB6CKK2/image.png', caption='Лови. Надеюсь, что смог помочь. Обращайся снова! '
                                                                     'Ссылка на фото: https://i.ibb.co/VB6CKK2/image.png')
        bot.send_message(call.message.chat.id,
                         "Окей, про Пифагора пока забудем. Теперь выбери интересующую тебя тему.", reply_markup=keyboard('tema1'))
        bot.answer_callback_query(call.id)
    elif call.data == '13':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_photo(call.message.chat.id,
                       'https://i.ibb.co/LQK7qtH/image.jpg', caption='Лови. Надеюсь, что смог помочь. Обращайся снова! '
                                                                     'Ссылка на фото: https://i.ibb.co/LQK7qtH/image.jpg')
        bot.send_message(call.message.chat.id,
                         "Надеюсь, у тебя хорошо развито пространственное мышление, потому что геометрия в 11 классе – это что-то жуткое. Но не будем отчаиваться, выбирай тему.", reply_markup=keyboard('tema2'))
        bot.answer_callback_query(call.id)
    elif call.data == '14':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_photo(call.message.chat.id,
                       'https://i.ibb.co/2WR7B32/image.jpg', caption='Лови. Надеюсь, что смог помочь. Обращайся снова! '
                                                                     'Ссылка на фото: https://i.ibb.co/2WR7B32/image.jpg')
        bot.send_message(call.message.chat.id,
                         "Надеюсь, у тебя хорошо развито пространственное мышление, потому что геометрия в 11 классе – это что-то жуткое. Но не будем отчаиваться, выбирай тему.", reply_markup=keyboard('tema2'))
        bot.answer_callback_query(call.id)
    elif call.data == '15':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_photo(call.message.chat.id,
                       'https://i.ibb.co/S5ZhW34/image.png', caption='Лови. Надеюсь, что смог помочь. Обращайся снова! '
                                                                      'Ссылка на фото: https://i.ibb.co/S5ZhW34/image.png')
        bot.send_message(call.message.chat.id,
                         "Надеюсь, у тебя хорошо развито пространственное мышление, потому что геометрия в 11 классе – это что-то жуткое. Но не будем отчаиваться, выбирай тему.", reply_markup=keyboard('tema2'))
        bot.answer_callback_query(call.id)
    elif call.data == '16':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_photo(call.message.chat.id,
                       'https://i.ibb.co/cgkQt8H/image.png', caption='Лови. Надеюсь, что смог помочь. Обращайся снова! '
                                                                      'Ссылка на фото: https://i.ibb.co/cgkQt8H/image.png')
        bot.send_message(call.message.chat.id,
                         "Надеюсь, у тебя хорошо развито пространственное мышление, потому что геометрия в 11 классе – это что-то жуткое. Но не будем отчаиваться, выбирай тему.", reply_markup=keyboard('tema2'))
        bot.answer_callback_query(call.id)
    elif call.data == '17':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_photo(call.message.chat.id,
                       'https://i.ibb.co/X2cWDPW/image.jpg', caption='Лови. Надеюсь, что смог помочь. Обращайся снова! '
                                                                      'Ссылка на фото: https://i.ibb.co/X2cWDPW/image.jpg')
        bot.send_message(call.message.chat.id,
                         "Надеюсь, у тебя хорошо развито пространственное мышление, потому что геометрия в 11 классе – это что-то жуткое. Но не будем отчаиваться, выбирай тему.", reply_markup=keyboard('tema2'))
        bot.answer_callback_query(call.id)
    elif call.data == '18':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_photo(call.message.chat.id,
                       'https://i.ibb.co/YDX9DH0/image.png', caption='Лови. Надеюсь, что смог помочь. Обращайся снова! '
                                                                      'Ссылка на фото: https://i.ibb.co/YDX9DH0/image.png')
        bot.send_message(call.message.chat.id,
                         "Окей, про Пифагора пока забудем. Теперь выбери интересующую тебя тему.", reply_markup=keyboard('tema1'))
        bot.answer_callback_query(call.id)
    elif call.data == '19':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_photo(call.message.chat.id,
                       'https://i.ibb.co/zVKy6V9/image.png', caption='Лови. Надеюсь, что смог помочь. Обращайся снова! '
                                                                      'Ссылка на фото: https://i.ibb.co/zVKy6V9/image.png')
        bot.send_message(call.message.chat.id,
                         "Надеюсь, у тебя хорошо развито пространственное мышление, потому что геометрия в 11 классе – это что-то жуткое. Но не будем отчаиваться, выбирай тему.", reply_markup=keyboard('tema2'))
        bot.answer_callback_query(call.id)
    elif call.data == '20':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_photo(call.message.chat.id,
                       'https://i.ibb.co/rykyXZp/image.png', caption='Лови. Надеюсь, что смог помочь. Обращайся снова! '
                                                                      'Ссылка на фото: https://i.ibb.co/rykyXZp/image.png')
        bot.send_message(call.message.chat.id,
                         "Надеюсь, у тебя хорошо развито пространственное мышление, потому что геометрия в 11 классе – это что-то жуткое. Но не будем отчаиваться, выбирай тему.", reply_markup=keyboard('tema2'))
        bot.answer_callback_query(call.id)
    elif call.data == '21':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_photo(call.message.chat.id,
                       'https://i.ibb.co/4Ph2Z3c/image.png', caption='Лови. Надеюсь, что смог помочь. Обращайся снова! '
                                                                      'Ссылка на фото: https://i.ibb.co/4Ph2Z3c/image.png')
        bot.send_message(call.message.chat.id,
                         "Надеюсь, у тебя хорошо развито пространственное мышление, потому что геометрия в 11 классе – это что-то жуткое. Но не будем отчаиваться, выбирай тему.", reply_markup=keyboard('tema2'))
        bot.answer_callback_query(call.id)
    elif call.data == '22':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_photo(call.message.chat.id,
                       'https://i.ibb.co/8jKWvq3/image.png', caption='Лови. Надеюсь, что смог помочь. Обращайся снова! '
                                                                      'Ссылка на фото: https://i.ibb.co/8jKWvq3/image.png')
        bot.send_message(call.message.chat.id,
                         "Окей, про Пифагора пока забудем. Теперь выбери интересующую тебя тему.", reply_markup=keyboard('tema1'))
        bot.answer_callback_query(call.id)
    elif call.data == '23':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_photo(call.message.chat.id,
                       'https://i.ibb.co/sVZRvBq/image.png', caption='Лови. Надеюсь, что смог помочь. Обращайся снова! '
                                                                      'Ссылка на фото: https://i.ibb.co/sVZRvBq/image.png')
        bot.send_message(call.message.chat.id,
                         "Окей, про Пифагора пока забудем. Теперь выбери интересующую тебя тему.", reply_markup=keyboard('tema1'))
        bot.answer_callback_query(call.id)
    elif call.data == '24':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_photo(call.message.chat.id,
                       'https://i.ibb.co/7t92Cgv/image.png', caption='Лови. Надеюсь, что смог помочь. Обращайся снова! '
                                                                      'Ссылка на фото: https://i.ibb.co/7t92Cgv/image.png')
        bot.send_message(call.message.chat.id,
                         "Окей, про Пифагора пока забудем. Теперь выбери интересующую тебя тему.", reply_markup=keyboard('tema1'))
        bot.answer_callback_query(call.id)
    elif call.data == '25':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_photo(call.message.chat.id,
                       'https://i.ibb.co/LCLXCk6/1.png', caption='Лови. Надеюсь, что смог помочь. Обращайся снова! '
                                                                      'Ссылка на фото: https://i.ibb.co/LCLXCk6/1.png')
        bot.send_message(call.message.chat.id,
                         "Здесь собраны некоторые лайфхаки и просто полезные теоремы и формулы для успешной сдачи экзамена:", reply_markup=keyboard('pl_eg'))
        bot.answer_callback_query(call.id)
    elif call.data == '26':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_photo(call.message.chat.id,
                       'https://i.ibb.co/BLXJ1tm/image.jpg', caption='Лови. Надеюсь, что смог помочь. Обращайся снова! '
                                                                      'Ссылка на фото: https://i.ibb.co/BLXJ1tm/image.jpg')
        bot.send_message(call.message.chat.id,
                         "Здесь собраны некоторые лайфхаки и просто полезные теоремы и формулы для успешной сдачи экзамена:", reply_markup=keyboard('pl_eg'))
        bot.answer_callback_query(call.id)
    elif call.data == '27':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_photo(call.message.chat.id,
                       'https://i.ibb.co/1GSv8kq/2.png', caption='Лови. Надеюсь, что смог помочь. Обращайся снова! '
                                                                      'Ссылка на фото: https://i.ibb.co/1GSv8kq/2.png')
        bot.send_message(call.message.chat.id,
                         "Здесь собраны некоторые лайфхаки и просто полезные теоремы и формулы для успешной сдачи экзамена:", reply_markup=keyboard('pl_eg'))
        bot.answer_callback_query(call.id)
    elif call.data == '28':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_photo(call.message.chat.id,
                       'https://i.ibb.co/XFWK9Cv/3.png', caption='Лови. Надеюсь, что смог помочь. Обращайся снова! '
                                                                      'Ссылка на фото: https://i.ibb.co/XFWK9Cv/3.png')
        bot.send_message(call.message.chat.id,
                         "Здесь собраны некоторые лайфхаки и просто полезные теоремы и формулы для успешной сдачи экзамена:", reply_markup=keyboard('pl_eg'))
        bot.answer_callback_query(call.id)
    elif call.data == 'n_1':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Что ищешь? Теорему из геометрии, а может формулу из алгебры? Выбери предмет', reply_markup=keyboard('teoria'))
        bot.answer_callback_query(call.id)
    elif call.data == 'n_2':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                         text='Что ищешь? Теорему из геометрии, а может формулу из алгебры? Выбери предмет', reply_markup=keyboard('teoria'))
    if call.data == 'n_4':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                         text='Что ищешь? Теорему из геометрии, а может формулу из алгебры? Выбери предмет', reply_markup=keyboard('teoria'))
        bot.answer_callback_query(call.id)
    elif call.data == 'n_3':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                         text='Пока!  ( ° ∀ ° )ﾉﾞ', reply_markup=None)

        sql1 = """UPDATE test SET k=? WHERE user_id=?"""
        b=(1, call.message.chat.id)
        cursor.execute(sql1, b)
        conn.commit()
        bot.answer_callback_query(call.id)

bot.polling(none_stop=True, interval=0)
