import strings


class TestStrings(object):
    def test_lower(self):
        s = "HELLO"
        expected = s.lower()
        assert strings.lower(s) == expected

    def test_upper(self):
        s = "hello"
        expected = s.upper()
        assert strings.upper(s) == expected

    def test_title(self):
        s = "lord of the rings"
        expected = s.title()
        assert strings.title(s) == expected

    def test_length(self):
        s = "This is a test."
        expected = len(s)
        assert strings.length(s) == expected
