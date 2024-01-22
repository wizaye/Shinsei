from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from discord.ext import commands
from responses import get_response, get_anime_info, get_anime_recommendations, get_random_anime_quote

# Loading from dotenv
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
print(TOKEN)

# Activate permissions (Intents)
intents: Intents = Intents.default()
intents.message_content = True
bot: commands.Bot = commands.Bot(command_prefix='!', intents=intents)

# Handling the startup
@bot.event
async def on_ready() -> None:
    print(f'{bot.user} is now running!')

# Command to get information about an anime
@bot.command(name='animeinfo', help='Get information about an anime')
async def anime_info(ctx: commands.Context, anime_title: str) -> None:
    anime_info = get_anime_info(anime_title)
    await ctx.send(anime_info)

# Command to get a random anime quote
@bot.command(name='animequote', help='Get a random anime quote')
async def anime_quote(ctx: commands.Context) -> None:
    quote = get_random_anime_quote()
    await ctx.send(quote)

# Command to get anime recommendations based on preferences
@bot.command(name='animerecommend', help='Get anime recommendations based on preferences')
async def anime_recommendations(ctx: commands.Context, preferences: str) -> None:
    recommendations = get_anime_recommendations(preferences)
    await ctx.send(recommendations)

# Message functionality (use commands.Bot.process_commands for command processing)
@bot.event
async def on_message(message: Message) -> None:
    if message.author == bot.user:
        return

    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {message.author.display_name}:"{user_message}"')

    # Process commands
    await bot.process_commands(message)

# Main entry point
def main() -> None:
    bot.run(token=TOKEN)

if __name__ == '__main__':
    main()
