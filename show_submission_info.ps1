# 제출 화면을 캡처하기 전에 개발 환경과 Git 이력을 한 번에 확인합니다.

Write-Host "=== 개발 환경 ==="
py -3 --version
git --version
git config --global --list

Write-Host "`n=== Git 로그 ==="
git log --oneline --graph --all

Write-Host "`n프로그램 실행: py -3 prompt_manager.py"
