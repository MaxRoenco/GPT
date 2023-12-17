import openai

KEY = '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'

openai.api_key = KEY

def generate_response(text):
    response = openai.Completion.create(
        prompt=text,
        engine='text-davinci-003',
        max_tokens=100,
        temperature=0.9,
        n=1,
        stop=None,
        timeout=15
    )

    if response and response.choices:
        return response.choices[0].text.strip()
    else:
        return None


res = generate_response('Единорог в яичной скорлупе на марсе где идет снег с 3д надписью Continent LM Family')

print(res)