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

def xor_str(s1, s2):
    '''XOR between two strings. The longer one is truncated.'''
    return ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(s1, s2))

def cbc_paddingoracle(ciphertext, oraclefunc, blocklen=16, verbose=False):
    '''An implementation of the padding oracle attack against AES CBC.

    NB: The algorithm assumes PKCS#7 padding.

    Arguments:
        ciphertext -- the complete ciphertext, IV included
        oraclefunc -- an oracle padding function. The function must take a ciphertext as a string and return True if the padding is correct, False otherwise
        blocklen   -- the AES block length (default: 16)
        verbose    -- print debug information if True (default: False)

    Returns the decrypted plaintext.
    '''

    if len(ciphertext) % blocklen != 0:
        raise ValueError('The length of the ciphertext is not a multiple of the block length!')

    if len(ciphertext) < blocklen * 2:
        raise ValueError('The ciphertext is too short! (it must at least contain the IV block and another block)')

    plaintext = ''

    # continue until we decrypted all useful blocks
    while len(ciphertext) >= blocklen * 2:

        # decrypted last block
        plainblock = ''

        for i in xrange(blocklen):
            found = False
            for guess in xrange(256):
                if guess != i:
                    # take next to last block
                    newblock = ciphertext[(-2 * blocklen):-blocklen]
                    # try to null out the decrypted last block
                    newblock = xor_str(newblock, (chr(guess) + plainblock).rjust(blocklen))
                    # the result should be padded correctly
                    newblock = xor_str(newblock, (chr(i) * i).rjust(blocklen))
                    # if the padding is correct
                    if oraclefunc(ciphertext[:(-2 * blocklen)] + newblock + ciphertext[-blocklen]):
                        # the plaintext is guess
                        plainblock = chr(guess) + plainblock
                        found = True
                        break
            # if none of the guesses were ok
            if not found:
                # the plaintext is i
                plainblock = chr(i) + plainblock

            if verbose:
                print 'Block {}, index {}'.format(len(plaintext)/blocklen, i)
                print plainblock

        # update plaintext
        plaintext = plainblock + plaintext

        if verbose:
            print 'Result so far:'
            print plaintext

        # remove last block and repeat
        ciphertext = ciphertext[:-blocklen]

    return plaintext

def ecb_chosenprefix(encfunc, prefixindex=0, blocklen=16, verbose=False):
    '''An implementation of the chosen prefix attack against AES ECB.

    This attack assumes that the attacker can insert an arbitrary string in the plaintext, and has access to an oracle encryption function which can provide the corresponding ciphertext.
    NB: the attack can only decrypt the plaintext that follows the prefix.

    Arguments:
        encfunc     -- an encryption oracle function. It must take as argument the prefix (as a string), and return the ciphertext corresponding to the plaintext with the prefix inserted
        prefixindex -- position where the prefix will be inserted in the ciphertext (default: 0)
        blocklen    -- the AES block length (default: 16)
        verbose     -- print debug information if True (default: False)

    Returns the decrypted plaintext (the part after prefixindex).
    '''

    # initial values
    PAD = 'A'
    plaintext = ''
    ciphertext = encfunc('')

    if prefixindex >= len(ciphertext):
        return ''

    prefixblock = prefixindex / blocklen
    indexinblock = prefixindex % blocklen

    # Part 1: block where the prefix starts

    # for each character in the prefix block after prefixindex
    for i in xrange(blocklen - indexinblock):

        # get ciphertext block containing a prefix we know and the next missing character
        prefix = PAD * (blocklen - indexinblock - 1 - i)
        newciphertext = encfunc(prefix)
        newblock = newciphertext[(prefixblock * blocklen):((prefixblock + 1) * blocklen)]

        # try to guess the missing character
        for guess in xrange(256):
            prefix = PAD * (blocklen - indexinblock - 1 - i) + plaintext + chr(guess)
            guessciphertext = encfunc(prefix)
            guessblock = guessciphertext[(prefixblock * blocklen):((prefixblock + 1) * blocklen)]
            if guessblock == newblock:
                plaintext += chr(guess)
                break

        # check if the plaintext has grown accordingly 
        if (len(plaintext) - 1) != i:
            # if it didn't we probably hit the padding at the end and we should stop
            if prefixblock == len(ciphertext) / blocklen - 1 and plaintext[-1] == '\x01':
                if verbose:
                    print 'Padding hit, we\'re done.'
                plaintext = plaintext[:-1]
                break
            else:
                raise AssertionError('Something went wrong.')

        if verbose:
            print 'Block {}, index {}'.format(prefixblock, indexinblock + i)
            print plaintext

    # Part 2: following blocks

    # for each block after the prefixblock
    for blockindex in xrange(prefixblock + 1, len(ciphertext) / blocklen):

        # for each character in the block
        for i in xrange(blocklen):

            # get ciphertext block containing a prefix we know and the next missing character
            prefix = PAD * (blocklen - 1 - i)
            newciphertext = encfunc(prefix)
            newblock = newciphertext[(blockindex * blocklen):((blockindex + 1) * blocklen)]

            # try to guess the missing character
            for guess in xrange(256):
                prefix = PAD * (blocklen - 1 - i) + plaintext + chr(guess)
                guessciphertext = encfunc(prefix)
                guessblock = guessciphertext[(blockindex * blocklen):((blockindex + 1) * blocklen)]
                if guessblock == newblock:
                    plaintext += chr(guess)
                    break

            # check if the plaintext has grown accordingly 
            if (len(plaintext) + prefixindex - 1) % blocklen != i:
                # if it didn't we probably hit the padding at the end and we should stop
                if blockindex == len(ciphertext) / blocklen - 1 and plaintext[-1] == '\x01':
                    if verbose:
                        print 'Padding hit, we\'re done.'
                    plaintext = plaintext[:-1]
                    break
                else:
                    raise AssertionError('Something went wrong.')

            if verbose:
                print 'Block {}, index {}'.format(blockindex, i)
                print plaintext

    return plaintext