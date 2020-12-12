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
    def __init__(self, message):
        # Если в сообщении есть текст(если его нет возвращается None телеграмом)
        if message != None: 
            self.message = message 
            # Разбиваем сообщение на слова
            self.messageSplit = self.message.split() 
        # Если в сообщении есть текст(если его нет возвращается None телеграмом)
        else: 
        	# Случайный текст который никому не нужен
            self.message = "jadkasd" 
            # Никому не нужный массив, но он избавит нас от ошибок 
            self.messageSplit = ['0', '0', '0'] 

class Commands(Message):
    """
    Здесь хранятся все действия команд, ну то есть итоговый результат, 
    сам процесс выполнения команды
    """
    def compatibility(self):
        # Выбираем случайное число
        percent = randint(0, 100) 

        #Создаем текст
        message = f"Твоя совместимость с {self.messageSplit[1]} = {percent}%" 
        
        # Отправляем
        print(bot.send_message(-1001372561007, message)) 

    def call(self):
        message = "@miymiymiymiy2cotaiodnacoshechka @begemotik_na_safari @prihtihpih @great_insignificance @nikanikazaya @VismutXd @SofiFriend @nikamurmurmur @Funny_bunnyyyyyyy @RealIvanShevchenko @S_hishk_a @483866062 @1067032717 @manda_rin_ochka @1012942756 @1034087554 \n были призваны кентом выше"
        # Отправляем
        
        print(bot.send_message(-1001372561007, message))


class Check(Message):
    """
	Класс проверки на команду. 
	С вызывающим действием отправки сообщения
    """

    # Функция, возвращающая то, к какой команде могло бы принадлежать сообщение
    def returnCommand(self) -> str: 

    	#Если первое слово такое, то возвращаем call
        if self.messageSplit[0] == "@all":
            self.result = "call"
        
        #Если же совместимость первое слово и есть второе слово то возвращаем "совместимость"
        # == 2 - чтобы не допускать многословия, спрашиваем совместимость мою, и, например, Вити
        elif self.messageSplit[0].lower() == "совместимость" and (len(self.messageSplit) == 2):
            self.result = "compatibility"
        
        #Иначе возвращаем мессагу с ошибкой, чтобы в дальнейшем если что - оно выскочило 
        else:
            self.result = "Error: command not found"

        #Возвращаем результат
        return self.result

    #Функция возвращающая отправку сообщения. Короче вызываем отправку сообщения
    def act(self, message):
        
        # присваиваем переменной строковое значение - команда, которую хочет пользователь
        self.var = self.returnCommand()
        
        #Объявляем и инициализируем класс с командами
        command = Commands(message)
        
        #вызываем если подходит
        if self.var == "compatibility":
            return command.compatibility()

        #Вызываем если подходит сюда
        elif self.var == "call":
            return command.call()

	
#Трогать его не надо
class MyError(Exception):
    """
    Если нужны будут ексепшены - воспользуюсь классом
    """
    def __init__(self, text):
        self.txt = text


tg_token = "12XCKOfP1bijo4WQArvI" #Токен
 
bot = telebot.TeleBot(tg_token)

tg_id = -1001372561007

@bot.message_handler(content_types=['text', 'document', 'audio', 'sticker', 'photo', 'video', 'video_note', 'animation', 'caption', 'voice', 'venue', 'dice', 'poll', 'new_chat_member'])

def start(message):
    check = Check(message.text)
    print(check.act(message.text))

#лонгпул
bot.polling(none_stop=True, interval=0)

#Слепак id 483866062
# Васильченко 1067032717