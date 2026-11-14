## 다운로드 / Download

**[Windows용 Slink.exe 다운로드 / Download for Windows](https://github.com/jaesungkr/slink/releases/download/v3.2.2/Slink.exe)**

Windows 10/11 · 포터블 실행 파일 / Portable executable · 20.85 MiB

### 한국어

Slink는 앱 창과 작업표시줄 버튼을 함께 숨기고 필요할 때 다시 표시하는 Windows 도구입니다. 앱이나 프로세스를 종료하지 않습니다.

1. 위 링크 또는 아래 **Assets**에서 `Slink.exe`를 내려받아 실행하세요. `Source code` ZIP은 실행 파일이 아닙니다.
2. **Visible** 목록에서 창을 선택하고 **Hide**를 누릅니다. 같은 프로세스의 다른 창도 숨겨질 수 있습니다.
3. 숨긴 창을 선택하고 **Show**를 누르면 다시 표시됩니다.
4. **X**는 트레이로 숨기기입니다. 완전히 종료하려면 트레이 메뉴의 **Quit**를 사용하세요. 정상 종료할 때 숨긴 창을 복원합니다.

**v3.2.2 변경:** Visible 목록에서 `explorer.exe` 창을 제외했습니다.

Windows 전용이며 일부 Store 앱과 특수한 창에는 제한이 있습니다. 강제 종료·충돌 시 복원은 보장하지 않습니다. 업데이트 전에 숨긴 창을 복원하고 작업을 저장하세요. Windows 보안 경고가 나오면 출처를 확인하고, 백신을 끄거나 경고를 무조건 우회하지 마세요.

### English

Slink hides app windows and their taskbar buttons, then restores them when needed. It does not close the app or hide its process.

1. Download and run `Slink.exe` using the link above or **Assets** below. The `Source code` ZIP is not the executable.
2. Select a window in **Visible**, then click **Hide**. Other windows from the same process may also be hidden.
3. Select a hidden window and click **Show** to restore it.
4. **X** hides Slink to the tray. Use **Quit** in the tray menu to exit. Normal exit restores hidden windows.

**Changed in v3.2.2:** Excludes `explorer.exe` windows from the Visible list.

Windows only. Some Store apps and special windows have limited support. Restoration after a crash or forced termination is not guaranteed. Restore hidden windows and save work before updating. Verify the source if Windows displays a security warning; do not disable antivirus or blindly bypass warnings.

[한국어 안내 / Korean guide](https://github.com/jaesungkr/slink#readme) · [English guide](https://github.com/jaesungkr/slink/blob/master/README.en.md) · [문제 제보 / Report an issue](https://github.com/jaesungkr/slink/issues)

### 파일 확인 / File verification

SHA-256 for this release's `Slink.exe` (GitHub release asset digest):

```text
1aae123fd0dca30b0cb9ae2cd8c5c55233974b39509dd2fa2f86843a2223a6a6
```

PowerShell:

```powershell
Get-FileHash .\Slink.exe -Algorithm SHA256
```

해시 일치는 파일 일치 여부를 확인할 뿐 안전성을 보증하지 않습니다. / A matching hash verifies file identity, not software safety.

**Full Changelog**: https://github.com/jaesungkr/slink/compare/v3.2.1...v3.2.2
