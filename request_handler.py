import requests

def request_leetcode_stats(username: str):
    """Fetch LeetCode statistics for the given username."""
    url = "https://leetcode.com/graphql/"
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
        "variables": {"username": username},
        "operationName": "userSessionProgress"
    }

    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code != 200:
        print(f"Error {response.status_code}: {response.text}")
        return None
    
    return response.json()

def find_all_appearances_json(data, key1, key2):
    """Find all appearances of key1 and key2 in a nested JSON and store them in a dictionary."""
    stats_dict = {}
    
    def traverse(obj):
        if isinstance(obj, dict):
            if key1 in obj and key2 in obj:
                stats_dict.setdefault(obj[key1], []).append(obj[key2])
            for value in obj.values():
                traverse(value)
        elif isinstance(obj, list):
            for item in obj:
                traverse(item)
        return stats_dict
    
    return traverse(data)