import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio

# .env-Datei laden
load_dotenv()

# Token aus Umgebungsvariable holen
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Eingeloggt als {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"🔁 Slash-Befehle synchronisiert ({len(synced)} Befehle).")
    except Exception as e:
        print(f"Fehler beim Syncen der Slash-Befehle: {e}")

async def load_extensions():
    for filename in os.listdir("."):
        if filename.startswith("m_") and filename.endswith(".py"):
            await bot.load_extension(filename[:-3])
            print(f"📦 Modul geladen: {filename}")

async def main():
    async with bot:
        await load_extensions()
        await bot.start(TOKEN)

asyncio.run(main())
