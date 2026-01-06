import os
from PIL import Image

# --- TUNE THESE NUMBERS ---
START_X = 10   # Increase if dragon is cut on the LEFT
START_Y = 10   # Increase if dragon is cut on the TOP
GAP_X = 5      # Space between columns (if any)
GAP_Y = 5      # Space between rows (if any)
# --------------------------

def bulletproof_split(file_name):
    img = Image.open(file_name).convert("RGBA")
    w, h = img.size
    
    # We divide the remaining space by the number of frames
    fw = (w - START_X) // 6 
    fh = (h - START_Y) // 5

    actions = ["idle", "run", "think", "pounce", "catch"]
    
    for r in range(5):
        action = actions[r]
        os.makedirs(f"frames/{action}", exist_ok=True)
        
        for c in range(6):
            # The Math: Start + (Column * Width) + Any Gaps
            left = START_X + (c * fw) + (c * GAP_X)
            top = START_Y + (r * fh) + (r * GAP_Y)
            right = left + fw - GAP_X
            bottom = top + fh - GAP_Y
            
            frame = img.crop((left, top, right, bottom))
            
            # Transparency: Turn 'almost white' into see-through
            datas = frame.getdata()
            newData = []
            for item in datas:
                if item[0] > 220 and item[1] > 220 and item[2] > 220:
                    newData.append((255, 255, 255, 0))
                else:
                    newData.append(item)
            frame.putdata(newData)
            frame.save(f"frames/{action}/{action}_{c}.png")

    print(f"Done! Created frames using Width:{fw} and Height:{fh}")

bulletproof_split("chara3.png")
