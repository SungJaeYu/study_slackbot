from slack_sdk import WebClient
import baekjun as bkj
from datetime import date, datetime, timedelta

import secret as sc

class slack_bot:
    
    ASSIGNMENT_NOT_DONE = 0
    ASSIGNMENT_DONE = 1
    NOT_CONNECTED = 2

    def __init__(self, token, week):
        self.client = WebClient(token)
        self.week = week

    def send_message(self, channel, text):
        response = self.client.chat_postMessage(
                channel=channel,
                text=text
                )
    
    def check_assignment_user(self, user, problem_id):
        count, solved_problem = bkj.get_solved(user)
        if count == 0:
            return self.NOT_CONNECTED
        for problem in solved_problem:
            if problem.get("problemId") == problem_id:
                return self.ASSIGNMENT_DONE
        return self.ASSIGNMENT_NOT_DONE

    def check_assignment(self):
        problem_id = sc.PROBLEMS[self.week - 1]
        done_list = []
        for i, user in enumerate(sc.USERS):
            done = self.check_assignment_user(user, problem_id)
            if done == self.ASSIGNMENT_NOT_DONE:
                done_list.append(sc.NAMES[i] + " : Fail")
            elif done == self.ASSIGNMENT_DONE:
                done_list.append(sc.NAMES[i] + " : Success")
            else:
                done_list.append(sc.NAMES[i] + " : Not Connected solved.ac")

        channel = "#" + str(self.week) + "주차"
        for check_noti in done_list:
            self.send_message(channel, check_noti)

    def check_rank(self):
        name_rank_list = []
        for i, user in enumerate(sc.USERS):
            profile = bkj.get_profile(user)
            rank = profile.get("rank")
            name_rank = (sc.NAMES[i], rank)
            name_rank_list.append(name_rank)
        
        sorted(name_rank_list, key=lambda name_rank: name_rank[1])
        channel = "#rank"
        for i, (name, rank) in enumerate(name_rank_list):
            text = "Rank " + str(i) + " : " + name + " (" + str(rank) + ")"
            self.send_message(channel, text)

        
        
            
