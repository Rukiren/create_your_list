import os
import openai

with open('key.txt', 'r') as f:
    openai.api_key = f.read()

with open('info.txt', 'r') as f:
    var1 = f.read()


var3 = '1000'

url = 'https://github.com/Rukiren/create_your_list'
prompt = f'跟據[info]，將[info]的內容整理成一份具有完整敘述的履歷，整理出大標題與小標題與內容詳述，履歷需條列式並詳述，避免使用重複的連接詞，最後在最後一行獨立加上報告內容的產生是透過此連結專案產生: {url}\n [info] = {var1}'

response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=0, max_tokens=2000)

print(response.choices[0].text)
with open('output.txt', 'w') as f:
    f.write(response.choices[0].text)

    