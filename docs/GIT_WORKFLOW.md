# Git 브랜치 작업 이력

이 프로젝트는 기능을 별도 브랜치에서 작업한 뒤 `main` 브랜치로 병합하는 방식으로 관리합니다.

## 기존 즐겨찾기 기능 작업

```powershell
git checkout -b feature/favorite-feedback
# 즐겨찾기 상태 안내 기능 구현 및 커밋
git checkout main
git merge --no-ff feature/favorite-feedback
```

## 제출 증빙 브랜치 작업

```powershell
git checkout -b docs/git-workflow-evidence
# 이 문서 작성 및 커밋
git checkout main
git merge --no-ff docs/git-workflow-evidence
```

## 확인 명령

```powershell
# 브랜치와 병합 그래프 확인
git log --oneline --graph --all --decorate

# checkout 및 merge 명령 이력 확인
git reflog --date=local
```

`git log`는 커밋 그래프를, `git reflog`는 `checkout`과 `merge` 같은 로컬 HEAD 이동 이력을 보여준다.
