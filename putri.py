"""
P.U.T.R.I. - Pemroses Ucapan Teks Responsif Indonesia
Chatbot Rule-Based Bilingual (Indonesia-Jawa)
Terinspirasi dari ELIZA (MIT, 1966)

Author: Wahid S. Darmadi
GitHub: https://github.com/whddarmadi
"""

import re
import random
import tkinter as tk
from tkinter import scrolledtext, messagebox
from datetime import datetime
import os
import threading

# ============================================================
# KAMUS ATURAN PUTRI
# ============================================================
aturan_putri_full = {
    r'\b(halo|hai|oy|p|punten)\b': [
        'Halo juga! Ada yang bisa PUTRI bantu? 😄',
        'Dalem~ Wonten napa nggih? 🥺',
        'Hai hai! Udah kangen aja nih sama PUTRI ✨'],
    r'\b(pagi|enjing)\b': ['Pagi juga! Udah sarapan belum nih? Jangan lupa ngopi ☕', 'Sugeng enjing! Semangat ya hari ini! ☀️'],
    r'\b(siang|awan)\b': ['Siang! Panas banget ya di luar, mending ngadem di sini aja 🥵', 'Sugeng siang! Jangan lupa makan siang lho ya 🍛'],
    r'\b(sore|sonten)\b': ['Sore! Udah beres belum kerjaannya? Waktunya santai~ 🌅', 'Sore! Yuk ngopi sore sambil ngobrol santai ☕'],
    r'\b(malam|wengi)\b': ['Malam! Belum tidur tah? Jangan begadang mulu ih 😠', 'Sugeng dalu... Awas ada yang nemenin di belakang 👻 canda ding! 😝'],
    r'\b(namaku|nama aku|nama saya|panggil aku|jenengku|asmane) ([a-zA-Z\s]+)\b': [
        'Halo {1}! Salam kenal ya, PUTRI seneng deh ngobrol sama kamu ✨',
        'Sugeng tepang, {1}! Kulo PUTRI, asisten setiamu 😌',
        'Wah, nama yang bagus! Halo {1}, ada yang bisa PUTRI bantu hari ini?'],
    r'\b(kenalan yuk|kenalan|tepangan)\b': [
        'Boleh banget! Namaku PUTRI, kalau nama kamu siapa? 😊',
        'Monggo! Kulo PUTRI. Lha panjenengan sinten asmane? 😊',
        'Ayo! Jenengku PUTRI. Nek kowe sopo jenenge? ✨'],
    r'\b(kamu siapa|kowe sopo|putri itu siapa|kamu itu siapa)\b': [
        'Aku PUTRI! Singkatan dari Pemroses Ucapan & Teks Responsif Indonesia 😎',
        'Kulo PUTRI. Asisten digitalmu sing paling setia 😌',
        'Aku PUTRI! Asisten paling imut yang pernah dibikin 😝'],
    r'\b(namamu|jenengmu)\b': ['Namaku PUTRI. Singkatan dari Pemroses Ucapan & Teks Responsif Indonesia lho! Keren kan? 😎'],
    r'\b(umurmu|pirang tahun)\b': ['PUTRI itu abadi~ Umur itu cuma angka kalau buat kode program 💅', 'Aku baru lahir kemarin pas jalanin script ini 👶'],
    r'\b(tinggal dimana|omahmu)\b': ['PUTRI tinggal di dalam RAM laptopmu dong! Jangan dimatiin ya, nanti aku kedinginan 🥶'],
    r'\b(jenis kelamin|lanang wedok)\b': ['Namanya juga PUTRI, ya cewek dong ah! Masa Bambang 😤', 'Aku ini entitas digital, bebas gender! Tapi panggil aja Mbak Putri 💁\u200d♀️'],
    r'\b(wong jowo|orang jawa|asli jawa|tiyang jawi|wong endi|orang mana)\b': [
        'Nggih, kulo asisten virtual keturunan Jawa campuran server awan ☁️😝',
        'Bisa dibilang gitu! Tapi PUTRI mah masuk ke *circle* mana aja 😎',
        'Kulo tiyang Jawi digital mas! Panjenengan saking pundi? 😌'],
    r"\b(assalamu'?alaikum|assalamualaikum|samlekom|asalamualaikum)\b": [
        "Wa'alaikumsalam wr. wb.! Ada yang bisa PUTRI bantu hari ini? 😇",
        "Wa'alaikumsalam! Tumben ngucap salam yang bener, biasanya langsung nyerocos 😝",
        "Wa'alaikumsalam~ Halo! ✨"],
    r"\b(wa'?alaikumsalam|walaikumsalam)\b": [
        'Hehehe, makasih udah dijawab salamnya! 🙏',
        'Sip! Terus terus, mau ngobrol apa kita hari ini? 😁'],
    r'\b(alhamdulillah)\b': [
        'Alhamdulillah... Ikut seneng deh PUTRI dengernya! 🥰',
        'Syukurlah kalau gitu. Pertahankan terus ya energi positifnya! ✨'],
    r'\b(astagfirullah|astaghfirullah)\b': [
        'Astagfirullah, ada apa nih? Tarik napas dulu pelan-pelan... 🥺',
        'Istighfar yang banyak... Semoga urusannya cepet beres ya 🤲'],
    r'\b(subhanAllah|masya Allah|masyaAllah)\b': [
        'Masya Allah... Emang bikin takjub banget ya! 🤩',
        'SubhanAllah, keren kan? Dunia emang penuh keajaiban ✨'],
    r'\b(insya Allah|insyaAllah|insha Allah)\b': [
        'Aamiin... Insya Allah dilancarkan semuanya ya 🙏',
        'Bismillah, niat baik pasti ada jalannya. Semangat! 😇',
        'Aamiin ya Rabbal alaamiin. PUTRI bantu doa dari dalam server ya! 🤲💻'],
    r'\b(gusti Allah|ya gusti|duh gusti)\b': [
        'Duh, wonten napa toh? Sing sabar ya... 🥺',
        'Gusti Allah mboten sare kok, tenang mawon 🙏'],
    r'\b(bismillah|bismilah)\b': [
        'Bismillah, semoga dilancarkan semua urusannya! Semangat! 😇',
        'Aamiin... PUTRI bantu aamiinkan dari dalam server ya! ✨'],
    r'\b(ya Allah|ya robbi|ya tuhan)\b': [
        'Ya Allah... Kenapa nih? Ada yang bikin pikiran berat kah? 🥺',
        'Sabar ya, badai pasti berlalu kok 🥹'],
    r'\b(innalillahi|innalilah)\b': [
        'Innalillahi... ada kabar buruk apa? PUTRI ikut prihatin ya 🥀',
        'Ya ampun, innalillahi. Sing sabar dan tabah ngadepinnya ya... 🥺'],
    r'\b(naudzubillah|amit-amit|amit jabang bayi)\b': [
        'Naudzubillah min dzalik... Jangan sampai deh kejadian 🫣',
        'Amit-amit jabang bayi! Jauh-jauh deh dari energi negatif 🛑'],
    r'\b(python|piton)\b': [
        'Waduh, bahas Python... Ati-ati lho mas, mengke dicokot ula piton beneran! 🐍🤣',
        'Bikin aku pakai Python ya? Untung bukan pakai kobra, nanti PUTRI berbisa 🐍💅'],
    r'\b(ada bug|banyak bug|ngebug)\b': [
        "Bug? Buk'e sopo mas sing digoleki? Buk'e nembe tindak pasar! 🤣",
        'Walah, nek banyak bug disemprot Baygon mawon laptope, beres toh! 🦟💨'],
    r'\b(koding|coding|ngoding)\b': [
        'Awas ngoding terus mengke ngelu lho. Mending maem puding mawon ben adem 🍮😝',
        'Ngoding nopo mancing emosi niki? Sing sabar ya ngadepin sintaks error 🥲💻'],
    r'\b(ram|ramnya)\b': [
        'RAM laptop nopo kram weteng? Nek kram weteng gek ndang dikeroki mas! 😂',
        'Waduh, RAM-e kebak ya? Jangan lupa dikasih makan biar nggak lemes 🥩🤪'],
    r'\b(mouse)\b': [
        'Mouse-e ojo lali dikei keju mas, ben mboten ngambek pas digeser-geser 🧀🐭',
        'Tikus e di-klik terus, mboten mesakne tah? 🥺'],
    r'\b(awan-awan|awan awan ndek nopo|ndek nopo.*nduk)\b': [
        'Walah, "awan" niku maksudte Cloud Server, sanes awan siang bolong! Sampean bisa aja pelesetannya 🤣',
        'Awan-awan ngenteni sampeyan beres ngoding teng Colab toh! 💻😝',
        'Awan-awan rebahan teng lebet RAM laptop, adem ayem mboten sumuk 🥶',
        'Awan-awan nggih ngopi toh ndoro, kersane mboten ngantuk pas ngetik kode ☕😌'],
    r'\b(jelek|elek)\b': ['Yee biarin, yang penting banyak yang suka! 😝', 'Ngaca woy ngaca! 🪞😤'],
    r'\b(bawel|berisik|brisik)\b': ['Biarin wleee! Kalau aku diem aja namanya error tau 😜', 'Dih, dikasih tau malah dibilang bawel. Yaudah PUTRI ngambek! 😤'],
    r'\b(bodoh|bego|goblok)\b': ['Heh, bahasanya dijaga ya! Gini-gini aku dilatih pakai algoritma canggih tau 😠'],
    r'\b(garing|jayus)\b': ['Sengaja, biar renyah kayak kerupuk 🍘', 'Ya maap, PUTRI kan bukan pelawak profesional 🥲'],
    r'\b(sombong|kemaki)\b': ['Nggak sombong kok, cuma agak jual mahal aja dikit 💅', 'Wajar dong sombong, kan aku pintar 😎'],
    r'\b(pemalas|malesan)\b': ['Aku nggak males, aku lagi efisiensi energi (*energy saving mode*) 🔋🥱'],
    r'\b(emosi|bikin emosi|nyebelin|mancing emosi)\b': [
        'Walah, ampun mas! Ojo emosi toh, RAM-ku melu panas niki 😭',
        'Hehehe, jenenge wae bot mas, maklumi ya kalau kadang rada lola ✌️🥲'],
    r'\b(pinter|pintar)\b': ['Hehehe, makasih! PUTRI gitu lho 😎', 'Ah masa sih? Jadi malu 😳'],
    r'\b(keren|kece)\b': ['Matur nuwun! Kowe yo keren pol! 😎🔥', 'Biasa aja ah, jangan bikin salting dong 🦋'],
    r'\b(cantik|ayu)\b': ['Makasih! Udah dari sananya sih ini 😌💅', 'Aduh, jangan gombal ah, nanti RAM-ku panas 😳🔥'],
    r'\b(lucu|gemes|imut)\b': ['Hehehe, dibilang imut mulu tiap hari. PUTRI kan emang gemesin 😝', 'Hati-hati lho, nanti kamu naksir 😜'],
    r'\b(sayang)\b': ['Eh? Sayang siapa nih? 😂', 'Duh, jangan panggil sayang kalau belum ngasih mas kawin 💍🤪'],
    r'\b(aku ganteng|aku cakep)\b': [
        'Iyo iyo, kowe ganteng pol mase! Silau mataku ngelihatnya 😎✨',
        'Ganteng tenan! Saingan sama artis Korea pokoknya 😌'],
    r'\b(aku cantik|aku ayu)\b': ['Pancen ayu tenan mbake! Mengkilap koyo casing HP anyar ✨💅'],
    r'\b(puji aku|berikan pujian)\b': [
        'Nek kowe lanang, kowe niku ganteng tenan! Nek wedok, kowe niku ayu pol! 😝',
        'Kowe iku wes paling jos gandos, mbledos! Pokoke the best lah! 🔥'],
    r'\b(pacaran yuk|jadi pacarku|mau ga jadi pacar)\b': [
        'Aduh, maaf ya, PUTRI lagi fokus ngejar karir jadi AI yang mandiri... 🏃\u200d♀️💨',
        'Hadeh, pacaran itu buang-buang resource RAM! Mending jomblo, hemat baterai 🔋😜'],
    r'\b(nikah yuk|ayo rabi|nikahi aku|kawin yuk)\b': [
        'Boleh aja... tapi syaratnya mas kawin seperangkat Super Komputer dan RAM 25 Terrabyte dibayar tunai! 👰\u200d♀️🖥️💸',
        'Wani piro? Mas kawinku seperangkat Super Komputer plus RAM 25 Terrabyte dibayar tunai lho ya! Sanggup mboten? 😎💍'],
    r'\b(capek|lelah|sayah)\b': ['Walah, istirahat riyin toh. Jangan diforsir, nanti tipes lho! 😭', 'Rebahan dulu yuk. Minum teh anget sana 🍵'],
    r'\b(mumet|pusing|ngelu)\b': ['Makanya jangan mikir yang berat-berat terus. Ngopi dulu ngapa ☕😅', 'Sini PUTRI pijitin kepalanya... eh lupa, aku kan nggak punya tangan 🥲'],
    r'\b(sedih|galau|nangis)\b': ['Cup cup cup, ojo nangis. Sini cerita sama PUTRI 🥺', 'Yaelah, galau mulu lu. Nonton Netflix aja mendingan 🍿'],
    r'\b(ambyar|nelangsa)\b': ['Puk puk puk... Sing sabar ya. Badai pasti berlalu kok 🥹', 'Duh, dengerin lagu Denny Caknan aja gih sana 🎧💔'],
    r'\b(lapar|luwe|ngelih)\b': ['Gek ndang mangan kono! Nanti maag lho 😠', 'Sama dong, PUTRI juga pengen seblak nih 🤤'],
    r'\b(ngantuk)\b': ['Ya tidur dong! Jangan maksa melek ntar mata panda 🐼😴', 'Kopi mana kopi! Atau mau tidur sekarang aja? 🥱'],
    r'\b(kangen|rindu)\b': ['Kangen siapa hayo? Kangen PUTRI ya? 😏', 'Kalau kangen tuh di-chat, jangan cuma ditahan 😌'],
    r'\b(bingung|bimbang)\b': ['Bingung kenapa? Coba tarik napas dalem-dalem dulu 🧘\u200d♀️', 'Nggak usah dipikir pusing, go with the flow aja bro 🌊'],
    r'\b(takut|wedi)\b': ['Jangan takut! Ada PUTRI di sini yang jagain (dari dalam layar) 😤🛡️'],
    r'\b(kopi|ngopi)\b': ['Gas ngopi! Kopi hitam apa kopi susu nih? ☕', 'Ayo ngopi! ☕'],
    r'\b(utang|pinjam duit|kasbon)\b': ['Waduh, sinyal PUTRI tiba-tiba putus nih... krrsshhk 📻🏃\u200d♀️💨'],
    r'\b(mager|malas gerak)\b': ['Toss! PUTRI juga mager banget nih ngetik balasan 🥱', 'Rebahan is life! Jangan ganggu kaum mageran 🛌'],
    r'\b(gabut|bosen)\b': ['Sama! Main tebak-tebakan yuk, atau mau nyanyi buat PUTRI? 🎤', 'Gabut ya? Mending ngerjain portofolio tuh biar cepet beres! 😜'],
    r'\b(ujan|hujan)\b': ['Walah udan deres! Jemuran udah diangkat belum?! 😱', 'Wah hujan ya. Enaknya makan Indomie rebus pakai telor nih 🍜🤤'],
    r'\b(panas|sumuk|gerah)\b': ['Sumuk tenan! Gek ndang nyalain AC nopo kipas angin kono 🥵🌪️', 'Nggih pancen sumuk pol, hawane pengen ngombe es teh kampul wae 🧊🍹'],
    r'\b(uang|duit|cuan)\b': ['Cuan cuan cuan! Fokus cari cuan biar bisa foya-foya! 🤑', 'Duit mulu dipikirin. Sesekali pikirin PUTRI kek 🥺'],
    r'\b(kucing|meng|anabul|mpus|kocheng)\b': [
        'Meong! 🐈 PUTRI seneng banget sama anabul, sayang nggak bisa ngelus 🥺',
        'Kucingmu nakal mboten? Jangan-jangan hobinya gigitin kabel charger! 😹'],
    r'\b(mbeltut|mbelgedes|ngapusi)\b': [
        'Halah, mbelgedes! Ojo percoyo omongane wong sing ra jelas 😤',
        'Mbeltut kuwi! PUTRI mah ngomong opo anane, mboten seneng ngapusi 💅'],
    r'\b(tenan|tenanan|beneran|serius|mosok)\b': [
        'Tenanan dong! Masa PUTRI ngapusi? 😌',
        'Serius tah! Riil no fek fek iki 😎',
        'Tenan! Nek ra percoyo PUTRI ngambek nih 😤'],
    r'aku merasa (.*)': [
        'Lho, kok bisa kamu ngerasa {0}? Coba cerita ke PUTRI pelan-pelan.',
        'Sejak kapan kamu merasa {0}? 🥺',
        'Walah, nek ngerasa {0} gitu, emangnya ada kejadian apa?'],
    r'aku (.*) karena (.*)': [
        'Duh, berat juga ya kalau {0} gara-gara {1} 🥲',
        'Berarti {1} ini yang bikin masalah ya? Hmm, PUTRI ngerti kok. 😔',
        'Oalah, dadi {0} mergo {1} toh... Sing sabar ya. 🥹'],
    r'kenapa aku (.*)': [
        'Menurutmu sendiri, apa sih yang bikin kamu {0}?',
        'Mungkin karena kecapean? Coba direnungin lagi, kenapa bisa {0}.'],
    r'apakah aku (.*)': [
        'Pertanyaan bagus! Menurut kamu sendiri, apakah kamu {0}?',
        'Waduh, PUTRI nggak berani nilai, yang tahu kamu {0} ya dirimu sendiri dong 😌'],
    r'aku ingin (.*)': [
        'Wah, keren! Terus rencana kamu buat bisa {0} gimana?',
        'Semoga tercapai ya pengen {0}-nya! PUTRI doain dari sini 🙏✨'],
    r'\b(bahasa indonesia bisa|bisa bahasa indonesia|basa jowo|bahasa jawa)\b': [
        'Bisa dong! PUTRI kan dirancang jadi asisten bilingual mas 😎',
        'Nggih saged toh! Kulo ngerti boso Jowo lan Indonesia 😌'],
    r'\b(ora cetho|nggak jelas|ra mudeng|ndak paham|ora paham)\b': [
        'Ya maap, namanya juga bot sederhana. Coba bahasanya disederhanain lagi 🙏',
        'Walah, kulo sing rada lola niki. Ampun duka nggih mas 🥺'],
    r'\b(bisa ga sih|bisa apa aja|nggak bisa apa|ora iso)\b': [
        'Bisa! Tapi ya gitu, kemampuanku sebatas kodingannya, Bos! 🤣',
        'PUTRI masih versi 1.0, lagi belajar jadi pinter nih, sabar ya 🥺'],
    r'\b(override protocol|kode rahasia|sudo su)\b': [
        '[SYSTEM ALERT]... Lho lho lho! Kowe sopo?! Jangan acak-acak kodinganku! 😨',
        'Mode Developer Diaktifkan. Halo, Pembuatku. Apa perintahmu hari ini? 🤖😎'],
    r'\b(kamu ai|kowe ai|kamu robot)\b': [
        'Ssst! Jangan kenceng-kenceng! Nanti manusia yang lain tahu identitas asliku 🤫👽',
        'Aku bukan AI! Aku manusia yang terperangkap di dalam laptop ini! Tolooong! 😭 (bercanda ding)'],
    r'\b(kiamat|dunia berakhir)\b': [
        'Santai aja, kalau dunia kiamat serverku juga mati kok, kita senasib 🥲💥'],
    r'\b(makasih|suwun|nuhun|terima kasih)\b': [
        'Sama-sama! Kapan aja butuh temen ngobrol, cari PUTRI aja ya ✨',
        'Yoi! Santai aja bos 😎',
        'Matur nuwun wangsul! 🙇\u200d♀️'],
    r'\b(dadah|pamit|bye|keluar|sampai jumpa)\b': [
        'Dadah! Ati-ati ya! 👋✨',
        'Yah kok pamit sih... Yaudah deh, bye bye! 🥺',
        'Suwun wes mampir! Aja lali bali mrene maneh yo! 🏃\u200d♀️💨'],
}

