"""리스트와 딕셔너리로 만든 터미널 프롬포트 관리 프로그램."""

from typing import Dict, List, Optional

CATEGORIES = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]
Prompt = Dict[str, object]


def create_default_prompts() -> List[Prompt]:
    """이전 미션의 예시 프롬포트 3개를 리스트에 담아 반환한다."""
    return [
        {"id": 1, "title": "블로그 글 작성", "content": "당신은 전문 블로거입니다. 주어진 주제를 친절한 블로그 글로 작성해 주세요.", "category": "텍스트 생성", "favorite": False},
        {"id": 2, "title": "이미지 프롬프트 만들기", "content": "당신은 이미지 프롬프트 전문가입니다. 주제에 맞는 상세한 이미지 생성 프롬프트를 작성해 주세요.", "category": "이미지 생성", "favorite": False},
        {"id": 3, "title": "학습 코치 페르소나", "content": "당신은 친절한 학습 코치입니다. 목표와 기간을 바탕으로 주간 학습 계획을 제안해 주세요.", "category": "페르소나", "favorite": False},
    ]


def input_required(label: str) -> str:
    """빈 값이면 다시 입력받는다."""
    while True:
        value = input(label).strip()
        if value:
            return value
        print("입력값이 비어 있습니다. 다시 입력해 주세요.")


def get_categories(prompts: List[Prompt]) -> List[str]:
    """기본 카테고리와 사용자가 직접 입력한 카테고리를 함께 반환한다."""
    categories = list(CATEGORIES)
    for prompt in prompts:
        category = str(prompt["category"])
        if category not in categories:
            categories.append(category)
    return categories


def choose_category(prompts: List[Prompt]) -> str:
    """번호 선택 또는 직접 입력으로 카테고리를 받는다."""
    categories = get_categories(prompts)
    print("\n카테고리 목록")
    for index, category in enumerate(categories, start=1):
        print(f"{index}. {category}")
    print("0. 직접 입력")
    while True:
        choice = input("카테고리 번호: ").strip()
        if choice == "0":
            return input_required("직접 입력할 카테고리: ")
        if choice.isdigit() and 1 <= int(choice) <= len(categories):
            return categories[int(choice) - 1]
        print("올바른 카테고리 번호를 입력해 주세요.")


def find_prompt(prompts: List[Prompt], prompt_id: int) -> Optional[Prompt]:
    """번호에 해당하는 딕셔너리를 찾는다."""
    return next((prompt for prompt in prompts if prompt["id"] == prompt_id), None)


def read_prompt_id() -> Optional[int]:
    """프롬포트 번호를 안전하게 입력받는다."""
    try:
        return int(input("프롬포트 번호: ").strip())
    except ValueError:
        print("번호는 정수로 입력해 주세요.")
        return None


def print_prompt_summary(prompt: Prompt) -> None:
    """제목·카테고리·즐겨찾기 여부를 한 줄로 출력한다."""
    favorite = "★ 즐겨찾기" if prompt["favorite"] else "☆ 일반"
    print(f"[{prompt['id']}] {prompt['title']} | {prompt['category']} | {favorite}")


def show_list(prompts: List[Prompt], heading: str = "프롬포트 목록") -> None:
    """프롬포트 목록 또는 빈 목록 안내를 출력한다."""
    print(f"\n--- {heading} ---")
    if not prompts:
        print("표시할 프롬포트가 없습니다.")
        return
    for prompt in prompts:
        print_prompt_summary(prompt)


def add_prompt(prompts: List[Prompt]) -> None:
    """제목, 내용, 카테고리를 받아 새 딕셔너리를 리스트에 추가한다."""
    print("\n--- 프롬포트 추가 ---")
    title = input_required("제목: ")
    content = input_required("내용: ")
    category = choose_category(prompts)
    next_id = max((int(prompt["id"]) for prompt in prompts), default=0) + 1
    prompts.append({"id": next_id, "title": title, "content": content, "category": category, "favorite": False})
    print(f"'{title}' 프롬포트가 추가되었습니다.")


def show_by_category(prompts: List[Prompt]) -> None:
    """선택한 카테고리의 프롬포트만 출력한다."""
    category = choose_category(prompts)
    matches = [prompt for prompt in prompts if str(prompt["category"]).casefold() == category.casefold()]
    show_list(matches, f"'{category}' 카테고리")


def search_prompts(prompts: List[Prompt]) -> None:
    """제목 또는 내용에 키워드가 있는 프롬포트를 검색한다."""
    keyword = input_required("검색어: ").casefold()
    matches = [prompt for prompt in prompts if keyword in str(prompt["title"]).casefold() or keyword in str(prompt["content"]).casefold()]
    show_list(matches, f"'{keyword}' 검색 결과")


def show_detail(prompts: List[Prompt]) -> None:
    """번호로 선택한 프롬포트의 전체 정보를 출력한다."""
    prompt_id = read_prompt_id()
    prompt = find_prompt(prompts, prompt_id) if prompt_id is not None else None
    if prompt is None:
        print("해당 번호의 프롬포트를 찾을 수 없습니다.")
        return
    print("\n--- 프롬포트 상세 ---")
    print(f"번호: {prompt['id']}\n제목: {prompt['title']}\n카테고리: {prompt['category']}")
    print(f"즐겨찾기: {'예' if prompt['favorite'] else '아니오'}\n내용: {prompt['content']}")


def toggle_favorite(prompts: List[Prompt]) -> None:
    """번호로 선택한 프롬포트의 즐겨찾기를 등록 또는 해제한다."""
    prompt_id = read_prompt_id()
    prompt = find_prompt(prompts, prompt_id) if prompt_id is not None else None
    if prompt is None:
        print("해당 번호의 프롬포트를 찾을 수 없습니다.")
        return
    prompt["favorite"] = not bool(prompt["favorite"])
    state = "등록" if prompt["favorite"] else "해제"
    print(f"'{prompt['title']}' 즐겨찾기가 {state}되었습니다.")


def show_menu() -> None:
    """메인 메뉴를 출력한다."""
    print("\n========== 프롬포트 관리 프로그램 ==========")
    print("1. 프롬포트 추가\n2. 전체 목록 보기\n3. 카테고리별 조회\n4. 검색")
    print("5. 상세 보기\n6. 즐겨찾기 등록/해제\n7. 즐겨찾기 목록\n0. 종료")


def run() -> None:
    """기능 실행 뒤 항상 메뉴로 돌아오는 메인 반복문이다."""
    prompts = create_default_prompts()
    actions = {
        "1": lambda: add_prompt(prompts), "2": lambda: show_list(prompts),
        "3": lambda: show_by_category(prompts), "4": lambda: search_prompts(prompts),
        "5": lambda: show_detail(prompts), "6": lambda: toggle_favorite(prompts),
        "7": lambda: show_list([prompt for prompt in prompts if prompt["favorite"]], "즐겨찾기 목록"),
    }
    print("프롬포트 관리 프로그램을 시작합니다.")
    while True:
        show_menu()
        choice = input("메뉴 번호: ").strip()
        if choice == "0":
            print("프로그램을 종료합니다. 이번 실행에서 추가한 데이터는 초기화됩니다.")
            return
        action = actions.get(choice)
        if action is None:
            print("잘못된 메뉴 번호입니다. 다시 선택해 주세요.")
        else:
            action()


if __name__ == "__main__":
    run()
