# Changelog

## 1.0.1

- Preserve the English interface and exactly one random selection per launch.
- Resolve words.txt relative to the source file or Windows executable.
- Show actionable English dialogs for missing, unreadable, empty or invalid
  UTF-8 word lists.
- Accept UTF-8 BOMs and ignore blank lines before choosing a word.
- Rename the window to RandomWord and wrap long entries as the window resizes.
- Support Enter and Escape to close the app.
- Add a guarded entry point, regression tests and a Windows build script.
- Keep the original word list unchanged.
