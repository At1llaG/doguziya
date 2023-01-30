from nltk.chat.util import Chat, reflections

m_pairs = [
    ["Benim adim (.*)", ["Merhaba %1 nasilsin?"]],
    ['(merhaba|selam|sa)',["merhabalarrr", "as"]],
    ['(.*) hava çok (.*)', ['bence de %1 hava %2']],
    ["gittim mi", ["mi"]]
]

m_reflections = {
    'merhabalar': 'merhaba, nasilsin',
    'gittim': 'gittin',
    'sa':'as'
}

m_chat = Chat(m_pairs, m_reflections)
m_chat.converse(quit="exit")
#print(chat._substitute('merhaba'))