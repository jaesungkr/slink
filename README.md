# Slink

Windows에서 잠시 보이지 않게 하고 싶은 앱 창을 숨기고, 필요할 때 다시 꺼내는 작은 도구입니다.

**한국어** · [English](README.en.md)

[**Windows용 Slink.exe 다운로드**](https://github.com/jaesungkr/slink/releases/latest/download/Slink.exe) · [다운로드 및 실행 안내](docs/download.md) · [릴리스 기록](https://github.com/jaesungkr/slink/releases)

별도 설치 과정 없이 실행합니다. Windows 10/11용이며 macOS와 Linux는 지원하지 않습니다.

## 무엇을 할 수 있나요?

- 선택한 앱의 창과 작업표시줄 버튼을 함께 숨기고 복원합니다.
- 숨긴 창이 다시 나타나면 백그라운드에서 다시 숨깁니다.
- 창 제목과 프로세스 이름으로 목록을 검색합니다.
- 다크/라이트 테마를 선택하고 설정을 저장합니다.
- 시스템 트레이에서 다시 열거나 종료할 수 있습니다.
- 앱에서 GitHub의 새 릴리스를 확인하고 실행 파일을 업데이트할 수 있습니다.

창만 숨길 뿐 앱을 종료하거나 프로세스를 숨기는 도구는 아닙니다. 같은 프로세스에 속한 다른 창도 함께 숨겨질 수 있습니다.

## 처음 사용하기

1. 위 링크에서 `Slink.exe`를 내려받아 실행합니다.
2. **Visible** 목록에서 숨길 창을 선택한 뒤 **Hide**를 누릅니다.
3. 다시 표시하려면 숨긴 창을 선택하고 **Show**를 누릅니다.
4. Slink의 **X** 버튼은 종료가 아니라 트레이로 숨기기입니다.
5. 완전히 종료하려면 트레이 아이콘 메뉴에서 **Quit**를 선택합니다. 정상 종료할 때 숨긴 창을 복원합니다.

실행이 안 되거나 숨긴 창을 찾기 어렵다면 [다운로드 안내의 문제 해결](docs/download.md#문제-해결)을 확인해 주세요.

## 알아둘 점

- 관리자 권한으로 실행 중인 앱은 Slink에도 같은 권한이 필요할 수 있습니다. 일반 앱에는 관리자 실행이 필요하지 않습니다.
- 일부 Microsoft Store 앱과 특수한 창은 정상적으로 제어되지 않을 수 있습니다.
- 강제 종료나 충돌 시 자동 복원은 보장하지 않습니다. 먼저 중요하지 않은 창으로 시험해 보세요.
- 설정은 `%APPDATA%\Slink\settings.json`에 저장합니다.
- 창 숨기기는 보안·개인정보 보호 기능이 아닙니다.

## 소스 실행 및 빌드

Windows와 Python 3.12를 기준으로 하는 [개발 안내](docs/development.md)에 실행, 빌드, 검증 방법을 정리했습니다. 실행 파일의 버전과 개발 중인 소스는 다를 수 있습니다.

| 파일 | 역할 |
| --- | --- |
| `main.py` | 실행 진입점과 단일 인스턴스 관리 |
| `ui.html` | HTML/CSS/JavaScript 인터페이스 |
| `slink/gui.py` | pywebview 창과 로컬 HTTP API |
| `slink/core.py`, `slink/win32.py` | 창 숨김·복원 및 Windows API |
| `slink/tray.py` | 시스템 트레이 |
| `slink/updater.py` | GitHub Releases 업데이트 |

## 문제 제보

[Issues](https://github.com/jaesungkr/slink/issues)에 Windows 버전, Slink 버전, 재현 순서를 남겨 주세요. 스크린샷에는 개인적인 창 제목이나 내용이 포함되지 않도록 확인해 주세요.

현재 저장소에는 별도 LICENSE 파일이 없습니다. 재배포나 코드 재사용 조건은 아직 명시되지 않았습니다.