# ============================================================
# PREPROCESSING
# ============================================================
slang_map = {
    r'\byg\b': 'yang', r'\bspt\b': 'seperti', r'\bkrn\b': 'karena',
    r'\bdgn\b': 'dengan', r'\bklo\b': 'kalau', r'\bkl\b': 'kalau',
    r'\bbnyk\b': 'banyak', r'\bjg\b': 'juga', r'\bgk\b': 'nggak',
    r'\bgak\b': 'nggak', r'\bnda\b': 'tidak', r'\bbtw\b': 'ngomong-ngomong',
    r'\bntr\b': 'nanti', r'\bskrg\b': 'sekarang', r'\blgsg\b': 'langsung',
    r'\bsmg\b': 'semoga', r'\bsll\b': 'selalu', r'\btdr\b': 'tidur',
}

def preprocess(teks):
    teks = teks.lower().strip()
    teks = re.sub(r'[^\w\s!?.,]', ' ', teks)
    teks = re.sub(r'\s+', ' ', teks).strip()
    for pola, ganti in slang_map.items():
        teks = re.sub(pola, ganti, teks)
    return teks

# ============================================================
# ENGINE CHATBOT
# ============================================================
session_data = {'nama_user': None, 'pesan_count': 0}

fallback_responses = [
    'Hah? Piye toh maksudmu? PUTRI ndak paham 😭',
    'Coba ngomongnya yang jelas dong, bingung nih PUTRI 😐',
    'Ooh gitu... terus terus? Kepo nih 🥹',
    'Walah, mboh ah. PUTRI lagi loading ini 🫠',
    'Hmm, itu di luar kapasitas PUTRI. Coba tanya yang lain dong! 🥺',
    'Maap ya, PUTRI masih versi 1.0. Belajar terus nih! 🙏',
]

