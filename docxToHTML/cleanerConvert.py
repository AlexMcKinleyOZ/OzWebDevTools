from docx import Document

def docx_to_html(docx_path):
    doc = Document(docx_path)
    new_html_content = ""
    set_tag = None
    next_tag = None
    
    h1_tag = ['h1', 'class="h2"']
    p_title = ['p', 'class="entry__txt bold"']
    p_tag = ['p', '']

    def get_font_size(run):
        if run.font.size:
            return run.font.size.pt
        return None

    for para in doc.paragraphs:
        text = para.text.strip()

        if not text:
            if set_tag != None:
                 new_html_content += f'</{set_tag[0]}>\n'
            
            next_tag = None
            set_tag  = None
            continue

        font_sizes = [get_font_size(run) for run in para.runs if get_font_size(run)]
        font_size = max(font_sizes) if font_sizes else 11  # default fallback

        first_bold = False
        for run in para.runs:
            if run.text.strip():
                first_bold = run.bold is True
                break

        full_text = para.text

        if first_bold and font_size <= 11:
            next_tag = p_title

        if first_bold and font_size >= 12:
            next_tag = h1_tag

        if not first_bold:
            next_tag = p_tag    

        if set_tag == None:
            full_text = f'<{next_tag[0]} {next_tag[1]}>{full_text}'
            set_tag = next_tag
            new_html_content += full_text
        elif set_tag != next_tag:
            full_text = f'</{set_tag[0]}>\n<{next_tag[0]} {next_tag[1]}>{full_text}'
            set_tag = next_tag
            new_html_content += full_text
        elif set_tag == next_tag:
            new_html_content += full_text
        

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