"""Tests for the prompt manager's in-memory data helpers."""

import unittest

from prompt_manager import create_default_prompts, find_prompt, get_categories


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


if __name__ == "__main__":
    unittest.main()
