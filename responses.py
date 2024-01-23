from anime_api.apis import AnimechanAPI,NekoBotAPI,WaifuImAPI
from aniwrap import Client
from random import choice, randint
from dotenv import load_dotenv
from jikanpy import Jikan
import random



from anime_api.apis.waifu_im.types import ImageTag, SearchSort, ImageOrientation

load_dotenv()

def get_anime_info(anime_title: str) -> str:
    try:
        jikan = Jikan()
        anime = jikan.search(search_type='anime', query=anime_title)
        anime_data = anime['data'][0]

        # Format the anime details into a string
        formatted_details = f"**Title:** {anime_data['titles'][0]['title']} ({anime_data['type']})\n" \
                            f"**Episodes:** {anime_data['episodes']}\n" \
                            f"**Status:** {anime_data['status']}\n" \
                            f"**Aired:** {anime_data['aired']['string']}\n" \
                            f"**Duration:** {anime_data['duration']}\n" \
                            f"**Rating:** {anime_data['rating']}\n" \
                            f"**Score:** {anime_data['score']}\n" \
                            f"**Ranked:** {anime_data['rank']}\n" \
                            f"**Scored By:** {anime_data['scored_by']}"

        # Add titles
        titles = "\n".join(title['title'] for title in anime_data['titles'])
        formatted_details += f"\n**Titles:** {titles}"

        return formatted_details
    except Exception as e:
        print(e)
        return f"An error occurred while fetching information for '{anime_title}'."
def get_anime_facts(anime_title: str) -> str:
    try:
        pass
    except Exception as e:
        return f'An error occurred: {str(e)}'

def get_random_anime_quote() -> str:
    try:
        quote=AnimechanAPI()
        response=quote.get_random_quote()
        # You may need to adjust the code based on the specific API or method for getting random anime quotes
        # This example assumes you're using the anime-api library, but you may need a different approach for quotes
        return response
    except Exception as e:
        return f'An error occurred: {str(e)}'
def get_random_waifu_image() -> str:
    try:
        api = WaifuImAPI()
        image = api.get_random_image(
            # tags=[ImageTag.NSFW.MILF],
            excluded_tags=[ImageTag.SFW.MAID],
            excluded_files=["some-image-signature"],
            is_nsfw=False,
            is_gif=False,
            order_by=SearchSort.RANDOM,
            orientation=ImageOrientation.LANDSCAPE,
        )
        return image.url
    except Exception as e:
        return f'An error occurred: {str(e)}'

def get_anime_recommendations() -> str:
    try:
        jikan = Jikan()
        anime_recommendations = jikan.recommendations(type='anime', page=2)

        # Shuffle the list of recommendations
        random.shuffle(anime_recommendations['data'])

        # Use random.choice to pick a random entry from the shuffled list
        random_entry = random.choice(anime_recommendations['data'])

        return format_recommendation(random_entry)
    except Exception as e:
        return f'An error occurred: {str(e)}'

def get_response(user_input: str) -> str:
    lowered = user_input.lower()

    if lowered == '':
        return "Well, you're silent..."
    elif 'hello' or 'hi' in lowered:
        return 'Hello there!'
    elif 'how are you' in lowered:
        return 'I\'m doing great! Thanks for asking.'
    elif 'bye' in lowered:
        return 'See ya later!'
    elif 'roll dice' in lowered:
        return f'You rolled: {randint(1, 6)}'
    elif 'what\'s date today?' in lowered:
        return f'Today is {datetime.datetime.now().strftime("%Y-%m-%d")}.'
    elif 'anime' in lowered:
        return 'I love anime too!'
    elif 'favorite anime' in lowered:
        return 'It\'s so hard to choose, there are so many great ones!'
    elif 'best anime' in lowered:
        return 'Opinions on the best anime vary, but there are many classics and popular ones.'
    elif 'anime recommendation' in lowered:
        return 'Method not implemented for anime recommendations using anime-api.'
    else:
        return choice(['I do not understand...', 'What are you talking about?', 'Do you mind rephrasing that?'])



#donot change 
    
def format_recommendation(recommendation_data: dict) -> str:
    entry_data = recommendation_data['entry']
    user_data = recommendation_data['user']
    
    formatted_recommendation = f"**Recommendation from {user_data['username']}**\n"
    formatted_recommendation += f"Date: {recommendation_data['date']}\n\n"
    
    for entry in entry_data:
        formatted_recommendation += f"**Anime Title:** {entry['title']}\n"
        formatted_recommendation += f"**MAL ID:** {entry['mal_id']}\n"
        formatted_recommendation += f"**URL:** {entry['url']}\n"
        
        # Add images information
        image_data = entry['images']['jpg']
        formatted_recommendation += f"**Image URL:** {image_data['image_url']}\n"
        formatted_recommendation += f"**Small Image URL:** {image_data['small_image_url']}\n"
        formatted_recommendation += f"**Large Image URL:** {image_data['large_image_url']}\n\n"

    formatted_recommendation += f"**Content:** {recommendation_data['content']}\n"
    
    # Add user information
    formatted_recommendation += f"\n**User Profile:** {user_data['url']}\n"
    formatted_recommendation += f"**Username:** {user_data['username']}\n"

    return formatted_recommendation