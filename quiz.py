from tkinter import Toplevel, Canvas, Button, Label
from PIL import Image, ImageTk

# JSON tabanlı soru verisi
questions = [
    {
        "question": "What is the common port number used for SSH?",
        "options": ["22", "80", "443", "21"],
        "answer": "22"
    },
    {
        "question": "Which tool is commonly used for monitoring network traffic?",
        "options": ["Wireshark", "Metasploit", "Nmap", "Burp Suite"],
        "answer": "Wireshark"
    },
    {
        "question": "Which of the following is a strong password?",
        "options": ["password123", "123456", "qwerty", "3x@mpl3Str0ng!"],
        "answer": "3x@mpl3Str0ng!"
    }
]

def quiz_screen():
    current_question = 0
    score = 0
    time_left = 15  # 15 saniye için zamanlayıcı

    def next_question(selected_option=None):
        nonlocal current_question, score, time_left

        # Cevabı kontrol et
        if selected_option == questions[current_question]["answer"]:
            score += 1

        # Bir sonraki soruya geç
        current_question += 1
        time_left = 15  # Zamanı sıfırla

        if current_question < len(questions):
            load_question()
        else:
            # Tüm sorular bittiğinde sonucu göster
            canvas.delete("all")
            canvas.create_text(
                screen_width // 2,
                screen_height // 2,
                text=f"Quiz Finished! Your Score: {score}/{len(questions)}",
                font=("Arial", 36, "bold"),
                fill="white"
            )
            for button in option_buttons:
                button.destroy()

    def load_question():
        nonlocal time_left
        time_left = 15  # Her yeni soruda zamanlayıcıyı sıfırla

        # Soruyu ve seçenekleri güncelle
        question_data = questions[current_question]
        question_label.config(text=question_data["question"])
        for i, option in enumerate(question_data["options"]):
            option_buttons[i].config(
                text=option,
                command=lambda opt=option: next_question(opt)
            )
        update_timer()  # Timer başlat

    def update_timer():
        nonlocal time_left
        if time_left > 0:
            timer_label.config(text=f"Time Left: {time_left}s")
            time_left -= 1
            quiz_window.after(1000, update_timer)  # Zamanlayıcıyı 1 saniyede bir güncelle
        else:
            next_question()  # Zaman bittiğinde bir sonraki soruya geç

    # Quiz ekranını başlat
    quiz_window = Toplevel()
    quiz_window.title("Quiz Screen")
    screen_width = quiz_window.winfo_screenwidth()
    screen_height = quiz_window.winfo_screenheight()
    quiz_window.geometry(f"{screen_width}x{screen_height}+0+0")

    # Arka plan resmi
    bg_image = Image.open("bg_image.jpeg")
    bg_image = bg_image.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    # Canvas
    canvas = Canvas(quiz_window, width=screen_width, height=screen_height, highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")

    # Resim referansını sakla (çöp toplanmasını önlemek için)
    canvas.image = bg_photo

    # Soru etiketi (Arka plan rengi yok)
    question_label = Label(quiz_window, text="", font=("Arial", 24, "bold"), fg="white")
    question_label.place(relx=0.1, rely=0.3, anchor="w")  # Sol tarafa hizalanmış
    
    # Zamanlayıcı etiketi (Arka plan rengi yok)
    timer_label = Label(quiz_window, text="", font=("Arial", 20, "bold"))
    timer_label.place(relx=0.1, rely=0.2, anchor="w")  # Sol tarafa hizalanmış


    # Seçenek butonları (Main menu gibi)
    option_buttons = []
    button_positions = [
        (0.1, 0.4),  # Sol üst
        (0.1, 0.5),  # Sol orta
        (0.1, 0.6),  # Sol alt
        (0.1, 0.7)   # Alt
    ]

    # Main menu tarzı butonları oluştur
    for pos in button_positions:
        btn = Button(
            quiz_window,
            text="",
            font=("Arial", 18),
            bg="#002244",  # Butonun arka plan rengi
            fg="#FFFFFF",  # Buton metni rengi beyaz
            width=20,
            height=2,
            relief="solid"
        )
        btn.place(relx=pos[0], rely=pos[1], anchor="w")
        option_buttons.append(btn)

    # İlk soruyu yükle
    load_question()

    quiz_window.mainloop()

# Test için çalıştırma, bu dosya sadece import ediliyor.
if __name__ == "__main__":
    quiz_screen()
