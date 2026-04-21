from apps.integrations.openai_service import ask_gpt


def process_bot_message(bot, user_input):
    prompt = f"{bot.system_prompt}\nUser: {user_input}"
    return ask_gpt(prompt)
