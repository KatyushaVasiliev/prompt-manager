# 제출 안내

## GitHub 저장소 URL

https://github.com/KatyushaVasiliev/prompt-manager

## 개발 환경 설정 스크린샷

1. VS Code에서 `prompt-manager` 폴더를 연다.
2. 내장 터미널에서 아래 명령을 실행한다.

   ```powershell
   python -V
   py -3 -V
   git --version
   git config --global --list
   ```

3. VS Code 탐색기, 편집 중인 `prompt_manager.py`, 터미널 출력이 함께 보이도록 캡처한다.

`python -V`가 인식되지 않는 Windows 환경에서는 `py -3 -V` 출력도 함께 캡처한다.

## Git clone 실행 증빙

새 폴더 또는 다른 컴퓨터에서 다음 명령을 실행해 복제 화면을 캡처한다.

```powershell
git clone https://github.com/KatyushaVasiliev/prompt-manager.git
cd prompt-manager
```

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
git log --oneline --graph --all --decorate
```

`feature/favorite-feedback` 브랜치가 `main`에 병합된 그래프와 기능 단위 커밋 10개 이상이 보이도록 캡처한다.

실제 실행 결과 예시는 [실행 증빙](COMMAND_EVIDENCE.md)에 기록되어 있다.

`checkout`과 `merge` 명령 이력도 별도로 보이게 하려면 다음 명령 결과를 추가 캡처한다.

```powershell
git reflog --date=local
```

## 최종 확인 명령

```powershell
py -3 -m unittest discover -s tests
git status
```

테스트가 `OK`로 끝나고 작업 트리가 깨끗하면 제출 준비가 완료된 것이다.
