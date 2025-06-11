import subprocess

run = True
times = 0

def create_dummy_image(filename, width, height, bg_color, text, text_color, pointsize):
    command = [
        "magick",
        f"-size", f"{width}x{height}",
        f"xc:{bg_color}",
        "-gravity", "center",
        "-pointsize", f"{pointsize}",
        "-fill", text_color,
        "-annotate", "+0+0", text,
        filename
    ]

    try:
        subprocess.run(command, check=True)
        print(f"Created image: {filename}")
    except subprocess.CalledProcessError as e:
        print("Error running ImageMagick command:", e)

# Example usage

while run:
    how_many = input("How many: ")
    width = input("Width: ")
    height = input("Height: ")
    text = width + " X " + height
    how_many = int(how_many)
    height = int(height)
    width = int(width)
    pointsize = 72
    if width <= 250:
        pointsize = 36
    for i in range(how_many):
        times += 1
        create_dummy_image(f"dummy_{times}.jpeg", width, height, "gray", text, "white", pointsize)
        
    input("Exit")
    run = False
