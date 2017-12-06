from gmail import GMail, Message
from random import choice


html_content =['''<p>Em ch&agrave;o c&ocirc;</p>
<p>Em xin nghỉ buổi học h&ocirc;m nay v&igrave; em {sick_ness}</p>
<p>Em cảm ơn c&ocirc;</p>''',

''' '''
''' '''
]

reason_sick = ['ốm', 'đau bụng', 'mệt']
random_sick = choice(reason_sick)

html_content = html_content.replace('{sick_ness}', random_sick)

gmail = GMail('anhquan190528011996@gmail.com', 'quan1905quan')
msg = Message('C4E14', to = 'anhquan190528011996@gmail.com', html = html_content)
gmail.send(msg)
