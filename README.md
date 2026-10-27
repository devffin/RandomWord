# RandomWord 1.0.1

RandomWord is a small Windows desktop app that displays **one random word per
launch**. Click **OK**, press **Enter** or **Escape**, or close the window to quit.
Launch the app again to draw another word. Consecutive launches may select the
same word.

## Run the Windows app

Extract the complete distribution before running `RandomWord.exe`. Keep
`words.txt` beside the executable and keep the `_internal` folder when using
the provided build script. The app works even when launched from another working
directory, such as through a shortcut.

## Run from source

Use Python 3.9 or later with Tkinter installed:

```console
python main.py
```

Keep `words.txt` beside `main.py`. No third-party Python packages are needed to
run the source. On Linux, Tkinter may need to be installed separately using your
distribution's package manager. Windows is the primary target; desktop display
access is required.

## Word list

The list is an external UTF-8 text file, with or without a BOM, containing one
entry per line. Blank lines are ignored and surrounding whitespace is removed.
An absent, unreadable, incorrectly encoded or empty list produces an English
error dialog instead of an unhandled file-loading exception.

The original list is retained: entries include abbreviations, numbers, proper
nouns and hyphenated terms. This release does not filter or deduplicate entries.
Each non-empty line has the same probability of being selected.

## Build on Windows

Install Python 3.9 or later, including Tkinter and the Python launcher, and run
`build_windows.bat` from the extracted source folder. The script installs
PyInstaller into a local `.build-venv` virtual environment and creates:

```text
dist/RandomWord/
    RandomWord.exe
    words.txt
    LICENSE
    README.md
    _internal/
```

Distribute the entire `dist/RandomWord` folder, for example as a ZIP archive.
Build on Windows to produce a Windows executable. The script requires internet
access to install PyInstaller on the first run. Build requirements are in
`requirements-build.txt`; the resolved version is recorded in
`dist/RandomWord/build-requirements.txt`.

## Tests

```console
python -m unittest discover -s tests -v
```

Tests cover word loading, resource paths and the one-draw-per-launch contract.
The UI tests use doubles and do not verify Windows rendering or an actual
PyInstaller build. Before releasing a Windows binary, check long words, display
scaling, shortcuts with a different working directory, the error dialogs and
all closing methods.

## Word list credits

This project was made possible by these word-list projects:

- [devffin/LeMotDuJour](https://github.com/devffin/LeMotDuJour)
- [dwyl/english-words](https://github.com/dwyl/english-words)
