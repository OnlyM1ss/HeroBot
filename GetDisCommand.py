#Самый крутой бот для игры:D
# -*- coding: utf-8 -*-
import discord
import asyncio
import ctypes
from discord.ext import commands
TOKEN = 'Njk1MzkyNTQ4NzYzNTk4ODY4.XoZhTw.Sor6GTduurK6PXLMqLM6QfNj9-0'
class MyClient(discord.Client):
    def commands_for_game():
        up = "Вверх"
        down = "Вниз"
        right = "Вправо"
        left = "Влево"
        print("up: {up}\n down:{down}\n right{right}\n left{left}")
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        comand = message.content
        if(comand == 'right'):
            await message.channel.send("вы выбрали идти вправо")
        if(comand == 'left'):
            await message.channel.send("вы выбрали идти налево")
        if(comand == 'up'):
            await message.channel.send("Вы выбрали идти вверх")
        if(comand == 'down'):
            await message.chennel.send("Вы выбрали идти вниз")
        if message.content.startswith(':help'):
            await message.channel.send('Привет,{0.author}, Список доступных команд:')
            await message.channel.send('up: вверх\n down:вниз\n right: вправо\n left: налево(кстати не ходим)')
client = MyClient()
client.run(TOKEN)
