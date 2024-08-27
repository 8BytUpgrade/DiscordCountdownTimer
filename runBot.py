import argparse
import os
from main import main  # Replace 'your_bot_script' with the actual script name


def parse_args():
    parser = argparse.ArgumentParser(description="Run the Discord bot")
    parser.add_argument('--token', type=str, help='Discord bot token')
    return parser.parse_args()


def set_token_env_variable(token):
    os.environ["TOKEN"] = token


if __name__ == "__main__":
    args = parse_args()
    if args.token:
        set_token_env_variable(args.token)
    main()
