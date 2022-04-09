from argparse import ArgumentParser
from snapchat_bots import SnapchatBot

class CaptureBot(SnapchatBot):
    def on_snap(self, sender, snap):
        snap.save()

if __name__ == '__main__':
    parser = ArgumentParser("Capture Bot")
    parser.add_argument('-u', 'capturebot81723871', required=True, type=str, help="Username of the account to run the bot on")
    parser.add_argument('-p', '1qa2ws3ed', required=True, type=str, help="Password of the account to run the bot on")

    args = parser.parse_args()

    bot = CaptureBot(args.username, args.password)
    bot.listen(timeout=60)
