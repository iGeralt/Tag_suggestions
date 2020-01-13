import json
import requests

def findkeys(node, kv):
    if isinstance(node, list):
        for i in node:
            for x in findkeys(i, kv):
                if x == 'food-items-v1.0':
                   print('')
                else :
                    yield x
    elif isinstance(node, dict):
        if kv in node:
            yield node[kv]
        for j in node.values():
            for x in findkeys(j, kv):
                if x == 'food-items-v1.0':
                   print('')
                else:
                    yield x

def get_tags_suggestions(image_url):
    headers = {
    'Authorization': 'Key 407af2f185ac4303bfc5f0335360b549', #407af2f185ac4303bfc5f0335360b549 is api key
    'Content-Type': 'application/json',
    }
    data = '{"inputs": [{"data": {"image": {"url": "'+image_url+'"}}}]}'

    response = requests.post('https://api.clarifai.com/v2/models/bd367be194cf45149e75f01d59f77ba7/outputs', headers=headers, data=data)
    print(response)
    json_data = json.loads(response.text)
    data=list(findkeys(json_data,'name'))
    return data


if __name__ == '__main__':
    test_image_url = 'https://image.shutterstock.com/image-photo/fresh-tasty-burger-isolated-on-260nw-705104968.jpg' #provide image url
    tags_suggessted = get_tags_suggestions(test_image_url)
    print(tags_suggessted)
