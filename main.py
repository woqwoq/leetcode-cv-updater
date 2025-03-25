import requests

url = "https://leetcode.com/graphql/"
your_leetcode_username = 'cim8848'
headers = {"Content-Type": "application/json"}

payload = {
    "query": """
        query userSessionProgress($username: String!) {
            allQuestionsCount {
                difficulty
                count
            }
            matchedUser(username: $username) {
                submitStats {
                    acSubmissionNum {
                        difficulty
                        count
                        submissions
                    }
                }
            }
        }
    """,
    "variables": {"username": your_leetcode_username},
    "operationName": "userSessionProgress"
}

response = requests.post(url, json=payload, headers=headers)

if response.status_code != 200:
    print(f"Error {response.status_code}: {response.text}")



response = response.json()

import json
print(json.dumps(response, indent=4))



def find_all_appearances_json(json, app1, app2):
    stats_dict = {}

    def traverse(my_dict):
        if isinstance(my_dict, dict):

            if app1 in my_dict and app2 in my_dict:
                if(my_dict[app1] not in stats_dict):
                    stats_dict[my_dict[app1]] = []
                stats_dict[my_dict[app1]].append(my_dict[app2])

            for element in my_dict:
                if isinstance(my_dict[element], list) or isinstance(my_dict[element], dict):
                    traverse(my_dict[element])

        elif isinstance(my_dict, list):
            for element in my_dict:
                    traverse(element)

        return stats_dict

    return traverse(json)

print(find_all_appearances_json(response, 'difficulty', 'count'))


