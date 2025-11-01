# Plugin Manager Skill for Claude Code

A cross-platform skill for managing and querying Claude Code plugins. This skill provides easy access to plugin information since the `claude plugin list` command does not exist.

## Features

- List all installed plugins with their status (enabled/disabled)
- Check if a specific plugin is installed
- Display plugin information in multiple formats (table, JSON, list)
- Count total plugins and view statistics
- Cross-platform support (Windows, Unix, Linux, Mac)

## Installation

### Using Claude Code

1. Copy this skill directory to your Claude Code skills folder:
   ```bash
   # Windows
   cp -r plugin-manager-skill "$USERPROFILE/.claude/skills/"

   # Unix/Mac
   cp -r plugin-manager-skill ~/.claude/skills/
   ```

2. The skill will be automatically available in Claude Code

### Manual Installation

Clone or download this repository to your Claude Code skills directory:

```bash
# Windows
git clone https://github.com/s2005/plugin-manager-skill.git "$USERPROFILE/.claude/skills/plugin-manager"

# Unix/Mac
git clone https://github.com/s2005/plugin-manager-skill.git ~/.claude/skills/plugin-manager
```

## Usage

The skill is triggered when you ask Claude Code about plugins:

- "List all installed plugins"
- "What plugins do I have?"
- "Is markdown-linter-fixer installed?"
- "Show me plugin status"
- "How many plugins are enabled?"

### Direct Command Usage

#### Python Script (Recommended - Cross-Platform)

```bash
# List all plugins
python scripts/list_plugins.py

# Table format
python scripts/list_plugins.py --format table

# JSON format
python scripts/list_plugins.py --format json

# Check specific plugin
python scripts/list_plugins.py --check "plugin-name@marketplace-name"

# Count plugins
python scripts/list_plugins.py --count
```

#### jq Commands

See platform-specific guides for jq command examples:
- **Windows**: [docs/windows-guide.md](docs/windows-guide.md)
- **Unix/Mac**: [docs/unix-guide.md](docs/unix-guide.md)

## Structure

```
plugin-manager-skill/
├── README.md             # This file
├── SKILL.md              # Main skill configuration
├── docs/
│   ├── windows-guide.md  # Windows-specific commands (Git Bash/MINGW64)
│   └── unix-guide.md     # Unix/Mac-specific commands
└── scripts/
    └── list_plugins.py   # Cross-platform Python script
```

## Platform Support

- **Windows** (Git Bash/MINGW64)
- **Unix/Linux**
- **macOS**

The skill automatically detects your platform and provides appropriate path syntax.

## Requirements

- **Python 3.6+** (for `list_plugins.py` script)
- **jq** (optional, for advanced JSON queries)
- **Claude Code** installed and configured

## Documentation

- [SKILL.md](SKILL.md) - Main skill documentation and quick reference
- [Windows Guide](docs/windows-guide.md) - Windows-specific commands and troubleshooting
- [Unix Guide](docs/unix-guide.md) - Unix/Mac-specific commands and advanced usage

## Common Issues

### Windows Path Errors

If you encounter "No such file or directory" errors on Windows:

- ✓ Use forward slashes: `scripts/list_plugins.py`
- ✗ Don't use backslashes: `scripts\list_plugins.py`
- ✓ Use `$USERPROFILE`: `$USERPROFILE/.claude/settings.json`
- ✗ Don't use `~`: `~/.claude/settings.json`

See [docs/windows-guide.md](docs/windows-guide.md) for complete troubleshooting.

## How It Works

This skill reads plugin information directly from Claude Code's `settings.json` file:

- **Windows**: `$USERPROFILE/.claude/settings.json`
- **Unix/Mac**: `~/.claude/settings.json`

The `enabledPlugins` object in this file contains all installed plugins and their status.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

MIT License

## Author

Created for the Claude Code community to simplify plugin management.

## Related Resources

- [Claude Code Documentation](https://docs.claude.com/claude-code)
- [Claude Code GitHub](https://github.com/anthropics/claude-code)

## Changelog

### v1.0.0 (2025-11-01)
- Initial release
- Cross-platform Python script
- Platform-specific documentation (Windows/Unix)
- Support for multiple output formats (table, JSON, list)
- Plugin checking and counting features
