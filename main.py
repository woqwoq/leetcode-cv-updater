from file_handler import replace_stats
from request_handler import request_leetcode_stats, find_all_appearances_json
from config_parser import get_cv_filename, get_username

leetcode_username = get_username()
cv_filename = get_cv_filename()


response_data = request_leetcode_stats(leetcode_username)
if response_data:
    stats_dict = find_all_appearances_json(response_data, 'difficulty', 'count')
    replace_stats(cv_filename, stats_dict)