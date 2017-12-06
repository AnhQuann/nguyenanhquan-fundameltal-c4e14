from pymongo import MongoClient

client = MongoClient('mongodb://admin:admin@ds021182.mlab.com:21182/c4e')

db = client.get_default_database()

posts = db['posts']

new_post = {
    'title': 'Mùa đông không lạnh',
    'author': 'Nguyễn Anh Quân',
    'content':
    '''
        Đông này vẫn giống Đông xưa
        Vẫn đi xe máy vẫn chưa có bồ
        Ra đường vẫn cứ solo
        Về nhà mẹ hỏi "có bồ chưa con? "
        Đáp rằng "Con vẫn còn son"
        Nhiều em nhưng chẳng thể chọn được ai
        Nào mẹ đâu biết chông gai
        Tình trường hiểm ác, con trai rụt rè.
    '''
}
posts.insert_one(new_post)
# posts.remove(new_post)
