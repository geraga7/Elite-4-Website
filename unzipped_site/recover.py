import json
import os

log_file = "/Users/user/.gemini/antigravity/brain/a336c116-435a-42f7-88c5-337c17724c83/.system_generated/logs/overview.txt"
dest_dir = "/Users/user/Documents/Elite 4/"

with open(log_file, 'r') as f:
    lines = f.readlines()

pages = ["index.html", "about.html", "services.html", "portfolio.html", "faq.html", "testimonials.html", "process.html"]

for page in pages:
    found = False
    for i in range(len(lines)-1, -1, -1):
        line = lines[i]
        if f'"{page}"' in line and '"write_to_file"' in line:
            try:
                data = json.loads(line)
                for tc in data.get("tool_calls", []):
                    if tc.get("name") == "write_to_file":
                        args = tc.get("args", {})
                        if page in args.get("TargetFile", ""):
                            content = args.get("CodeContent")
                            if content:
                                # Sometimes it's double encoded
                                if content.startswith('"'):
                                    content = json.loads(content)
                                out_path = os.path.join(dest_dir, page)
                                with open(out_path, 'w') as out:
                                    out.write(content)
                                print(f"Recovered {page}")
                                found = True
                                break
            except Exception as e:
                pass
        if found:
            break
