import os
import openai

with open('key.txt', 'r') as f:
    openai.api_key = f.read()

with open('info.txt', 'r') as f:
    var1 = f.read()




var3 = '1000'
url = 'https://github.com/Rukiren/create_your_list'
prompt = f'請閱讀以下內容[{var1}]，將其中的內容整理成一份具有完整敘述的履歷，履歷需條列式並詳述，方便產生下一份報告，並在結尾加上報告內容是透過此連結專案產生: {url}'

response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=0, max_tokens=2000)

print(response.choices[0].text)
with open('output.txt', 'w') as f:
    f.write(response.choices[0].text)

    