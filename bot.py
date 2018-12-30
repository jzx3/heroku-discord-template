from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from discord.ext import commands
import discord
import os
import sys

sys.path.insert(0, 'src/')
import utility

bot = commands.Bot(command_prefix=';',
                   description='Heroku Discord Bot Example')


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
async def shell(ctx, *, cmd):
    """Run a shell command"""
    utility.shell_cmd(cmd)
    await ctx.send(txt)

    
# ----- Run the Bot -----------------------------------------------------------
if __name__ == '__main__':
    token = str(os.environ.get('DISCORD_BOT_TOKEN'))
    bot.run(token)
