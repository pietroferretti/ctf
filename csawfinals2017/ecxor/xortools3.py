# -*- coding: utf-8 -*-

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

import itertools
import string
import math
import ast


def str2bytes(s):
    return b''.join(ord(char).to_bytes(1, 'little') for char in s)

def bytes2str(b):
    return ''.join(chr(x) for x in b)


def xor_str(s1, s2):
    '''XOR between two strings. The longer one is truncated.'''
    return ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(s1, s2))


def blockify(text, blocklen):
    '''Splits the text as a list of blocklen-long strings'''
    return [text[i:i+blocklen] for i in range(0, len(text), blocklen)]


def columnify(ciphertext, keylen, fill=False):
    '''Takes the ciphertext and collects the characters corresponding to each key position.
    
    Arguments:
        ciphertext -- the ciphertext as a string
        keylen     -- the length of the xor key
        fill       -- if True all the lists of characters will 
                      be filled with None to have the same length (default False)

    Returns a list of lists of characters.
    '''
    
    # split ciphertext in blocks
    blocks = blockify(ciphertext, keylen)

    # build list of lists
    result = [list(tup) for tup in itertools.zip_longest(*blocks)]

    # remove Nones
    if not fill:
        for l in result:
            if None in l:
                l.remove(None)    # at most one None

    return result


def hamming_distance(s1, s2):
    '''Returns the Hamming Distance between two strings of equal length.'''
    assert len(s1) == len(s2)
    distance = 0
    for char1, char2 in zip(s1, s2):
        byte1 = ord(char1)
        byte2 = ord(char2)
        diff = byte1 ^ byte2
        distance += sum(int(bit, 2) for bit in bin(diff)[2:])
    return distance


def egcd(a, b):
    '''Euclidean Greatest Common Divisor'''
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


# TODO increase score if actual english words are found
def englishscore(text):
    '''Estimates how close the text is to the english language character distribution. 

    NB: A lot of stuff in this function is hand picked to make it work. It is absolutely not guaranteed to be optimal.

    Returns the score for the text as a number (higher is better).
    '''
    
    # letter distribution + custom punctuation to taste (as percentages)
    distributions = {'a': 8.167, 'b': 1.492, 'c': 2.782, 'd': 4.253, 'e': 12.702, 'f': 2.228, 'g': 2.015, 'h': 6.094, 'i': 6.966, 'j': 0.153, 'k': 0.772, 'l': 4.025, 'm': 2.406, 'n': 6.749, 'o': 7.507, 'p': 1.929, 'q': 0.095, 'r': 5.987, 's': 6.327, 't': 9.056, 'u': 2.758, 'v': 0.978, 'w': 2.360, 'x': 0.150, 'y': 1.974, 'z': 0.074, ' ': 14, '0': 0.1, '1': 0.1, '2': 0.1, '3': 0.1, '4': 0.1, '5': 0.1, '6': 0.1, '7': 0.1, '8': 0.1, '9': 0.1,  '.': 0.1, ',': 0.1, '-': 0.05, '?': 0.05, '!': 0.05 }
    otherchars = [chr(x) for x in range(256) if chr(x) not in distributions]
    for c in otherchars:
        distributions[c] = 0.0
    MAXSCORE = 1000

    textlen = len(text)

    # compute distribution for every character
    textdist = {}
    for x in text:
        if x in textdist:
            textdist[x] += 1.0 / textlen * 100
        else:
            textdist[x] = 1.0 / textlen * 100

    # compute mean squared error
    error = 0
    for c in distributions:
        error += (distributions[c] - textdist.get(c, 0)) ** 2
    mserror = error / len(distributions)

    if mserror == 0:
        score = MAXSCORE
    else:
        score = min(1 / mserror, MAXSCORE)

    # decrease score sharply if the text contains unprintable characters
    for x in text:
        if x not in string.printable:
            score /= 2

    return score


def findkeylen_all(ciphertext, maxcompperlen=100, verbose=False):
    '''Determines the length of a repeated xor key given a ciphertext.
    
    The algorithm works using the Normalized Hamming Distance.

    Arguments:
        ciphertext    -- the ciphertext as a string
        maxcompperlen -- the maximum number of comparisons between blocks that will be performed for each candidate length
        verbose       -- print debug information if True

    Returns all the possible key lengths and their respective score as a list of (length, score) tuples.
    The list is ordered from the best to the worst score (lower is better).
    '''
    
    len_score_list = []

    # try every useful length
    for keylen in range(1, len(ciphertext)/2 + 1):
        if verbose:
            print('Checking key length ' + str(keylen))

        # split in blocks
        blocks = blockify(ciphertext, keylen)

        # keep only full-length blocks 
        blocks = filter(lambda b: len(b) == keylen, blocks)
        
        # get hamming distance of each block with every other block
        total_distance = 0
        n_comparisons = 0
        for block1, block2 in itertools.combinations(blocks, 2):
            total_distance += hamming_distance(block1, block2)
            n_comparisons += 1
            if n_comparisons >= maxcompperlen:
                break

        avg_distance = float(total_distance) / n_comparisons
        norm_distance = avg_distance / keylen

        len_score_list.append((keylen, norm_distance))

    # order by ascending score
    result = sorted(len_score_list, key=(lambda t: t[1]))
    return result


