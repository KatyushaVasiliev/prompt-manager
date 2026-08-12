# 명령 실행 증빙

아래는 2026-08-12에 이 프로젝트에서 실제로 실행해 확인한 결과입니다. 제출 시에는 동일한 명령을 VS Code 터미널에서 다시 실행해 화면을 캡처합니다.

## GitHub 복제

실행 명령:

```powershell
git clone https://github.com/KatyushaVasiliev/prompt-manager.git C:\Users\kw067\prompt-manager-clone-verification
```

실행 결과:

```text
Cloning into 'C:\Users\kw067\prompt-manager-clone-verification'...
```

## 병합 그래프

실행 명령:

```powershell
git log --oneline --graph --all --decorate -20
```

실행 결과:

```text
*   6f64cd7 (HEAD -> main, origin/main) merge: enhance prompt data management
|\  
| * fa24304 (origin/feature/dictionary-prompt-data, feature/dictionary-prompt-data) feat: use dictionary prompts and predefined categories
|/  
*   3d2e966 merge: add Git workflow evidence
|\  
| * 42dd850 (origin/docs/git-workflow-evidence, docs/git-workflow-evidence) docs: add checkout and merge evidence guide
|/  
* ac788d3 docs: add assignment submission checklist
* 86714fc docs: add automated test command
* ac32f91 test: cover prompt detail display
* a1792ee test: verify favorite marker in list output
*   0ad9828 merge: integrate favorite feedback improvements
|\  
| * 79575eb (feature/favorite-feedback) docs: add favorite menu usage guidance
| * d53f585 feat: standardize favorite status feedback
|/  
* 7eb8774 feat: display available categories before filtering
* 0b1eae8 test: cover starter prompt data and lookup
* 0b29754 docs: explain session-only data behavior
* 2097571 feat: add console prompt manager foundation
```

## checkout 및 merge 기록

`git reflog --date=local`로 실제 HEAD 이동 기록도 확인할 수 있습니다. `checkout: moving from ...`과 `merge ...` 항목이 출력됩니다.
