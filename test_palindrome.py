import palindrome


def test_basic():
    """ Basic test for palindrome """
    # True positives
    for test in ('Wow', 'stats', 'madam', 'refer', '1'):
        assert palindrome.is_palindrome(test) == True
    # True negatives
    for test in ('neuron', 'fox', 'Amygdala'):
        assert palindrome.is_palindrome(test) == False


# after writing this part of the code, I installed the Pytest package and typed 'pytest test_palindrome.py' in terminal

def test_with_spaces():
    """ Testing palindrome strings with extra spaces """
    # True positives
    for test in ('No lemon no melon',
                 'Madam Im Adam',
                 'red rum sir is murder',
                 'Taco cat'):
        assert palindrome.is_palindrome(test) == True
    # True negatives
    for test in ('Believe it or not',
                 'Wonderful life',
                 'Wild animals in a cave'):
        assert palindrome.is_palindrome(test) == False


# after writing this part of the code, I typed 'pytest test_palindrome.py' in terminal
# and received 1 error: FAILED test_palindrome.py::test_with_spaces - AssertionError: assert False == True
# after this I decided to extend my is_palindrome function in palindrome.py

def test_with_punctuations():
    """ Testing palindrome strings with extra punctuations """
    # True positives
    for test in ("Don't nod.",
                 'I did, did I?',
                 'Was it a cat I saw?',
                 'Eva, can I see bees in a cave?',
                 'Top spot!'):
        assert palindrome.is_palindrome(test) == True
    # True negatives
    for test in ('Robin is a bird',
                 'Wonderful time',
                 'Are these palindromes?'):
        assert palindrome.is_palindrome(test) == False


# after writing this part of the code I repeat steps described above (pytest, function extension, pytest)

if __name__ == '__main__':
    print('PyCharm')
