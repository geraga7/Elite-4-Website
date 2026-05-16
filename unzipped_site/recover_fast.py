import json
import os
import linecache

log_file = "/Users/user/.gemini/antigravity/brain/a336c116-435a-42f7-88c5-337c17724c83/.system_generated/logs/overview.txt"
dest_dir = "/Users/user/Documents/Elite 4/"

lines_to_extract = {
    27: "index.html",
    28: "services.html",
    29: "about.html",
    30: "portfolio.html",
    31: "faq.html",
    48: "testimonials.html",
    64: "process.html"
}

for line_num, page in lines_to_extract.items():
    line = linecache.getline(log_file, line_num)
    try:
        data = json.loads(line)
        for tc in data.get("tool_calls", []):
            if tc.get("name") == "write_to_file":
                args = tc.get("args", {})
                content = args.get("CodeContent")
                if content:
                    if content.startswith('"'):
                        content = json.loads(content)
                    out_path = os.path.join(dest_dir, page)
                    with open(out_path, 'w') as out:
                        out.write(content)
                    print(f"Recovered {page}")
    except Exception as e:
        print(f"Failed on {page}: {e}")