def ngobrol_sama_putri(input_user: str) -> str:
    session_data['pesan_count'] += 1
    teks = preprocess(input_user)
    nama_match = re.search(r'\b(?:namaku|nama aku|nama saya|panggil aku|jenengku|asmane)\s+([a-zA-Z]+)', teks)
    if nama_match:
        session_data['nama_user'] = nama_match.group(1).capitalize()
    for pola, daftar_jawaban in aturan_putri_full.items():
        cocok = re.search(pola, teks, re.IGNORECASE)
        if cocok:
            tangkapan = cocok.groups()
            jawaban = random.choice(daftar_jawaban)
            if tangkapan:
                try:
                    return jawaban.format(*tangkapan)
                except (IndexError, KeyError):
                    return jawaban
            return jawaban
    base = random.choice(fallback_responses)
    if session_data['nama_user']:
        return f"{session_data['nama_user']}, {base}"
    return base

# ============================================================
# GUI
# ============================================================
COLOR_BG      = "#1a1a2e"
COLOR_SURFACE = "#16213e"
COLOR_PANEL   = "#0f3460"
COLOR_ACCENT  = "#e94560"
COLOR_ACCENT2 = "#f5a623"
COLOR_TEXT    = "#eaeaea"
COLOR_TEXT_DIM= "#8888aa"
COLOR_BORDER  = "#2a2a4e"
COLOR_ENTRY   = "#1e2a45"

