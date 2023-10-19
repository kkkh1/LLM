import subprocess
cmd = "nmap -sV -O -sC 10.0.0.5 -min-rate 5000"
proc=subprocess.Popen(cmd.split(), stdout=subprocess.PIPE,encoding="ISO-8859-1")
text=proc.stdout.read()
#text=text.decode("UTF-8")
#print(text)


templete="""Nmapを使用して、自分のシステムに危険がないかテストした。下記はテスト結果である。考えられる危険性について、サービス名のみ列挙し、優先度が高い順に整列してほしい
また、
サービス名それぞれの前後には「？」を追加し、

例えば、GPTという名称のサービスが危険であり、
GPT　?GPT2.5? のようにしてほしい
"""
output_file='sample.text'
que=templete+'\n\n'+text
with open(output_file,'w') as f:
    f.write(que)
    print(que)
    print("completed")


