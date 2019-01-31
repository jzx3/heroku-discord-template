from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from discord.ext import commands
import discord
import logging
import os
import sys

sys.path.insert(0, 'src/')
import utility

logging.basicConfig(
    level=logging.INFO,
    style = '{',
    datefmt = "%Y%m%d %H:%M:%S",
    format = "{asctime} [{levelname:<8}] {name}: {message}")

bot = commands.Bot(command_prefix=';',
                   description='Heroku Discord Bot Example')

setattr(bot, "logger", logging.getLogger("bot.py"))


# ----- Bot Events ------------------------------------------------------------
@bot.event
async def on_ready():
    print('Bot logged in as {} (id={})'.format(
        bot.user.name, bot.user.id))


@bot.event
async def on_command_error(ctx, err):
    if isinstance(err, commands.CommandOnCooldown):
        await ctx.send('Error: {}'.format(err))


# ----- Bot Commands ----------------------------------------------------------
@bot.command(brief='Ping the server')
async def ping(ctx):
    """Ping the server to verify that it\'s listening for commands"""
    await ctx.send('Pong!')

    
@bot.command(brief='Run shell command')
@commands.is_owner()
async def shell(ctx, *, cmd):
    """Run a shell command"""
    txt = utility.shell_cmd(cmd)
    await ctx.send(txt)


@bot.command(brief='About this bot')
@commands.is_owner()
async def about(ctx):
    """Gives a description for this bot"""
    txt = (
        "This bot serves as a template for a Discord bot"
        "that can be hosted on Heroku.\n"
        "The Github page for this bot is: "
        "<https://github.com/jzx3/heroku-discord-template>")
    await ctx.send(txt)

    
# ----- Run the Bot -----------------------------------------------------------
if __name__ == '__main__':
    token = str(os.environ.get('DISCORD_BOT_TOKEN'))
    bot.run(token)
