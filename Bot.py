import telebot 
import requests
import random 
import vodka
from telebot import types
from time import sleep
import time
import os,sys
from telegraph import Telegraph
def vodka(s):
 for ASU in s + '\n':
  sys.stdout.write(ASU)
  sys.stdout.flush()
  sleep(2./600)
Z = '\x1b[1;31m'#احمر
X = '\x1b[1;32m'#اخضر
C = '\x1b[1;33m'#yellow
V = '\x1b[1;34m'#blue	
B = '\x1b[1;35m'#pink
N = '\x1b[1;36m'#لبني
M = '\x1b[1;37m'#ابيض	 
t = time.localtime()
current_time = time.strftime('%H:%M:%S', t)
current_date =  time.strftime('%D', t)
vodka(X+'__     _____  ____  _  __    _    ')
vodka(Z+'\ \   / / _ \|  _ \| |/ /   / \   ')
vodka(X+' \ \ / / | | | | | |   /   / _ \  ')
vodka(Z+'  \ V /| |_| | |_| | . \  / ___ \ ')
vodka(X+'   \_/  \___/|____/|_|\_\/_/   \_\ ')
vodka(N+'Time Now : '+M+current_time)
vodka(N+'Date Now : '+M+current_date)
vodka(M+'- - - - - - - - - - - - - - - - - - - - ')
vodka(Z+'('+X+'⌯'+Z+')'+N+'Telegram : '+M+'@Vodka_tk')
vodka(Z+'('+X+'⌯'+Z+')'+N+'GitHub : '+M+'https://github.com/Vodkahunter.com')
vodka(Z+'('+X+'⌯'+Z+')'+N+'Program Code : '+M+'python3')
vodka(Z+'('+X+'⌯'+Z+')'+N+'Program App : '+M+'pycharm')
vodka(M+'- - - - - - - - - - - - - - - - - - - - ')
Token = input(N+'('+B+'⌯'+N+')'+B+'Enter Token : '+M)
bot = telebot.TeleBot(Token)
co = types.InlineKeyboardButton(text ="- VODKA_Tools </>",url='https://t.me/Vodka_Tools')
by = types.InlineKeyboardButton(text ="- Version",callback_data = 'vodka')
@bot.message_handler(commands=['start'])
def first(message):
    maac = types.InlineKeyboardMarkup()
    maac.row_width = 2
    maac.add(co,by)    
    bot.send_message(message.chat.id , f'<b>Hi VODKA #1st - python☬\n- - - - - - - - - - - - - -\nWelcome To Telegraph Uploader Bot!\nSend The Title|The Content!\nEx : |Hey|Hi_Vodka|\n- - - - - - - - - - - - - -\nBy  : @Vodka_tk</b>', parse_mode="html",reply_to_message_id=message.message_id, reply_markup=maac)
@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    if call.data == "vodka":
        bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="- VERSION 0.0.1")
@bot.message_handler(func=lambda m:True)      
def telegraph(message):
    msg = message.text
    data = str(msg).split('|')
    title =  data[1]
    content = data[2]   
    telegraph = Telegraph()     
    telegraph.create_account(short_name='1337')

    response = telegraph.create_page(
   f'{title}',
        html_content=f'<p>{content}</p>'
    )
    x = (response['url'])    
    
    bot.reply_to(message,f'<b>- We Are Uploding Your Content Wait Please</b>', parse_mode='html')
    sleep(2)
    bot.send_message(message.chat.id,f'<b>Your Telegraph Site : {x}</b>',parse_mode='html')  
bot.polling(True)      
