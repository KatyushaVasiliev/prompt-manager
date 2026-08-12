# 제출 안내

## GitHub 저장소 URL

https://github.com/KatyushaVasiliev/prompt-manager

## 개발 환경 설정 스크린샷

1. VS Code에서 `prompt-manager` 폴더를 연다.
2. 내장 터미널에서 아래 명령을 실행한다.

   ```powershell
   py -3 --version
   git --version
   git config --global --list
   ```

3. VS Code 탐색기, 편집 중인 `prompt_manager.py`, 터미널 출력이 함께 보이도록 캡처한다.

## 프로그램 실행 결과 스크린샷

내장 터미널에서 다음을 실행한다.

```powershell
py -3 prompt_manager.py
```

아래 입력 순서로 메뉴, 추가, 목록, 검색 결과를 한 번에 보여줄 수 있다.

```text
1
자기소개 작성
취업
당신은 커리어 코치입니다. 자기소개서를 작성해 주세요.
2
4
자기소개
6
4
7
0
```

입력 후 화면에는 새 프롬포트 추가 메시지, 전체 목록, 검색 결과, 즐겨찾기 목록이 표시된다. 메뉴가 보이는 상태와 결과가 보이는 상태를 각각 캡처한다.

## Git 로그 스크린샷

다음 명령을 실행한다.

```powershell
git log --oneline --graph --all
```

`feature/favorite-feedback` 브랜치가 `main`에 병합된 그래프와 기능 단위 커밋 10개 이상이 보이도록 캡처한다.

## 최종 확인 명령

```powershell
py -3 -m unittest discover -s tests
git status
```

테스트가 `OK`로 끝나고 작업 트리가 깨끗하면 제출 준비가 완료된 것이다.