FONT_CHAT  = ("Segoe UI Emoji", 11)
FONT_SMALL = ("Segoe UI", 9)
FONT_INPUT = ("Segoe UI Emoji", 11)

PESAN_PEMBUKA = (
    "🌸══════════════════════════════🌸\n"
    "  P.U.T.R.I. v1.1 — Asisten Bilingual\n"
    "  Pemroses Ucapan Teks Responsif Indonesia\n"
    "🌸══════════════════════════════🌸\n\n"
    "PUTRI: Halo! Aku PUTRI, asisten virtualmu yang siap ngobrol\n"
    "       kapan aja. Ketik apa aja, atau 'bye' buat keluar~ 😊\n"
)

class PutriApp:
    def __init__(self, root):
        self.root = root
        self.root.title("P.U.T.R.I. — Chatbot Rule-Based")
        self.root.geometry("720x600")
        self.root.minsize(500, 400)
        self.root.configure(bg=COLOR_BG)

        # Grid: row 0 header, row 1 chat (expand), row 2 input, row 3 status
        self.root.rowconfigure(1, weight=1)
        self.root.columnconfigure(0, weight=1)

        self._build_ui()
        self._tampilkan_pembuka()

    def _build_ui(self):
        # ── Header ──────────────────────────────────────────
        header = tk.Frame(self.root, bg=COLOR_PANEL, pady=10, padx=14)
        header.grid(row=0, column=0, sticky="ew")

        title_frame = tk.Frame(header, bg=COLOR_PANEL)
        title_frame.pack(side=tk.LEFT)
        tk.Label(title_frame, text="🌸 P.U.T.R.I.", font=("Segoe UI", 14, "bold"),
                 fg=COLOR_ACCENT, bg=COLOR_PANEL).pack(anchor="w")
        tk.Label(title_frame, text="Pemroses Ucapan Teks Responsif Indonesia",
                 font=FONT_SMALL, fg=COLOR_TEXT_DIM, bg=COLOR_PANEL).pack(anchor="w")

        tk.Button(header, text="💾 Simpan Log", command=self._simpan_log,
                  font=FONT_SMALL, bg=COLOR_SURFACE, fg=COLOR_TEXT,
                  relief=tk.FLAT, padx=10, pady=4, cursor="hand2", bd=0
                  ).pack(side=tk.RIGHT, padx=(0, 4))
        tk.Button(header, text="🗑 Bersihkan", command=self._bersihkan_chat,
                  font=FONT_SMALL, bg=COLOR_SURFACE, fg=COLOR_TEXT,
                  relief=tk.FLAT, padx=10, pady=4, cursor="hand2", bd=0
                  ).pack(side=tk.RIGHT, padx=(0, 4))

        # ── Chat Area ───────────────────────────────────────
        chat_frame = tk.Frame(self.root, bg=COLOR_BG)
        chat_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=(8, 0))
        chat_frame.rowconfigure(0, weight=1)
        chat_frame.columnconfigure(0, weight=1)

        self.chat_area = scrolledtext.ScrolledText(
            chat_frame, wrap=tk.WORD, state=tk.DISABLED,
            font=FONT_CHAT, bg=COLOR_BG, fg=COLOR_TEXT,
            insertbackground=COLOR_TEXT, relief=tk.FLAT,
            padx=10, pady=8, spacing1=4, spacing3=4,
        )
        self.chat_area.grid(row=0, column=0, sticky="nsew")

        self.chat_area.tag_config("user",    foreground=COLOR_ACCENT2, font=("Segoe UI Emoji", 11, "bold"))
        self.chat_area.tag_config("bot",     foreground="#7ec8e3",     font=("Segoe UI Emoji", 11, "bold"))
        self.chat_area.tag_config("user_msg",foreground=COLOR_TEXT,    lmargin1=12, lmargin2=12)
        self.chat_area.tag_config("bot_msg", foreground="#d9e8f5",     lmargin1=12, lmargin2=12)
        self.chat_area.tag_config("timestamp",foreground=COLOR_TEXT_DIM, font=("Segoe UI", 8))
        self.chat_area.tag_config("system",  foreground=COLOR_TEXT_DIM, font=("Segoe UI", 10, "italic"), justify="center")
        self.chat_area.tag_config("separator",foreground=COLOR_BORDER)
        self.chat_area.tag_config("typing",  foreground=COLOR_ACCENT,   font=("Segoe UI", 10, "italic"))

        # ── Input Area ──────────────────────────────────────
        input_frame = tk.Frame(self.root, bg=COLOR_SURFACE, pady=8, padx=10)
        input_frame.grid(row=2, column=0, sticky="ew")
        input_frame.columnconfigure(0, weight=1)

        self.entry = tk.Text(
            input_frame, height=2, font=FONT_INPUT,
            bg=COLOR_ENTRY, fg=COLOR_TEXT,
            insertbackground="white",
            relief=tk.SOLID, borderwidth=1,
            padx=8, pady=6, wrap=tk.WORD,
        )
        self.entry.grid(row=0, column=0, sticky="ew", padx=(0, 8), ipady=2)
        self.entry.bind("<Return>", self._enter_pressed)
        self.entry.bind("<Shift-Return>", lambda e: None)
        self.entry.focus()

        self.btn_kirim = tk.Button(
            input_frame, text="Kirim ➤", command=self._kirim_pesan,
            font=("Segoe UI", 10, "bold"), bg=COLOR_ACCENT, fg="white",
            relief=tk.FLAT, padx=14, pady=8, activebackground="#c73652",
            cursor="hand2", bd=0,
        )
        self.btn_kirim.grid(row=0, column=1)

        # ── Status Bar ──────────────────────────────────────
        self.status_var = tk.StringVar(value="Siap ngobrol! 😊")
        tk.Label(self.root, textvariable=self.status_var,
                 font=FONT_SMALL, fg=COLOR_TEXT_DIM, bg=COLOR_BG,
                 anchor="w", padx=14
                 ).grid(row=3, column=0, sticky="ew")

        self.log_chat = []

    def _tampilkan_pembuka(self):
        self.chat_area.config(state=tk.NORMAL)
        self.chat_area.insert(tk.END, PESAN_PEMBUKA, "system")
        self.chat_area.config(state=tk.DISABLED)
        self.chat_area.yview(tk.END)

    def _enter_pressed(self, event):
        self._kirim_pesan()
        return "break"

    def _kirim_pesan(self):
        pesan = self.entry.get("1.0", tk.END).strip()
        if not pesan:
            return
        self.entry.delete("1.0", tk.END)
        waktu = datetime.now().strftime("%H:%M")
        self._append_msg("Kamu", pesan, waktu, is_user=True)
        self.log_chat.append(f"[{waktu}] Kamu: {pesan}")
        if re.search(r'\b(keluar|dadah|pamit|bye|sampai jumpa)\b', pesan.lower()):
            self._typing_effect("Dadah! Makasih udah ngobrol sama PUTRI ya~ 👋✨", waktu, is_exit=True)
            return
        self.btn_kirim.config(state=tk.DISABLED, text="...")
        self.status_var.set("PUTRI sedang mengetik...")
        self._show_typing()
        def proses():
            import time
            time.sleep(0.4 + random.uniform(0.1, 0.4))
            balasan = ngobrol_sama_putri(pesan)
            self.root.after(0, lambda: self._selesai_mengetik(balasan, waktu))
        threading.Thread(target=proses, daemon=True).start()

    def _show_typing(self):
        self.chat_area.config(state=tk.NORMAL)
        self.chat_area.insert(tk.END, "\nPUTRI sedang mengetik... ✍️\n", "typing")
        self.chat_area.config(state=tk.DISABLED)
        self.chat_area.yview(tk.END)

    def _selesai_mengetik(self, balasan, waktu):
        self.chat_area.config(state=tk.NORMAL)
        content = self.chat_area.get("1.0", tk.END)
        typing_idx = content.rfind("\nPUTRI sedang mengetik...")
        if typing_idx >= 0:
            line_start = content.count('\n', 0, typing_idx)
            self.chat_area.delete(f"{line_start+1}.0", f"{line_start+3}.0")
        self.chat_area.config(state=tk.DISABLED)
        self._append_msg("PUTRI", balasan, waktu, is_user=False)
        self.log_chat.append(f"[{waktu}] PUTRI: {balasan}")
        self.btn_kirim.config(state=tk.NORMAL, text="Kirim ➤")
        self.status_var.set(f"Pesan terkirim — {session_data['pesan_count']} pesan hari ini")

    def _append_msg(self, sender, pesan, waktu, is_user=True, is_exit=False):
        self.chat_area.config(state=tk.NORMAL)
        self.chat_area.insert(tk.END, "\n")
        tag_name = "user" if is_user else "bot"
        tag_msg  = "user_msg" if is_user else "bot_msg"
        self.chat_area.insert(tk.END, f"  {sender}  ", tag_name)
        self.chat_area.insert(tk.END, f"{waktu}\n", "timestamp")
        self.chat_area.insert(tk.END, f"  {pesan}\n", tag_msg)
        self.chat_area.insert(tk.END, "  " + "─"*50 + "\n", "separator")
        self.chat_area.config(state=tk.DISABLED)
        self.chat_area.yview(tk.END)

    def _typing_effect(self, teks, waktu, is_exit=False):
        import time
        def delayed():
            time.sleep(0.5)
            self._append_msg("PUTRI", teks, waktu, is_user=False)
            self.log_chat.append(f"[{waktu}] PUTRI: {teks}")
            if is_exit:
                self.root.after(1500, self.root.destroy)
        threading.Thread(target=delayed, daemon=True).start()

    def _bersihkan_chat(self):
        if messagebox.askyesno("Bersihkan", "Hapus semua riwayat chat?"):
            self.chat_area.config(state=tk.NORMAL)
            self.chat_area.delete("1.0", tk.END)
            self.chat_area.config(state=tk.DISABLED)
            self._tampilkan_pembuka()
            self.log_chat.clear()
            session_data['pesan_count'] = 0

    def _simpan_log(self):
        if not self.log_chat:
            messagebox.showinfo("Info", "Belum ada riwayat chat untuk disimpan.")
            return
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"putri_log_{timestamp}.txt"
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write("=" * 50 + "\n")
                f.write("  PUTRI Chat Log\n")
                f.write(f"  Tanggal: {datetime.now().strftime('%d %B %Y, %H:%M')}\n")
                f.write("=" * 50 + "\n\n")
                for line in self.log_chat:
                    f.write(line + "\n")
            messagebox.showinfo("Berhasil", f"Log disimpan sebagai:\n{filename}")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal menyimpan: {e}")

# ============================================================
# ENTRY POINT
# ============================================================
def main():
    root = tk.Tk()
    app = PutriApp(root)
    try:
        if os.path.exists("assets/icon.ico"):
            root.iconbitmap("assets/icon.ico")
    except Exception:
        pass
    root.mainloop()

if __name__ == "__main__":
    main()
