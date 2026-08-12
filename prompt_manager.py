"""Terminal based prompt manager."""

from dataclasses import dataclass
from typing import Iterable, List, Optional


@dataclass
class Prompt:
    """A saved reusable prompt."""

    id: int
    title: str
    category: str
    content: str
    favorite: bool = False


def create_default_prompts() -> List[Prompt]:
    """Return starter prompts from the previous prompt-writing mission."""
    return [
        Prompt(1, "학습 계획 만들기", "교육", "당신은 학습 코치입니다. 목표와 기간을 바탕으로 주간 학습 계획을 만들어 주세요."),
        Prompt(2, "회의록 요약", "업무", "당신은 업무 비서입니다. 다음 회의록을 핵심 결정 사항, 할 일, 담당자로 나누어 요약해 주세요."),
        Prompt(3, "여행 일정 추천", "여행", "당신은 여행 플래너입니다. 예산과 선호를 고려해 하루 단위 여행 일정을 제안해 주세요."),
    ]


def input_required(label: str) -> str:
    """Read a non-empty value from the user."""
    while True:
        value = input(label).strip()
        if value:
            return value
        print("비어 있을 수 없습니다. 다시 입력해 주세요.")


def find_prompt(prompts: Iterable[Prompt], prompt_id: int) -> Optional[Prompt]:
    """Find a prompt by its id."""
    return next((prompt for prompt in prompts if prompt.id == prompt_id), None)


def get_categories(prompts: Iterable[Prompt]) -> List[str]:
    """Return unique categories in their first-seen order."""
    return list(dict.fromkeys(prompt.category for prompt in prompts))


def print_prompt_summary(prompt: Prompt) -> None:
    """Print one prompt in list format."""
    mark = "★" if prompt.favorite else " "
    print(f"[{prompt.id}] {mark} {prompt.title} | {prompt.category}")


def show_prompts(prompts: List[Prompt], heading: str = "프롬포트 목록") -> None:
    """Show a list, including a friendly empty state."""
    print(f"\n--- {heading} ---")
    if not prompts:
        print("표시할 프롬포트가 없습니다.")
        return
    for prompt in prompts:
        print_prompt_summary(prompt)


def add_prompt(prompts: List[Prompt]) -> None:
    """Add a new prompt for the current program session."""
    print("\n--- 프롬포트 추가 ---")
    title = input_required("제목: ")
    category = input_required("카테고리: ")
    content = input_required("내용: ")
    next_id = max((prompt.id for prompt in prompts), default=0) + 1
    prompts.append(Prompt(next_id, title, category, content))
    print(f"'{title}' 프롬포트가 추가되었습니다.")


def show_by_category(prompts: List[Prompt]) -> None:
    """Show prompts that belong to a category."""
    print("사용 가능한 카테고리: " + ", ".join(get_categories(prompts)))
    category = input_required("조회할 카테고리: ")
    matches = [prompt for prompt in prompts if prompt.category.casefold() == category.casefold()]
    show_prompts(matches, f"'{category}' 카테고리")


def search_prompts(prompts: List[Prompt]) -> None:
    """Search titles, categories, and contents by a keyword."""
    keyword = input_required("검색어: ").casefold()
    matches = [
        prompt for prompt in prompts
        if keyword in prompt.title.casefold()
        or keyword in prompt.category.casefold()
        or keyword in prompt.content.casefold()
    ]
    show_prompts(matches, f"'{keyword}' 검색 결과")


def show_detail(prompts: List[Prompt]) -> None:
    """Show all fields for one prompt."""
    prompt_id = read_prompt_id()
    if prompt_id is None:
        return
    prompt = find_prompt(prompts, prompt_id)
    if prompt is None:
        print("해당 번호의 프롬포트를 찾을 수 없습니다.")
        return
    print("\n--- 프롬포트 상세 ---")
    print(f"번호: {prompt.id}\n제목: {prompt.title}\n카테고리: {prompt.category}")
    print(f"즐겨찾기: {'예' if prompt.favorite else '아니오'}\n내용: {prompt.content}")


def read_prompt_id() -> Optional[int]:
    """Safely read an integer prompt id."""
    try:
        return int(input("프롬포트 번호: ").strip())
    except ValueError:
        print("번호는 정수로 입력해 주세요.")
        return None


def toggle_favorite(prompts: List[Prompt]) -> None:
    """Toggle favorite state for a prompt."""
    prompt_id = read_prompt_id()
    if prompt_id is None:
        return
    prompt = find_prompt(prompts, prompt_id)
    if prompt is None:
        print("해당 번호의 프롬포트를 찾을 수 없습니다.")
        return
    prompt.favorite = not prompt.favorite
    state = "등록" if prompt.favorite else "해제"
    print(f"'{prompt.title}' 즐겨찾기가 {state}되었습니다.")


def show_menu() -> None:
    """Print the main selection menu."""
    print("\n========== 프롬포트 관리 프로그램 ==========")
    print("1. 프롬포트 추가")
    print("2. 전체 목록 보기")
    print("3. 카테고리별 조회")
    print("4. 검색")
    print("5. 상세 보기")
    print("6. 즐겨찾기 등록/해제")
    print("7. 즐겨찾기 목록")
    print("0. 종료")


def run() -> None:
    """Run the interactive application until the user exits."""
    prompts = create_default_prompts()
    actions = {
        "1": lambda: add_prompt(prompts),
        "2": lambda: show_prompts(prompts),
        "3": lambda: show_by_category(prompts),
        "4": lambda: search_prompts(prompts),
        "5": lambda: show_detail(prompts),
        "6": lambda: toggle_favorite(prompts),
        "7": lambda: show_prompts([prompt for prompt in prompts if prompt.favorite], "즐겨찾기 목록"),
    }
    print("프롬포트 관리 프로그램을 시작합니다.")
    while True:
        show_menu()
        choice = input("메뉴 번호: ").strip()
        if choice == "0":
            print("프로그램을 종료합니다. 이번 실행에서 추가한 데이터는 초기화됩니다.")
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print("올바른 메뉴 번호를 입력해 주세요.")


if __name__ == "__main__":
    run()
