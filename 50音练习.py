# coding=utf-8
import os
import random

length = 104
hi = ('あ', 'い', 'う', 'え', 'お',
      'か', 'き', 'く', 'け', 'こ',
      'さ', 'し', 'す', 'せ', 'そ',
      'た', 'ち', 'つ', 'て', 'と',
      'な', 'に', 'ぬ', 'ね', 'の',
      'は', 'ひ', 'ふ', 'へ', 'ほ',
      'ま', 'み', 'む', 'め', 'も',
      'や', 'ゆ', 'よ',
      'ら', 'り', 'る', 'れ', 'ろ',
      'わ', 'を',
      'ん',
      'きゃ', 'きゅ', 'きょ',
      'しゃ', 'しゅ', 'しょ',
      'ちゃ', 'ちゅ', 'ちょ',
      'にゃ', 'にゅ', 'にょ',
      'ひゃ', 'ひゅ', 'ひょ',
      'みゃ', 'みゅ', 'みょ',
      'りゃ', 'りゅ', 'りょ',
      'が', 'ぎ', 'ぐ', 'げ', 'ご',
      'ざ', 'じ', 'ず', 'ぜ', 'ぞ',
      'だ', 'ぢ', 'づ', 'で', 'ど',
      'ば', 'び', 'ぶ', 'べ', 'ぼ',
      'ぱ', 'ぴ', 'ぷ', 'ぺ', 'ぽ',
      'ぎゃ', 'ぎゅ', 'ぎょ',
      'じゃ', 'じゅ', 'じょ',
      'びゃ', 'びゅ', 'びょ',
      'ぴゃ', 'ぴゅ', 'ぴょ')
ka = ('ア', 'イ', 'ウ', 'エ', 'オ',
      'カ', 'キ', 'ク', 'ケ', 'コ',
      'サ', 'シ', 'ス', 'セ', 'ソ',
      'タ', 'チ', 'ツ', 'テ', 'ト',
      'ナ', 'ニ', 'ヌ', 'ネ', 'ノ',
      'ハ', 'ヒ', 'フ', 'ヘ', 'ホ',
      'マ', 'ミ', 'ム', 'メ', 'モ',
      'ヤ', 'ユ', 'ヨ',
      'ラ', 'リ', 'ル', 'レ', 'ロ',
      'ワ', 'ヲ',
      'ン',
      'キャ', 'キュ', 'キョ',
      'シャ', 'シュ', 'ショ',
      'チャ', 'チュ', 'チョ',
      'ニャ', 'ニュ', 'ニョ',
      'ヒャ', 'ヒュ', 'ヒョ',
      'ミャ', 'ミュ', 'ミョ',
      'リャ', 'リュ', 'リョ',
      'ガ', 'ギ', 'グ', 'ゲ', 'ゴ',
      'ザ', 'ジ', 'ズ', 'ゼ', 'ゾ',
      'ダ', 'ヂ', 'ヅ', 'デ', 'ド',
      'バ', 'ビ', 'ブ', 'ベ', 'ボ',
      'パ', 'ピ', 'プ', 'ペ', 'ポ',
      'ギャ', 'ギュ', 'ギョ',
      'ジャ', 'ジュ', 'ジョ',
      'ビャ', 'ビュ', 'ビョ',
      'ピャ', 'ピュ', 'ピョ')
ro = ('a', 'i', 'u', 'e', 'o',
      'ka', 'ki', 'ku', 'ke', 'ko',
      'sa', 'shi', 'su', 'se', 'so',
      'ta', 'chi', 'tsu', 'te', 'to',
      'na', 'ni', 'nu', 'ne', 'no',
      'ha', 'hi', 'fu', 'he', 'ho',
      'ma', 'mi', 'mu', 'me', 'mo',
      'ya', 'yu', 'yo',
      'ra', 'ri', 'ru', 're', 'ro',
      'wa', 'o',
      'n',
      'kya', 'kyu', 'kyo',
      'sha', 'shu', 'sho',
      'cha', 'chu', 'cho',
      'nya', 'nyu', 'nyo',
      'hya', 'hyu', 'hyo',
      'mya', 'myu', 'myo',
      'rya', 'ryu', 'ryo',
      'ga', 'gi', 'gu', 'ge', 'go',
      'za', 'ji', 'zu', 'ze', 'zo',
      'da', 'ji', 'zu', 'de', 'do',
      'ba', 'bi', 'bu', 'be', 'bo',
      'pa', 'pi', 'pu', 'pe', 'po',
      'gya', 'gyu', 'gyo',
      'ja', 'ju', 'jo',
      'bya', 'byu', 'byo',
      'pya', 'pyu', 'pyo')

def hiragana():
    os.system("cls")
    print('''根据给出的片假名输入对应的罗马音，例如：
あ 输入a并回车
输入exit返回选择界面。
请按回车键继续...''')
    str = input()
    count = 0
    right = 0
    wrong = 0
    os.system("cls")
    print(f'总计答题{count}个，正确{right}个，错误{wrong}个。正确率100%')
    while True:
        rand = random.randint(0, length-1)
        str = input(f'请输入{hi[rand]}的罗马音：')
        count += 1
        if str == ro[rand]:
            right += 1
        elif str == 'exit':
            os.system("cls")
            if count > 1:
                print(f'总计答题{count-1}个，正确{right}个，错误{wrong}个。正确率{right / (count-1) * 100}%')
            print('请按回车键继续...')
            str = input()
            break
        else:
            wrong += 1
            print(f'这道题答错了，正确答案是{ro[rand]}，再接再厉！')
            print('请按回车键继续...')
            str = input()
        os.system("cls")
        print(f'总计答题{count}个，正确{right}个，错误{wrong}个。正确率{right / count * 100}%')


def katakana():
    os.system("cls")
    print('''根据给出的平假名输入对应的罗马音，例如：
    ア 输入a并回车
    输入exit返回选择界面。
    请按回车键继续...''')
    str = input()
    count = 0
    right = 0
    wrong = 0
    os.system("cls")
    print(f'总计答题{count}个，正确{right}个，错误{wrong}个。正确率100%')
    while True:
        rand = random.randint(0, length - 1)
        str = input(f'请输入{ka[rand]}的罗马音：')
        count += 1
        if str == ro[rand]:
            right += 1
        elif str == 'exit':
            os.system("cls")
            if count > 1:
                print(f'总计答题{count - 1}个，正确{right}个，错误{wrong}个。正确率{right / (count - 1) * 100}%')
            print('请按回车键继续...')
            str = input()
            break
        else:
            wrong += 1
            print(f'这道题答错了，正确答案是{ro[rand]}，再接再厉！')
            print('请按回车键继续...')
            str = input()
        os.system("cls")
        print(f'总计答题{count}个，正确{right}个，错误{wrong}个。正确率{right / count * 100}%')


def run():
    while True:
        os.system("cls")
        print('''请选择需要练习的内容（输入1或者2并回车）：
1.平假名练习
2.片假名练习
输入exit退出。''')
        str = input()
        if str == '1':
            hiragana()
        elif str == '2':
            katakana()
        elif str == 'exit':
            break
        else:
            pass


if __name__ == "__main__":
    run()
