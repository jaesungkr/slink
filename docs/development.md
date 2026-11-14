# 개발 안내 / Development

## 실행 / Run

Windows에서 실행합니다. 릴리스 워크플로와 동일한 Python 3.12를 권장합니다. 아래 명령은 PowerShell용입니다.

Run on Windows. Python 3.12 matches the release workflow. These commands are for PowerShell.

```powershell
git clone https://github.com/jaesungkr/slink.git
cd slink
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe main.py
```

## 실행 파일 만들기 / Build an executable

```powershell
.\.venv\Scripts\python.exe -m pip install pyinstaller
.\.venv\Scripts\python.exe -m PyInstaller --onefile --windowed --name Slink --icon=slink.ico --add-data "slink.ico;." --add-data "slink.png;." --add-data "ui.html;." --hidden-import comtypes.stream --hidden-import comtypes.client --hidden-import pystray._win32 --hidden-import PIL.Image --hidden-import PIL.ImageDraw --hidden-import webview.platforms.edgechromium --hidden-import webview.platforms.winforms --hidden-import clr_loader --hidden-import clr --hidden-import pythonnet --hidden-import bottle --hidden-import slink.core --hidden-import slink.gui --hidden-import slink.win32 --hidden-import slink.tray --hidden-import slink.updater --hidden-import slink.resources --noconfirm main.py
```

결과 / Output: `dist/Slink.exe`

자동 빌드는 [`build.yml`](../.github/workflows/build.yml)에 정의되어 있습니다. `v*` 태그를 push하면 Windows에서 빌드하고 릴리스에 실행 파일을 올립니다. 일반 문서 커밋은 새 실행 파일을 배포하지 않습니다.

The [release workflow](../.github/workflows/build.yml) builds on Windows and uploads an executable when a `v*` tag is pushed. Documentation commits do not release a new executable.

## 확인 / Checks

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
.\.venv\Scripts\python.exe -m compileall -q main.py slink
```

문서 검사는 링크 경로와 기본 안내의 일관성을 확인합니다. Windows 실행·숨기기·복원·트레이·업데이트를 검증하는 테스트는 아닙니다. 배포 전 실제 Windows에서 해당 동작을 별도로 확인해야 합니다.

Documentation checks verify local links and essential guidance. They do not test Windows launch, hiding, restoration, tray behavior, or updates. Check these separately on Windows before a release.

소스 실행 상태에서 앱의 업데이트 기능을 사용하지 마세요. 현재 소스 업데이트는 `main.py`만 교체하므로 다중 파일 변경을 동기화하지 못합니다. 소스는 Git으로 업데이트하세요.

Do not use the in-app updater when running from source: its current source-mode path replaces only `main.py`, not the entire project. Update source through Git instead.
