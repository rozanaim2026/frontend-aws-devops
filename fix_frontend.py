import re

# Files with a duplicate "const API" line — needs config.js inserted + line removed
html_files = [
    "public/profile.html",
    "public/admin.html",
    "public/product-details.html",
    "public/orders.html",
    "public/order-details.html",
    "public/collections.html",
]

for f in html_files:
    with open(f) as fh:
        content = fh.read()
    content = re.sub(r'<script', '<script src="config.js"></script>\n<script', content, count=1)
    content = re.sub(r'[ \t]*const API = "https://api\.rozana-projects\.online";\s*\n?', '', content)
    with open(f, "w") as fh:
        fh.write(content)
    print(f"Updated {f}")

# products.html: config.js insert + CDN URL fix (no API declaration here)
f = "public/products.html"
with open(f) as fh:
    content = fh.read()
content = re.sub(r'<script', '<script src="config.js"></script>\n<script', content, count=1)
content = content.replace('https://cdn.rozana-projects.online/', 'assets/')
content = re.sub(r'const CDN = "https://cdn\.rozana-projects\.online";', 'const CDN = "assets";', content)
with open(f, "w") as fh:
    fh.write(content)
print(f"Updated {f}")

# Remaining CDN-only fixes
for f in ["public/style.css", "public/orders.html", "src/wishlist.js", "src/cart.js"]:
    with open(f) as fh:
        content = fh.read()
    new_content = content.replace('https://cdn.rozana-projects.online/', 'assets/')
    if new_content != content:
        with open(f, "w") as fh:
            fh.write(new_content)
        print(f"Updated CDN refs in {f}")

# Remove duplicate declarations from JS files
with open("src/app.js") as fh:
    lines = fh.readlines()
lines = [l for l in lines if 'const API_BASE_URL = "https://api.rozana-projects.online";' not in l]
with open("src/app.js", "w") as fh:
    fh.writelines(lines)
print("Updated src/app.js")

for f in ["src/wishlist.js", "src/checkout.js"]:
    with open(f) as fh:
        lines = fh.readlines()
    lines = [l for l in lines if 'const API = "https://api.rozana-projects.online";' not in l]
    with open(f, "w") as fh:
        fh.writelines(lines)
    print(f"Updated {f}")

print("Done.")
