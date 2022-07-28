import json
import requests


""" https://gist.github.com/is2js/3c32a75986e6f17364c39e6fa2a05cbc """
def get_profile(user_id):
    """
    정보 조회 - user_id를 입력하면 백준 사이트에서 해당 user의 프로필 정보 중 일부를 반환해줌.
    :param str user_id: 사용자id
    :return: 백준 프로필 정보
    :rtype: dict
    """
    url = f"https://solved.ac/api/v3/user/show?handle={user_id}"
    r_profile = requests.get(url)
    if r_profile.status_code == requests.codes.ok:
        profile = json.loads(r_profile.content.decode('utf-8'))
        profile = \
        {
        "tier" : profile.get("tier"),
        "rank" : profile.get("rank"),
        "solvedCount" : profile.get("solvedCount"),
        "rating" : profile.get("rating"),
        "exp" : profile.get("exp"),
        }
    else:
        print("프로필 요청 실패")
    return profile

def get_solved(user_id):
    """
    정보 조회 - user_id를 입력하면 백준 사이트에서 해당 user가 푼 총 문제수, 문제들 정보(level 높은 순)를 튜플(int, list)로 반환해줌.
    :param str user_id: 사용자id
    :return: 내가 푼 문제수, 내가 푼 문제들 정보
    :rtype: int, list
    """
    url = f"https://solved.ac/api/v3/search/problem?query=solved_by%3A{user_id}&sort=level&direction=desc"
    r_solved = requests.get(url)
    if r_solved.status_code == requests.codes.ok:
        solved = json.loads(r_solved.content.decode('utf-8'))
        
        count = solved.get("count")

        items = solved.get("items")
        solved_problems = []
        for item in items:
            solved_problems.append(
                {
                    'problemId': item.get("problemId"),
                    'titleKo': item.get("titleKo"),
                    'level': item.get("level"),
                }
            )
        # print("푼 문제수와 젤 고난이도 문제 1개만 >>>", count, solved_problems[0])
    else:
        print("푼 문제들 요청 실패")
    return count, solved_problems

