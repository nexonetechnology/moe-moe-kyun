import os
from gtts import gTTS

phrases = {
    # # 1. Welcome / Greetings
    # "01_okaeri": "おかえり！",
    # "02_okaerinasai": "お帰りなさい！",
    # # 2. Customer Titles
    # "03_goshujinsama": "ご主人様！",
    # "04_ojousama": "お嬢様！",
    # # 3. Waiting
    # "05_chotto_matte_kudasai": "ちょっと待ってください！",
    # "06_shoushou_omachi_kudasai": "少々お待ちください。",
    # # 4. Table Service & Chants
    # "07_seno": "せーの！",
    # "08_oishiku_naare_moe_moe_kyun": "美味しくなーれ、萌え萌えキュン！",
    # "09_seno_oishiku_naare_moe_moe_kyun": "せーの、美味しくなーれ、萌え萌えキュン！",
    # "10_douzo": "どうぞ！",
    # # 5. Gratitude
    # "11_arigatou": "ありがとう！",
    # "12_arigatou_gozaimasu": "ありがとうございます！",
    # # 6. Farewell / Departure
    # "13_itterasshai": "行ってらっしゃい！",
    # "14_itterasshaimase": "行ってらっしゃいませ！",
    # "15_okaerinasaimase": "お帰りなさいませ！",
    "16_janken_pon": "じゃんけん、ぽん！",
    "17_acchi_muite_hoi": "あっち向いてホイ！"
}

output_dir = "maid_cafe_audio"
os.makedirs(output_dir, exist_ok=True)

for filename, text in phrases.items():
    tts = gTTS(text=text, lang="ja")
    path = os.path.join(output_dir, f"{filename}.mp3")
    tts.save(path)
    print(f"Downloaded Google TTS audio: {path}")