def findkeylen(ciphertext, topn=7, maxcompperlen=100, verbose=False):
    '''Determines the length of a repeated xor key given a ciphertext.

    Takes the greatest common divisor of the most probable candidates, because multiples of the actual key length often get better scores.
    (see also https://trustedsignal.blogspot.it/2015/06/xord-play-normalized-hamming-distance.html)
    NB: this works best when the characters of the key are very different from one another.

    Arguments:
        ciphertext    -- the ciphertext as a string
        topn          -- the number of candidate lengths to consider in the gcd step
        maxcompperlen -- the maximum number of comparisons between blocks that will be performed for each candidate length
        verbose       -- print debug information if True

    Returns the most probable key length.
    '''

    TOPN = topn    # number of top candidates to consider for the gcd step
    
    if verbose:
        print('Collecting key length candidates...')
    len_score_list = findkeylen_all(ciphertext, maxcompperlen=maxcompperlen, verbose=verbose)
    topn_lengths = [t[0] for t in len_score_list[:TOPN]]

    if verbose:
        print('Computing most common gcd...')
    gcd_occurences = {}
    for len1, len2 in itertools.combinations(topn_lengths, 2):
        gcd = egcd(len1, len2)[0]
        if gcd != 1:
            if gcd not in gcd_occurences:
                gcd_occurences[gcd] = 1
            else:
                gcd_occurences[gcd] += 1

    # return most common gcd
    return max(gcd_occurences.keys(), key=(lambda k: gcd_occurences[k]))


def findkeychars(ciphertext, keylen=None, charset=string.printable, decfunc=xor_str, verbose=False):
    '''Finds all possible characters for each key index given a set of characters that can appear in the plaintext.

    This function assumes a polyalphabetic substition cipher is used.

    Arguments:
        ciphertext -- the ciphertext as a string
        charset    -- a string containing all the characters that can be found in the plaintext (default: all printable characters)
        keylen     -- the length of the key (default: found using findkeylen)
        decfunc    -- a function that takes a character of ciphertext and a character of key and returns a character of plaintext (default: xor)
        verbose    -- print debug information if True (default: False)
    Returns a list of lists of characters, one list for each key index.
    '''

    if keylen is None:
        if verbose:
            print('Finding key length...')
        keylen = findkeylen(ciphertext, verbose=verbose)
        if verbose:
            print('Key length = ' + str(keylen))

    columns = columnify(ciphertext, keylen)

    if verbose:
        print('Finding acceptable character sets...')
    result = []
    i = 1
    for column in columns:
        if verbose:
            print('Checking column ' + str(i))
        # list of acceptable values for this key index
        good_chars = [chr(x) for x in range(256)]
        for char in column:
            # find values of key that map to an acceptable plaintext
            ok_set = [chr(k) for k in range(256) if (decfunc(char, chr(k)) in charset)]
            # take intersection with previous acceptable values
            good_chars = filter((lambda e: e in ok_set), good_chars)

        # order good_chars by closeness to the english character distribution
        if verbose:
            print('Sorting characters by score...')
        fitnessfunc = lambda k: englishscore(''.join(decfunc(c, k) for c in column))
        good_chars = sorted(good_chars, key=fitnessfunc)[::-1]

        if verbose:
            print(good_chars)
        result.append(good_chars)
        i += 1

    if verbose:
        print('Done finding acceptable key characters.')
    return result


def findkeys(ciphertext, keylen=None, charset=string.printable, decfunc=xor_str, verbose=False):
    '''Finds all possible keys given a set of characters that can appear in the ciphertext.

    This function assumes a substition cipher is used. (char by char)

    Arguments:
        ciphertext -- the ciphertext as a string
        charset    -- a string containing all the characters that can be found in the plaintext (default: all printable characters)
        keylen     -- the length of the key (default: found using findkeylen)
        decfunc    -- a function that takes a character of ciphertext and a character of key and returns a character of plaintext (default: xor)
        verbose    -- print debug information if True (default: False)

    Returns a generator that yields keys as strings.
    '''

    char_list = findkeychars(ciphertext, keylen, charset, decfunc, verbose)

    def key_generator(iter_prod):
        while True:    # stop when iter_prod raises StopIteration
            yield ''.join(iter_prod.__next__())

    return key_generator(itertools.product(*char_list))


