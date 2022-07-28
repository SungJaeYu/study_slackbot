import slackbot as sb
import secret

def main():
    week = int(input())
    bot = sb.slack_bot(secret.TOKEN, week)
    bot.check_assignment()

if __name__ == '__main__':
    main()
