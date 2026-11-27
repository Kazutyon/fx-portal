import unittest

import style_measure as sm


class StyleMeasureTests(unittest.TestCase):
    def test_counts_chars_numbers_and_politeness(self):
        m = sm.measure("ドル円は159.21円で終わりました。株は3.3％上昇した。")
        self.assertEqual(m["chars"], 30)
        self.assertEqual(m["polite_pct"], 50)
        self.assertEqual(m["numbers_per_100"], round(100 * 2 / 30, 1))  # 159.21 and 3.3 are one number each

    def test_empty_text_does_not_divide_by_zero(self):
        self.assertEqual(sm.measure("")["chars"], 0)

    def test_the_note_line_holds_numbers_only(self):
        mine, ref = sm.measure("ドル円は159円です。"), sm.measure("円買いが進みました。")
        line = sm.note_line(mine, ref)
        self.assertIn("字数 ", line)
        self.assertNotIn("ドル円", line)  # no report text is ever printed
        self.assertNotIn("円買い", line)


if __name__ == "__main__":
    unittest.main()
