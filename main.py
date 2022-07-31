import slackbot as sb
import secret

def week_check():
    week = int(input())
    bot = sb.slack_bot(secret.TOKEN, week)
    bot.check_assignment()

def rank_check():
    bot = sb.slack_bot(secret.TOKEN, 0)
    bot.check_rank()


def main():
    week_check()

if __name__ == '__main__':
    main()
