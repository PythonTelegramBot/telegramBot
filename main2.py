# -*- coding: utf-8 -*-
import requests
import telebot
from random import randint

class Message:
    """
    Самый главный класс, который другие классы будут наследовать
    подается текст сообщения
    обрабатываем сообщение(если текст)
    """
    type_of_message = None #
    text_of_message = None #
    command_in_message = None
    variable_in_message = None
    def __init__(self, message):
        self.type_of_message = message.content_type
        if self.type_of_message == 'text':
            self.text_of_message = message.text
            splited_text = message.text.split()
            if len(splited_text)>=3:
                self.command_in_message = splited_text[1]
                self.variable_in_message = splited_text[2]



class Commands(Message):
    """
    Здесь хранятся все действия команд, ну то есть итоговый результат,
    сам процесс выполнения команды
    """
    def compatibility(self):
        # Выбираем случайное число
        percent = randint(0, 100)
        # Создаем текст
        message = f"Твоя совместимость с {self.variable_in_message} = {percent}%"
        # Отправляем
        bot.send_message(-1001372561007, message)
    def call(self):
        message = "@miymiymiymiy2cotaiodnacoshechka @begemotik_na_safari @prihtihpih @great_insignificance @nikanikazaya @VismutXd @SofiFriend @nikamurmurmur @Funny_bunnyyyyyyy @RealIvanShevchenko @S_hishk_a @483866062 @1067032717 @manda_rin_ochka @1012942756 @1034087554 \n были призваны кентом выше"
        # Отправляем
        print(bot.send_message(-1001372561007, message))

    all_my_command = {'совместимость': compatibility,
                      '@all':call}

class Check(Message):
    """
	Класс проверки на команду.
	С вызывающим действием отправки сообщения
    """
    # Функция возвращающая отправку сообщения. Короче вызываем отправку сообщения
    def act(self, message):
        # Объявляем и инициализируем класс с командами
        command = Commands(message)
        if self.command_in_message != None:
            if self.command_in_message in command.all_my_command.keys():
                return command.all_my_command[self.command_in_message](self)
            else:
                bot.send_message(-1001372561007, 'Прости, малыш! Такого я не умею')


# Трогать его не надо
class MyError(Exception):
    """
    Если нужны будут ексепшены - воспользуюсь классом
    """
    def __init__(self, text):
        self.txt = text


tg_token = "1229540188:AAGqGiNy0nM17YHtpXCKOfP1bijo4WQArvI"  # Токен

bot = telebot.TeleBot(tg_token)

tg_id = -1001372561007


@bot.message_handler(
    content_types=['text'],commands=['bot'])
def start(message):
    check = Check(message)
    check.act(message)


# лонгпул
bot.polling(none_stop=True, interval=0)

# Слепак id 483866062
# Васильченко 1067032717
