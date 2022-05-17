import unittest
from DevProgLang import lex

KEYWORD = 'KEYWORD'
INT = 'INT'
ID = 'ID_VAR'
token_exprs = [
    (r'[ \t\n]+', None),
    (r'#[^\n]*', None),
    (r'keyword', KEYWORD),
    (r'[0-9]+', INT),
    (r'[A-Za-z][A-Za-z0-9_]*', ID)
]

class TestLexer(unittest.TestCase):
    def lexer_test(self, code, expected):
        #print('code:', code, 'expected:', expected)
        actual = lex(code)
        self.assertEqual(expected, actual)

    def test_empty(self):
        self.lexer_test('', [])

    def test_id(self):
        self.lexer_test('abc', [('abc', ID)])

    def test_keyword_first(self):
        self.lexer_test('keyword', [('keyword', ID)])

    def test_space(self):
        self.lexer_test(' ', [])

    def test_id_space(self):
        self.lexer_test('abc def', [('abc', ID), ('def', ID)])


if __name__ == '__main__':
    test_names = ['test_lexer', 'test_combinators', 'test_imp_parser', 'test_eval']
    suite = unittest.defaultTestLoader.loadTestsFromNames(test_names)
    result = unittest.TextTestRunner().run(suite)