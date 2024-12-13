from PIL import Image, ImageTk
import tkinter as tk
import quiz

def show_warning():
    """Create a warning screen with a centered message and a start button."""
    # Yeni bir pencere oluştur
    window = tk.Toplevel()  # Ana pencerenin üstünde yeni bir pencere
    window.title("Warning Screen")

    # Pencere boyutunu ekran boyutuna ayarla
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window.geometry(f"{screen_width}x{screen_height}+0+0")

    # Arka plan resmi yükle
    bg_image = Image.open("encrypt.jpg")
    bg_image = bg_image.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    # Canvas oluştur ve resmi yerleştir
    canvas = tk.Canvas(window, width=screen_width, height=screen_height, highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")

    # İlk metin: "Pay attention"
    canvas.create_text(
        screen_width // 2,
        screen_height // 2 - 50,
        text="Pay Attention",
        font=("Arial", 36, "bold"),
        fill="white"
    )

    # İkinci metin: "Eğer sen ilk level 3 sehv etsen sekiller faylin sifrelenecek"
    canvas.create_text(
        screen_width // 2,
        screen_height // 2 + 20,
        text="If you make the first level 3 mistake, the image file will be encrypted.",
        font=("Arial", 24),
        fill="white"
    )

    # Buton ekle
    def start_game():
        print("Game started!")  # Buraya oyunun başlama fonksiyonunu ekleyebilirsiniz.
        quiz.quiz_screen()
        window.destroy()  # Uyarı ekranını kapatır.

    # Buton oluştur
    start_button = tk.Button(
        window,
        text="Start Game",
        font=("Arial", 20, "bold"),
        bg="#00FF00",
        fg="#000000",
        command=start_game
    )
    # Butonu pencerenin altına yerleştir
    start_button.place(
        x=screen_width // 2 - 100,
        y=screen_height // 2 + 100,
        width=200,
        height=50
    )

    # Resim referansını sakla (çöp toplanmasını önlemek için)
    canvas.image = bg_photo

    # Pencereyi döngüde çalıştır
    window.mainloop()

# Test için çalıştır
show_warning()