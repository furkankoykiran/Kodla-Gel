import random

ball_count = input(f"Top sayısını giriniz: ")
ball_count = int(ball_count) if ball_count.isdigit() else exit("Top sayısı sayısal değer olmalı.")

slot_count = input(f"Yuva sayısını giriniz: ")
slot_count = int(slot_count) if slot_count.isdigit() else exit("Yuva sayısı sayısal değer olmalı.")

# Topların düştüğü yuvaları tutmak için bir liste oluşturuyoruz.
positions = []

# 1'den başlayıp ball_count'a kadar tüm topları işliyoruz.
for ball_number in range(1, ball_count + 1):
    # Topların girebileceği yuva sayısının en ortasını buluyoruz. (Piramit olacağı için bu şekilde)
    middle = (slot_count // 2) + 1 if slot_count % 2 == 1 else (slot_count / 2) + 0.5
    # Slot sayısından 1 az kadar döngüye giriyoruz her döngüde rastgele bir yöne doğru hareket ediyoruz.
    for slot_number in range(1, slot_count):
        move = random.choice([-0.5, 0.5]) # -0.5 sola, 0.5 sağa hareket ediyor.
        middle += move
        if move == 0.5:
            print(f"Top {ball_number} sağa gitti.")
        else:
            print(f"Top {ball_number} sola gitti.")
    print(f"Top {ball_number} {int(middle)} numaralı yuvaya düştü.\n")
    positions.append(middle)

# Topların düştüğü yuvaları sayıyoruz.
for slot_number in range(1, slot_count + 1):
    count = positions.count(slot_number)
    print(f"{slot_number} numaralı yuvaya {count} top düştü.")