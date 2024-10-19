import os
from tkinter import *
from tkinter import ttk, filedialog, messagebox
from transliterate import translit

root = Tk()
root.title('Транслитерация песен')
root.geometry('800x800')
root.resizable(False, True)


show_result = Text(root, height=30, width=79)
show_result.place(x=40, y=150)
show_result.config(bg='beige', 
                   font=('Arial', 13), 
                   borderwidth=2, 
                   cursor='ibeam',
                   highlightcolor="red",
                   #borderwidth=4,
                   )

def show_process(msg: str) -> None:
    show_result.insert(END, msg + '\n')
    show_result.see(END)




def transliterate_song_title(title: str) -> str:
    return translit(title, 'ru', reversed=True)

def rename_music_files(directory: str) -> None:
    renamed_files = 0
    for filename in os.listdir(directory):
        file_extension = os.path.splitext(filename)[1]
        title, _ = os.path.splitext(filename)
        
        # Проверка на русские буквы
        if any('а' <= char <= 'я' or 'А' <= char <= 'Я' for char in title):
            new_title = transliterate_song_title(title)
            # транслитерация
            new_filename = f"{new_title}{file_extension}"
            #путь к старым и новому файлу
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_filename)
            
            # переименование файлов
            os.rename(old_file, new_file)
            show_process(f"Переименовано: '{filename}' -> '{new_filename}'")
            renamed_files += 1

    if renamed_files == 0:
        show_process('Файлы для переименования не найдены.')
    else:
        show_process(f'Всего переименовано файлов: {renamed_files}')
        


def dir_choice():
    directory = filedialog.askdirectory()
    if directory:
        rename_music_files(directory)
        
clue_label = Label(text="Выберите папку с файлами которые вы хотите транслитерировать...",  font=('Arial', 14))
clue_label.place(x=40, y=10)

label_style = ttk.Style()
label_style.configure('button_style.TButton',          # имя стиля
                    font="helvetica 14",    # шрифт
                    foreground="#004D40",   # цвет текста
                    padding=10,             # отступы
                    background="#B2DFDB",
                    relief="solid",
                    cursor='hand1',
                    width="63"
                    )
run_btn = ttk.Button(text='Choose directory', command=dir_choice,  style="button_style.TButton")
run_btn.place(x=40, y=60)
root.mainloop()
