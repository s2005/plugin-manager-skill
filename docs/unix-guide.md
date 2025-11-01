# Plugin Manager - Unix/Linux/Mac Guide

## Settings File Location

```bash
~/.claude/settings.json
```

**Alternative locations:**
- Project-specific: `./.claude/settings.json`
- Explicit path: `$HOME/.claude/settings.json`

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
jq -r '.enabledPlugins | to_entries[] | "\(.key): \(if .value then "enabled" else "disabled" end)"' ~/.claude/settings.json
```

**Formatted table view:**
```bash
echo "INSTALLED PLUGINS:" && jq -r '.enabledPlugins | to_entries[] | "  [\(if .value then "✓" else " " end)] \(.key | split("@")[0]) (from: \(.key | split("@")[1]))"' ~/.claude/settings.json
```

**Check if specific plugin exists:**
```bash
jq -r --arg plugin "PLUGIN_NAME@MARKETPLACE" '.enabledPlugins[$plugin] // "not installed"' ~/.claude/settings.json
```

**Get raw JSON:**
```bash
jq '.enabledPlugins' ~/.claude/settings.json
```

**Count total plugins:**
```bash
jq '.enabledPlugins | length' ~/.claude/settings.json
```

**List only plugin names:**
```bash
jq -r '.enabledPlugins | keys[]' ~/.claude/settings.json
```

**List all enabled plugins only:**
```bash
jq -r '.enabledPlugins | to_entries[] | select(.value == true) | .key' ~/.claude/settings.json
```

**List all disabled plugins only:**
```bash
jq -r '.enabledPlugins | to_entries[] | select(.value == false) | .key' ~/.claude/settings.json
```

## Common Workflows

**Verify plugin installation after install:**
```bash
python scripts/list_plugins.py --check "plugin-name@marketplace-name"
```

**Quick check of enabled plugins:**
```bash
jq -r '.enabledPlugins | to_entries[] | select(.value == true) | .key' ~/.claude/settings.json
```

**Export plugin list to file:**
```bash
jq '.enabledPlugins' ~/.claude/settings.json > my-plugins.json
```

**Count enabled vs disabled:**
```bash
echo "Enabled: $(jq '[.enabledPlugins[] | select(. == true)] | length' ~/.claude/settings.json)"
echo "Disabled: $(jq '[.enabledPlugins[] | select(. == false)] | length' ~/.claude/settings.json)"
```

## Error Handling

If `~/.claude/settings.json` does not exist:
- Check that Claude Code is properly installed
- Verify you have run Claude Code at least once (creates settings file)
- Check alternative location: `.claude/settings.json` (project-specific)

**File not found error:**
```bash
# Check if file exists
ls -la ~/.claude/settings.json

# Check directory exists
ls -la ~/.claude/

# Verify Claude Code installation
which claude
```

## Advanced Usage

**Search for specific marketplace plugins:**
```bash
jq -r '.enabledPlugins | to_entries[] | select(.key | contains("@anthropic-agent-skills")) | .key' ~/.claude/settings.json
```

**Get plugin name without marketplace:**
```bash
jq -r '.enabledPlugins | keys[] | split("@")[0]' ~/.claude/settings.json
```

**Format as CSV:**
```bash
jq -r '.enabledPlugins | to_entries[] | "\(.key),\(.value)"' ~/.claude/settings.json
```

**Combine with other tools (grep, sort, etc.):**
```bash
# Find all enabled plugins, sorted
jq -r '.enabledPlugins | to_entries[] | select(.value == true) | .key' ~/.claude/settings.json | sort

# Count plugins by marketplace
jq -r '.enabledPlugins | keys[] | split("@")[1]' ~/.claude/settings.json | sort | uniq -c
```

## Platform Notes

- Forward slashes are standard on Unix/Linux/Mac
- `~` expands to your home directory (`/home/username` or `/Users/username`)
- Shell expansion with `$HOME` also works: `$HOME/.claude/settings.json`
- Python script uses `pathlib` and works seamlessly across all Unix-like systems
