import tkinter as tk
import os
MemeTalk = os.environ.get("MemeTalk")
window = tk.Tk()
window.title("Talking Meme Man")
window.iconbitmap(f"{MemeTalk}\\images\\icon.ico")
window.geometry("1913x1000")
window.config(bg="#000000")
frame = tk.Frame(
    window,
    bg="#000000"
)
frame.pack(side="left", padx=0, pady=0)
canvas = tk.Canvas(
    frame,
    height=700,
    width=500,
    bg="#000000"
)
canvas.pack()
MemeMan = tk.PhotoImage(file=f"{MemeTalk}\\images\\MemeMan.png")
canvas.create_image(
    0,
    0,
    anchor=tk.NW,
    image=MemeMan
)
input_text = tk.Text(
    window,
    height=8,
    width=174,
    bg="#FFFFFF"
)
input_text.pack()
label1 = tk.Label(text="Input", bg="#00FF00")
label1.pack()
def mimic():
    text_to_mimic = input_text.get(1.0, "end-1c")
    output_text.insert(tk.END, text_to_mimic)
button = tk.Button(
    text="M I M I C",
    bg="#FF00FF",
    command=mimic
)
button.pack(side="right")
label2 = tk.Label(text="Output", bg="#00FF00")
label2.pack(side="bottom")
output_text = tk.Text(
    window,
    height=8,
    width=174,
    bg="#FFFFFF"
)
output_text.pack(side="bottom")
window.mainloop()