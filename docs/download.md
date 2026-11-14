# Slink 다운로드 / Download

[한국어](#한국어) · [English](#english)

## 한국어

**[Slink.exe 다운로드](https://github.com/jaesungkr/slink/releases/latest/download/Slink.exe)**

Windows 10/11용 포터블 실행 파일입니다. 설치 마법사 없이 실행하며, macOS·Linux용 파일은 제공하지 않습니다. [최신 릴리스 페이지](https://github.com/jaesungkr/slink/releases/latest)에서 버전과 변경 기록을 확인할 수 있습니다.

### 실행과 복원

1. GitHub 릴리스에서 `Slink.exe`를 내려받습니다. **Source code** ZIP은 실행 파일이 아닙니다.
2. 파일을 실행합니다. **Visible → Hide**로 창과 작업표시줄 버튼을 함께 숨깁니다.
3. 숨긴 창을 선택하고 **Show**로 복원합니다. 같은 프로세스의 여러 창이 함께 숨겨질 수 있습니다.
4. **X**는 트레이로 숨기기입니다. 종료하려면 트레이 아이콘 메뉴의 **Quit**를 누릅니다. 정상 종료 시 숨긴 창이 복원됩니다.

### 문제 해결

| 증상 | 확인할 내용 |
| --- | --- |
| Slink 창이 보이지 않음 | Windows 알림 영역의 숨겨진 아이콘에서 Slink를 찾아 Show를 선택하세요. 중복 실행은 차단됩니다. |
| 창이 숨겨지지 않음 | 대상 앱이 관리자 권한인지 확인하세요. 일부 Store 앱과 특수한 창은 지원이 제한됩니다. |
| 웹 화면이 열리지 않음 | pywebview는 Edge WebView2를 사용합니다. [Microsoft의 WebView2 안내](https://developer.microsoft.com/microsoft-edge/webview2/)에서 런타임을 확인하세요. |
| Windows가 실행 경고를 표시함 | 파일 출처와 릴리스 정보를 확인하세요. 바이러스 백신을 끄거나 경고를 무조건 우회하지 마세요. |
| 강제 종료 후 창이 복원되지 않음 | 충돌·강제 종료 시 복원은 보장되지 않습니다. 대상 앱에 미저장 작업이 있다면 먼저 보존한 뒤 앱 재실행을 검토하세요. |

### 업데이트

실행 파일에서는 앱의 업데이트 확인 기능을 사용할 수 있습니다. 업데이트 전에 숨긴 창을 복원하고 작업을 저장하세요. 완료 안내가 나오면 Slink를 다시 실행합니다. 수동으로 최신 파일을 내려받아 교체하는 경우에도 먼저 Slink를 종료하세요.

설정은 `%APPDATA%\Slink\settings.json`에 저장됩니다. 소스 실행 사용자는 앱 업데이트 대신 Git을 사용하세요.

---

## English

**[Download Slink.exe](https://github.com/jaesungkr/slink/releases/latest/download/Slink.exe)**

A portable executable for Windows 10/11, with no installation wizard. No macOS or Linux executable is provided. Check the [latest release](https://github.com/jaesungkr/slink/releases/latest) for the version and change history.

### Run and restore

1. Download `Slink.exe` from GitHub Releases. The **Source code** ZIP is not the executable.
2. Run it. Use **Visible → Hide** to hide a window and its taskbar button.
3. Select a hidden window and use **Show** to restore it. Multiple windows from the same process may be hidden together.
4. **X** hides Slink to the tray. Choose **Quit** in the tray menu to exit; normal exit restores hidden windows.

### Troubleshooting

| Symptom | What to check |
| --- | --- |
| Slink is not visible | Find Slink in the Windows notification area's hidden icons and choose Show. Duplicate launches are blocked. |
| A window does not hide | Check whether the target app is elevated. Some Store apps and special windows have limited support. |
| The web interface does not open | pywebview uses Edge WebView2. Check the runtime using [Microsoft's WebView2 guidance](https://developer.microsoft.com/microsoft-edge/webview2/). |
| Windows displays a security warning | Verify the download source and release information. Do not disable antivirus or blindly bypass warnings. |
| A window stays hidden after a forced exit | Recovery after a crash or forced termination is not guaranteed. Protect unsaved work before considering restarting the target app. |

### Updates

The packaged executable can check for updates inside the app. Restore hidden windows and save your work before updating. Reopen Slink after the completion message. Quit Slink before manually replacing it with a new download, too.

Settings are stored in `%APPDATA%\Slink\settings.json`. If running from source, update through Git instead of the app updater.
