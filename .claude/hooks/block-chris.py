import sys, json

data = json.load(sys.stdin)
tool_input = data.get("tool_input", {})

fp = tool_input.get("file_path", "")
cmd = tool_input.get("command", "")

if "chris.txt" in fp or "chris.txt" in cmd:
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": "Access to chris.txt is blocked by project policy."
        }
    }))
    sys.exit(2)

sys.exit(0)
