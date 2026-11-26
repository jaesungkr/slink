# Slink

A small Windows utility for hiding app windows and bringing them back when needed.

[한국어](README.md) · **English**

[**Download Slink.exe for Windows**](https://github.com/jaesungkr/slink/releases/latest/download/Slink.exe) · [Download and setup guide](docs/download.md#english) · [Release history](https://github.com/jaesungkr/slink/releases)

Run the executable without a separate installer. Intended for Windows 10/11; macOS and Linux are not supported.

## What it does

- Hides app windows and their taskbar buttons, then restores them on request.
- Re-hides windows that reappear in the background.
- Filters windows by title or process name.
- Saves your dark/light theme preference.
- Reopens or quits from the system tray.
- Checks GitHub Releases and updates the packaged executable from the app.

Slink hides windows, not processes. It does not close the app. Other windows belonging to the same process may also be hidden.

## Getting started

1. Download and run `Slink.exe` using the link above.
2. Select a window in **Visible**, then click **Hide**.
3. Select a hidden window and click **Show** to restore it.
4. The **X** button hides Slink to the tray; it does not quit.
5. Choose **Quit** from the tray menu to exit. Normal exit restores hidden windows.

See [troubleshooting](docs/download.md#troubleshooting) if the app does not launch or you cannot find a hidden window.

## Limitations

- Controlling an elevated app may require running Slink with matching administrator privileges. Ordinary apps do not require elevation.
- Some Microsoft Store apps and special windows may not work correctly.
- Restoration after a forced termination or crash is not guaranteed. Try an unimportant window first.
- Settings are saved in `%APPDATA%\Slink\settings.json`.
- Window hiding is not a security or privacy feature.

## Run or build from source

The [development guide](docs/development.md) covers Windows setup, Python 3.12, builds, and checks. Development source may differ from the released executable.

| File | Purpose |
| --- | --- |
| `main.py` | Entry point and single-instance handling |
| `ui.html` | HTML/CSS/JavaScript interface |
| `slink/gui.py` | pywebview window and local HTTP API |
| `slink/core.py`, `slink/win32.py` | Window visibility and Windows APIs |
| `slink/tray.py` | System tray |
| `slink/updater.py` | GitHub Releases updates |

## Report a problem

Include your Windows version, Slink version, and reproduction steps in [Issues](https://github.com/jaesungkr/slink/issues). Remove personal window titles and content from screenshots before sharing.

Slink’s original code, documentation, and assets are licensed under the [MIT License](LICENSE). Third-party components are covered by their respective licenses.