def findkey(ciphertext, keylen=None, charset=string.printable, decfunc=xor_str, verbose=False):
    '''A wrapper to get the first, most probable key from findkeys()'''
    return findkeys(ciphertext, keylen, charset, decfunc, verbose).__next__()


# TODO: add option to find all indexes such that the crib only decrypts in a specified charset
def cribdrag(ciphertext, keylen, decfunc=xor_str, keyfunc=None):
    '''Starts an interactive cribdrag session.

    This function assumes a polyalphabetic substition cipher is used.

    Arguments:
        ciphertext -- the ciphertext as a string
        keylen     -- the length of the key
        decfunc    -- a function that takes a character of ciphertext and a character of key and returns a character of plaintext (default: xor)
        keyfunc    -- a function that takes a character of ciphertext and a character of plaintext and returns a character of key (default: same as decfunc)

    Returns the state of the key at the end of the session as a list of characters and None.
    '''

    def print_lines(blocks, cribindex, criblen):
        '''Print blocks line by line'''
        blocklen = len(blocks[0])
        pad = int(math.log(blocklen * len(blocks), 10))
        for i in range(len(blocks)):
            block = blocks[i]
            line = str(i * blocklen)
            line += ' ' * (pad - len(line) + 2)
            for j in range(len(blocks[i])):
                if cribindex == (i * blocklen + j) and criblen != 0:
                    line += '['
                elif (cribindex + criblen) != (i * blocklen + j) or j == 0:
                    line += ' '
                line += block[j]
                if (cribindex + criblen) == (i * blocklen + j + 1) and criblen != 0:
                    line += ']'
            print(line)

    def getkey(ciphertext, keylen, crib, cribindex, keyfunc):
        '''Find the key corresponding to a crib at position cribindex'''
        key = [None] * keylen
        for i in range(len(crib)):
            keychar = keyfunc(ciphertext[cribindex + i], crib[i])
            key[(cribindex + i) % keylen] = keychar
        return key

    def decrypt(ciphertext, key, decfunc):
        '''Decrypt the ciphertext with key, unknown bytes are replaced with "*"'''
        res = ''
        for i in range(len(ciphertext)):
            if key[i % keylen] is None:
                res += '*'
            else:
                res += decfunc(ciphertext[i], key[i % keylen])
        return res

    def update_and_print():
        '''Update key with current crib and print result'''
        
        # empty curr_key
        del curr_key[:]
        # update curr_key
        cribkey = getkey(ciphertext, keylen, crib, cribindex, keyfunc)
        for i in range(keylen):
            if cribkey[i] != None:
                curr_key.append(cribkey[i])
            elif key[i] != None:
                curr_key.append(key[i])
            else:
                curr_key.append(None)

        # print decrypted blocks
        dec_blocks = blockify(decrypt(ciphertext, curr_key, decfunc), keylen)
        print_lines(dec_blocks, cribindex, len(crib))
        print('Crib: {}'.format(crib))
        print('Index: {}'.format(cribindex))
        print('Key: {}'.format(key))
        print('New key: {}'.format(curr_key))

    def prompt(prevchoice, prevarg):
        userinput = raw_input('> ')
        userinput = userinput.lstrip()
        if userinput == '':
            return prevchoice, prevarg
        choice = userinput.split(' ')[0]
        argument = userinput[len(choice) + 1:]
        return choice, argument

    # initial parameters
    crib = ''
    cribindex = 0
    key = [None] * keylen
    curr_key = key[:]
    if keyfunc is None:
        keyfunc = decfunc

    update_and_print()

    # prompt
    choice, argument = prompt('h', '')

    while (choice != 'q' and choice != 'quit'):

        if (choice == 'h' or choice == 'help'):
            guide = ''
            guide += 'Commands:\n'
            guide += '  (c)rib <your_crib> -- set the crib (argument is like \"asdf\\x10\\n jkl\")\n'
            guide += '  (n)ext -- move the crib forward by one\n'
            guide += '  (p)rev -- move the crib back by one\n'
            guide += '  (j)ump <index> -- move the crib to an index\n'
            guide += '  (o)k -- update the key using the current crib\n'
            guide += '  (k)ey <char_list> -- set the key (argument is like [\'a\', \'\\x01\', None])\n'
            guide += '  (s)how -- show current decrypted plaintext\n'
            guide += '  (r)eset -- reset everything from this session\n'
            guide += '  (q)uit -- exit from the cribdrag tool\n'
            guide += '  (h)elp -- show this guide\n'
            print(guide)

        elif (choice == 'c' or choice == 'crib'):
            # remove spaces from sides
            argument = argument.strip()
            if argument == '':
                argument = '""'
            try:
                newcrib = ast.literal_eval(argument)
                if type(newcrib) != str:
                    print('The crib must be a string!')
                elif len(newcrib) > keylen:
                    print('The crib {} is longer than the key! The maximum allowed length is {}.'.format(newcrib, keylen))
                else:
                    # set crib
                    crib = newcrib
                    cribindex = 0
                    update_and_print()

            except (TypeError, ValueError, SyntaxError):
                print('Couldn\'t parse the crib!')
                print('The command should be called like this:')
                print('  crib \"as\\\"df\\x10\\n jkl\"')

        elif (choice == 'n' or choice == 'next'):
            if crib == '':
                print('You need to set a crib.')
            elif cribindex == (len(ciphertext) - len(crib)):
                print('Can\'t increase the index or the crib won\'t fit.')
            else:
                cribindex += 1
                update_and_print()

        elif (choice == 'p' or choice == 'prev'):
            if crib == '':
                print('You need to set a crib.')
            elif cribindex == 0:
                print('Can\'t set the index at less than 0.')
            else:
                cribindex -= 1
                update_and_print()

        elif (choice == 'j' or choice == 'jump'):
            if crib == '':
                print('You need to set a crib.')
            else:
                try:
                    newindex = int(argument)
                    if newindex < 0:
                        print('The index must be a positive number.')
                    elif newindex > (len(ciphertext) - len(crib)):
                        print('That index is too big, the crib won\'t fit.')
                        print('The maximum acceptable index is {}.'.format(len(ciphertext) - len(crib)))
                    else:
                        cribindex = newindex
                        update_and_print()

                except ValueError:
                    'Error: {} is not a valid number'
            
        elif (choice == 'o' or choice == 'ok'):
            # update global key
            cribkey = getkey(ciphertext, keylen, crib, cribindex, keyfunc)
            newkey = []
            for i in range(keylen):
                if cribkey[i] != None:
                    newkey.append(cribkey[i])
                elif key[i] != None:
                    newkey.append(key[i])
                else:
                    newkey.append(None)
            key = newkey[:]

            # reset crib
            crib = ''
            cribindex = 0
            print('Key updated: {}'.format(key))
            print('Crib reset.')

        elif (choice == 'k' or choice == 'key'):
            # remove spaces from sides
            argument = argument.strip()
            try:
                newkey = ast.literal_eval(argument)
                if type(newkey) != list:
                    print('The argument must be passed as a list!')
                    print('The command should be called like this:')
                    print('  key [\'a\', \'\\x01\', None, \'\\n\']')
                elif len(newkey) != keylen:
                    print('The key must be {} characters long!'.format(keylen))
                else:
                    print('Key updated.')
                    key = newkey[:]
                    update_and_print()

            except (TypeError, ValueError, SyntaxError):
                print('Couldn\'t parse the key!')
                print('The command should be called like this:')
                print('  key [\'a\', \'\\x01\', None, \'\\n\']')

        elif (choice == 's' or choice == 'show'):
            print(decrypt(ciphertext, key, decfunc))

        elif (choice == 'r' or choice == 'reset'):
            crib = ''
            cribindex = 0
            key = [None] * keylen
            print('Crib and key have been reset.')

        else:
            print('Command "{}" not recognized.'.format(choice))
            print('Enter "h" or "help" for a list of available commands.')

        # prompt
        choice, argument = prompt(choice, argument)

    return key


