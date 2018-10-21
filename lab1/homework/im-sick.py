from gmail import GMail, Message

gmail = GMail('phuonghoa2303.2000@gmail.com', 'hayhoahocaachennhi?')

html_template = '''
<p>Dear Boss,</p>
<p>yesterday i had a serious accident: <strong>{reason}</strong>. As a result, I cannot move or do anything required using legs. Therefore, I am writing this e-mail to ask for permission that you could me 3 days off so that I could recover from my accident.</p>
<p>I promise that I will finish all of my unfinished works at the company while being at home.</p>
<p>I really hope that you could understand and I am looking forward for your reply.</p>
<p>Regards,</p>
<p>Le Phuong Hoa.</p>
...
reason_list = ["I have fallen from the stairs, which caused me a broken leg", "I ran into a truck, which caused me a broken leg", "I was dumped by my boyfriend, which cause me broken heart (and leg)"]

html_content = html_template.replace("{{reason}}", choice(reason_list))
msg = Message("Hello boss", to = "hoa.hlp00@gmail.com", html = html_content)


import datetime
set_time = 7
loop_counter = 0
while True:
    now = datetime.datetime.now()

    if now.hour == set_time:
        loop_counter += 1
        if loop_counter == 1:
            gmail.send(msg)
        loop_counter = 0