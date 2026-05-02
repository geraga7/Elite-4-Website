import re
import os

log_files = [
    "/Users/user/.gemini/antigravity/brain/a336c116-435a-42f7-88c5-337c17724c83/.system_generated/logs/overview.txt",
    "/Users/user/.gemini/antigravity/brain/4d9ed821-f4dc-43f9-b112-a737e7a90578/.system_generated/logs/overview.txt"
]

files_to_recover = [
    "about.html", "services.html", "portfolio.html", 
    "process.html", "faq.html", "testimonials.html"
]

for log_file in log_files:
    if not os.path.exists(log_file):
        continue
        
    with open(log_file, 'r') as f:
        content = f.read()
        
    for target in files_to_recover:
        if os.path.exists(target):
            # Let's check size. If it's small, it was destroyed.
            if os.path.getsize(target) > 2000:
                continue # Probably fine? Actually my regex deleted half, so it might be 1000 bytes.
                
        # We need to find where write_to_file was called with TargetFile = target
        # In the logs, it looks like a JSON block or a code block.
        # Let's just find the last occurrence of the file content.
        # Usually it's in a tool call for write_to_file
        # "TargetFile": ".../about.html",\n "CodeContent": "..."
        pattern = r'"TargetFile":\s*"[^"]*' + target + r'".*?"CodeContent":\s*"(.*?)"'
        matches = re.findall(pattern, content, re.DOTALL)
        if matches:
            last_match = matches[-1]
            # It's JSON escaped, so we need to decode it
            # A simple way to decode JSON string in python:
            import json
            try:
                # Wrap in JSON to decode string
                decoded = json.loads('{"c": "' + last_match + '"}')["c"]
                with open("recovered_" + target, 'w') as out:
                    out.write(decoded)
                print(f"Recovered {target}")
            except Exception as e:
                print(f"Error decoding {target}: {e}")

