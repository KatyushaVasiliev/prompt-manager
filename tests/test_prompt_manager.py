"""리스트·딕셔너리 기반 프롬포트 관리 기능 테스트."""

import unittest
from contextlib import redirect_stdout
from io import StringIO
from unittest.mock import patch

from prompt_manager import CATEGORIES, add_prompt, create_default_prompts, find_prompt, get_categories, show_detail, show_list


class PromptManagerTests(unittest.TestCase):
    def test_default_data_is_a_list_of_dictionaries(self):
        prompts = create_default_prompts()
        self.assertGreaterEqual(len(prompts), 3)
        self.assertIsInstance(prompts[0], dict)
        self.assertTrue({"title", "content", "category", "favorite"}.issubset(prompts[0]))

    def test_default_prompts_use_required_categories(self):
        self.assertTrue(all(prompt["category"] in CATEGORIES for prompt in create_default_prompts()))

    def test_find_prompt_returns_dictionary(self):
        prompt = find_prompt(create_default_prompts(), 2)
        self.assertEqual("이미지 프롬프트 만들기", prompt["title"])

    def test_categories_include_predefined_values(self):
        self.assertEqual(CATEGORIES, get_categories(create_default_prompts())[:len(CATEGORIES)])

    def test_list_output_includes_favorite_state(self):
        output = StringIO()
        prompt = {"id": 9, "title": "테스트", "content": "내용", "category": "기타", "favorite": True}
        with redirect_stdout(output):
            show_list([prompt])
        self.assertIn("★ 즐겨찾기", output.getvalue())

    def test_detail_output_contains_full_content(self):
        output = StringIO()
        with patch("builtins.input", return_value="1"), redirect_stdout(output):
            show_detail(create_default_prompts())
        self.assertIn("친절한 블로그 글", output.getvalue())

    def test_added_prompt_defaults_to_not_favorite(self):
        prompts = create_default_prompts()
        with patch("builtins.input", side_effect=["새 프롬포트", "새 내용", "1"]):
            add_prompt(prompts)
        self.assertFalse(prompts[-1]["favorite"])


if __name__ == "__main__":
    unittest.main()
