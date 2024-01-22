from random import choice,randint
def get_response(user_input:str)-> str:
    # raise NotImplementedError('Code is Missing')
    lowered:str=user_input.lower()
    if(lowered==''):
        return "Well, you\'re silent..."
    elif 'hello' in lowered:
        return 'Hello there!'
    elif 'how are you' in lowered:
        return 'I\'m doing great!,Thanks for asking'
    elif 'bye' in lowered:
        return 'See Ya Later!'
    elif 'roll dice' in lowered:
        return f'You rolled:{randint(1,6)}'
    elif 'What\'s date today?' in lowered:
        return 'Sorry I can\'t do that'
    else:
        return choice(['I do not understand....','What are you Talking about?','Do you mind rephrasing that?'])