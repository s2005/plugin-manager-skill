#!/usr/bin/env python3
"""
Claude Code Plugin Manager

Lists, checks, and provides information about installed Claude Code plugins.
Since 'claude plugin list' command does not exist, this script reads directly
from ~/.claude/settings.json to retrieve plugin information.
"""

import json
import sys
from pathlib import Path
import argparse


def get_settings_path():
    """Get the path to Claude settings.json file."""
    home = Path.home()
    settings_path = home / ".claude" / "settings.json"
    
    if not settings_path.exists():
        print(f"Error: Settings file not found at {settings_path}", file=sys.stderr)
        print("Ensure Claude Code is installed and has been run at least once.", file=sys.stderr)
        sys.exit(1)
    
    return settings_path


def load_plugins():
    """Load plugin information from settings.json."""
    settings_path = get_settings_path()
    
    try:
        with open(settings_path, 'r', encoding='utf-8') as f:
            settings = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error: Failed to parse settings.json: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: Failed to read settings.json: {e}", file=sys.stderr)
        sys.exit(1)
    
    plugins = settings.get('enabledPlugins', {})
    
    if not plugins:
        print("No plugins found in settings.json", file=sys.stderr)
        return {}
    
    return plugins


def format_list(plugins):
    """Format plugins as a simple list with status."""
    for plugin_name, enabled in plugins.items():
        status = "enabled" if enabled else "disabled"
        print(f"{plugin_name}: {status}")


def format_table(plugins):
    """Format plugins as a table."""
    print("INSTALLED PLUGINS:")
    print()
    
    for plugin_name, enabled in plugins.items():
        parts = plugin_name.split('@')
        if len(parts) == 2:
            name, marketplace = parts
        else:
            name = plugin_name
            marketplace = "unknown"
        
        checkbox = "[X]" if enabled else "[ ]"
        print(f"  {checkbox} {name} (from: {marketplace})")


def format_json(plugins):
    """Format plugins as JSON."""
    print(json.dumps(plugins, indent=2))


def check_plugin(plugins, plugin_name):
    """Check if a specific plugin is installed."""
    if plugin_name in plugins:
        status = "enabled" if plugins[plugin_name] else "disabled"
        print(f"{plugin_name}: {status}")
        return 0
    else:
        print(f"{plugin_name}: not installed")
        return 1


def count_plugins(plugins):
    """Count total plugins."""
    total = len(plugins)
    enabled = sum(1 for v in plugins.values() if v)
    disabled = total - enabled
    
    print(f"Total plugins: {total}")
    print(f"  Enabled: {enabled}")
    print(f"  Disabled: {disabled}")


def main():
    parser = argparse.ArgumentParser(
        description="List and check Claude Code plugins"
    )
    
    parser.add_argument(
        '--format',
        choices=['list', 'table', 'json'],
        default='list',
        help="Output format (default: list)"
    )
    
    parser.add_argument(
        '--check',
        metavar='PLUGIN',
        help="Check if a specific plugin is installed"
    )
    
    parser.add_argument(
        '--count',
        action='store_true',
        help="Count total plugins"
    )
    
    args = parser.parse_args()
    
    plugins = load_plugins()
    
    if args.check:
        sys.exit(check_plugin(plugins, args.check))
    elif args.count:
        count_plugins(plugins)
    elif args.format == 'table':
        format_table(plugins)
    elif args.format == 'json':
        format_json(plugins)
    else:
        format_list(plugins)


if __name__ == '__main__':
    main()
