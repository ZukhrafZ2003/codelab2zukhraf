import tkinter as tk

# Create window
root = tk.Tk()
root.title("Movie Details")
root.geometry("600x400")
root.configure(bg="lightyellow")

# Movie Title (white text)
title_label = tk.Label(root, text="Spider-Man: No Way Home",
                       font=("Arial", 20, "bold"), bg="navy", fg="white")
title_label.place(x=50, y=20, width=500, height=40)

# Release Date
release_label1 = tk.Label(root, text="Release Date:", font=("Arial", 12, "bold"), bg="lightyellow", fg="black")
release_label1.place(x=50, y=80)
release_label2 = tk.Label(root, text="17 December 2021", font=("Arial", 12), bg="lightyellow", fg="black")
release_label2.place(x=200, y=80)

# Director
director_label1 = tk.Label(root, text="Director:", font=("Arial", 12, "bold"), bg="lightyellow", fg="black")
director_label1.place(x=50, y=110)
director_label2 = tk.Label(root, text="Jon Watts", font=("Arial", 12), bg="lightyellow", fg="black")
director_label2.place(x=200, y=110)

# Cast
cast_label1 = tk.Label(root, text="Main Cast:", font=("Arial", 12, "bold"), bg="lightyellow", fg="black")
cast_label1.place(x=50, y=140)
cast_label2 = tk.Label(root, text="Tom Holland, Zendaya, Benedict Cumberbatch",
                       font=("Arial", 12), bg="lightyellow", fg="black")
cast_label2.place(x=200, y=140)

# Genre
genre_label1 = tk.Label(root, text="Genre:", font=("Arial", 12, "bold"), bg="lightyellow", fg="black")
genre_label1.place(x=50, y=170)
genre_label2 = tk.Label(root, text="Action, Adventure, Sci-Fi", font=("Arial", 12), bg="lightyellow", fg="black")
genre_label2.place(x=200, y=170)

# Runtime
runtime_label1 = tk.Label(root, text="Runtime:", font=("Arial", 12, "bold"), bg="lightyellow", fg="black")
runtime_label1.place(x=50, y=200)
runtime_label2 = tk.Label(root, text="148 minutes", font=("Arial", 12), bg="lightyellow", fg="black")
runtime_label2.place(x=200, y=200)

# Short Description
desc_label1 = tk.Label(root, text="Synopsis:", font=("Arial", 12, "bold"), bg="lightyellow", fg="black")
desc_label1.place(x=50, y=230)

desc_text = ("Peter Parker’s identity as Spider-Man is revealed, "
             "bringing chaos into his life. He seeks help from Doctor Strange, "
             "but a spell goes wrong, causing villains from other universes to appear.")

desc_label2 = tk.Label(root, text=desc_text, wraplength=500, justify="left",
                       font=("Arial", 11), bg="lightyellow", fg="black")
desc_label2.place(x=50, y=260)

# Exit Button
exit_button = tk.Button(root, text="Close", font=("Arial", 12), command=root.destroy, bg="lightblue", fg="black")
exit_button.place(x=260, y=340, width=80, height=30)

# Run window
root.mainloop()
