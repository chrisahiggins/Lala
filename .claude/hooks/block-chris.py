import sys, json

data = json.load(sys.stdin)
fp = data.get("tool_input", {}).get("file_path", "")

if "chris.txt" in fp:
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": "Access to chris.txt is blocked by project policy."
        },
        "reason": "chris.txt is blocked"
    }))
    sys.exit(2)

sys.exit(0)
