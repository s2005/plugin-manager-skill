# Plugin Manager - Windows Guide (Git Bash/MINGW64)

## Critical Path Rules for Windows

**ALWAYS follow these rules when generating bash commands on Windows:**

1. **ALWAYS use forward slashes (/) in file paths**
2. **NEVER use backslashes (\) - they are escape characters in bash**
3. **Use `$USERPROFILE` instead of `~` for user home directory**
4. **Quote paths with spaces**: Use `"$USERPROFILE/.claude/settings.json"`
5. **Relative paths**: Use `./scripts/file.py` not `.\scripts\file.py`

## Settings File Location

```bash
$USERPROFILE/.claude/settings.json
```

**Common path equivalents:**
- `~/.claude/settings.json` → `$USERPROFILE/.claude/settings.json`
- `%USERPROFILE%\.claude\settings.json` (cmd.exe) → `$USERPROFILE/.claude/settings.json` (bash)

## Using the Python Script

**List all plugins with status:**
```bash
python scripts/list_plugins.py
```

**List in table format:**
```bash
python scripts/list_plugins.py --format table
```

**Get JSON output:**
```bash
python scripts/list_plugins.py --format json
```

**Check if specific plugin exists:**
```bash
python scripts/list_plugins.py --check "markdown-linter-fixer@markdown-linter-fixer-marketplace"
```

**Count total plugins:**
```bash
python scripts/list_plugins.py --count
```

## Using jq Commands

**List all plugins with status:**
```bash
jq -r '.enabledPlugins | to_entries[] | "\(.key): \(if .value then "enabled" else "disabled" end)"' "$USERPROFILE/.claude/settings.json"
```

**Formatted table view:**
```bash
echo "INSTALLED PLUGINS:" && jq -r '.enabledPlugins | to_entries[] | "  [\(if .value then "✓" else " " end)] \(.key | split("@")[0]) (from: \(.key | split("@")[1]))"' "$USERPROFILE/.claude/settings.json"
```

**Check if specific plugin exists:**
```bash
jq -r --arg plugin "PLUGIN_NAME@MARKETPLACE" '.enabledPlugins[$plugin] // "not installed"' "$USERPROFILE/.claude/settings.json"
```

**Get raw JSON:**
```bash
jq '.enabledPlugins' "$USERPROFILE/.claude/settings.json"
```

**Count total plugins:**
```bash
jq '.enabledPlugins | length' "$USERPROFILE/.claude/settings.json"
```

**List only plugin names:**
```bash
jq -r '.enabledPlugins | keys[]' "$USERPROFILE/.claude/settings.json"
```

**List all enabled plugins only:**
```bash
jq -r '.enabledPlugins | to_entries[] | select(.value == true) | .key' "$USERPROFILE/.claude/settings.json"
```

**List all disabled plugins only:**
```bash
jq -r '.enabledPlugins | to_entries[] | select(.value == false) | .key' "$USERPROFILE/.claude/settings.json"
```

## Common Windows Errors

### "No such file or directory"
**Cause:** You used backslashes instead of forward slashes

- ✗ Wrong: `python scripts\list_plugins.py`
- ✓ Correct: `python scripts/list_plugins.py`

### "Path not found" or "~: No such file or directory"
**Cause:** You used `~` instead of `$USERPROFILE`

- ✗ Wrong: `jq '.enabledPlugins' ~/.claude/settings.json`
- ✓ Correct: `jq '.enabledPlugins' "$USERPROFILE/.claude/settings.json"`

### "Syntax error near unexpected token"
**Cause:** You mixed Windows-style paths with bash commands

- ✗ Wrong: `jq '.enabledPlugins' ~\.claude\settings.json`
- ✓ Correct: `jq '.enabledPlugins' "$USERPROFILE/.claude/settings.json"`

## Quick Reference: Good vs Bad

| ✗ Wrong (Windows-style) | ✓ Correct (Bash-style) |
|------------------------|------------------------|
| `scripts\file.py` | `scripts/file.py` |
| `.\scripts\file.py` | `./scripts/file.py` |
| `~\.claude\settings.json` | `$USERPROFILE/.claude/settings.json` |
| `%USERPROFILE%\...` | `$USERPROFILE/...` |
| `C:\Users\...` | `/c/Users/...` or `$USERPROFILE/...` |

## Environment Variables

In Git Bash/MINGW64:
- `$USERPROFILE` → User home directory (e.g., `/c/Users/YourName`)
- `$HOME` → Usually same as `$USERPROFILE`
- `~` → May not work reliably, prefer `$USERPROFILE`

## Alternative: Using cmd.exe or PowerShell

If you need to use Windows-native shells instead of Git Bash:

**cmd.exe:**
```cmd
python scripts\list_plugins.py
jq .enabledPlugins %USERPROFILE%\.claude\settings.json
```

**PowerShell:**
```powershell
python scripts/list_plugins.py
jq .enabledPlugins "$env:USERPROFILE\.claude\settings.json"
```

**Note:** This skill assumes Git Bash/MINGW64. For cmd.exe or PowerShell, use backslashes and appropriate environment variable syntax.
