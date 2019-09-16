import unittest
from src.scanner import Scanner


class ScannerTestCases(unittest.TestCase):

    def test_peek_past_whitespace(self):
        '''Find literal past whitespace.'''
        s = Scanner('     += ')
        self.assertTrue(s.peek().is_plus(), 'whitespace before ...')

    def test_literal_tokens_with_whitespace(self):
        '''Find two literals inside whitespace.'''
        s = Scanner('     += ')
        self.assertTrue(s.next_token().is_plus())
        self.assertTrue(s.next_token().is_equals())
        self.assertTrue(s.next_token().is_eof())

    def test_word_past_whitespace(self):
        '''Find word past whitespace.'''
        s = Scanner('   heLlo ')
        self.assertTrue(s.peek().is_word(), 'peek past whitespace')

        next_token = s.next_token()
        self.assertTrue(next_token.is_word(), 'right token type')
        self.assertEqual(next_token.value(), 'heLlo', 'right token value')

        self.assertTrue(s.next_token().is_eof(), 'EOF after word')

    def test_keyword_past_whitespace(self):
        '''Find word past whitespace.'''
        s = Scanner('   if ')
        self.assertTrue(s.peek().is_if(), 'peek past whitespace')

        next_token = s.next_token()
        self.assertTrue(next_token.is_if(), 'right token type')
        self.assertEqual(next_token.value(), 'if', 'right token value')

        self.assertTrue(s.next_token().is_eof(), 'EOF after word')

    def test_word_within_iterals(self):
        '''Find word within two literals.'''
        s = Scanner('+hello=')
        self.assertTrue(s.next_token().is_plus())
        self.assertTrue(s.next_token().is_word())
        self.assertTrue(s.next_token().is_equals())

    def test_two_words(self):
        '''Find two words.'''
        s = Scanner(' tyler rahe')
        next_token = s.next_token()
        self.assertTrue(next_token.is_word(), 'first token right')
        self.assertEqual(next_token.value(), 'tyler')
        next_token = s.next_token()
        self.assertTrue(next_token.is_word(), 'second token right')
        self.assertEqual(next_token.value(), 'rahe')

    def test_word_with_number(self):
        '''Find word and number.'''
        s = Scanner(' tyler12')
        next_token = s.next_token()
        self.assertTrue(next_token.is_word(), 'first token right')
        self.assertEqual(next_token.value(), 'tyler')
        next_token = s.next_token()
        self.assertTrue(next_token.is_number(), 'second token right')
        self.assertEqual(next_token.value(), 12)

    def test_one_number(self):
        '''Find number.'''
        s = Scanner('42')
        next_token = s.next_token()
        self.assertTrue(next_token.is_number(), 'found right token')
        self.assertEqual(next_token.value(), 42)

    def test_two_numbers(self):
        '''Find two numbers in whitespace.'''
        s = Scanner(' 3540  \n\t    4550      ')
        next_token = s.next_token()
        self.assertTrue(next_token.is_number(), 'found right token')
        self.assertEqual(next_token.value(), 3540)
        next_token = s.next_token()
        self.assertTrue(next_token.is_number(), 'found right token')
        self.assertEqual(next_token.value(), 4550)

    def test_assignment(self):
        '''Recognize tokens in an assignment statement.'''
        s = Scanner(' klien=3\n')
        next_token = s.next_token()
        self.assertTrue(next_token.is_word(), 'first token right')
        self.assertEqual(next_token.value(), 'klien')
        self.assertTrue(s.next_token().is_equals())
        next_token = s.next_token()
        self.assertTrue(next_token.is_number(), 'found right token')
        self.assertEqual(next_token.value(), 3)

    def test_addition_spec(self):
        '''Recognize tokens in a addition specification.'''
        s = Scanner(' 1+100\t')
        next_token = s.next_token()
        self.assertTrue(next_token.is_number(), 'found right token')
        self.assertEqual(next_token.value(), 1)
        self.assertTrue(s.next_token().is_plus())
        next_token = s.next_token()
        self.assertTrue(next_token.is_number(), 'found right token')
        self.assertEqual(next_token.value(), 100)

    def test_lessthan_spec(self):
        '''Recognize tokens in a less than specification.'''
        s = Scanner(' 1<100\t')
        next_token = s.next_token()
        self.assertTrue(next_token.is_number(), 'found right token')
        self.assertEqual(next_token.value(), 1)
        self.assertTrue(s.next_token().is_lessthan())
        next_token = s.next_token()
        self.assertTrue(next_token.is_number(), 'found right token')
        self.assertEqual(next_token.value(), 100)

    def test_perens(self):
        '''Find two perens inside whitespace.'''
        s = Scanner('     (=) ')
        self.assertTrue(s.next_token().is_leftperen())
        self.assertTrue(s.next_token().is_equals())
        self.assertTrue(s.next_token().is_rightperen())
        self.assertTrue(s.next_token().is_eof())