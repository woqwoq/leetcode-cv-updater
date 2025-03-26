from file_handler import replace_stats
from request_handler import request_leetcode_stats, find_all_appearances_json

leetcode_username = 'cim8848'


response_data = request_leetcode_stats(leetcode_username)
if response_data:
    stats_dict = find_all_appearances_json(response_data, 'difficulty', 'count')
    replace_stats('cv.tex', stats_dict)