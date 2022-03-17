#------------------------------------------------------------------------------
# Definitions and configuration for text_miner_JP.py
#------------------------------------------------------------------------------

char_enc = [
    'utf-8 sig',
    'cp932',
    'euc_jp',
    'euc_jis_2004',
    'euc_jisx0213',
    'iso2022_jp',
    'iso2022_jp_1',
    'iso2022_jp_2',
    'iso2022_jp_2004',
    'iso2022_jp_3',
    'iso2022_jp_ext',
    'shift_jis',
    'shift_jis_2004',
    'shift_jisx0213',
    ]

particles = [
    'は', 'が', 'を', 'も', 'の', 'と', 'や',
    'か', 'よ', 'ね', 'に', 'へ', 'で'
    ]
grammar = [
    'です', 'から', 'ない', 'ある', 'する', 'けど'
    ]

punctuation = [
    '。', '、', '？',
    '(', ')', '（', '）', '～', ',', '-'
    ]

single_hiragana = [
    'あ', 'い', 'う', 'え', 'お', 
    'か', 'き', 'く', 'け', 'こ',
    'さ', 'し', 'す', 'せ', 'そ',
    'た', 'ち', 'つ', 'て', 'と',
    'な', 'に', 'ぬ', 'ね', 'の',
    'は', 'ひ', 'ふ', 'へ', 'ほ',
    'ま', 'み', 'む', 'め', 'も',
    'や', 'ゆ', 'よ',
    'ら', 'り', 'る', 'れ', 'ろ',
    'わ', 'を', 'ん',
    'が', 'ぎ', 'ぐ', 'げ', 'ご',
    'ざ', 'じ', 'ず', 'ぜ', 'ぞ',
    'だ', 'ぢ', 'づ', 'で', 'ど',
    'ば', 'び', 'ぶ', 'べ', 'ぼ',
    'ぱ', 'ぴ', 'ぷ', 'ぺ', 'ぽ'
    ]

digits = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
]

file_name = 'text_miner_output'
ext = '.csv'
data_columns = [
    'Word',
    'Frequency'
    ]

char_to_num = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'I': 8,
    'J': 9,
    'K': 10,
    'L': 11,
    'M': 12,
    'N': 13,
    'O': 14,
    'P': 15,
    'Q': 16,
    'R': 17,
    'S': 18,
    'T': 19,
    'U': 20,
    'V': 21,
    'W': 22,
    'X': 23,
    'Y': 24,
    'Z': 25
    }