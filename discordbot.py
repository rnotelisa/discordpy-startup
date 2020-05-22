from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

# 起動時に動作する処理
@bot.command()
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

@bot.command()
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await ctx.send('にゃーん')

bot.run(token)
