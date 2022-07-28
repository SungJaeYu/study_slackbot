import os
from slack_sdk.rtm_v2 import RTMClient
import baekjun as bkj
from datetime import date, datetime, timedelta

class slack_bot:

    def __init__(self, token):
        self.client = RTMClient(token)
        self.done_date = date(2022, 8, 2)
        self.week = 3

    def send_message(self, channel, text):
        response = self.client.web_client.chat_postMessage(
                channel=channel,
                text=text
                )
    
    def check_assignment_user(self, user, problem_id):
        solved_problem = bkj.get_solved(user)
        for problem in solved_problem:
            if problem.get("problemId") == problem_id:
                return True
        return False

    def check_assignment(self):
        problem_id = problem_list[self.week]
        done_list = []
        for i, user in enumerate(users):
            done = self.check_assignment_user(user, problem_id)
            if done == False:
                done_list.append(name_list[i] + "Fail")
            else:
                done_list.append(name_list[i] + "Success")
        
        channel = "#" + self.week + "주차"
        for check_noti in done_list:
            self.send_message(channel, check_noti)
        # TODO : 연속된 한개의 메시지로 출력하도록 수정
        
    def time_check(self):
        if date.now() == self.done_date:
            self.check_assignment()
            self.done_date = self.done_date + timedelta(days=7)


        

