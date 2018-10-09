import discord
import asyncio
import configparser


config = configparser.ConfigParser()
config.read('./config.ini', 'UTF-8')


server = discord.Object(id=config.get('server', 'server'))
t_ch1  = discord.Object(id=config.get('t_channels', 't_ch1'))
t_ch2  = discord.Object(id=config.get('t_channels', 't_ch2'))
t_ch3  = discord.Object(id=config.get('t_channels', 't_ch3'))
t_ch4  = discord.Object(id=config.get('t_channels', 't_ch4'))
t_ch5  = discord.Object(id=config.get('t_channels', 't_ch5'))
BOT_TOKEN   = config.get('token', 'TOKEN')
client = discord.Client()

@client.event
async def on_ready():
    print('\U0001F423 ' * 10)
    print(client.user.name + ' has logged in')
    print('\U0001F423 ' * 10)
    client.loop.create_task(ch_status_message())

@client.event
async def on_message(message):
    if '/member' in message.content:
        server_member  = [member.name for member in client.get_all_members()]
        await client.send_message(message.channel, 'このサーバには現在'+ len(server_member) + '人います。')

    if ('ぴよ' or 'ひよこ' or 'っぴ') in message.content:
        await client.add_reaction(message, "\U0001F423")

@client.event
async def ch_status_message():
    while True:
        server_member  = [member.name for member in client.get_all_members()]
        logined_member = [member.name for member in client.get_all_members() if member.voice.voice_channel is not None]

        if len(logined_member) >= 1:
            m = "誰かがボイスチャットにいます。"
            await client.send_message(ch_4, m)
            await asyncio.sleep(7200)
        else:
            await asyncio.sleep(300)

client.run(BOT_TOKEN)
