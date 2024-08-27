import discord
from discord.ext import commands, tasks
import asyncio
import os
import time
from datetime import datetime, timedelta

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')


@bot.command()
async def countdown(ctx, hours: int, minutes: int, seconds: int):
    total_seconds = hours * 3600 + minutes * 60 + seconds
    end_time = time.time() + total_seconds
    current_time = time.time()
    remaining_time = 100

    message = await ctx.send(
        f'# Time remaining: {hours:02}:{minutes:02}:{seconds:02}')

    while remaining_time > 0:
        timer = timedelta(seconds=total_seconds)
        remaining_time = max(0, end_time - time.time())
        hours, remainder = divmod(int(remaining_time), 3600)
        minutes, seconds = divmod(remainder, 60)
        await message.edit(
            content=f'# Time remaining: {hours:02}:{minutes:02}:{seconds:02}')
        time.sleep(1.2)

    await message.edit(content='Time is up!')


@bot.command()
async def txtcountdown(ctx, title: str, hours: int, minutes: int,
                       seconds: int):
    total_seconds = hours * 3600 + minutes * 60 + seconds
    end_time = time.time() + total_seconds
    current_time = time.time()
    remaining_time = 100

    message = await ctx.send(f'# {title} {hours:02}:{minutes:02}:{seconds:02}')
    while remaining_time > 0:
        timer = timedelta(seconds=total_seconds)
        remaining_time = max(0, end_time - time.time())
        hours, remainder = divmod(int(remaining_time), 3600)
        minutes, seconds = divmod(remainder, 60)
        await message.edit(
            content=f'# {title} {hours:02}:{minutes:02}:{seconds:02}')
        time.sleep(1.2)
    await message.edit(content=f'# {title} is up!')


def main():
    token = os.getenv("TOKEN")

    if token:
        bot.run(token)
    else:
        print(
            "Error: Discord bot token not found. Set the DISCORD_BOT_TOKEN environment variable."
        )


if __name__ == "__main__":
    main()
