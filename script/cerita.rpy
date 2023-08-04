##image scene
image bg_kantin = "images/kantin.jpg"
image bg_kelas = "images/kelas.jpg"
image bg_koridor = "images/koridor.png"
image bg_kelas_gelap = "images/kelas (2).jpg"
image bg_tamat = "images/True Ending.png"
##Image Character
image Ziki:
    "images/ziki.png"
    zoom 0.7
image Ziki_senang:
    "images/ziki_senang.png"
    zoom 0.7
image Ziki_kaget:
    "images/ziki_kaget.png"
    zoom 0.7
image Sukma:
    "images/sukma.png"
    zoom 0.7
image Sukma_bingung:
    "images/sukma_bingung.png"
    zoom 0.7
image Sukma_senyum:
    "images/sukma_senyum2.png"
    zoom 0.7
image Sukma_bingung:
    "images/sukma_bingung.png"
    zoom 0.7
image Sukma_ketawa:
    "images/sukma_ketawa.png"
    zoom 0.7
image Rina:
    "images/Rina.png"
    zoom 0.7
image Rina_senyum:
    "images/rina_senyum.png"
    zoom 0.7
image Rina_kaget:
    "images/rina_kaget.png"
    zoom 0.7
image Rina_ketawa:
    "images/rina_ketawa.png"
    zoom 0.7
image Rina_senang:
    "images/rina_senang.png"
    zoom 0.7

image side rendi netral = im.Scale("rendi.png", 300, 300, xoffset=0, yoffset=0)
image side rendi senyum = im.Scale("rendi_senyum.png", 300, 300, xoffset=0, yoffset=0)
image side rendi senang = im.Scale("rendi_senang.png", 300, 300, xoffset=0, yoffset=0)
image side rendi ketawa = im.Scale("rendi_ketawa.png", 300, 300, xoffset=0, yoffset=0)
image side ziki netral = im.Scale("ziki.png", 300, 300, xoffset=0, yoffset=0)
image side ziki kaget = im.Scale("ziki_kaget.png",300,300, xoffset=0, yoffset=0)
image side sukma netral = im.Scale("sukma.png", 300, 300, xoffset=0, yoffset=0)
image side sukma senyum = im.Scale("sukma_senyum2.png", 300, 300, xoffset=0, yoffset=0)
image side sukma ketawa = im.Scale("sukma_ketawa.png", 300, 300, xoffset=0, yoffset=0)
image side sukma bingung = im.Scale("sukma_bingung.png", 300, 300, xoffset=0, yoffset=0)
image side rina netral = im.Scale("Rina.png", 300, 300, xoffset=0, yoffset=0)
image side rina senyum = im.Scale("rina_senyum.png", 300, 300, xoffset=0, yoffset=0)
image side rina kaget = im.Scale("rina_kaget.png", 300, 300, xoffset=0, yoffset=0)
image side rina ketawa = im.Scale("rina_ketawa.png", 300, 300, xoffset=0, yoffset=0)
image side rina senang = im.Scale("rina_senang.png", 300, 300, xoffset=0, yoffset=0)

define r = Character("Rendi", color="#eb4b28", image="rendi")
define z = Character("Ziki", color="#1A72D5", image="ziki")
define s = Character("Sukma", color="#270c66", image="sukma")
define ri = Character("Rina", color="#E513C8", image="rina")
define bareng = Character("Rendi, Rina, Sukma, dan Ziki", color="#5f1806")

