import discord
from discord import app_commands
from discord.ext import commands

class WarnSystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.warnings = {}  # user_id : anzahl

    @app_commands.command(name="warn", description="Verwarnt einen Nutzer.")
    async def warn(self, interaction: discord.Interaction, member: discord.Member, reason: str = "Kein Grund angegeben."):
        user_id = member.id
        self.warnings[user_id] = self.warnings.get(user_id, 0) + 1
        await interaction.response.send_message(
            f"⚠️ {member.mention} wurde verwarnt! Grund: {reason} (Anzahl: {self.warnings[user_id]})",
            ephemeral=False
        )

    @app_commands.command(name="warns", description="Zeigt die Anzahl der Verwarnungen eines Nutzers.")
    async def warns(self, interaction: discord.Interaction, member: discord.Member):
        count = self.warnings.get(member.id, 0)
        await interaction.response.send_message(f"📋 {member.mention} hat {count} Verwarnung(en).")

async def setup(bot):
    await bot.add_cog(WarnSystem(bot))
