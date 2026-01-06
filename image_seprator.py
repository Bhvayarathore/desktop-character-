import os
from PIL import Image

def split_character_actions(file_name):
    # 1. Define the actions based on your row description
    actions = ["idle", "run", "think", "pounce", "catch"]
    cols = 6
    rows = 5

    # 2. Open and prepare the image
    img = Image.open("chara3.png").convert("RGBA") # Convert to handle transparency
    width, height = img.size
    fw = width // cols   # Frame Width
    fh = height // rows  # Frame Height

    for r in range(rows):
        action_name = actions[r]
        # Create a folder for each action (e.g., /frames/run/)
        folder_path = f"frames/{action_name}"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        for c in range(cols):
            # Calculate the box for this specific frame
            left = c * fw
            top = r * fh
            right = (c + 1) * fw
            bottom = (r + 1) * fh
            
            frame = img.crop((left, top, right, bottom))

            # --- TRANSPARENCY TRICK ---
            # This logic turns "near-white" pixels into transparent pixels
            datas = frame.getdata()
            newData = []
            for item in datas:
                # If the pixel is very bright (white), make it transparent
                if item[0] > 240 and item[1] > 240 and item[2] > 240:
                    newData.append((255, 255, 255, 0))
                else:
                    newData.append(item)
            frame.putdata(newData)
            
            # Save the frame
            frame.save(f"{folder_path}/{action_name}_{c}.png")

    print("✨ Surgery Complete! Your character actions are sorted into folders.")

# Run the function (Make sure your file name is correct!)
split_character_actions("your_character_sheet.png")
