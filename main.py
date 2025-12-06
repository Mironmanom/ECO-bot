import telebot
import os
import random
game = 0
advs = ["Сади деревья,они поглашают углекислый газ !",
        "Пользуйся велосипедами и другими экологичными транспортными средствами.",
        "Пользуйся многоразовыми вещами!",
        ]
facts = ["2010 - 2019 гг стал самым жарким десетилетием owo ",
         "за последние 100 лет средняя температура земли увеличилась на 1,2C ! Owo"
         "c 20 века уровень воды поднялся на 20 см ! OwO",
         "за последние 40 лет ледяной покров Арктики сократился на 40%! OwO",
         "с 1993 по 2019 год ледняки Гренландии потеряли около 250 МИЛЛИАРДОВ тонн льда!!! QwQ",
         "человечество вырабатывает больше углекислого газа чем вулканы ! owo"]
bot = telebot.TeleBot("7704115421:AAHykbkd5vqZPMuRj5w-9WJX26g0UZIhGJw") 

@bot.message_handler(commands=['start',"hi","hello"])
def send_welcome(message):
    bot.reply_to(message, "Привет!я Эко-бот и я могу помочь тебе с глобальным потеплением >w< (/help если нужна помощь с командами 0W0))")



@bot.message_handler(commands=['advs'])
def send_adv(message):
    adv = random.choice(advs)
    bot.reply_to(message,f'{adv} =w= /help - для поиска команд')



@bot.message_handler(commands=['cho'])
def send_adv(message):
    cho = int(message.text.split()[1]) if len(message.text.split()) > 1 else 0
    if cho == 0:
        bot.reply_to(message, '1 - Глобальное потепление , 2 - парниковый эффект, 3 - парниковые газы OwO')
    if cho == 1:
        bot.reply_to(message, 'Глобальное потепление - это повышение средней температуры земли, вызваное парниковым эффектом. owo /help - для поиска команд')
    if cho == 2:
        bot.reply_to(message, 'Парниковый эффект - это когда солнце светит на нашу планету и часть её радиации отражается к солнцу, а часть снова отражается к земле из-за парниковых газов, нагревая её. OwO /help - для поиска команд')
    if cho == 3:
        bot.reply_to(message, 'Парниковые газы - метан,водяные пары,угликислые газы,оксиды азотов и др. !w! /help - для поиска команд')

@bot.message_handler(commands=['fact'])
def send_fact(message):
    fact = random.choice(facts)
    r_number = random.randint(1,3)
    number = ''
    if r_number == 1:
        number = 'А ты знал что, '
    elif r_number == 2:
        number = 'Оказывается '
    elif r_number == 3:  
        number = 'Интересный факт: '
    bot.reply_to(message,f'{number}{fact} /help - для поиска команд ')



@bot.message_handler(commands=["gamelist"])
def send_list(message):
    list_choice = int(message.text.split()[1]) if len(message.text.split()) > 1 else 0
    if list_choice == 0:
        bot.reply_to(message, '1 - игра с семечками /game (число игры) - чтобы выбрать игру ^w^')
    if list_choice == 1:
        bot.reply_to(message, '1 - игра с семечками наподобие угадай число 1-10 /game (число игры) - чтобы выбрать игру ^w^')


@bot.message_handler(commands=["game"])
def send_game(message):
    game_choice = int(message.text.split()[1]) if len(message.text.split()) > 1 else 0
    
    if game_choice == 0:
        bot.reply_to(message,"Забыл поставить номер игры после команды! -W-")
    if game_choice == 1:
        global game,dice

        dice = random.randint(1,10)
        game = 1
        bot.reply_to(message,"Выбрана игра с семечками, угадай число от 1 до 10 ! (напиши комманду /play,пробел и потом число) ^w^ ")

@bot.message_handler(commands=["play"])
def send_play(message):
    global game , dice
    play = int(message.text.split()[1]) if len(message.text.split()) > 1 else 0
    if game == 0:
        bot.reply_to(message,"Игра не выбрана! -W- ")
    if game == 1:
        if play == dice:
            bot.reply_to(message,"Ты угадал число! ^w^")
        else:
            bot.reply_to(message,f"Ты не угадал число!, правильным числом было:{dice} *w*")
        dice = random.randint(1,10)
    
@bot.message_handler(commands=['help'])
def send_commands(message):
    bot.reply_to(message,'/advs - даёт совет по борьбе с глобальным потеленем,/fact - случайный факт про глобальные потепления,/gamelist - список мини игр,/game - выбор мини игры,/play - действие в игре (если игра выбрана),/cho - узнай о чем-нибуть. ^w^')



bot.infinity_polling()