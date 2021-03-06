import re
import requests
import os

def dowmloadPic(html, keyword):
    pic_url = re.findall('"objURL":"(.*?)",', html, re.S)
    i = 1
	
    print('find keyword:' + keyword)
    path = r'/root/app/images'
    os.chdir(path)
    if i<100:
        for each in pic_url:
            print('downloading' + str(i) + str(each))
            try:
                pic = requests.get(each, timeout=10)
            except requests.exceptions.ConnectionError:
                print('error')
                continue

            dir = '../images/' + keyword + '_' + str(i) + '.jpg'
            fp = open(dir, 'wb')
            fp.write(pic.content)
            fp.close()
            i += 1


if __name__ == '__main__':
    word = raw_input("Input key word: ")
    url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + str(word) + '&ct=201326592&v=flip'
    result = requests.get(url)
    print(result.text)
    dowmloadPic(result.text, word)
