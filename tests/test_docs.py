"""Offline documentation checks; not Windows application integration tests."""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class DocumentationTests(unittest.TestCase):
    def test_local_links_exist(self):
        for path in [ROOT / 'README.md', ROOT / 'README.en.md', *ROOT.glob('docs/*.md')]:
            for target in re.findall(r'\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
                if '://' in target or target.startswith('#'):
                    continue
                with self.subTest(document=path.name, target=target):
                    self.assertTrue((path.parent / target.split('#')[0]).is_file())

    def test_both_readmes_point_to_portable_download(self):
        url = 'https://github.com/jaesungkr/slink/releases/latest/download/Slink.exe'
        for name in ['README.md', 'README.en.md']:
            with self.subTest(document=name):
                text = (ROOT / name).read_text(encoding='utf-8')
                self.assertIn(url, text)
                for control in ['Visible', 'Hide', 'Show', 'Quit']:
                    self.assertIn(control, text)
                self.assertNotIn('License-MIT', text)

    def test_bilingual_download_guide(self):
        text = (ROOT / 'docs/download.md').read_text(encoding='utf-8')
        self.assertIn('## 한국어', text)
        self.assertIn('## English', text)
        self.assertIn('### 문제 해결', text)
        self.assertIn('### Troubleshooting', text)

    def test_powershell_build_does_not_use_cmd_continuation(self):
        text = (ROOT / 'docs/development.md').read_text(encoding='utf-8')
        self.assertNotRegex(text, r'\^\s*\n')
        self.assertIn('--add-data "ui.html;."', text)


if __name__ == '__main__':
    unittest.main()
