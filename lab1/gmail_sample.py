from gmail import GMail, Message

gmail = GMail('phuonghoa2303.2000@gmail.com', 'dmthangancap123')




# msg = Message("Don't follow your dream, follow me on instagram", to='c4e.techkidsvn@gmail.com',text="hihi",html="https://www.instagram.com/phng.hoa/",attachments=['hoa.jpg'])

html_template = '''
<p>Hello, tomorrow I have to {{reason}} at {{time}} pm. Therefore, I could not come to the interview.&nbsp;</p>
<p>I want to know that whether I can change my interview shift or not. Please let me know if it is okay.</p>
<p>Yours faithfully,</p>
<p>Hoa.</p>
'''
reason_list = [
    {
        "reason":....,
        ""
    },
    {}

]
# x = choice(reason_list)
html_content = html_template.replace("{{reason}}", choice(reason_list).replace("{{time}}", x)
msg = Message("Ui chao", to = "c4e.techkidsvn@gmail.com", html = html_content)
gmail.send(msg)