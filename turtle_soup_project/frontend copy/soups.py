soups = [
    {
        'id': 1,
        'title': '生日派对的秘密',
        'soup_q': '一个人过生日，邀请他所有的好朋友来参加。吹完蜡烛的时候，这个人把他所有的好朋友都杀了。',
        'soup_a': '男主和朋友曾经一起去探险，一段时间后没有了食物，因为男主本身是一个盲人，所以这帮朋友都骗他说每人砍下一只手来吃，可最后只砍了男主一个人的手。之后有一次男主邀请朋友们来参加自己的生日聚会，吹完蜡烛后所有人都鼓掌了，男主发现只有自己的手被砍下来吃了，男主无法忍受这样的欺骗于是杀了所有的好朋友。',
        'image': '/static/images/soup1.png',
        'audio': '/static/audio/soup1.mp3'
    },
    {
        'id': 2,
        'title': '深夜的脚步声',
        'soup_q': '一个女孩每晚听到家里的脚步声，但她独自生活。最终她搬走了，脚步声却跟着她到了新家。',
        'soup_a': '女孩的房子被安装了监控设备，一个陌生人通过监控观察她并模仿她的脚步声。搬家后，陌生人继续跟踪她，在新家重现脚步声。',
        'image': '/static/images/soup2.png',
        'audio': '/static/audio/soup2.mp3'
    },
    {
        'id': 3,
        'title': '消失的影子',
        'soup_q': '一个男人发现自己的影子不见了，无论在阳光下还是灯光下都没有影子。他开始感到恐惧，最后选择了自杀。',
        'soup_a': '男人被诊断出患有一种罕见的心理疾病，导致他无法感知自己的影子。他误以为自己失去了影子，恐惧和绝望最终导致他自杀。',
        'image': '/static/images/soup3.png',
        'audio': '/static/audio/soup3.mp3'
    }
]

def get_soup_by_id(soup_id):
    return next((soup for soup in soups if soup['id'] == soup_id), None)

def get_all_soups():
    return soups