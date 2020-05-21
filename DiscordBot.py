import discord
import asyncio
import re

client = discord.Client()
general_ch = discord.Object(id='')
announcement_ch = discord.Object(id='')
BOT_TOKEN = ''


@client.event
async def on_ready():
    display_login_message()
    client.loop.create_task(search_vc_member())


@client.event
async def search_vc_member():
    while True:
        vc_logined_member = [member.name for member in client.get_all_members() if member.voice.voice_channel is not None]

        if len(vc_logined_member) >= 1:
            m = ""
            for user in vc_logined_member:
                m += user + "と"
            m = m[:-1]
            m += "がボイスチャットにいるっぴ！"
            await client.send_message(announcement_ch, m)
            await asyncio.sleep(3600)
        else:
            await asyncio.sleep(300)


@client.event
async def on_channel_create():
    await client.send_message(announcement_ch, "新しいちゃねんるが増えたっぴ!")


@client.event
async def on_voice_state_update(before, after):
    # if((before.voice.self_mute is not after.voice.self_mute) or (before.voice.self_deaf is not after.voice.self_deaf)):
    #     return False
    if (before.voice.self_mute is not after.voice.self_mute):
        print(after.name + "がボイスミュートステータスを変更")
        return

    elif (before.voice.self_deaf is not after.voice.self_deaf):
        print(after.name + "が音声ミュートステータスを変更")
        return

    elif (before.voice_channel is None):
        await client.send_message(announcement_ch, after.name + "がボイスチャットに入ったっぴ！")

    elif (after.voice_channel is None):
        await client.send_message(announcement_ch, after.name + "がボイスチャットから抜けたっぴ！")


@client.event
async def on_message(message):
    if '/call' in message.content:
        arg = message.content.split(" ")
        tm = [member.mention for member in client.get_all_members() if member.display_name == arg[1] ]
        tm = str(tm)
        tm = tm.strip('[')
        tm = tm.strip(']')
        tm = tm.strip('\'')
        c = int(arg[2])
        if tm is not None:
            if c < 10 or c >= 0:
                c = 10
            while c != 0:
                await client.send_message(message.channel, tm)
                await asyncio.sleep(5)
                c = c-1


def display_login_message():
    print('\U0001F423 ' * 10)
    print(client.user.name + ' has logged in')
    print('\U0001F423 ' * 10)


client.run(BOT_TOKEN)
