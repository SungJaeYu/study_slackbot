import slack_bot from slackbot
import TOKEN from secret

def main():
    week = int(input())
    bot = slack_bot(TOKEN, week)
    bot.check_assignment

if __name__ == '__main__':
    main()
