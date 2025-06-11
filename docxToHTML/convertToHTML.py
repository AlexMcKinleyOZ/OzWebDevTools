from docx import Document

def docx_to_html(docx_path):
    doc = Document(docx_path)
    new_html_content = ""

    def get_font_size(run):
        if run.font.size:
            return run.font.size.pt
        return None

    for para in doc.paragraphs:
        text = para.text.strip()

        # Skip blank paragraphs
        if not text:
            continue

        # Get max font size from the paragraph
        font_sizes = [get_font_size(run) for run in para.runs if get_font_size(run)]
        font_size = max(font_sizes) if font_sizes else 11  # default fallback

        # Determine if the first meaningful run is bold
        first_bold = False
        for run in para.runs:
            if run.text.strip():  # skip empty runs
                first_bold = run.bold is True
                break

        full_text = para.text
        if first_bold:
            full_text = f'<span class="bold">{full_text}</span>'

        # Choose block tag
        if font_size >= 12:
            new_html_content += f'<h1 class="h2">{full_text}</h1>\n'
        else:
            new_html_content += f"<p>{full_text}</p>\n"

    return new_html_content

if __name__ == "__main__":
    path = "src.docx"  # Replace with your actual file
    html_content = docx_to_html(path)

    # Wrap in a basic HTML structure with optional bold style
    full_html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>Auto Converted</title>
    <style>
        body {{ font-family: Noto sans; }}
        p {{ font-size: 16px;
        font-weight: 400;
        line-height: 1.8; }}
        .h2 {{ font-size: 36px;
        font-weight: 700;
        line-height: 1.4;}}
        .bold {{ font-weight: bold; }}
    </style>
</head>
<body>
{html_content}
</body>
</html>
"""

    with open("autoconvert.html", "w", encoding="utf-8") as f:
        f.write(full_html)

    print("✅ HTML saved to autoconvert.html")