label cerita1:
    scene bg_kelas
    with Fade(1,0,1)
    play music "audio/lagupengantar2.mp3"
    "Namaku Rendi."
    "Seorang mahasiswa baru di Jurusan Teknik Informatika di Universitas Teknologi Sinar Jaya."
    "Saat pertama kali aku menginjakkan kaki di kampus ini, perasaan campur aduk terasa di hatiku."
    "Semua ini terasa begitu menakutkan, namun juga menggembirakan."
    "Berbekal semangat dan keingintahuan yang besar, aku siap mengeksplorasi dunia ilmu komputer yang menanti di hadapanku."
    "Hari-hari pertamaku di kampus penuh dengan perjuangan, tetapi juga kegembiraan."
    "Aku bertemu dengan teman-teman sekelas yang sama-sama semangat dalam belajar."
    "Kami saling membantu dan mendukung satu sama lain."
    "Di antara sesi kuliah dan praktikum, kami menghabiskan waktu luang untuk eksperimen dan bermain-main dengan kode-kode lucu."
    "Suatu hari, kami mendapat tugas untuk membuat program sederhana menggunakan bahasa pemrograman Python."
    "Aku dan teman-temanku mulai berkumpul di kelas untuk memulai tugas kami."
    "Temanku, Rina, duduk di sebelahku dan menunjukkan kode lucu yang dia temukan di internet."
    show Rina_senyum
    ri senyum "Ren, coba lihat ini."
    ri senyum "Ternyata, jika kamu mencetak 'Hello World' sebanyak 10 kali, maka kamu bisa menyapa dunia dengan 'Hello World' berulang-ulang!"
    hide Rina_senyum
    "Kami tertawa terbahak-bahak melihat hasil keluaran dari kode kocak tersebut."
    "Namun, Rina tidak berhenti di situ. Dia juga menemukan kode untuk membuat program menggambar pola-pola aneh dan menghasilkan suara-suara lucu."
    "Setiap kali kami menemukan kode-kode unik, kami dengan riang membagikannya satu sama lain."
    stop music
    "Suatu malam, ketika kami tengah berada di kelas hampir tengah malam, kesenangan tak terduga datang."
    "Pada saat kami sedang asyik menyelesaikan tugas akhir semester." 
    scene bg_kelas_gelap
    with dissolve
    play sound "audio/lampu.mp3"
    "Tiba-tiba lampu di kelas mati dan membuat ruangan menjadi gelap gulita."
    show Ziki_kaget at center
    z kaget "Apa yang terjadi?"
    r netral "Kayaknya ada pemadaman listrik deh."
    show Rina_kaget at right
    ri kaget "Apa yang harus kita lakukan sekarang?"
    show Sukma_bingung at left
    s bingung "Duh, nampaknya kita tidak bisa melanjutkan pekerjaan kita tanpa listrik"
    hide Ziki_kaget
    hide Rina_kaget
    hide Sukma_bingung
    menu:
        r netral "{i}Apa yang harus aku lakukan?{/i}"
        "Ajak teman-temanmu untuk meneruskan bekerja tanpa listrik dan menyelesaikan tugas akhir semester dengan laptop yang tersisa.":
            jump lanjut1
        "Ajak teman-temanmu untuk bercerita seram dan membuat lelucon tentang 'hantu' yang menghantui kelas di malam hari.":
            jump lanjut2
        "Ajak Rina untuk membuat kode lucu yang bisa menciptakan suara-suara aneh dan melihat reaksi teman-teman saat mendengarkannya.":
            jump lanjut3
        "Keluar dari kelas dan mengadakan perjalanan ke kantin untuk menikmati makanan tengah malam bersama.":
            jump lanjut4
    return
    
    label lanjut1:
        "Aku teringat bahwa aku memiliki laptop dengan daya baterai cukup banyak."
        r senyum "Hei, guys, jangan khawatir! Kita masih punya laptop ini dengan daya baterai yang cukup untuk meneruskan pekerjaan."
        show Rina_senyum
        ri senyum "Rendi, kamu selalu menjadi penyelamat! Baguslah, setidaknya kami tidak harus kehilangan waktu untuk menunggu listrik kembali."
        show Ziki at left
        z netral "Kamu benar, Rendi! Kita harus menggunakan waktu yang ada dengan sebaik-baiknya. Sekarang, mari kita kembali ke tugas akhir kita!"
        show Sukma at right
        s netral "Tapi, tunggu dulu. Meskipun kita bisa meneruskan tugasnya, ruangan ini cukup gelap. Apa kita bisa mencari sumber cahaya tambahan?"
        play music "lagupengantar3.mp3"
        r netral "Oh ya, kamu benar, Ayu. Mari kita lihat apa yang bisa kita temukan."
        hide Rina_senyum
        hide Ziki
        hide Sukma
        "Sambil mengeluarkan ponsel dan menyalakannya untuk mencari sumber cahaya"
        show Ziki at left
        z netral "Lihat, di sini ada senter kecil di loker. Ayo gunakan itu untuk membantu penerangan."
        show Rina
        ri netral "Baik, sekarang kita punya cahaya tambahan!"
        show Sukma at right
        s senyum "Baiklah, mari kita kembali ke pekerjaan kita sekarang."
        stop music
        hide Rina
        hide Ziki
        hide Sukma
        play music "malam.mp3"
        "Kami pun mulai bekerja dengan semangat, menggunakan laptop dan cahaya senter untuk membantu kami melihat layar. Meskipun situasinya tidak biasa, kami tetap terus bekerja dengan penuh semangat."
        show Ziki at left
        z netral "Hey, teman-teman, mengapa kita tidak membuat kode lucu sebagai hiburan sambil menunggu program kita berjalan?"
        show Rina_senyum
        ri senyum "Kedengarannya menarik! Ayo buatlah sesuatu yang lucu."
        show Sukma at right
        s netral "Ide yang bagus Ziki. Kita bisa saling berbagi kode kocak yang pernah kita temukan."
        hide Rina_senyum
        hide Ziki
        hide Sukma
        stop music
        play music "laguromantis.mp3"
        "Kami pun mulai berbagi kode lucu satu sama lain, dan suasana kelas menjadi riang. Meskipun situasi kami tak biasa, kami tetap menikmati perjalanan kami dalam dunia kode-kode lucu."
        "Akhirnya, setelah berjam-jam bekerja, tugas akhir kami selesai. Meskipun ruangan masih gelap, semangat kami tidak surut. Kami saling memberikan pujian dan berterima kasih atas kerjasama yang baik."
        r senang "Terima kasih, teman-teman. Tanpa kalian, mungkin tugas ini tidak akan selesai dengan lancar"
        show Rina_senyum
        ri senyum "Tentu saja, Rendi. Kita tim yang hebat!"
        show Ziki at left
        z netral "Benar! Sekarang, mari kita tunggu sampai listrik kembali dan kita bisa mengumpulkan hasil tugas kita."
        show Sukma_senyum at right
        s senyum "Setuju! Semoga listrik cepat kembali."
        hide Rina_senyum
        hide Ziki
        hide Sukma_senyum
        "Kami pun menunggu dengan sabar hingga listrik kembali. Sambil menunggu, kami masih tertawa mengenang momen-momen lucu yang kami alami hari ini."
        "Akhirnya, listrik kembali menyala, dan kami pun bisa mengumpulkan hasil tugas kami. Kami merasa bangga dan bahagia karena berhasil menyelesaikan tugas akhir di situasi yang unik dan lucu"
        "Setelah itu, kami keluar dari kelas dengan senyum bahagia di wajah kami, siap menghadapi tantangan baru dalam dunia teknik informatika yang menunggu di depan kami."
        scene bg_tamat
        with Fade(1,0,1)
        stop music
        return

    label lanjut2:
        play music "lagupengantar2.mp3"
        "Rendi dan teman-temannya duduk di sekeliling meja di kelas yang gelap karena pemadaman listrik."
        r netral "Hei, kalian pernah dengar cerita tentang hantu yang katanya menghantui kelas ini di malam hari?"
        show Rina_kaget
        ri kaget "Serius, Rendi? itu kayaknya bukan ide yang bagus, bisa-bisa aku takut sendiri nanti."
        show Ziki at left
        z netral "Tapi di malam hari di sini memang agak seram sih, apalagi tanpa listrik seperti ini."
        r netral "Bagaimana kalau kita mencoba membuat lelucon tentang 'hantu' ini? Tentu saja, tanpa menyakiti perasaan orang lain."
        show Sukma_senyum at right
        s senyum "Ide bagus, Rendi! Kita bisa menakuti teman-teman yang lain dengan trik lucu."
        r senang "Aku punya ide. Bagaimana jika kita menyebarkan cerita palsu tentang hantu yang berada di salah satu ruang server? Kita bisa menggunakan suara-suara aneh yang Rina ciptakan tadi untuk menambah efeknya."
        show Rina
        ri netral "Oh, jadi aku akan menjadi hantunya itu, ya?"
        r netral "Iya! Dan Sukma, kamu bisa bertindak sebagai orang yang yang melihat hantu itu."
        show Sukma at right
        s netral "Hmm, bagus juga ide itu. Tapi pastikan tidak ada yang benar-benar ketakutan, ya!"
        z netral "Oke, mari kita mulai rencana ini. Kita bisa membagikan cerita palsu itu di grup mahasiswa Teknik Informatika dan biarkan rumor menyebar."
        show Rina_senyum
        ri senyum "Ayo mulai sesi rekaman suara hantunya sekarang juga!"
        "Mereka mulai merekam suara-suara aneh dengan gaya hantu dan tertawa bersama-sama."
        r senang "Kita sebaiknya menyebutnya 'Hantu Server'! Hehehe."
        show Sukma_senyum at right
        s senyum "Baiklah, mari kita bagikan rekaman ini dan lihat reaksi teman-teman kita!"
        hide Rina_kaget
        hide Rina_senyum
        hide Ziki
        hide Sukma_senyum
        hide Rina
        hide Sukma
        "Rekaman suara hantu server telah dibagikan bersama cerita palsu tentang hantu yang menghantui kelas di malam hari."
        "Kemudian dalam waktu singkat, banyak anggota grup ikut merespons dengan tawa dan lelucon sendiri tentang hantu server. Mereka menyadari bahwa itu hanya lelucon dan suasana seram di kelas berubah menjadi suasana riang."
        play music "laguromantis.mp3"
        r senang "Wah, sepertinya lelucon kita berhasil, guys!"
        show Sukma_senyum
        s senyum "Ternyata, membuat lelucon tentang hantu bisa menyatukan kita semua dalam tawa."
        show Rina_senyum at left
        ri senyum "Iya, senang rasanya bisa membuat suasana lebih ceria di malam yang gelap ini."
        show Ziki_senang
        z senang "Siapa sangka kita bisa mengubah kelas yang seram jadi kelas yang penuh canda tawa."
        hide Sukma_senyum
        hide Rina_senyum
        hide Ziki_senang
        "Semua tertawa bersama-sama dan melanjutkan malam mereka dengan keceriaan, meskipun listrik masih belum menyala."
        scene bg_tamat
        with Fade(1,0,1)
        stop music
        return

    label lanjut3:
        play music "malam.mp3"
        "Di tengah suasana gelap dan redup karena pemadaman listrik, aku melihat Rina duduk di sebelahku dengan penuh semangat. Melihat kesempatan ini, aku mendekatinya sambil tersenyum."
        r netral "Rina, bagaimana kalau kita membuat kode lucu yang bisa menciptakan suara-suara aneh? Kita bisa melihat reaksi teman-teman saat mendengarkannya!"
        show Rina_senang
        "Rina langsung senang mendengar usulanku."
        ri senyum "Keren! Ayo kita coba! Apa suara aneh yang ingin kita buat?"
        hide Rina_senang
        "Aku berpikir sejenak, lalu muncul ide lucu dalam benakku."
        r netral "Bagaimana kalau kita membuat suara seperti kucing menggendong bayi? Atau suara tikus yang sedang bernyanyi?"
        show Rina_ketawa
        ri ketawa "Hahaha, itu pasti lucu! Baiklah, mari kita mulai!"
        hide Rina_ketawa
        "Kami duduk berdekatan dan mulai mengetik kode-kode lucu kami di laptop masing-masing."
        "Setelah beberapa saat, kami berhasil menciptakan kode untuk menghasilkan suara kucing menggendong bayi yang konyol dan suara tikus yang sedang bernyanyi dengan nafas tertahan."
        show Rina
        ri netral "Baik, sekarang saatnya menguji efek suara lucu kita!"
        hide Rina
        "Aku dengan bersemangat mengumpulkan teman-teman kami yang lain"
        r senang "Hey, teman-teman! Kami punya sesuatu yang ingin kami tunjukkan padamu!"
        "Mereka penasaran dan berkumpul di sekitar kami. Tanpa basa-basi, kami menyalakan kode-kode lucu kami dan membiarkan suara-suaranya mengisi ruangan."
        play music "gabungan.mp3"
        "Tiba-tiba, terdengar suara kucing yang menggendong bayi dan suara tikus yang bernyanyi. Teman-teman kami langsung bingung dan terkejut. Beberapa dari mereka tertawa, sementara yang lain mencoba menebak dari mana asal suara tersebut."
        show Sukma at left
        s netral "Apakah itu suara kucing?"
        show Ziki at right
        z netral "Tunggu, itu suara tikus atau apa?"
        stop music
        "Rina dan aku tertawa melihat reaksi lucu teman-teman kami. Sebagian dari mereka mencoba menirukan suara-suara tersebut dan akhirnya kami semua berakhir dalam tawa yang menggema di dalam kelas yang gelap."
        hide Sukma
        hide Ziki
        play music "malam.mp3"
        show Ziki_senang at left
        z senang "Kalian berdua memang luar biasa, hahaha! Suara kucing menggendong bayi, siapa yang bisa berpikir seperti itu!"
        r ketawa "Haha, kami senang kalian menyukainya! Kami hanya ingin menghibur dan membuat suasana lebih ceria di sini."
        show Rina_senyum
        ri senyum "Iya, terima kasih sudah mendukung ide gila kami!"
        hide Ziki_senang
        hide Rina_senyum
        "Pemadaman listrik yang awalnya mengganggu pekerjaan kami malah berubah menjadi momen menyenangkan dan menghibur. Kami semua bersenang-senang bersama, menikmati kebersamaan dalam kegilaan kami menciptakan kode-kode lucu."
        scene bg_tamat
        with Fade(1,0,1)
        stop music
        return

    label lanjut4:
        "Akhirnya kami memutuskan untuk keluar dari kelas dan menuju ke kantin."
        play music "malam.mp3"
        scene bg_koridor
        "Setelah memutuskan keluar dari kelas, kami semua berjalan bersama menuju kantin kampus. Udara malam terasa sejuk, tapi semangat kami tak terbendung. Kami berbicara dan bercanda dalam perjalanan menuju kantin."
        r ketawa "Haha, siapa yang tahu mencetak 'Hello World' bisa menjadi semacam salam perkenalan bagi para programmer di dunia maya?"
        show Rina_senyum
        ri senyum "Iya, dan siapa sangka kode-kode lucu ini bisa menghibur kami saat pemadaman listrik tadi."
        show Sukma_senyum at left
        s senyum "Tentu saja! Kode-kode itu berhasil mengubah situasi dari tegang menjadi menyenangkan."
        show Ziki_senang at right
        z senang "Kamu ingat saat Rina menunjukkan kode untuk membuat gambar wajah senyum menggunakan karakter ASCII? Kami semua terpingkal-pingkal melihatnya!"
        show Rina
        ri netral "Kamu bisa mencobanya juga, kok! Ini simpel banget, dan hasilnya kocak!"
        hide Rina_senyum
        hide Rina
        hide Ziki_senang
        hide Sukma_senyum
        stop music
        scene bg_kantin
        play music "audio/suasanakantin.mp3" volume 0.5
        "Kami tiba di kantin yang masih ramai, meskipun sudah tengah malam. Kami memesan makanan dan minuman favorit kami, lalu duduk di sebuah meja besar."
        r netral "Aku rasa, perjalanan kita di Teknik Informatika akan menyenangkan jika terus berjalan seperti ini."
        show Ziki_senang
        z senang "Benar sekali! Selama kita bersama, kita pasti bisa mengatasi segala tantangan dengan penuh semangat."
        show Sukma_senyum
        s senyum "Ya, aku merasa beruntung memiliki teman-teman seperjuangan seperti kalian."
        show Rina_senyum
        ri senyum "Ayo kita angkat gelas! Untuk persahabatan kita yang baru terbentuk di dunia coding dan teknik informatika!"
        bareng "Cheers!"
        "Perjalanan kami di Teknik Informatika mungkin baru dimulai, tapi semangat dan kebersamaan yang kami rasakan sejak hari pertama telah membentuk ikatan yang kuat di antara kami."
        "Di tengah tawa dan canda, kami merasa yakin bahwa bersama-sama, tak ada hal yang tak mungkin kami raih."
        scene bg_tamat
        with Fade(1,0,1)
        stop music
        return
    return