def keyinplaintext(ciphertext, keylen, keyindex, seed, seedindex, decfunc=xor_str, keyfunc=None):
    '''Solves the case when the key used to encrypt is embedded in the plaintext itself.

    This function assumes a polyalphabetic substition cipher is used.

    Arguments:
        ciphertext -- the ciphertext as a string
        keylen     -- the key length
        keyindex   -- the position of the key in the plaintext
        seed       -- a single known character in the plaintext
        seedindex  -- the position of the seed in the plaintext
        decfunc    -- a function that takes a character of ciphertext and a character of key and returns a character of plaintext (default: xor)
        keyfunc    -- a function that takes a character of ciphertext and a character of plaintext and returns a character of key (default: same as decfunc)

    Returns the  key.
    '''

    if keyindex % keylen == 0:
        raise ValueError("The key in the plaintext is in the same position as the key used when encrypting. Impossible to solve")

    # initial parameters
    if keyfunc is None:
        keyfunc = decfunc
    key = [None] * keylen
    key[seedindex % keylen] = keyfunc(ciphertext[seedindex], seed)

    # iterate to find all the characters in the key
    for _ in range(keylen):
        newkey = key[:]
        for i in range(len(key)):
            if key[i] is not None:
                newkey[(i + keyindex) % keylen] = decfunc(ciphertext[keyindex + i], key[i])
        key = newkey[:]

    assert not None in key

    return ''.join(key)
