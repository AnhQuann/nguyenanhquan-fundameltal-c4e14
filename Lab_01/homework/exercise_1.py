from gmail import GMail, Message
from random import choice
import datetime

html_content = ['''<p>K&iacute;nh gửi c&ocirc; gi&aacute;o!</p>
<p>H&ocirc;m qua em ăn uống sinh hoạt thất thường n&ecirc;n cơ thể em rất {sick_ness}, e gửi mail n&agrave;y xin ph&eacute;p c&ocirc; cho em nghỉ buổi học h&ocirc;m nay ạ&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-frown.gif" alt="frown" /></p>
<p>Em cảm ơn c&ocirc;!</p>''',
'''<p>K&iacute;nh gửi c&ocirc; gi&aacute;o!</p>
<p>H&ocirc;m qua em ngấm mưa ngo&agrave;i đường rất l&acirc;u n&ecirc;n đ&atilde; bị cảm lạnh, hiện giờ em đang cảm thấy v&ocirc; c&ugrave;ng {sick_ness}, e gửi mail n&agrave;y xin ph&eacute;p c&ocirc; cho em nghỉ buổi học h&ocirc;m nay ạ&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-frown.gif" alt="frown" /></p>
<p>Em cảm ơn c&ocirc;!</p> ''',
]

reason_sick = ['mệt mỏi', 'khó chịu']

random_content = choice(html_content)
random_sick = choice(reason_sick)

perfect_mail = random_content.replace('{sick_ness}', random_sick )

gmail = GMail('anhquan190528011996@gmail.com', 'quan1905quan')
msg = Message('Đơn xin nghỉ ốm', to = 'anhquan190528011996@gmail.com', html = perfect_mail)

hour = choice(range(7,10))
now = datetime.datetime.now()
while True:
    if now.hour = hour:
        gmail.send(msg)
        break
