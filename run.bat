rem 1.2.5
@echo off
python -m pip install requests
python update.py
python -m pip install python_dotenv
python -m pip install discord.py
python -m pip install openai
python bot.py
pause