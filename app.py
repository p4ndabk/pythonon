from dotenv import load_dotenv
import src.commands.command as command

def start():
    load_dotenv()
    command.start()

start()