import json
import requests

res = requests.get('https://jsonplaceholder.typicode.com/posts')
result_dic = json.loads(res.text)


for data in result_dic : 

    comment_url = 'https://jsonplaceholder.typicode.com/comments?postId=' + str(data['id'])
    comment_res = requests.get(comment_url)

    comment_data = {
        'id': data['id'],
        'title': data['title'],
        'comment': []
    }

    print(comment_data)

    all_data = []
    for comment in comment_res.json():
        comment_data['comment'].append(comment['body'].replace('\n',''))

        all_data.append(comment_data)

    with open('data2.json', 'w') as f:
        json.dump(all_data, f)
    