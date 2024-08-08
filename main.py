meme_dict = {
                "CRINGE": "Garip ya da utandırıcı bir şey",
                "LOL": "Komik bir şeye verilen cevap",
                "TROLL":"Şaka yapanlara veya yapılana denir. - İronik",
                "FAKE":"Sahte",
                "CREEPY":"If you say that something or someone is creepy, you mean they make you feel very nervous or frightened."
                }

while True:
    word = input("Anlamadığınız bir kelime yazınız:")
    if word in meme_dict.keys():
        print("Girdiğiniz kelimenin anlamı:", meme_dict [word])
    else:
        print("Maalesef ne olduğunu bilmiyorum. Tekrar deneyin (tüm büyük harflerle girin!).")
