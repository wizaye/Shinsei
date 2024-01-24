import discord
from typing import Final
import os
from dotenv import load_dotenv
from discord import app_commands
from discord.ext import commands
from responses import get_random_anime_quote, get_anime_info, get_anime_recommendations, get_response, get_random_waifu_image

# Importing token
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# Activate permissions (Intents)
intents: discord.Intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Command to get a random anime quote
@bot.tree.command(name="anime-quote")
async def anime_quote(interaction: discord.Interaction):
    try:
        quote = get_random_anime_quote()
        formatted_message = (
            f"Hey {interaction.user.mention}! Here's a random quote!\n"
            f'"{quote.quote}"\n'
            f'~ **{quote.character}** from **{quote.anime}**'
        )
        await interaction.response.send_message(formatted_message)
    except Exception as e:
        await interaction.response.send_message(f"An error occurred: {str(e)}", ephemeral=True)

# Command to generate a random waifu image
@bot.tree.command(name="generate-waifu-img")
async def anime_img(interaction: discord.Interaction):
    try:
        image_data = get_random_waifu_image()
        await interaction.response.send_message(image_data, ephemeral=True)
    except FileNotFoundError as e:
        await interaction.response.send_message(str(e), ephemeral=True)
    except Exception as e:
        await interaction.response.send_message(f"An unexpected error occurred: {str(e)}", ephemeral=True)

# Command to get anime information
@bot.tree.command(name="anime-info")
@app_commands.describe(anime_name="What anime should I Search for? (Please keep the first letter capitalized)")
async def anime_info(interaction: discord.Interaction, anime_name: str):
    try:
        anime_details = get_anime_info(anime_name)
        await interaction.response.send_message(f"Hey! {interaction.user.mention}\nAnime information for '{anime_name}':\n{anime_details}")
    except Exception as e:
        await interaction.response.send_message(f"An error occurred: {str(e)}", ephemeral=True)

# Command to get anime recommendations based on preferences
@bot.tree.command(name="anime-recommendations")
async def anime_recommendations(interaction: discord.Interaction):
    try:
        recommendations = get_anime_recommendations()
        await interaction.response.send_message(f"{recommendations}")
    except Exception as e:
        await interaction.response.send_message(f"An error occurred: {str(e)}", ephemeral=True)

# Command to handle generic user input
@bot.tree.command(name="talk-to-shinsei")
@app_commands.describe(user_query="Your input")
async def user_input_command(interaction: discord.Interaction, user_query: str):
    try:
        response = get_response(user_query)
        await interaction.response.send_message(f"{interaction.user.mention} {response}")
    except Exception as e:
        await interaction.response.send_message(f"An error occurred: {str(e)}", ephemeral=True)

# Handling the startup
@bot.event
async def on_ready():
    print("Bot is Up and Ready!")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
        print(f'{bot.user} is now running!')
    except Exception as e:
        print(f"An error occurred during startup: {str(e)}")

# Main entry point
def main() -> None:
    bot.run(token=TOKEN)

if __name__ == '__main__':
    main()
