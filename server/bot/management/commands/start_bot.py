import os
import time
import discord
from discord.ext import commands
from django.core.management.base import BaseCommand
from asgiref.sync import sync_to_async
from rest.models import DiscordMessage


DISCORD_BOT_TOKEN = os.environ["DISCORD_BOT_TOKEN"]
DISCORD_CHANNEL_ID = int(os.environ["TEST_CHANNEL_ID"])


class Command(BaseCommand):
    help = "Starts discord bot"

    def handle(self, *args, **kwargs):
        intents = discord.Intents.default()
        intents.message_content = True
        bot = commands.Bot(command_prefix="!", intents=intents)

        @bot.event
        async def on_ready():
            print(f"✅ Logged in as {bot.user.name} ({bot.user.id})")
            channel = bot.get_channel(DISCORD_CHANNEL_ID)

            while True:
                time.sleep(3)
                discord_messages = await sync_to_async(list)(DiscordMessage.objects.filter(sent=False))
                for message in discord_messages:
                    if channel:
                        await channel.send(message.content)
                    message.sent = True
                    await sync_to_async(message.save)()

        bot.run(DISCORD_BOT_TOKEN)