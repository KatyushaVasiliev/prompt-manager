"""Tests for the prompt manager's in-memory data helpers."""

import unittest
from contextlib import redirect_stdout
from io import StringIO

from prompt_manager import Prompt, create_default_prompts, favorite_message, find_prompt, get_categories, show_prompts


class DefaultPromptTests(unittest.TestCase):
    def test_default_prompts_include_three_categories(self):
        prompts = create_default_prompts()
        self.assertGreaterEqual(len(prompts), 3)
        self.assertEqual({"교육", "업무", "여행"}, {prompt.category for prompt in prompts})

    def test_find_prompt_returns_matching_item(self):
        prompt = find_prompt(create_default_prompts(), 2)
        self.assertIsNotNone(prompt)
        self.assertEqual("회의록 요약", prompt.title)

    def test_categories_are_unique(self):
        self.assertEqual(["교육", "업무", "여행"], get_categories(create_default_prompts()))

    def test_favorite_message_reflects_state(self):
        prompt = Prompt(9, "테스트", "테스트", "내용", favorite=True)
        self.assertIn("등록", favorite_message(prompt))

    def test_list_output_marks_favorite(self):
        output = StringIO()
        with redirect_stdout(output):
            show_prompts([Prompt(9, "테스트", "테스트", "내용", favorite=True)])
        self.assertIn("★", output.getvalue())


if __name__ == "__main__":
    unittest.main()
