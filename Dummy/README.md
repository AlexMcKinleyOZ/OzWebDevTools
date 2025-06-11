# ダミー画像ジェネレーター

テキスト付きのダミーJPEG画像を簡単に作成できるPythonスクリプトです。フロントエンド開発時のレイアウト確認やモックアップ作成などに便利です。内部では [ImageMagick](https://imagemagick.org/) を使用しています。

---

## 🛠 必要環境

- **Python 3.x**
- **ImageMagick**（`magick` コマンドとして使えるように）

---

## 🧪 インストール手順

### 1. Python のインストール

公式サイトからインストール：

👉 https://www.python.org/downloads/

インストール後、バージョン確認：

```bash
python3 --version
```

### 2. ImageMagick のインストール

macOS（Homebrew 使用）:

```bash
brew install imagemagick
```

その他の環境では以下からダウンロード：

👉 https://imagemagick.org/script/download.php

インストール後、確認：

```bash
magick --version
```

---

## 🚀 使い方

1. 以下のスクリプトを `generate_dummy_images.py` という名前で保存します。

2. ターミナルで実行：

```bash
python3 generate_dummy_images.py
```

3. プロンプトが表示されるので、以下を入力します：
   - 作成したい画像の枚数
   - 幅（px）
   - 高さ（px）

作成される画像の特徴：
- 背景色はグレー
- 中央に白い文字（例：`450 X 200`）
- ファイル名：`dummy_1.jpeg`, `dummy_2.jpeg`, ...

---

## 📄 スクリプト本体

```python
import subprocess

run = True
times = 0

def create_dummy_image(filename, width, height, bg_color, text, text_color, pointsize):
    command = [
        "magick",
        "-size", f"{width}x{height}",
        f"xc:{bg_color}",
        "-gravity", "center",
        "-pointsize", str(pointsize),
        "-fill", text_color,
        "-annotate", "+0+0", text,
        filename
    ]
    try:
        subprocess.run(command, check=True)
        print(f"Created image: {filename}")
    except subprocess.CalledProcessError as e:
        print("ImageMagickコマンドの実行に失敗しました:", e)

while run:
    how_many = input("作成する画像の枚数: ")
    width = input("幅（px）: ")
    height = input("高さ（px）: ")
    text = width + " X " + height
    how_many = int(how_many)
    width = int(width)
    height = int(height)
    pointsize = 72
    if width <= 250:
        pointsize = 36
    for i in range(how_many):
        times += 1
        create_dummy_image(f"dummy_{times}.jpeg", width, height, "gray", text, "white", pointsize)
    
    input("終了するにはEnterを押してください")
    run = False
```

---

## ✅ 使用例

**入力:**

```
作成する画像の枚数: 2
幅（px）: 400
高さ（px）: 300
```

**出力:**

- `dummy_1.jpeg`（サイズ：400x300、テキスト付き）
- `dummy_2.jpeg`（同上）

---

