import requests
import json

def prob_info(dir_name):
    global problems
    under_bar = []
    comma = []
    open_brace = 0
    prob_category = []

    for i in range(len(dir_name)):
        if dir_name[i] == '_':
            under_bar.append(i)
        if dir_name[i] == '(':
            open_brace = i
        if dir_name[i] == ',' or dir_name[i] == ')':
            comma.append(i)

    prob_num = dir_name[0:under_bar[0]]
    
    if len(under_bar) > 1:
        prob_source = 'boj'
        prob_name = dir_name[under_bar[1]+1:open_brace]
    else:
        prob_source = 'swea'
        prob_name = dir_name[under_bar[0]+1:open_brace]
    
    prob_diff = dir_name[open_brace+1:comma[0]]
    
    for i in range(len(comma) - 1):
        prob_category.append(dir_name[comma[i]+2:comma[i+1]])

    prob_obj = {}
    prob_obj['prob_num'] = prob_num
    prob_obj['prob_source'] = prob_source
    prob_obj['prob_name'] = prob_name
    prob_obj['prob_diff'] = prob_diff
    prob_obj['prob_category'] = prob_category

    problems.append(prob_obj)




algo_URL = 'https://api.github.com/repos/edugieun/Algorithm-Solving/contents/'
type_list = requests.get(algo_URL).json()
# print(type_list[0]['type'])

problems = []

# test cnt
cnt = 0

for prob_type_obj in type_list:
    if prob_type_obj['type'] == 'dir':
        prob_type = prob_type_obj['name']
        if prob_type == '풀이중':
            continue
        else:
            prob_list = requests.get(algo_URL + prob_type).json()
            for prob_dir in prob_list:
                prob_info(prob_dir['name'])

                # test 하나씩만 담아보기
                break

with open('test.json', 'w', encoding='utf-8') as make_files:
    json.dump(problems, make_files, ensure_ascii=False, indent="\t")