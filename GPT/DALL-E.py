import requests

KEY = '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'


def generate(message):
    url = 'https://api.openai.com/v1/images/generations'

    headers = {
        'Authorization': f'Bearer {KEY}',
        'Content-Type': 'application/json'
    }

    response = requests.post(url, json={'prompt': message}, headers=headers)

    if response.status_code == 200:
        result = response.json()
        print(result)
    else:
        print("Error: ", response.text)


text = 'Futuristic picture of a Unicorn in an eggshell on Mars where it snows with a 3D inscription Continent LM Family'
generate(text)