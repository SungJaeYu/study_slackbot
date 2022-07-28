from slack_sdk import WebClient
import baekjun as bkj
from datetime import date, datetime, timedelta

import secret as sc

class slack_bot:

    def __init__(self, token, week):
        self.client = WebClient(token)
        self.week = week

    def send_message(self, channel, text):
        response = self.client.chat_postMessage(
                channel=channel,
                text=text
                )
    
    def check_assignment_user(self, user, problem_id):
        _, solved_problem = bkj.get_solved(user)
        for problem in solved_problem:
            if problem.get("problemId") == problem_id:
                return True
        return False

    def check_assignment(self):
        problem_id = sc.PROBLEMS[self.week - 1]
        done_list = []
        for i, user in enumerate(sc.USERS):
            done = self.check_assignment_user(user, problem_id)
            if done == False:
                done_list.append(sc.NAMES[i] + " : Fail")
            else:
                done_list.append(sc.NAMES[i] + " : Success")
        
        channel = "#" + str(self.week) + "주차"
        for check_noti in done_list:
            self.send_message(channel, check_noti)

