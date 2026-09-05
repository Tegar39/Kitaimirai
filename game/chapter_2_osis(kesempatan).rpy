label chapter_2_osis_kesempatan:
    scene bg_classroom with fade
    play music "audio/bgm/schoolgate.mp3" fadein 2.0

    "{cps=35}Aku melangkah masuk ke kelas dengan napas yang masih sedikit memburu. Suasana kelas pagi ini terasa sangat bising, tipikal kelas yang ditinggal gurunya.{/cps}"

    "{cps=35}Aku melihat Yuuka sudah duduk di bangkunya. Dia sedang dikerumuni oleh beberapa siswi lain, tapi matanya sesekali melirik ke arah pintu.{/cps}"

    if jujur == False:
        "{cps=35}Saat mata kami bertemu, Yuuka langsung membuang muka dan pura-pura tertawa mendengar cerita teman di sebelahnya.{/cps}"
        "{cps=35}Hatiku mencelos. Sepertinya hari ini akan menjadi hari yang sangat panjang.{/cps}"
    else:
        "{cps=35}Yuuka melambai pelan ke arahku, meski senyumnya tidak selebar biasanya. Setidaknya, dia masih mau menatapku.{/cps}"

    "{cps=35}Aku berjalan menuju bangkuku. Namun, sebelum aku sempat duduk, seseorang menepuk bahuku dari belakang.{/cps}"

    "{cps=50}Dan seperti yang kuduga{/cps}"

    "{cps=40}[v] muncul di belakangku dengan wajah yang sedikit curiga{/cps}"

    show vina_smile with dissolve
    v "{cps=60}Ara, ara... [mc]. Wajahmu terlihat seperti orang yang baru saja lolos dari hukuman mati.{/cps}"

    mc "{cps=40}[v] Kamu selalu muncul tiba-tiba ya...{/cps}"

    v "{cps=60}Fufufu. Aku hanya penasaran. Kemarin [m]-senpai membawamu pergi dengan aura yang menyeramkan.{/cps}"
    v "{cps=60}Jadi... {w=0.1}bagaimana hasilnya?{/cps}"
    v "{cps=60}Apakah dia membuangmu ke gudang belakang, atau kamu berhasil melakukan 'negosiasi' dengannya?{/cps}"
    
    # TAMBAHAN START
    "{cps=35}Vina menumpukan dagunya di atas tangannya yang terlipat di sandaran kursiku. Matanya yang tajam seolah sedang memindai setiap inci reaksiku.{/cps}"
    
    mc "{cps=40}Negosiasi apa maksudmu? Dia itu Ketua, bukan pedagang pasar.{/cps}"
    
    v "{cps=60}Fufufu. Di sekolah ini, Maya-senpai ADALAH hukum. Dan hukum selalu punya harga.{/cps}"
    
    v "{cps=60}Ayo jujur, Specimen. Dia pasti menyebutkan nama 'Ikazaki [mi]', kan? Wajahmu berubah jadi pucat setiap kali nama itu terlintas.{/cps}"
    
    "{cps=35}Aku terkejut. Bagaimana Vina bisa tahu? Padahal pembicaraan kemarin bersifat sangat privat.{/cps}"
    
    mc "{cps=40}Kamu... nguping?{/cps}"
    
    v "{cps=60}Ya... anggap saja aku punya 'telinga' di mana-mana. Jadi, pilihanmu?{/cps}"
    # TAMBAHAN END
    mc "{cps=40}Aku... {w=0.1}memilih OSIS.{/cps}"
    mc "{cps=40}Aku baru saja menyerahkan kertasnya pada [m]-senpai tadi di gerbang.{/cps}"

    # Vina terkejut (Gunakan ekspresi terkejut jika ada)
    # show vina_surprised with dissolve
    v "{cps=60}Ehh?! Kamu serius?{/cps}"
    if jujur == False:
        "{cps=35}Yuuka yang mendengar percakapan ini terlihat terkejut, seakan-akan tidak percaya kalau aku memilih osis{/cps}"
    
    "{cps=35}Vina sedikit membelalakkan matanya, lalu tawanya pecah.{/cps}"
    
    v "{cps=60}Hahaha! Aku tidak menyangka kamu akan menyerah secepat itu.{/cps}"
    v "{cps=60}Tapi... {w=0.1}pilihan yang cerdas untuk seseorang pria yang ingin 'bertahan hidup' di sekolah ini.{/cps}"
    mc "{cps=40}Hei! nggak gi-{/cps}"
    y "{cps=60}Dia tidak menyerah, [v]{/cps}"
    y "{cps=60}[mc] hanya... menyadari kalau dia punya potensi.{/cps}"

    v "{cps=60}Oh? Benarkah begitu, [y]-san?{/cps}"
    v "{cps=60}Atau mungkin karena dia tidak tahan melihatmu terus-terusan cemberut?{/cps}"

    y "{cps=60}A-apa sih! Bukan itu!{/cps}"

    "{cps=35}Yuuka membuang muka dengan wajah memerah, sementara Vina kembali menatapku dengan senyum yang lebih serius.{/cps}"

    v "{cps=60}Yah, apa pun alasannya, selamat bergabung di kapal yang penuh badai, [mc].{/cps}"
    v "{cps=60}Sebagai anggota OSIS, saranku hanya satu.{/cps}"
    v "{cps=60}Siapkan mentalmu untuk sore nanti. Maya-senpai tidak pernah memberikan 'selamat datang' yang manis.{/cps}"

    mc "{cps=40}Aku sudah merasakannya tadi...{w=0.1} Dia bahkan menyuruhku datang ke ruangannya tepat setelah bel pulang.{/cps}"

    v "{cps=60}Fufufu. Itu baru permulaan. Ayo, duduklah. Guru sebentar lagi datang.{/cps}"

    scene black with fade
    "{cps=35}Pelajaran pun dimulai. Namun, peringatan Vina terus terngiang di kepalaku. Apa sebenarnya yang sudah disiapkan Maya-senpai untukku di ruang OSIS nanti?{/cps}"

    "{cps=40}Disaat aku melamun....{/cps}"
    "{cps=40}BRAK!{/cps}"
    mc"{cps=40}Hue! Apa yan-{/cps}"
    "{cps=40}[t] melempar buku ke mejaku dengan cukup keras{/cps}"
    t "{cps=40}Hah.... gini ya [mc]{/cps}"
    t "{cps=40}Meskipun kamu sedang ngantuk...{/cps}"
    t "{cps=40}{b}MINIMAL MEMPERHATIKAN!{/b}{/cps}"
    mc "{cps=50}Baik bu...{/cps}"
    "{cps=50}Sial... {w=0.1}kenapa jadi begini...{/cps}"
    "{cps=50}Terdengar suara [v] yang tertawa kecil di belakangku. Dia pasti menikmati pemandangan ini.{/cps}"

    t "{cps=40}Karena kamu sepertinya punya dunia sendiri di dalam kepala itu, coba selesaikan soal yang ada di papan.{/cps}"
    
    # Soal yang lebih manusiawi
    t "{cps=40}Jika 3x + 5 = 20, berapakah nilai dari x?{/cps}"

    "{cps=35}Aduh... kepalaku mendadak kosong. Angka-angka itu seolah menari-nari di depan mataku.{/cps}"
    if jujur:
        "{cps=35}Yuuka di depanku terlihat panik, dia mengangkat lima jarinya di bawah meja sebagai isyarat.{/cps}"
    else:
        "{cps=35}Yuuka di depanku terlihat biasa saja, dia bahkan tidak memberi isyarat apapun.{/cps}"
    "{cps=40}Aku harus menjawab apa...{/cps}"
    menu:
        "5":
            $ correct_answer = True
            $ yuuka_rel += 5
            $ vina_rel += 5
            mc "{cps=40}Jawabannya... 5, Bu.{/cps}"
            
            "{cps=35}Ibu [t] terdiam sejenak, lalu menurunkan kacamatanya.{/cps}"
            
            t "{cps=40}Tepat. Sederhana, bukan?{/cps}"
            t "{cps=40}Ingat, dalam Aljabar, tujuan kita adalah mencari 'Nilai yang Hilang' (x) dengan cara menyeimbangkan kedua sisi.{/cps}"
            
            "{cps=35}Ibu [t] menuliskan coretan di papan dengan cepat.{/cps}"
            t "{cps=40}Jika kamu punya masalah besar (20) dan ada gangguan kecil (+5), hilangkan gangguannya dulu (20-5). Baru kemudian bagi beban sisa (15) dengan kapasitasmu (3).{/cps}"
            
            "{cps=35}Entah kenapa, penjelasan Bu [t] barusan tidak hanya terdengar seperti matematika, tapi seperti cara menghadapi hidup yang sedang berantakan ini.{/cps}"
            t "{cps=35}Sudah paham?{/cps}"
            mc "{cps=35}Sudah bu?{/cps}"
            t "{cps=40}Lain kali, perhatikan penjelasan saya. Duduk dan fokus!{/cps}"
            t "{cps=35}Sekarang kembali ke tempat dudukmu{/cps}"
            mc "{cps=35}Ba-baik bu{/cps}"
            
            show yuuka_smile with dissolve
            if jujur:
                "{cps=35}Yuuka menghela napas lega dan tersenyum kecil ke arahku. Di belakang, Vina tampak sedikit kecewa karena tidak bisa menertawakanku.{/cps}"
            v "{cps=60}Cih... ternyata si Specimen Langka ini bisa berhitung juga.{/cps}"

        "15":
            $ correct_answer = False
            $ yuuka_rel -= 2
            mc "{cps=40}Jawabannya... 15, Bu?{/cps}"
            
            "{cps=35}Seketika seisi kelas tertawa. Bahkan Vina di belakangku sampai harus menutup mulutnya agar tidak terdengar terlalu keras.{/cps}"
            t "{cps=40}Lima belas? Kamu ini sedang menghitung nilai x atau harga gorengan di kantin? Salah!{/cps}"
            t "{cps=40}Berdiri di depan sampai jam pelajaran saya selesai!{/cps}"
            
            show yuuka_sad with dissolve
            "{cps=35}Yuuka menepuk jidatnya. Dia sudah memberiku kode, tapi aku malah salah tangkap.{/cps}"

        "3":
            $ correct_answer = False
            $ yuuka_rel -= 2
            mc "{cps=40}Jawabannya... 3?{/cps}"
            
            t "{cps=40}Salah! Ternyata lamunanmu benar-benar merusak kemampuan logikamu.{/cps}"
            t "{cps=40}Silakan berdiri di samping papan tulis sampai saya selesai menjelaskan.{/cps}"
            
            "{cps=35}Aku hanya bisa tertunduk lesu sementara beberapa siswi lain berbisik-bisik menertawakanku.{/cps}"

    "{cps=50}Kelas pun kembali dilanjutkan{/cps}"
    if correct_answer:
        "{cps=35}Untung saja tadi jawabanku benar...{/cps}"
    else:
        "{cps=35}Andai saja tadi jawabanku benar... mungkin kakiku tidak akan sepegal ini karena berdiri di depan.{/cps}"
    
    "{cps=40}Dan tidak terasa sudah waktunya istirahat.{/cps}"
    
    play sound "audio/sfx/school bell.mp3"
    t "{cps=40}Baiklah, karena waktunya sudah jam segini, silakan kalian istirahat.{/cps}"
    t "{cps=40}Nanti kita ketemu lagi di jam siang.{/cps}"
    
    "Satu Kelas" "{cps=40}Baik, Bu!{/cps}"
    "{cps=40}[t] langsung meninggalkan kelas.{/cps}"

    mc "{cps=40}Hah.... akhirnya.{/cps}"
    
    if correct_answer == False:
        "{cps=40}[v] dan [y] langsung menghampiriku.{/cps}"
        "{cps=40}Sepertinya mereka ingin memberiku semacam 'wejangan'.{/cps}"
        
        show yuuka_determined at left
        show vina_smile at right
        with dissolve

        v "{cps=40}Yo! {w=0.1}Anak bodoh.{/cps}"
        mc "{cps=40}Hei!{/cps}"
        v "{cps=40}Ayolah, aku cuman bercanda. Tapi serius, ekspresimu tadi lucu sekali.{/cps}"
        mc "{cps=40}Apa sih...{/cps}"
        v "{cps=40}Tapi kakimu gimana? {w=0.1} Sehat?{/cps}"
        mc "{cps=40}Saking sehatnya aku sampai malas jalan{/cps}"
        v "{cps=40}Ahaha, sudah ku duga{/cps}"
        if jujur:
            y "{cps=40}Padahal sudah aku beritahu kodenya, [mc]. Kenapa kamu malah melamun?{/cps}"
            mc "{cps=40}Maaf... kepalaku mendadak blur melihat angka-angka itu.{/cps}"
            y "{cps=40}Kamu ini kebiasaan{/cps}"
            v "{cps=40}Heee kode apa tuch?{/cps}"
            y "{cps=40}Bukan apa-apa{/cps}"
            "{cps=40}[y] langsung pergi meninggalkanku{/cps}"
            v "{cps=40}Lah? Kenapa malah pergi{/cps}"
            v "{cps=40}[y].....{/cps}"
            "{cps=40}[v] langung mengejar [y]{/cps}"
            "{cps=40}Meninggalkanku sendiri{/cps}"
        else:
            y "{cps=40}Makanya, kalau di kelas itu diperhatikan. Jangan malah asyik sendiri.{/cps}"
            v "{cps=35}Hei... ada apa sih ka?{/cps}"
            y "{cps=40}Entahlah, kalau kamu mau tahu ya tanya ke [mc] langsung{/cps}"
            "{cps=40}[y] langsung meninggalkan kami tanpa sepatah kata apa pun{/cps}"
            v "{cps=40}Sepertinya ada drama nih..{/cps}"
            v "{cps=40}Kamu habis apain dia?{/cps}"
            mc "{cps=40}Ah nggak gitu{/cps}"
            v "{cps=40}Hah...{w=0.1} [y]!{/cps}"
            "{cps=40}[v] langung mengejar [y]{/cps}"
            "{cps=40}Meninggalkanku sendiri{/cps}"
        "{cps=40}.....{/cps}"
            
    else:
        "{cps=40}[v] dan [y] langsung menghampiriku.{/cps}"
        "{cps=40}Sepertinya mereka ingin memberiku semacam 'wejangan'.{/cps}"
        
        show yuuka_determined at left
        show vina_smile at right
        with dissolve

        v "{cps=40}Yo! {w=0.1}Anak pintar{/cps}"
        mc "{cps=40}Aku hanya beruntung tadi{/cps}"
        v "{cps=40}Sayang sekali tidak ada drama...{/cps}"
        v "{cps=40}Padahal kan aku ingin melihatmu kena hukuman{/cps}"
        mc "{cps=40}Hei! Niatmu buruk sekali ya.{/cps}"
        if jujur:
            y "{cps=40}Syukurlah kamu bisa menjawabnya, [mc]. Aku sempat panik tadi.{/cps}"
            y "{cps=40}Lain kali jangan melamun lagi, ya?{/cps}"
            mc "{cps=40}Iya, maaf...{/cps}"
        else:
            y "{cps=40}Ternyata kamu bisa mengerjakannya sendiri. Baguslah.{/cps}"
        v "{cps=40}Tapi ya sudahlah. Setidaknya hari ini aman, kan?{/cps}"
        mc "{cps=40}Aman sih...{/cps}"
        v "{cps=40}Mau ke kantin?{/cps}"
        if jajan == True:
            mc "{cps=40}Nggak terima kasih, aku masih kenyang.{/cps}"
            "{cps=40}(Karena tidak ingin keluar duit aja sih...){/cps}"
        else:
            mc "{cps=40}Sepertinya nggak dulu deh Vin, aku masih kenyang.{/cps}"
        
        v "{cps=40}Hah... yaudah kalau begitu.{/cps}"

        # Bagian ini cukup ditulis sekali setelah pengecekan jajan
        if jujur:
            v "{cps=40}Ayo Ka, kita ke kantin!{/cps}"
            y "{cps=40}Ayo.{/cps}"
        else:
            v "{cps=40}Ayo Yu— Loh? Tuh anak kemana?{/cps}"
            v "{cps=40}[mc] kamu melihatnya kan?{/cps}"
            mc "{cps=40}Dia bukannya sudah duluan?{/cps}"
            v "{cps=40}Eh!? [y] tunggu sebentar...{/cps}"

        "{cps=40}Mereka pun pergi meninggalkanku sendiri.{/cps}"
        "{cps=40}...{/cps}"
    "{cps=40}Suasana tenang ini{/cps}"
    "{cps=40}Kapan ya terakhir kali aku merasakannya...{/cps}"

    
    play sound "audio/sfx/walk.mp3"
    yk "{cps=60}He-ey! [mc]! Kenapa wajahmu terlihat seperti sedang memikirkan akhir dunia?{/cps}"

    show yukie_smile with dissolve
    "{cps=35}Yukie berdiri di depanku. Berbeda dengan [y] yang serius atau [v] yang usil, [y] selalu membawa aura yang... ringan.{/cps}"

    mc "{cps=40}Loh [yk], Kamu tidak ke kantin bersama yang lain?{/cps}"

    yk "{cps=60}Aku sudah makan bekal tadi. Lagipula, aku tidak tega meninggalkan 'Patung Cantik' itu sendirian di pojokan.{/cps}"

    "{cps=35}Yukie melirik ke arah Shoko yang masih duduk diam menatap jendela.{/cps}"

    yk "{cps=60}Oiya, [mc]. Karena kamu sekarang sudah jadi anggota OSIS yang 'berbakti', bisa minta tolong?{/cps}"
    yk "{cps=60}Aku harus ke ruang guru sebentar. Bisa titip berikan susu kotak ini pada Oneesan? Dia lupa minum sejak pagi.{/cps}"

    mc "{cps=40}Kenapa tidak ditaruh di mejanya saja?{/cps}"

    yk "{cps=60}Fufufu. [sh] itu kalau sudah melamun, dia tidak akan sadar dunia sekitar kecuali ada yang mengajaknya bicara.{/cps}"
    yk "{cps=60}Tolong ya, 'Specimen Langka'!{/cps}"

    hide yukie with dissolve
    "{cps=35}Yukie lari keluar kelas sebelum aku sempat menolak. Kini, di kelas yang hampir kosong ini, hanya ada aku dan dia.{/cps}"

    # MC mendekati Shoko
    "{cps=35}Aku berdiri di samping meja Shoko. Dia benar-benar tidak bergerak. Hanya matanya yang terlihat mengikuti butiran debu yang melayang di bawah sinar matahari.{/cps}"

    mc "{cps=40}Shirohana-san...{/cps}"

    "{cps=35}Lonceng di lehernya berdenting halus saat dia sedikit memiringkan kepalanya. Dia tidak menoleh sepenuhnya, hanya melirikku dari sudut matanya yang bening.{/cps}"

    sh "{cps=50}...Suara langkah kaki yang ragu-ragu. Kamu membawa sesuatu untukku, Ikazaki-kun?{/cps}"

    mc "{cps=40}Yukie menitipkan ini. Katanya kamu lupa minum sejak pagi.{/cps}"

    "{cps=35}Aku meletakkan susu kotak itu di mejanya. Shoko terdiam sejenak, lalu jemarinya yang pucat menyentuh kotak dingin itu.{/cps}"
    if correct_answer == True:
        sh "{cps=50}Terima kasih. Dan... selamat atas keberhasilanmu tadi.{/cps}"

        mc "{cps=40}Maksudmu soal matematika tadi? Ah, itu hanya keberuntungan.{/cps}"

        sh "{cps=50}Bukan angka-angkanya... tapi keberanianmu mencari 'keseimbangan' di depan kelas tadi.{/cps}"
        sh "{cps=50}Kebanyakan orang hanya melihat variabel 'x' sebagai beban. Tapi kamu... kamu menatapnya seolah-olah kamu sedang mencari sesuatu yang hilang dari dirimu sendiri.{/cps}"

    else:
        sh "{cps=50}Terima kasih. Dan... selamat atas kegagalanmu tadi.{/cps}"

        mc "{cps=40}Ternyata kamu memperhatikan ya?{/cps}"

        sh "{cps=50}Bukan salah benarnya... tapi keberanianmu mencari 'jawaban' di depan kelas tadi.{/cps}"
        sh "{cps=50}Kebanyakan orang hanya melihat kesalahanmu saja. Tapi kamu... kamu menanggapinya seakan kamu sedang mencari sesuatu yang hilang dari dirimu sendiri.{/cps}"

    "{cps=35}Perkataannya membuatku tertegun. Rasanya seperti dia baru saja membaca isi kepalaku.{/cps}"

    mc "{cps=40}Mungkin kamu benar...{/cps}"
    "{cps=40}Sepertinya aku harus memberitahu dia{/cps}"
    mc "{cps=40}Oh iya [sh], aku memilih OSIS loh{/cps}"
    mc "{cps=40}[sh] diam, dan reaksinya seakan ada yang satu hal penting yang mulai menghilang{/cps}"
    sh "{cps=40}Oh....{/cps}"
    sh "{cps=40}Selamat ya{/cps}"
    mc "{cps=40}Sepertinya kamu merasa ada yang hilang, apa itu?{/cps}"
    sh "{cps=40}Nggak ada...{/cps}"
    "{cps=40}Sepertinya [sh] mulai sedikit menjauh dariku...{/cps}"
    mc "{cps=40}Menurutmu, osis itu kayak gimana?{/cps}"

    sh "{cps=50}OSIS... tempat yang sangat bising. Banyak suara, tapi sedikit yang benar-benar bicara.{/cps}"
    sh "{cps=50}Tapi aku mengerti. Bagi seseorang yang membawa nama 'Ikazaki', mungkin kebisingan adalah cara untuk melupakan masa lalu, bukan?{/cps}"

    mc "{cps=40}Apa maksudmu? Kamu... tahu sesuatu tentang keluargaku?{/cps}"

    "{cps=35}Shoko akhirnya menoleh sepenuhnya. Tatapannya mendalam, seolah-olah dia sedang melihat melampaui waktu.{/cps}"

    sh "{cps=50}Sepuluh tahun adalah waktu yang lama untuk sebuah ingatan, tapi terlalu singkat untuk sebuah janji yang belum terpenuhi...{/cps}"

    # --- MOMEN KRUSIAL / SERIUS ---
    "{cps=35}Udara di sekitar kami mendadak terasa dingin. Jantungku berdegup kencang.{/cps}"
    mc "{cps=40}Apa maksudmu sepu-{/cps}"

    play sound "audio/sfx/door.mp3"
    g1 "{cps=40}[mc]! {w=0.1} [mc] ada di sini nggak?!{/cps}"

    "{cps=35}Suara pintu yang digeser dengan kasar menghancurkan kesunyian di antara kami.{/cps}"

    mc "{cps=40}A-ada apa?{/cps}"

    g1 "{cps=40}Duh, untung ketemu! Cepat ke koridor depan ruang OSIS sekarang! Maya-senpai mencarimu. Dia kelihatan... sangat tidak sabar.{/cps}"

    mc "{cps=40}Sekarang? Tapi ini kan masih jam istirahat?{/cps}"

    g1 "{cps=40}Mana berani aku tanya alasannya ke dia! Pokoknya cepat sana sebelum dia makin marah!{/cps}"

    "{cps=35}Aku menghela napas panjang. Aku menoleh kembali ke arah Shoko, tapi dia sudah kembali menatap jendela, seolah-olah percakapan tadi tidak pernah terjadi.{/cps}"

    sh "{cps=50}Pergilah... sang 'Ketua' tidak suka menunggu variabel yang tidak pasti.{/cps}"

    mc "{cps=40}Aku... aku pergi dulu, Shirohana-san.{/cps}"

    scene black with fade
    stop music fadeout 1.5

    "{cps=35}Aku melangkah keluar kelas dengan perasaan yang mengganjal. Rahasia tentang janji sepuluh tahun itu kembali tertutup oleh bayang-bayang perintah [m].{/cps}"

    scene bg_school_corridor with fade
    play music "audio/bgm/emptyroom.mp3" fadein 2.0

    "{cps=35}Aku berjalan menyusuri koridor gedung utama. Suara bising dari kantin terdengar samar di kejauhan, tapi koridor di depan ruang OSIS ini terasa begitu sunyi dan dingin.{/cps}"

    "{cps=35}Maya berdiri di sana, menyandarkan punggungnya pada jendela besar. Dia sedang menatap jam tangannya dengan ekspresi datar yang sulit dibaca.{/cps}"

    show maya_stern with dissolve
    m "{cps=40}Tiga menit dua puluh detik. Kamu lebih lambat dari perkiraanku, Ikazaki [mc].{/cps}"

    mc "{cps=40}Maaf, Kak. Tadi ada sedikit... urusan di kelas.{/cps}"

    m "{cps=40}Urusan dengan Shirohana bersaudara?{/cps}"

    "{cps=35}Deg. Bagaimana dia bisa tahu? Apakah OSIS benar-benar memiliki 'mata' di setiap sudut sekolah ini?{/cps}"

    m "{cps=40}Jangan memasang wajah terkejut seperti itu. Sebagai Ketua, aku harus tahu di mana posisi setiap 'aset' milikku.{/cps}"

    mc "{cps=40}Aset? Jadi aku sekarang hanya sekadar aset bagimu?{/cps}"

    m "{cps=40}Tergantung bagaimana kamu membuktikannya sore nanti. Tapi untuk sekarang...{/cps}"

    "{cps=35}Maya meraba saku blazernya dan mengeluarkan sebuah armband berwarna biru. armband resmi OSIS Sekolah ini{/cps}"

    m "{cps=40}Pakai ini. Aku tidak ingin ada anggota 'ilegal' yang berkeliaran di ruanganku sore nanti.{/cps}"

    # Opsi interaksi kecil yang berpengaruh ke harga diri MC
    if correct_answer == True:
        "{cps=40}Aduh! Tanganku masih rada sakit...{/cps}"
    else:
        "{cps=40}Apa aku isengin kak [m] ya...{/cps}"
    
    "{cps=40}Apa yang harus aku lakukan?{/cps}"
    
    menu:
        "Pasang Sendiri":
            $ pasang = False
            $ maya_rel += 2
            "{cps=35}Aku mengambil armband itu dari tangannya. Terasa dingin dan berat.{/cps}"
            mc "{cps=40}Terima kasih. Aku akan datang sore nanti.{/cps}"
            m "{cps=40}Bagus. Jangan buat armband itu terlihat memalukan di seragammu.{/cps}"

        "Dipasangin":
            $ maya_rel += 5
            $ yuuka_rel -= 3
            $ pasang = True # Jika nanti Yuuka tahu atau melihat dari kejauhan
            mc "{cps=40}Tangan saya sedang gemetar karena habis dihukum berdiri tadi. Bisa tolong pasangkan, Senpai?{/cps}"
            m "{cps=40}Hah?{/cps}"
            "{cps=35}Maya sedikit menaikkan alisnya. Untuk sesaat, topeng datarnya retak oleh rasa heran.{/cps}"
            m "{cps=40}Kamu... benar-benar punya nyali yang menarik.{/cps}"
            "{cps=35}Dia melangkah mendekat. Hawa dingin berganti dengan aroma parfum yang tajam namun menenangkan. Jemarinya yang cekatan memasangkan armband itu di bahu seragamku.{/cps}"
            m "{cps=40}Selesai. Sekarang pergilah makan. Aku tidak butuh anggota yang pingsan saat rapat koordinasi.{/cps}"
            mc "{cps=35}Baik kak{/cps}"
            

    hide maya with dissolve
    "{cps=35}Maya berbalik dan masuk ke ruangannya tanpa menunggu jawabanku.{/cps}"

    "{cps=35}Aku menyentuh armband di bahuku. Rasanya seperti sebuah borgol, namun di saat yang sama, ada rasa bangga yang aneh mulai muncul.{/cps}"
    # --- BAGIAN REAKSI YUUKA (The Hidden Observer) ---
    
    # Memberi jeda sunyi untuk membangun suasana
    stop music fadeout 3.0
    pause 1.0

    "{cps=35}Saat aku hendak berbalik untuk kembali ke kelas, aku menangkap siluet seseorang di ujung belokan koridor.{/cps}"
    
    # Visual hint: Hanya bayangan atau ujung rambut/pita biru yang lewat sekilas
    # show yuuka_shadow at far_distance with fast_dissolve 
    
    "{cps=35}Hanya sekejap. Bayangan itu menghilang sebelum aku sempat memastikan siapa itu.{/cps}"
    if pasang:
        if jujur:
            # Reaksi 1: Kaget tapi terpendam (Sakit hati karena MC tetap memilih 'sisi' Maya)
            unknown "{cps=40}...Kenapa... harus seragam itu?{/cps}"
            "{cps=35}Suara itu nyaris seperti bisikan angin. Begitu pelan, tapi penuh dengan nada tidak percaya.{/cps}"
            "{cps=35}Ada suara langkah kaki yang terburu-buru menjauh. Seperti seseorang yang sedang berusaha menahan napas agar tidak menangis.{/cps}"
            
            $ yuuka_rel -= 1 # Penurunan sedikit karena dia merasa MC menjauh
        else:
            # Reaksi 2: Sedih yang mendalam (Merasa dibohongi/dikhianati)
            unknown "{cps=40}Pembohong...{/cps}"
            "{cps=35}Sebuah kata singkat yang menusuk udara dingin koridor itu.{/cps}"
            "{cps=35}Aku mendengar suara sesuatu yang jatuh—mungkin sebuah gantungan kunci atau benda kecil lainnya—sebelum langkah kaki itu berlari menjauh dengan berat.{/cps}"
            "{cps=35}Ada getaran kesedihan yang tertinggal di sana, seolah-olah kepercayaan yang selama ini dibangun baru saja retak.{/cps}"
            
            $ yuuka_rel -= 5 # Penurunan drastis karena merasa dikhianati

    else:
        if jujur:
            unknown "{cps=40}Selamat ya...{/cps}"
            "{cps=40}Suara itu nyaris seperti bisikan angin. Begitu pelan, tapi penuh dengan nada gembira.{/cps}"
            "{cps=40}Ada suara langkah kaki yang terburu-buru menjauh{/cps}"
            "{cps=40}Namun dengan perasaan senang{/cps}"
            $ yuuka_rel += 2
        else:
            unknown "{cps=40}Aku tidak menyangka ini nyata...{/cps}"
            unknown "{cps=40}Namun kenapa tidak cerita dari awal...{/cps}"
            unknown "{cps=40}Pembohong{/cps}"
            "{cps=40}Suara itu nyaris seperti bisikan angin. Begitu pelan, tapi dengan nada yang seakan-akan mulai kehilangan kepercayaan.{/cps}"
            $ yuuka_rel -= 2

    mc "{cps=40}Siapa di sana?{/cps}"

    "{cps=35}Tidak ada jawaban. Hanya gema langkah kakiku sendiri yang memantul di dinding gedung utama.{/cps}"
    "{cps=35}Tiba-tiba, rasa bangga karena memakai armband ini tadi mendadak menguap, berganti dengan rasa sesak yang tidak bisa kujelaskan.{/cps}"

    "{cps=40}Dan disaat aku sedang berpikir{/cps}"
    "{cps=40}*Ting tong ting tong~{/cps}"
    "{cps=40}Waktu istirahat telah selesai{/cps}"
    "{cps=40}Seakan-akan waktu berjalan terlalu cepat{/cps}"
    mc "{cps=40}Sial, sudah waktunya ya{/cps}"

    scene bg_classroom with fade
    play music "audio/bgm/evewalk.mp3" fadein 2.0

    "{cps=35}Aku melangkah masuk ke kelas. Udara siang ini terasa sangat gerah, ditambah lagi suasana canggung yang menyelimuti bangkuku dan bangku [y].{/cps}"

    "{cps=35}Aku baru saja duduk ketika pintu kelas kembali terbuka. Dan benar saja...{/cps}"

    # Menggunakan kembali Guru [t]
    show teacher_t_serious with dissolve
    
    "{cps=35}Sosok yang tadi pagi menghukumku di depan kelas kini muncul lagi. Di sekolah ini, [t] memang dikenal sebagai guru 'serba bisa' yang memegang jadwal padat.{/cps}"

    t "{cps=40}Letakkan gadget kalian. Meskipun ini jam siang yang rawan kantuk, materi kita sekarang jauh lebih berat dari matematika tadi pagi.{/cps}"

    t "{cps=40}Buka buku Sejarah kalian. Kita akan membahas tentang 'Tragedi dan Pengkhianatan' dalam sejarah pergerakan organisasi.{/cps}"

    "{cps=35}Aku tersentak. Kenapa materi siang ini terasa seperti sedang menyindir kondisiku sekarang?{/cps}"

    t "{cps=40}Dalam sejarah, banyak tokoh besar yang jatuh bukan karena musuh dari luar, tapi karena rusaknya 'Kepercayaan' dari orang terdekatnya.{/cps}"
    
    # Elemen Ilmu Pengetahuan
    t "{cps=40}Ada sebuah istilah Latin: {b}'Falsus in Uno, Falsus in Omnibus'{/b}. Ada yang tahu artinya?{/cps}"

    "{cps=35}Kelas sunyi. Aku melirik [y], dia sedang mencatat dengan sangat cepat, seolah-olah berusaha mengabaikan keberadaanku di belakangnya.{/cps}"
    "{cps=40}Seperti biasa, dia selalu saja fokus{/cps}"
    "{cps=40}Berbeda denganku...{/cps}"

    t "{cps=40}[mc], coba kamu jawab. Kamu sepertinya sedang banyak pikiran siang ini.{/cps}"
    mc "{cps=40}Kok saya sih [t]?{/cps}"
    t "{cps=40}Memangnya yang cocok selain kamu siapa lagi?{/cps}"
    mc "{cps=40}Kan ada...{/cps}"
    "{cps=40}Aku memperhatikan kelas{/cps}"
    "{cps=40}Namun reaksi mereka tidak menunjukan tanda-tanda ingin menjawab{/cps}"
    t "{cps=40}Ada apa?{/cps}"
    mc "{cps=40}Tidak bu...{/cps}"
    t "{cps=40}Kalau tidak ada cepat jawab{/cps}"
    mc"{cps=40}Ummm...{/cps}"

    menu:
        "Satu kebohongan merusak semuanya":
            $ correct_answer_2 = True
            mc "{cps=40}Artinya... sekali berbohong dalam satu hal, maka seluruh perkataannya akan dianggap bohong, Pak/Bu.{/cps}"
            

            # --- PERCABANGAN 4 SKENARIO REAKSI YUUKA ---

            if jujur and pasang == False:
                # 1. MC JUJUR & PASANG SENDIRI (Jalur Paling Aman)
                $ yuuka_rel += 5
                "{cps=35}Yuuka menghentikan catatannya sesaat. Bahunya sedikit bergetar, tapi dia tetap tidak menoleh.{/cps}"
                "{cps=35}Dia seolah sedang mencerna kata-kata itu, meyakinkan dirinya bahwa keputusanku masuk OSIS—meskipun mendadak—adalah kejujuran yang pahit.{/cps}"

            elif jujur and pasang == True:
                # 2. MC JUJUR TAPI DIPASANGIN MAYA (Jalur Cemburu)
                $ yuuka_rel -= 2
                unknown "{cps=35}Lantas kenapa kamu membiarkan dia melakukannya...{/cps}"
                unknown "{cps=35}Katanya ingin masuk OSIS demi kita, tapi kenapa bermain di belakang dengan Ketua...{/cps}"
                "{cps=35}Terdengar suara gumaman yang sangat lirih depanku. Begitu pelan, tapi penuh dengan nada kecurigaan.{/cps}"

            elif jujur == False and pasang == False:
                # 3. MC GA JUJUR TAPI PASANG SENDIRI (Jalur Kekecewaan)
                $ yuuka_rel -= 3
                unknown "{cps=35}Dasar munafik...{/cps}"
                "{cps=35}Suara itu nyaris tidak terdengar, namun kata 'munafik' itu bergema di telingaku mengalahkan suara Nanami-sensei.{/cps}"
                "{cps=35}Yuuka mencengkeram penanya begitu kuat. Dia tahu aku baru saja membohonginya pagi tadi.{/cps}"

            elif jujur == False and pasang == True:
                # 4. MC GA JUJUR & DIPASANGIN MAYA (Jalur Pengkhianatan Total)
                $ yuuka_rel -= 5
                unknown "{cps=35}Pembohong...{/cps}"
                unknown "{cps=35}Setelah membohongiku, kamu langsung bersenang-senang dengannya di koridor...{/cps}"
                "{cps=35}Sebuah bisikan tajam yang membuat bulu kudukku berdiri. Yuuka bahkan tidak lagi mencatat, dia hanya menatap kosong ke bukunya dengan mata yang berkaca-kaca.{/cps}"

            t "{cps=40}Tepat. Itulah hukum moral yang sering kali lebih kejam daripada hukum tertulis.{/cps}"
            t "{cps=40}Sekali kamu merusak kepercayaan, butuh waktu seumur hidup untuk membangunnya kembali.{/cps}"

        "Kesalahan satu orang ditanggung semua":
            $ correct_answer_2 = False
            mc "{cps=40}Artinya kesalahan satu orang adalah kesalahan semua anggota kelompok?{/cps}"
            
            t "{cps=40}Salah. Itu namanya tanggung renteng. Fokus kita adalah integritas individu.{/cps}"
            t "{cps=40}Sepertinya kamu harus lebih banyak membaca daripada sekadar melamun, [mc].{/cps}"
            
            v "{cps=40}Fufufu... Sepertinya otak [mc] sudah mulai berasap karena pelajaran pagi tadi.{/cps}"
            v "{cps=40}Hati-hati, [mc]. Kalau kamu terlalu sering melamun, nanti 'integritasmu' dipetik orang lain lho.{/cps}"
            
            mc "{cps=40}(Sial... Vina selalu saja tahu celah untuk menyindirku. Adakah hal di sekolah ini yang dia tidak tahu?){/cps}"

    # --- BAGIAN NARASI DURASI PANJANG ---

    t "{cps=40}Sekali kamu merusak kepercayaan, butuh waktu seumur hidup untuk membangunnya kembali.{/cps}"
    
    "{cps=35}Yuuka menghentikan catatannya sesaat. Bahunya sedikit bergetar, tangannya menggenggam pena dengan sangat erat sampai buku jarinya memutih.{/cps}"
    "{cps=35}Aku tahu dia mendengarkan setiap kata itu. Dan aku tahu, kata-kata Nanami-sensei sedang menghujam tepat di tengah-tengah kecanggungan kami.{/cps}"

    "{cps=35}Nanami-sensei kembali ke papan tulis, kapur di tangannya berderit keras saat beliau menuliskan daftar nama-nama pengkhianat besar dalam sejarah.{/cps}"
    "{cps=35}Suasana kelas menjadi sangat berat. Hanya ada suara gesekan pena di atas kertas dan detak jam dinding yang seolah melambat secara sengaja.{/cps}"

    "{cps=35}Satu jam berlalu...{/cps}"
    "{cps=35}Sinar matahari siang yang menyengat perlahan mulai bergeser, menciptakan bayangan panjang dari kaki meja yang menembus lantai kayu kelas.{/cps}"
    "{cps=35}Beberapa teman sekelasku mulai terlihat mengantuk, kepala mereka terkantuk-kantuk mengikuti irama suara Nanami-sensei yang monoton namun tajam.{/cps}"
    
    "{cps=35}Suara [t] yang menjelaskan tentang runtuhnya kerajaan-kerajaan besar akibat pengkhianatan internal terasa seperti bisikan yang menghakimi setiap helai napasku.{/cps}"

    "{cps=35}Aku melirik ke depan. [y] masih tetap pada posisinya. Dia tidak pernah sekalipun melirik ke arahku, bahkan saat dia mengambil penggaris atau merapikan rambutnya.{/cps}"

    "{cps=35}Dua jam berlalu...{/cps}"
    "{cps=35}Waktu benar-benar terasa abadi. Kakiku terasa kaku, dan pikiranku mulai melayang pada Shoko, pada Maya, dan pada armband perak yang kini menempel di bahuku.{/cps}"
    "{cps=35}Setiap detik yang kami lalui dalam diam ini terasa lebih menyakitkan daripada hukuman berdiri di depan kelas tadi pagi.{/cps}"
    
    "{cps=35}Dinding es yang dibangun [y] di sebelahku terasa semakin tebal. Aku ingin bicara, tapi tenggorokanku terasa terkunci oleh beban rahasia dan pilihan yang baru saja kuambil.{/cps}"
    "{cps=35}Kehadiranku di sini... di belakangnya... seolah-olah sudah dihapus sepenuhnya dari dunia kecilnya.{/cps}"

    scene black with fade
    stop music fadeout 3.0

    play sound "audio/sfx/school bell.mp3"
    "{cps=40}Ting... Tong...{/cps}"
    "{cps=40}Bel pulang akhirnya berbunyi. Murid-murid lain mulai berhamburan keluar dengan riang, tapi aku...{/cps}"

    "{cps=35}Aku menyentuh armband biru OSIS di bahuku. Armband itu seolah mengingatkanku bahwa 'waktu bermainku' sudah berakhir.{/cps}"
    "{cps=35}Aku harus segera menuju ruang rapat, meninggalkan kesunyian kelas ini menuju 'medan perang' yang sebenarnya.{/cps}"

    jump chapter_2_osis_kfm

label chapter_2_osis_kfm:
    # Mengatur suasana sore hari yang dramatis
    scene bg_council_room_sunset with fade
    play music "audio/bgm/emptyroom.mp3" fadein 2.0

    "{cps=35}Aku berdiri di depan pintu ruang OSIS. Cahaya jingga matahari sore masuk melalui celah jendela koridor, memberikan bayangan panjang yang seolah-olah menarikku masuk ke dalam pusaran masalah baru.{/cps}"
    "{cps=35}Aku menarik napas panjang, merapikan kerah seragamku, lalu mendorong pintu itu perlahan.{/cps}"

    # Para heroine sudah berada di posisi masing-masing
    show maya_stern at center
    show vina_smile at right
    show yuuka_determined at left
    with dissolve

    m "{cps=40}Akhirnya, anggota 'pindahan' kita sampai juga tepat waktu.{/cps}"
    
    # --- IMPLEMENTASI 4 SKENARIO REAKSI YUUKA ---

    if jujur and pasang == False:
        # 1. MC JUJUR DAN PASANG SENDIRI (Jalur Green Flag)
        $ yuuka_rel += 3
        y "{cps=40}Kamu tepat waktu, [mc]. Aku sudah menyiapkan berkas yang perlu kamu pelajari sebagai anggota baru.{/cps}"
        "{cps=35}Yuuka menatapku dengan tenang. Meskipun wajahnya tampak lelah setelah pelajaran Nanami-sensei, ada binar dukungan di matanya.{/cps}"
        v "{cps=40}Heee... kompak sekali ya kalian berdua. Padahal tadi di kelas seperti ada dinding es yang memisahkan kalian. Fufufu...{/cps}"
        y "{cps=40}A-apa sih?{/cps}"
        "{cps=40}[y] tersipu malu mendengar tanggapan dari [v]{/cps}"

    elif jujur and pasang == True:
        # 2. MC JUJUR TAPI DIPASANGIN MAYA (Jalur Cemburu)
        $ yuuka_rel -= 1
        "{cps=35}Yuuka langsung menatap tajam ke arah bahu seragamku. Matanya menyipit saat melihat armband biru yang terpasang dengan sangat sempurna itu.{/cps}"
        y "{cps=40}armband itu... rapi sekali ya, [mc]. Sepertinya dipasangkan oleh seseorang yang 'sangat ahli'.{/cps}"
        v "{cps=40}Fufufu, tentu saja rapi. Tadi aku tidak sengaja melihat Maya-senpai memberikan 'servis khusus' di koridor. Benar kan, Ketua?{/cps}"
        "{cps=35}Yuuka meremas ujung roknya. Dia membuang muka, berusaha keras untuk kembali fokus pada tumpukan kertas di depannya.{/cps}"
        m "{cps=40}Sudahlah, tidak usah dibahas{/cps}"
        m "{cps=40}Lagipula kan tadi tangan [mc] pegal{/cps}"
        y "{cps=40}Tapi masa tidak bisa masang sendiri?{/cps}"
        v "{cps=40}Heee apa kamu yang mau memasangkannya?{/cps}"
        y "{cps=40}Bukan begitu...{/cps}"
        "{cps=40}Terlihat wajah [y] yang sedikit malu{/cps}"

    elif jujur == False and pasang == False:
        # 3. MC GA JUJUR TAPI PASANG SENDIRI (Jalur Dingin)
        $ yuuka_rel -= 1
        "{cps=35}Suasana mendadak menjadi sangat dingin saat aku masuk. Yuuka bahkan tidak mengangkat kepalanya untuk menatapku.{/cps}"
        y "{cps=40}Ketua, semua dokumen sudah siap. Kita tidak perlu menunggu penjelasan dari 'orang luar' yang tidak bisa menghargai waktu, kan?{/cps}"
        v "{cps=40}Duh, ada apa dengan suasana ini? Rasanya seperti aku sedang berada di dalam kulkas. Dingin sekali~{/cps}"
        "{cps=35}Yuuka memperlakukanku seperti benda mati. Kebohonganku pagi tadi benar-benar membangun benteng baja di antara kami.{/cps}"
        m "{cps=40}Tidak perlu sampai segitunya [y]{/cps}"
        m "{cps=40}Lagipula kita juga memerlukan dia{/cps}"
        y "{cps=40}Perlu? Untuk apa kak [m]?{/cps}"
        m "{cps=40}Habisnya kan dia satu-satunya anak laki disini{/cps}"
        m "{cps=40}Tenaga dia sangat bisa kita pakai{/cps}"
        y "{cps=40}Iya sih...{/cps}"

    elif jujur == False and pasang == True:
        # 4. MC GA JUJUR DAN DIPASANGIN MAYA (Jalur Pengkhianatan/Hancur)
        $ yuuka_rel -= 2
        "{cps=35}Begitu aku masuk, Yuuka berdiri secara tiba-tiba dari kursinya. Suara derit kursi itu terdengar sangat kasar di ruangan yang sunyi.{/cps}"
        y "{cps=40}Jadi ini alasanmu tidak jujur padaku tadi?{/cps}"
        y "{cps=40}Bukan cuma masuk OSIS secara diam-diam, tapi juga langsung menjadi 'peliharaan' kesayangan Ketua?{/cps}"
        v "{cps=40}Wah... wah... suasananya lebih panas dari yang kubayangkan. [mc], sepertinya kamu benar-benar melakukan dosa besar hari ini.{/cps}"
        "{cps=35}Yuuka menatapku dengan mata yang kosong. Bukan marah yang meledak-ledak, tapi sebuah kekecewaan yang sangat mendalam.{/cps}"
        m "{cps=40}Sudahlah [y], tadi kan tangan [mc] sakit, lagipula dia juga ingin memberimu surprise{/cps}"
        y "{cps=40}Ya... aku sudah mendapatkan surprise sih{/cps}"
        y "{cps=40}Saking terkejutnya dadaku sampai terasa sesak{/cps}"
        y "{cps=40}Kak [m], aku izin keluar dahulu, ingin menghirup udara segar{/cps}"
        m "{cps=40}Hah....{/cps}"

    # --- KEMBALI KE ALUR UTAMA RAPAT ---

    m "{cps=40}Sudah cukup dramanya. Kita di sini untuk bekerja, bukan untuk membuat sinetron picisan sore hari.{/cps}"
    "{cps=35}Maya mengetukkan pulpennya ke meja dengan keras. Suaranya yang otoriter seketika membungkam semua orang.{/cps}"
    if jujur == False and pasang == True:
        m "{cps=30}[y], jaga sikapmu! Tetaplah disini karena rapatnya mau aku mulai{/cps}"
        y "{cps=30}Hah... baik kak{/cps}"
        "{cps=30}[y] langsung mengambil tempat duduk yang rada jauh dibanding biasanya{/cps}"
    

    m "{cps=40}Jadi.. karena kalian adalah anggota baru, aku punya tugas pertama.{/cps}"
    m "{cps=40}tugas pertama untuk kalian adalah melakukan audit inventaris gudang aula.{/cps}"
    m "{cps=40}[mc], karena kamu anggota yang telat gabung, kamu harus belajar lapangan secepatnya. Kamu akan pergi ke gudang bersama Yuuka.{/cps}"
    v "{cps=40}Lalu kalau aku bagaimana kak?{/cps}"
    m "{cps=40}Kamu bantuin aku disini mengurus persuratan{/cps}"
    v "{cps=40}Heeee....{/cps}"
    m "{cps=40}Kamu tidak keberatan kan [y]?{/cps}"

    if yuuka_rel < 0:
        y "{cps=40}...Baik, Ketua. Saya akan membimbingnya... sebisanya.{/cps}"
        "{cps=35}Yuuka menjawab tanpa sedikit pun melihat ke arahku. Dia langsung berjalan menuju pintu dengan langkah yang cepat dan berat.{/cps}"
    else:
        y "{cps=40}Dimengerti{/cps}"

    scene black with fade
    stop music fadeout 3.0
    
    m "{cps=40}Setelah kalian dari gudang, hasil laporannya aku tunggu di ruangan ini, apakah bisa?{/cps}"
    y "{cps=40}Bisa kak{/cps}"
    m "{cps=40}Ada pertanyaan?{/cps}"
    y "{cps=40}Untuk saat ini tidak ada{/cps}"
    m "{cps=40}Baiklah, karena pembagian jobdesk sudah dilakukan, sekarang kalian kerjakan{/cps}"
    v "{cps=40}Selamat bersenang-senang di gudang yang berdebu itu ya, [mc].{/cps}"
    mc "{cps=40}Hei!{/cps}"
    "{cps=40}Aku kembali ke mejaku, menyiapkan semua yang dibutuhkan untuk melakukan audit{/cps}"
    v "{cps=60}Pssst... Specimen! Sini bentar.{/cps}"
    "{cps=35}Vina menarik ujung seragamku sampai aku hampir tersandung. Dia membawaku ke depan mejanya.{/cps}"

    mc "{cps=40}Apalagi sih, Vin? Aku harus segera ke gudang sama Yuuka.{/cps}"

    v "{cps=60}Justru itu! Kamu tahu nggak kenapa Maya-senpai kasih tugas itu ke kalian berdua?{/cps}"

    mc "{cps=40}Ya karena aku anggota baru dan Yuuka yang paling tahu prosedur audit?{/cps}"

    v "{cps=60}Cih! Polos banget.{/cps}"

    "{cps=35}Vina menepuk jidatnya sendiri. Dia lalu menyilangkan tangan di dada, menatapku dengan tatapan 'pakar cinta' gadungan.{/cps}"

    v "{cps=60}Maya-senpai itu nggak pernah kasih tugas berduaan kalau nggak ada maksudnya. Dia itu tipe yang efektif. Kalau cuma mau audit, satu orang juga cukup.{/cps}"

    v "{cps=60}Dia lagi ngasih 'ruang' buat kalian berdua. Dia tahu suasana di kelas tadi pagi kacau gara-gara hubunganmu dengan [y] memburuk kan?{/cps}"

    mc "{cps=40}Maksudmu... Maya-senpai sengaja bikin aku sama Yuuka baikan?{/cps}"

    v "{cps=60}Mungkin. Tapi jangan senang dulu. Maya-senpai itu nggak kasih 'hadiah' tanpa bayaran.{/cps}"

    v "{cps=60}Inget ya, Specimen. Maya-senpai itu nggak se-robot yang kamu kira. Dia lagi merhatiin kamu... entah kenapa, tatapannya ke kamu itu beda sama ke kita-kita.{/cps}"

    mc "{cps=40}Beda gimana?{/cps}"

    v "{cps=60}Nanti juga kamu tahu sendiri. Udah sana hus! Nanti pawangmu itu ngamuk lagi.{/cps}"

    # Yuuka manggil dari pintu
    if jujur and pasang == True:
        y "{cps=40}[mc]! Kamu ngapain sih lama banget? Ayo jalan!{/cps}"
    else:
        "{cps=40}Terlihat [y] di depan pintu ruangan dengan wajah yang sangat kesal{/cps}"

    v "{cps=60}Tuh kan, tanduknya udah keluar. Selamat berjuang, Specimen!{/cps}"

    if yuuka_rel < 0:
        "{cps=35}Disaat aku masih berbicara dengan [v]{/cps}"
        v "{cps=35}Sepertinya kamu harus bergegas deh [mc]...{/cps}"
        mc "{cps=35}Apa maksudmu?{/cps}"
        v "{cps=35}Lihat itu di depan pintu{/cps}"
        "{cps=40}[y] langsung pergi meninggalkanku{/cps}"
        mc "{cps=35}Hee!? [y] tunggu aku!{/cps}"
    else:
        y "{cps=40}A-apa sih kamu Vin, bukan berarti aku akan disana sampai malam ya{/cps}"
        v "{cps=40}Ehehe, siapa tahu kan...{/cps}"
        y "{cps=40}Ayo [mc], kita harus menyelesaikannya sebelum malam.{/cps}"
        mc "{cps=40}Baik. Ayo [y]{/cps}"


    "{cps=35}Rapat berakhir dengan perasaan yang campur aduk. Aku dan Yuuka kini berjalan menuju gedung aula yang terletak di area belakang sekolah.{/cps}"
    "{cps=35}Keheningan di sepanjang koridor ini terasa jauh lebih menyiksa daripada pelajaran Sejarah [t] tadi.{/cps}"
    mc "{cps=40}Ano... [y]...{/cps}"

    if jujur and pasang == False:
        # 1. Jalur Harmonis (Jujur & Mandiri)
        y "{cps=40}Hm? Ada apa?{/cps}"
        mc "{cps=40}Soal tadi... terima kasih ya sudah membelaku di depan Vina.{/cps}"
        y "{cps=40}A-apa sih, itu kan memang sudah tugas sesama anggota. Lagipula, aku senang kamu tidak aneh-aneh tadi.{/cps}"
        "{cps=35}Yuuka sedikit memperlambat langkahnya agar sejajar denganku. Suasana terasa jauh lebih ringan.{/cps}"

    elif jujur and pasang == True:
        # 2. Jalur Cemburu (Jujur tapi Dipasangin Maya)
        y "{cps=40}Masih tercium?{/cps}"
        mc "{cps=40}Eh? Apanya?{/cps}"
        y "{cps=40}Wangi parfum Kak Maya. Tadi jarak kalian dekat sekali, kan?{/cps}"
        mc "{cps=40}Itu... kan dia yang tiba-tiba memasangkannya.{/cps}"
        y "{cps=40}Hmph. Lain kali kalau mau minta tolong, bilang aku saja. Tidak usah merepotkan Ketua.{/cps}"
        "{cps=35}Yuuka berjalan sedikit lebih cepat, seolah ingin membuang rasa kesalnya ke udara.{/cps}"

    elif jujur == False and pasang == False:
        # 3. Jalur Kecewa (Ga Jujur & Mandiri)
        y "{cps=40}Simpan suaramu untuk menghitung barang nanti, [mc].{/cps}"
        mc "{cps=40}Yuuka, soal aku tidak bilang dari awal...{/cps}"
        y "{cps=40}Aku tidak butuh penjelasan sekarang. Aku cuma ingin tugas ini cepat selesai.{/cps}"
        "{cps=35}Yuuka sama sekali tidak menoleh. Jarak di antara kami terasa sangat jauh meski kami berjalan berdampingan.{/cps}"

    elif jujur == False and pasang == True:
        # 4. Jalur Hancur (Ga Jujur & Dipasangin Maya)
        y "{cps=40}...{/cps}"
        mc "{cps=40}Yuuka, tunggu sebentar. Dengarkan aku dulu...{/cps}"
        y "{cps=40}Jangan mendekat.{/cps}"
        mc "{cps=40}Memangnya aku salah apa sih? Sampai-sampai kamu sedingin ini?{/cps}"
        y "{cps=40}Tanya saja ke dirimu sendiri{/cps}"
        y "{cps=40}Fokus saja ke tugasmu. Aku di sini cuma menjalankan perintah Ketua, bukan sebagai temanmu.{/cps}"
        "{cps=35}Kata-katanya begitu tajam, lebih dingin daripada AC di ruang OSIS tadi. Aku hanya bisa tertunduk lesu di belakangnya.{/cps}"
    # --- KEMBALI KE NARASI UTAMA ---
    "{cps=35}Tak lama kemudian, kami sampai di depan sebuah pintu besi besar yang sudah sedikit berkarat.{/cps}"
    
    play sound "audio/sfx/door.mp3"
    "{cps=35}Suara derit pintu besi yang dibuka paksa memecah kesunyian area belakang sekolah.{/cps}"
    
    scene bg_warehouse_dark with dissolve
    "{cps=35}Bau debu dan kayu tua langsung menusuk hidung begitu kami melangkah masuk ke dalam gudang aula yang remang-remang.{/cps}"

    
    y "{cps=40}Cih, kotor banget... Kak Maya benar-benar memberikan kita 'harta karun' yang merepotkan.{/cps}"
    "{cps=35}Tanpa basa-basi, [y] langsung mencoba menggeser tumpukan kursi lipat yang berkarat. Suara besi yang beradu dengan lantai semen terdengar nyaring di ruangan sunyi ini.{/cps}"
    
    mc "{cps=40}Sini [y], biar aku bantu. Barang-barang ini terlalu berat kalau kamu sendiri yang angkat.{/cps}"

    if jujur and pasang == False:
        # 1. Jalur Harmonis (Jujur & Mandiri)
        y "{cps=40}Terima kasih, [mc].{/cps}"
        y "{cps=40}Maaf ya, tugas pertamamu di OSIS malah langsung kerja fisik begini. Tapi... setidaknya kita bisa menyelesaikannya berdua.{/cps}"
        "{cps=35}Yuuka tersenyum tipis ke arahku. Meskipun wajahnya sedikit kotor terkena debu, suasana di antara kami terasa sangat hangat.{/cps}"

    elif jujur and pasang == True:
        # 2. Jalur Cemburu (Jujur tapi Dipasangin Maya)
        y "{cps=40}Tidak usah. Lebih baik kamu simpan tenagamu untuk melayani 'Ketua' kesayanganmu itu.{/cps}"
        mc "{cps=40}Ayolah [y], jangan mulai lagi. Aku kan di sini sekarang bersamamu.{/cps}"
        y "{cps=40}Bisa saja kan nanti tiba-tiba dia memanggilmu lagi karena 'tanganmu pegal'?{/cps}"
        "{cps=35}Yuuka menghentak kursi itu dengan kasar. Dia benar-benar sedang menunjukkan taringnya karena kejadian di koridor tadi.{/cps}"

    elif jujur == False and pasang == False:
        # 3. Jalur Kecewa (Ga Jujur & Mandiri)
        y "{cps=40}Lakukan saja apa yang diperintahkan Ketua. Tidak perlu merasa kasihan padaku.{/cps}"
        mc "{cps=40}Aku tidak kasihan, aku cuma ingin membantu teman masa kecilku.{/cps}"
        y "{cps=40}Teman masa kecil?{/cps}"
        y "{cps=40}Kira-kira... teman masa kecil seperti apa yang merahasiakan hal sebesar ini, [mc]?{/cps}"
        "{cps=35}Yuuka berhenti bergerak. Dia menatap tumpukan debu di depannya dengan pandangan yang kosong dan terluka.{/cps}"

    elif jujur == False and pasang == True:
        # 4. Jalur Hancur (Ga Jujur & Dipasangin Maya)
        y "{cps=40}Jangan sentuh aku.{/cps}"
        "{cps=35}Yuuka menepis tanganku dengan kasar saat aku mencoba mengambil alih kotak yang dia bawa.{/cps}"
        mc "{cps=40}Yuuka, ini berbahaya kalau kamu paksakan sendiri!{/cps}"
        y "{cps=40}Lebih berbahaya mana dengan orang yang berpura-pura baik padaku tapi diam-diam tertawa di belakang bersama wanita lain?{/cps}"
        y "{cps=40}Kalau kamu memang tidak menganggapku penting, setidaknya jangan berikan harapan palsu dengan sok membantuku sekarang.{/cps}"
        "{cps=35}Suaranya bergetar. Dia benar-benar di ambang batas kesabarannya.{/cps}"

    # --- KEMBALI KE ALUR UTAMA AUDIT ---

    "{cps=35}Keheningan kembali menyelimuti gudang. Cahaya senja yang masuk dari celah atap mulai memanjang, menciptakan bayangan-bayangan raksasa di antara tumpukan barang rongsokan.{/cps}"

    y "{cps=40}Sudah, cepat buka buku laporannya. Kita mulai dari rak bagian timur.{/cps}"
    "{cps=35}Kami mulai bekerja dalam diam. Satu per satu barang kami data. Kursi, meja panggung, hingga peralatan festival tahun lalu yang sudah usang.{/cps}"
    
    # --- BAGIAN PENEMUAN PIALA & MISTERI ---
    mc "{cps=40}Yuuka, lihat ini...{/cps}"
    
    "{cps=35}Aku menarik sebuah piala perak dari tumpukan kain hitam yang berdebu. Piala itu terasa sangat berat dan dingin di tanganku.{/cps}"
    
    mc "{cps=40}'Vokal Terbaik'. Namanya... Kisaragi Sayoko.{/cps}"
    
    "{cps=35}Yuuka menghentikan catatannya. Dia menatap piala itu cukup lama, seolah-olah dia sedang melihat sebuah monumen kegagalan.{/cps}"
    
    y "{cps=40}Kisaragi Sayoko... {w=0.5} Diva legendaris yang tidak meninggalkan satu pun nyanyian resmi.{/cps}"
    
    mc "{cps=40}Apa maksudmu? Dia memenangkan piala ini, kan?{/cps}"
    
    y "{cps=40}Dia memang memenangkannya. Tapi Sayoko-senpai adalah satu-satunya pemenang yang tidak pernah lulus dari sekolah ini. Dia memilih untuk 'dropout' tepat sebelum hari kelulusannya.{/cps}" # Trivia [4] & [7]
    
    mc "{cps=40}Dia keluar? Kenapa?{/cps}"
    
    y "{cps=40}Katanya dia ingin fokus ke dunia profesional. Tapi di balik itu, ada rumor bahwa suaranya 'terlalu kuat' untuk standar sekolah.{/cps}" # Trivia [22]
    
    y "{cps=40}Guru vokal saat itu bilang, gayanya terlalu menonjolkan emosi mentah daripada mengikuti melodi. Baginya, musik bukan soal nada yang tepat, tapi soal teriakan jiwa.{/cps}" # Trivia [22]

    mc "{cps=40}Tunggu, di bawah sini ada ukiran kecil... 'Kisa'.{/cps}" 
    
    y "{cps=40}Ah, itu nama panggilannya. Tapi konon dia sangat benci dipanggil begitu. Dia merasa nama itu seperti barang produksi masal, padahal dia ingin menjadi dirinya sendiri.{/cps}"
    
    mc "{cps=40}Kisaragi Sayoko... {w=0.5} Nama ini benar-benar terasa familiar.{/cps}"

    mc "{cps=40}Kalau tidak salah, pembawa acara saat penerimaan kemarin marganya juga Kisaragi, kan? Fumi-san.{/cps}"
    
    y "{cps=40}Sudah kubilang, itu hanya kebetulan, [mc]. Sayoko-senpai itu sempurna, sedangkan pembawa acara kemarin... yah, dia kurang cocok untuk punya hubungan dengan 'Diva' sehebat Kisa.{/cps}" 
    
    y "{cps=40}Satu hal lagi. Alasan dia disebut 'Diva Tanpa Lagu' adalah karena tidak ada agensi yang berani merilis rekamannya. Suaranya dianggap 'berbahaya' karena terlalu jujur.{/cps}" # Trivia [22]
    
    mc "{cps=40}(Diva tanpa lagu... janji yang tidak terpenuhi... Kenapa sejarah sekolah ini seolah-olah mencoba menghapus suaranya?){/cps}"

    "{cps=35}Aku meletakkan piala Sayoko-senpai kembali ke rak. Namun, nama 'Kisa' seolah-olah terus berbisik di telingaku, menuntut untuk diingat kembali.{/cps}"

    "{cps=35}Aku harus mencari tahu apa yang sebenarnya terjadi 5 tahun lalu.{/cps}"
    
    y "{cps=40}Hei! Malah melamun lagi. Cepat bagi tugas, aku akan mengecek bagian tengah.{/cps}"
    
    jump warehouse_audit_loop

# --- MINIGAME AUDIT LOOP ---

label warehouse_audit_loop:
    if spots_searched >= 3:
        jump box_accident_scene 

    "{cps=35}Gudang ini terasa jauh lebih besar dan gelap dari yang terlihat dari luar. Di mana aku harus mulai mencari inventaris?{/cps}"

    menu:
        "Periksa Rak Besi di pojok" if not check_rak:
            $ check_rak = True
            $ spots_searched += 1
            "{cps=35}Aku mendekati rak besi yang sudah miring. Isinya adalah tumpukan piala tua yang sudah kusam.{/cps}"
            
            if jujur and pasang == False:
                y "{cps=40}Hati-hati, [mc]. Rak itu agak goyang. Sini, aku bantu pegangi bawahnya.{/cps}"
                mc "{cps=40}Terima kasih, Yuuka. Kamu perhatian sekali.{/cps}"
            
            elif jujur and pasang == True:
                y "{cps=40}Jangan sampai piala itu jatuh. Nanti kamu repot harus lapor ke 'Ketua' kesayanganmu itu.{/cps}"
                mc "{cps=40}Yuuka... masih soal itu ya?{/cps}"
            
            else: # Jalur Kecewa/Hancur
                y "{cps=40}Cepat catat nomor inventarisnya. Tidak usah banyak tanya.{/cps}"
            jump warehouse_audit_loop

        "Cek Tumpukan Meja Panggung" if not check_meja:
            $ check_meja = True
            $ spots_searched += 1
            "{cps=35}Meja-meja kayu ini sangat berat. Aku harus menggesernya sedikit untuk melihat stiker kode barang.{/cps}"
            
            if jujur == False:
                "{cps=35}Aku kesulitan menggeser meja itu sendiri. Yuuka melihatku, tapi dia hanya diam dan terus menulis di papan jalannya.{/cps}"
                mc "{cps=40}(Dingin sekali... sepertinya kebohonganku benar-benar membuatnya menutup diri.){/cps}"
            
            elif pasang == True:
                y "{cps=40}Minta tolong saja pada kak [m] kalau kamu tidak kuat. Dia kan suka membantu 'orang' sepertimu.{/cps}"
                mc "{cps=40}Kak [m] tidak ada di sini, Yuuka. Aku ingin kamu yang membantuku.{/cps}"
                y "{cps=40}Hmph.{/cps}"
            
            else:
                y "{cps=40}Sini, aku bantu dorong dari sebelah kiri. Satu... dua... tiga!{/cps}"
            jump warehouse_audit_loop

        "Geledah Peti Kayu di bawah jendela" if not check_peti:
            $ check_peti = True
            $ spots_searched += 1
            "{cps=35}Peti kayu ini berisi dekorasi festival sekolah yang sudah usang. Ada aroma melati kering yang aneh di dalamnya.{/cps}"
            
            mc "{cps=40}Yuuka, lihat ini. Ada selebaran konser musik tahun 2014...{/cps}"
            
            if jujur and pasang == False:
                y "{cps=40}2014? Itu kan masa jabatannya... {w=0.5} Ah, lupakan. Ayo fokus kerja lagi.{/cps}"
                mc "{cps=40}(Dia menyembunyikan sesuatu? Reaksinya sama seperti Maya-senpai.){/cps}"
            
            elif jujur == False and pasang == True:
                y "{cps=40}Tutup saja petinya. Kamu tidak butuh tahu soal masa lalu sekolah ini. Urus saja masa depanmu di OSIS.{/cps}"
            
            else:
                y "{cps=40}Simpan saja itu. Mungkin nanti bisa jadi referensi proker kita.{/cps}"
            jump warehouse_audit_loop

label box_accident_scene:
    "{cps=35}Suara derit besi dan gesekan kayu seolah menjadi melodi monoton yang menemani kami selama satu jam terakhir. Punggungku mulai terasa kaku, dan telapak tanganku sudah menghitam karena debu yang menempel.{/cps}"
    "{cps=35}Aku menyeka keringat yang menetes di pelipis. Di dalam gudang yang tertutup ini, sirkulasi udara terasa sangat minim, membuat setiap helai napas terasa lebih berat.{/cps}"
    "{cps=35}Aku melirik ke arah Yuuka. Cahaya matahari yang masuk dari celah atap mulai bergeser, menyinari debu-debu yang beterbangan di sekitarnya. Dia masih tampak tekun, meski sesekali dia memijat bahunya sendiri.{/cps}"
    play sound "audio/sfx/phone notif.mp3"
    "{cps=35}Tiba-tiba ponselku bergetar. Sebuah panggilan dari Vina.{/cps}"
    
    mc "{cps=40}Halo, Vin? Ada apa? Kami sedang sibuk di gudang.{/cps}"

    # Suara Vina di telepon (Gunakan gaya bicara yang cepat dan ceria)
    v "{cps=60}Halo halo! Specimen kebanggaanku masih bernapas? Atau sudah pingsan kena debu kursi tahun 90-an?{/cps}"
    
    mc "{cps=40}Kami sedang sibuk, Vin. Kalau cuma mau meledek, nanti saja.{/cps}"

    v "{cps=60}Fufufu, galak sekali. Aku cuma mau bilang, tadi aku nemu berkas pendaftaranmu. Kamu tahu nggak, Maya-senpai menulis catatan kecil di pojok kertasmu?{/cps}"
    mc "{cps=40}Catatan apa?{/cps}"
    v "{cps=60}Hmm... kasih tahu nggak ya? Bayarannya mahal lho. Kamu harus bawain aku minuman kaleng dari mesin otomatis belakang aula setelah selesai audit.{/cps}"
    mc "{cps=40}Yang bener kamu?{/cps}"


    # --- PERCABANGAN BERDASARKAN KONDISI ---

    if jujur and pasang == False:
        v "{cps=60}Ah nggak kok, aku cuma mau bilang, tadi aku nemu cokelat di laci meja OSIS-mu. Karena kamu anak baik yang jujur sama Yuuka, cokelatnya nggak aku makan deh. Aku simpen buat kamu nanti sore!{/cps}"
        mc "{cps=40}Cuma buat bilang itu? Kamu menelepon di saat yang tidak tepat, Vin.{/cps}"
        v "{cps=60}Fufufu, anggap saja ini 'moral support'. Semangat ya, jangan sampai Yuuka nambahin daftar inventarisnya dengan namamu!{/cps}"

    elif jujur and pasang == True:
        v "{cps=60}Hayo... lagi berduaan ya? Bau parfum Maya-senpai di bahumu sudah hilang belum?{/cps}"
        "{cps=35}Aku melirik Yuuka. Dia langsung menajamkan telinganya, mencoba mencuri dengar pembicaraan kami.{/cps}"
        v "{cps=60}Tadi Yuuka mukanya lucu banget pas liat kalian di koridor. Kayak mau makan orang! Hati-hati ya, jangan sampai ada 'kecelakaan' tak sengaja di gudang gelap itu. Dadah!{/cps}"
        mc "{cps=40}Vin! Tunggu—{/cps}"

    elif jujur == False and pasang == False:
        v "{cps=60}Specimen... suaramu kedengeran tertekan banget. Yuuka lagi mode diam ya?{/cps}"
        v "{cps=60}Makanya, lain kali jangan sok misterius. Rahasia itu kayak bom waktu, dan sepertinya bommu meledak duluan sebelum sampai gudang. Mau aku bawain air minum biar nggak seret?{/cps}"
        mc "{cps=40}Nggak perlu, Vin. Tutup teleponnya sekarang.{/cps}"

    elif jujur == False and pasang == True:
        v "{cps=60}Gila... kamu beneran 'suicidal' ya. Bohongin temen masa kecil, terus dapet servis ban lengan dari Ketua.{/cps}"
        v "{cps=60}Aku cuma mau cek aja sih, kamu masih punya semua anggota tubuh lengkap kan? Soalnya Yuuka tadi liat kalian di koridor dengan tatapan yang... wah, ngeri deh pokoknya.{/cps}"
        v "{cps=60}Selamat berjuang bertahan hidup ya! Fufufu!{/cps}"
            
    y "{cps=40}[mc]! Siapa itu? Cepat matikan dan bantu aku geser rak ini!{/cps}"
    v "{cps=60}Ups, 'Nyonya Besar' marah. Semangat ya, dadah!{/cps}"
    
    stop sound
    "{cps=35}Vina mematikan telepon secara sepihak. Aku hanya bisa menghela napas, sementara Yuuka menatapku dengan tatapan menyelidik.{/cps}"
    "{cps=35}Sudah hampir empat puluh menit kami berkutat dengan tumpukan besi dan kayu ini. Napas Yuuka mulai terdengar berat, dan kulihat ada butiran keringat di pelipisnya.{/cps}"

    mc "{cps=40}Yuuka, istirahat dulu yuk. Aku tadi sempat beli minuman dingin di mesin otomatis.{/cps}"
    
    y "{cps=40}Hah... {w=0.5}boleh juga. Tanganku juga sudah mulai kaku karena mencatat terus.{/cps}"

    "{cps=35}Kami duduk berdampingan di atas peti kayu yang cukup kokoh. Suara kaleng soda yang dibuka—*Pshhh!*—terasa sangat nyaring di tengah sunyinya gudang.{/cps}"

    # Dialog ini bisa sangat panjang tergantung variabel
    if yuuka_rel > 0:
        "{cps=35}Yuuka menyandarkan kepalanya sebentar di dinding. Suasananya terasa sangat damai meskipun tempat ini kotor.{/cps}"
        y "{cps=40}Ingat tidak dulu kita sering main petak umpet sampai ke halaman belakang sekolah lama?{/cps}"
        mc "{cps=40}Iya, dan kamu selalu menangis kalau tidak bisa menemukanku.{/cps}"
        y "{cps=40}Itu karena kamu sembunyinya terlalu niat, bodoh!{/cps}"
    else:
        "{cps=35}Kami duduk dengan jarak sekitar satu meter. Yuuka meminum sodanya dengan cepat, matanya menatap kosong ke arah deretan kursi.{/cps}"
        mc "{cps=40}Yuuka... maaf ya.{/cps}"
        y "{cps=40}Simpan maafmu. Cepat habiskan minumnya, kita masih punya banyak rak untuk dicek.{/cps}"

    "{cps=35}Momen istirahat ini terasa seperti jeda di tengah badai. Aku menyadari bahwa di balik semua organisasi dan rahasia ini, kami tetaplah dua orang yang sedang mencoba memahami satu sama lain.{/cps}"
    
    "{cps=35}Kami melanjutkan audit sekitar 30 menit dengan penuh keheningan. Sampai akhirnya...{/cps}"
    mc "{cps=35}Sip, barang terakhir sudah dicatat{/cps}"
    mc"{cps=35}[y], bagianmu sudah selesai belum?{/cps}"
    "{cps=40}Ketika aku memalingkan wajahku ke hadapan yuuka{/cps}"
    "{cps=40}Tiba-tiba ada setumpuk kardus yang terjatuh{/cps}"
    mc"{cps=40}[y]! Awas!{/cps}"
    y "{cps=40}Hah?{/cps}"
    "{cps=40}Aku mendorong [y] agar tidak tertimpa oleh kardus tersebut{/cps}"
    "{cps=40}{b}*BRAK{/b}{/cps}"
    y "{cps=40}Aduh....{/cps}"
    mc "{cps=40}[y]... kamu tidak apa....{/cps}"
    mc "{cps=40}Apa....?{/cps}"
    "{cps=40}Suasana sangat gelap{/cps}"
    "{cps=40}Aku hampir tidak bisa memegang apapun{/cps}"
    "{cps=40}Hei.... bisa menyingkir tidak?{/cps}"
    mc "{cps=40}Hah..?{/cps}"
    show bg tester with fade
    "{cps=40}LOH!?{/cps}"
    "{cps=40}Kok aku di atasnya [y]?{/cps}"
    "{cps=40}Jantungku berdegup sangat kencang. Aroma debu di gudang ini mendadak tertutup oleh aroma lembut dari rambut [y] yang berada tepat di bawahku.{/cps}"
    "{cps=40}Napasnya yang memburu terasa di leherku. Di kegelapan ini, hanya sepasang matanya yang terlihat berkilau menatapku.{/cps}"

    # --- LANJUTAN SAAT MC MASIH DI ATAS YUUKA ---

    "{cps=35}Suasana mendadak menjadi sangat sunyi. Hanya ada suara napas kami yang saling beradu di kegelapan gudang. Jantungku berdegup sangat kencang, seolah ingin melompat keluar dari dadaku.{/cps}"

    if jujur and pasang == False:
        # 1. Jalur Harmonis (Jujur & Mandiri)
        $ yuuka_rel += 5
        y "{cps=40}[mc]... {w=0.5}kamu mau di atas sana sampai kapan?{/cps}"
        mc "{cps=40}A-ah! Maaf! Tadi benar-benar refleks karena kardus itu...{/cps}"
        "{cps=35}Aku segera bangkit dengan terburu-buru, hampir saja tersandung kakiku sendiri. Yuuka perlahan duduk sambil merapikan rambutnya yang berantakan.{/cps}"
        y "{cps=40}T-terima kasih sudah menyelamatkanku. Tapi... jantungmu berisik sekali, tahu. Sampai terdengar ke telingaku.{/cps}"
        mc "{cps=40}Siapa yang tidak deg-degan dalam situasi seperti itu!{/cps}"
        y "{cps=40}Fufufu... benar juga. Tapi setidaknya, aku senang kamu yang ada di sini sekarang.{/cps}"
        "{cps=35}Yuuka tersenyum tipis. Meskipun gelap, aku bisa merasakan suasana di antara kami menjadi lebih hangat. Luka kecil karena ketegangan tadi pagi seolah mulai menutup.{/cps}"
        "{cps=35}Kami berdua perlahan berdiri, menjauh satu sama lain untuk merapikan seragam masing-masing dalam keheningan yang menyesakkan.{/cps}"

    elif jujur and pasang == True:
        # 2. Jalur Cemburu (Jujur tapi Dipasangin Maya)
        $ yuuka_rel += 2
        y "{cps=40}Lepaskan...{/cps}"
        mc "{cps=40}Tunggu, [y]. Kamu tidak luka, kan? Tadi kardusnya berat sekali.{/cps}"
        y "{cps=40}Aku tidak apa-apa. Cepat menyingkir... Bau parfum 'dia' di bajumu ini benar-benar membuatku sesak.{/cps}"
        mc "{cps=40}Yuuka, soal Maya-senpai tadi... aku benar-benar minta maaf kalau itu membuatmu tidak nyaman.{/cps}"
        y "{cps=40}Kenapa tidak minta tolong padaku saja? Padahal aku selalu ada di sampingmu...{/cps}"
        y "{cps=40}Apa kamu lebih suka disentuh oleh orang hebat seperti Ketua daripada oleh teman masa kecilmu yang biasa saja ini?{/cps}"
        mc "{cps=40}Bukan begitu! Aku hanya... aku tidak ingin merepotkanmu terus.{/cps}"
        y "{cps=40}Dengan menjauh dariku, kamu justru membuatku merasa lebih dari sekadar direpotkan, [mc]. Kamu membuatku merasa tidak dibutuhkan.{/cps}"
        mc "{cps=40}Nggak begitu...{/cps}"
        mc "{cps=40}Kalau aku tidak membutuhkanmu, lantas siapa yang menemaniku selama aku sendiri{/cps}"
        y "{cps=40}I-iya sih... kamu kan juga selalu sendirian{/cps}"
        y "{cps=40}Lagipula kan aku jarang melihatmu main diluar{/cps}"
        "{cps=35}Kami berdua perlahan berdiri, menjauh satu sama lain untuk merapikan seragam masing-masing dalam keheningan yang menyesakkan.{/cps}"

    elif jujur == False and pasang == False:
        # 3. Jalur Kecewa (Ga Jujur & Mandiri)
        $ yuuka_rel += 2
        y "{cps=40}Apa yang kamu lakukan?{/cps}"
        mc "{cps=40}Aku cuma tidak ingin kamu terluka, Yuuka. Tadi itu bahaya.{/cps}"
        y "{cps=40}Lalu kenapa? Kenapa tiba-masing jadi peduli sekarang?{/cps}"
        y "{cps=40}Kamu bisa menyembunyikan hal sebesar OSIS dariku, tapi sekarang kamu bertingkah seolah-olah kamu adalah pelindungku?{/cps}"
        mc "{cps=40}Aku minta maaf. Aku hanya ingin memberimu kejutan{/cps}"
        y "{cps=40}Tapi kan tidak perlu sampai segitunya..{/cps}"
        mc "{cps=40}Kamu tidak marah kan?{/cps}"
        mc "{cps=40}Tidak sih [mc]... setelah kamu menjelaskannya tadi..{/cps}"
        y "{cps=40}Namun rasanya... aku seperti orang asing bagimu.{/cps}"
        mc "{cps=40}Sudahlah, ayo berdiri{/cps}"
        "{cps=35}Kami berdua perlahan berdiri, menjauh satu sama lain untuk merapikan seragam masing-masing dalam keheningan yang menyesakkan.{/cps}"

    elif jujur == False and pasang == True:
        # 4. Jalur Hancur (Jalur yang kamu buat di Koikatsu)
        $ yuuka_rel += 1
        y "{cps=40}Singkirkan tanganmu, Ikazaki.{/cps}"
        mc "{cps=40}[y], aku—{/cps}"
        y "{cps=40}Jangan panggil namaku! {w=0.1}Jangan sentuh aku dengan tangan yang disentuh olehnya!{/cps}" with vpunch
        y"{cps=30}Hiks... hiks{/cps}"
        "{cps=40}Tiba-tiba aku merasakan setetes cairan hangat jatuh di punggung tanganku.{/cps}"
        "{cps=40}Dia... menangis?{/cps}"
        "{cps=35}Isakannya terdengar sangat pilu di ruangan yang pengap ini.{/cps}"
        y "{cps=40}Kenapa kamu harus membuatku terlihat seperti orang bodoh yang mengkhawatirkanmu sendirian selama ini?{/cps}"
        mc "{cps=43}[y], aku mau jujur!{/cps}"
        y "{cps=40}Apalagi yang mau kamu bicarakan! Sudahlah cepat menyingkir!{/cps}"
        mc "{cps=40}Dengarkan aku dulu!{/cps}"
        mc "{cps=40}Aku masuk ke OSIS ini murni karena aku ingin bersamamu!{/cps}"
        y "{cps=40}Terus? Kamu mau berbohong sampai kapan?{/cps}"
        mc "{cps=40}Aku nggak bohong!{/cps}"
        mc "{cps=40}Kan kamu sendiri kan yang memintaku untuk bergabung dari awal{/cps}"
        y "{cps=40}Memang sih...{/cps}"
        y "{cps=40}Tapi kamu selalu saja berbohong..{/cps}"
        y "{cps=40}Mengenai kak [m].. lalu [sh]... Organisasi...{/cps}"
        y "{cps=40}Mau sampai kapan kamu berbohong [mc]!{/cps}"
        y "{cps=40}Hiks.... hiks...{/cps}"
        mc "{cps=40}Aku memang berencana untuk memberimu kejutan...{/cps}"
        y "{cps=40}Kejutan? memang kok kamu sudah membuatku terkejut{/cps}"
        y "{cps=40}Saking terkejutnya aku sampai jadi begini...{/cps}"
        y "{cps=40}Kamu jahat..{/cps}"
        mc "{cps=40}Kejadian tadi memang tidak bisa dihindari [y]{/cps}"
        mc "{cps=40}Kan kamu tahu sendiri kalau tanganku sakit kan{/cps}"

        if correct_answer == False:
            y "{cps=40}Iya sih... {w=0.3}kamu memang terlihat kesulitan tadi.{/cps}"
            y "{cps=40}Tapi tetap saja... {w=0.3}apa aku sama sekali tidak bisa diandalkan sampai kamu lebih memilih bantuan Kak [m]?{/cps}"
            "{cps=35}Yuuka membuang muka. Meskipun dia sedikit menerima alasanmu, luka di hatinya masih terlalu lebar.{/cps}"
            mc "{cps=40}Bukan begitu... kan aku pikir kamu tidak ada di lokasi{/cps}"
            mc "{cps=40}Jadi wajar kan kalau aku minta bantuannya{/cps}"
            y "{cps=40}Kamunya aja yang tidak peka... Bodoh..{/cps}"
            mc "{cps=40}Sudahlah... Ayo berdiri..{/cps}"
            
        else:
            y "{cps=40}Berbohong lagi!{/cps}"
            y "{cps=40}Tadi di depan Nanami-sensei kamu baik-baik saja! Kamu bahkan menjawab semuanya dengan lancar!{/cps}"
            y "{cps=40}Mau sampai kapan sih kamu menganggapku sebagai orang bodoh yang bisa kamu tipu terus-menerus, [mc]...{/cps}"
            "{cps=40}Bukan begitu..{/cps}"
            y "{cps=40}{b}LALU APA!?{/b}{/cps}"
            y "{cps=40}Aku sudah muak denganmu{/cps}"
            y "{cps=40}Sekarang menyingkirlah{/cps}"
            "{cps=40}Tapi [y]-{/cps}"
            y "{cps=40}{b}MINGGIR!{/b}{/cps}"
            "{cps=35}Yuuka mendorong bahuku dengan sisa tenaganya. Penolakan itu terasa jauh lebih menyakitkan daripada tamparan.{/cps}"
            "{cps=35}Yuuka menutupi wajahnya dengan kedua tangan. Tangisannya mereda menjadi isakan kecil yang menyesakkan dada. Di gudang yang gelap ini, aku merasa seperti penjahat paling kejam.{/cps}"
    "{cps=35}Aku mulai memunguti kardus-kardus yang terjatuh tadi, sementara Yuuka hanya berdiri mematung di sudut gudang{/cps}"

    if jujur == False and pasang == True:
        "{cps=35}mencoba menghapus sisa air matanya.{/cps}"
    
    "{cps=35}Di antara tumpukan dokumen yang berserakan akibat kardus yang jatuh tadi, sebuah buku dengan menarik perhatianku.{/cps}"

    "{cps=35}Aku memungutnya. Di sampulnya, tertulis sebuah nama dengan tinta emas yang masih terlihat jelas... nama kakakku.{/cps}"

    mc "{cps=40}Ini... {w=0.5}milik Kakak?{/cps}"

    "{cps=35}Aku membuka map itu. Lembaran di dalamnya berisi konsep acara yang sangat mendetail. Judulnya: {b}'Festival Live Konser'{/b}.{/cps}"

    # --- REAKSI YUUKA BERDASARKAN 4 JALUR ---

    if jujur and pasang == False:
        # Jalur 1: Harmonis
        "{cps=35}Yuuka mendekat, rasa marahnya sudah benar-benar hilang digantikan rasa kagum.{/cps}"
        y "{cps=40}Wooo! Apa itu [mc]?{/cps}"
        mc "{cps=40}Sepertinya... ini proposal kakakku{/cps}"
        y "{cps=40}Oh iya! dipikir-pikir dia kan dulu anggota osis kan?{/cps}"
        y "{cps=40}Soalnya aku pernah melihat fotonya dirumahmu{/cps}"
        mc "{cps=40}Iya sih.. Namun sayangnya aku tidak terlalu ingat..{/cps}"
        mc "{cps=40}Karena kan sudah 10 tahun dia tiada...{/cps}"
        y "{cps=40}Mungkin begini [mc]{/cps}"
        y "{cps=40}Dia ingin membuktikan kalau sastra bisa dinikmati lewat musik. Jadi, dia benar-benar menyusun proposalnya?{/cps}"
        y "{cps=40}Tapi sepertinya ini tidak pernah sampai ke tahap rapat OSIS karena dia telah tiada{/cps}"

    elif jujur and pasang == True:
        # Jalur 2: Cemburu tapi Melunak
        "{cps=35}Yuuka melihat ke arah buku itu dari balik bahuku{/cps}"
        y "{cps=40}Buku itu... bukannya proposal kegiatan?{/cps}"
        mc "{cps=40}Sepertinya sih...{/cps}"
        y "{cps=40}Kenapa bisa ada di sini?{/cps}"
        "{cps=40}Kami terus membaca proposal itu{/cps}"

    elif jujur == False and pasang == False:
        # Jalur 3: Kecewa (Dingin)
        "{cps=35}Yuuka hanya melirik sekilas, namun ada kilat pengakuan di matanya.{/cps}"
        y "{cps=40}Jadi itu alasanmu masuk OSIS? Ingin melanjutkan apa yang gagal dilakukan Kakakmu?{/cps}"
        mc "{cps=40}Ya begitulah...{/cps}"
        y "{cps=40}Kalau iya, kenapa tidak bilang saja? Kenapa harus pakai drama rahasia segala?{/cps}"
        mc "{cps=40}Bukan begitu...{/cps}"
        "{cps=40}Kami terus membaca isi proposal itu{/cps}"

    elif jujur == False and pasang == True:
        # Jalur 4: Hancur (Broken)
        "{cps=35}Yuuka masih mengusap matanya yang sembab, tapi dia tertegun melihat nama yang tertera di sana.{/cps}"
        y "{cps=40}Ikazaki...{w=0.3} [mi]...{/cps}"
        y "{cps=40}Tunggu... bukankah ini kakakmu?{/cps}"
        "{cps=35}Dia mendekat perlahan, jemarinya yang gemetar menyentuh pinggiran buku yang sudah usang itu.{/cps}"
        mc "{cps=40}Iya. Sepertinya ini miliknya.{/cps}"
        y "{cps=40}Pantas saja kamu dari tadi bersikap seperti ini...{/cps}"
        "{cps=35}Suaranya melembut, seolah rasa sedihnya atas perilaku [mc] kini bersatu dengan rasa simpati atas kehilangan kakaknya.{/cps}"

    # --- KEMBALI KE ALUR UTAMA ---

    mc "{cps=40}Lihat, Yuuka. Di halaman terakhir... tidak ada stempel dari Bagian Kesiswaan. Ditambah, tidak ada tanda tangan Kepala sekolah periode itu.{/cps}"

    y "{cps=40}Aneh... bukannya Kakakmu adalah Ketua saat itu. Kenapa tidak dijalankan?{/cps}"

    mc "{cps=40}Aku tidak tahu. Tapi sepertinya aku akan membawa ini ke ruang OSIS{/cps}"

    y "{cps=40}Kamu yakin? Maya-senpai mungkin tidak akan suka{/cps}"

    mc "{cps=40}Aku harus tahu kenapa impian Kakakku berakhir di gudang ini.{/cps}"

    scene black with fade
    stop music fadeout 2.0

    "{cps=35}Keheningan gudang kini berganti dengan tekad yang baru. Kami berjalan keluar, meninggalkan debu masa lalu, menuju cahaya ruang OSIS yang sudah menunggu dengan sejuta tanya.{/cps}"

    scene bg_council_room_sunset with fade
    play music "audio/bgm/tiptoeing around.mp3" fadein 2.0

    "{cps=35}Cahaya oranye matahari sore kini jauh lebih redup, menyisakan bayangan panjang di lantai ruang OSIS yang sunyi.{/cps}"
    "{cps=35}Vina sedang asyik dengan tumpukan kertas, sementara Maya-senpai duduk tenang sambil menatap jendela, seolah sedang menunggu sesuatu.{/cps}"

    show maya_stern at center
    show vina_smile at right
    with dissolve

    v "{cps=40}Oho! Para pekerja keras kita sudah kembali. Bagaimana udaranya? Segar atau penuh debu?{/cps}"

    # Reaksi Yuuka masuk ruangan
    if yuuka_rel < 0:
        show yuuka_sad at left with dissolve
        "{cps=35}Yuuka masuk tanpa suara, matanya masih sedikit kemerahan. Dia langsung pindah ke sudut ruangan, menjauh dariku.{/cps}"
    else:
        show yuuka_determined at left with dissolve
        "{cps=35}Yuuka masuk mendahuluiku, membawa papan jalan audit dengan wajah yang sangat serius.{/cps}"

    m "{cps=40}Kulihat kalian membawa laporan inventarisnya. Letakkan saja di meja.{/cps}"

    "{cps=35}Aku melangkah maju. Tapi alih-alih memberikan daftar audit, aku meletakkan buku yang kusam itu tepat di hadapan Maya-senpai.{/cps}"

    play sound "audio/sfx/jatoh.mp3"
    "{b}*BRAK!*{/b}"

    mc "{cps=40}Kami menemukan ini di tumpukan paling bawah, Senpai. Terkubur di bawah kardus-kardus yang seharusnya sudah dibuang.{/cps}"

    # Vina mendekat karena penasaran
    v "{cps=40}Eh? Apa ini? Buku proposal? Sepertinya aku belum pernah melihat arsip dengan seperti ini...{/cps}"
    
    "{cps=35}Vina mencoba meraih map itu, tapi gerakan tangan Maya-senpai jauh lebih cepat. Dia menahan map itu dengan telapak tangannya.{/cps}"

    "{cps=35}Suasana mendadak menjadi sangat dingin. Aku bisa melihat jari-jari Maya sedikit menegang saat membaca nama di sampulnya.{/cps}"

    m "{cps=40}...Ikazaki [mi].{/cps}"

    mc "{cps=40}Itu milik kakakku, Senpai. Dia meninggal 12 tahun yang lalu saat masih menjabat sebagai Ketua di sini.{/cps}"
    mc "{cps=40}Kenapa proposal 'Festival Live Konser' miliknya berakhir menjadi sampah di gudang?{/cps}"

    m "{cps=40}...{/cps}"

    y "{cps=40}Kami juga memeriksa halaman terakhirnya, Kak Maya. Tidak ada stempel kesiswaan, tidak ada tanda tangan kepala sekolah.{/cps}"
    y "{cps=40}Seolah-olah... proposal ini sengaja dihilangkan sebelum sempat dibahas.{/cps}"

    v "{cps=40}Wah, ini... drama sejarah yang cukup berat ya?{/cps}"

    "{cps=35}Maya-senpai perlahan mengangkat wajahnya. Matanya yang biasanya tajam kini terlihat kosong, seakan sedang melihat sesuatu yang sangat jauh di masa lalu.{/cps}"

    m "{cps=40}[mc], ada alasan kenapa beberapa hal lebih baik tetap terkubur bersama debu di gudang itu.{/cps}"

    mc "{cps=40}Alasan apa? Apakah karena proposal ini berhubungan dengan alasan kenapa Kakakku...{/cps}"

    m "{cps=40}{b}CUKUP!{/b}{/cps}"

    play sound "audio/sfx/punch.mp3"
    "{cps=35}Maya membentak. Kali ini suaranya bukan hanya marah, tapi ada nada getaran ketakutan yang tertahan. Tangannya yang menekan map itu terlihat gemetar.{/cps}"

    m "{cps=40}Kamu tidak tahu apa-apa, [mc]. Kamu hanya melihat ini sebagai 'impian' yang terbuang...{/cps}"
    m "{cps=40}Tapi bagiku, dan para senior terdahulu... buku ini adalah alasan kenapa sekolah ini kehilangan 'suaranya'.{/cps}"

    mc "{cps=40}Apa maksudmu, Senpai? Apa hubungannya konser ini dengan kematian kakakku?{/cps}"
    mc "{cps=43}Memangnya apa sih yang membuat ini seperti terkutuk?{/cps}"

    m "{cps=40}Belum waktunya kamu tahu [mc]{/cps}"


    if yuuka_rel < 0:
        # Yuuka yang hancur tapi tetap berani membela sedikit
        y "{cps=40}Tapi Kak... ini soal keluarga [mc]. Kakak tahu kan kalau dia ingin mengetahui yang sebenarnya{/cps}"
    else:
        y "{cps=40}Ketua, aku rasa [mc] berhak tahu. Jika OSIS periode ini ingin transparan, mulailah dari hal ini.{/cps}"

    m "{cps=35}Kalian ingin tahu yang sebenarnya?{/cps}"
    mc "{cps=35}Iya kak{/cps}"
    m "{cps=35}Yakin tidak menyesal?{/cps}"
    "[mc],[v], dan [y]" "Iya kak"
    m "{cps=35}Baiklah kalau begitu{/cps}"
    m "{cps=35}Ini dari cerita terdahulu ya{/cps}"
    m "{cps=35}Waktu dimana kakakmu masih menjabat menjadi ketua{/cps}"
    m "{cps=35}Dia adalah panutan bagi seluruh murid disini{/cps}"
    m "{cps=35}Seorang ketua... sekaligus diva di mata semua murid{/cps}"
    m "{cps=35}Termasuk para guru{/cps}"
    m "{cps=35}Aku pun juga mengagumi kakakmu, karena kakakku juga sekolah disini di waktu yang sama{/cps}"
    m "{cps=35}Dan karena kakakku dan kakakmu adalah anggota osis{/cps}"
    m "{cps=35}Jadi mereka sering berkumpul bersama{/cps}"
    m "{cps=35}Aku juga kadang-kadang memperhatikan mereka{/cps}"
    m "{cps=35}Dan aku sempat mendengar mereka membahas proposal acara{/cps}"
    "Kakaknya [m]" "{cps=35}Hmmmm.... untuk acara tahun ini kita perlu ngadain apa ya [mi]?{/cps}"
    "Kakaknya [m]" "{cps=35}Kamu ada ide?{/cps}"
    mi "{cps=35}Apa ya...{/cps}"
    mi "{cps=35}Ah! Bagaimana kalau 'Festival Live Konser'?{/cps}"
    "Kakaknya [m]" "{cps=35}Ngapain itu?{/cps}"
    mi "{cps=35}Jadi kita bisa bekerja sama dengan anak sastra{/cps}"
    mi "{cps=35}Ditambah kan nanti siapa tahu bisa menjadi terkenal{/cps}"
    "Kakaknya [m]" "{cps=35}Bekerja sama dengan anak sastra? Kedengarannya ambisius sekali, [mi]. Kamu tahu kan mereka itu sekumpulan orang yang sulit ditebak?{/cps}"
    mi "{cps=35}Justru itu serunya! Bayangkan, bait-bait puisi yang mereka tulis dengan penuh perasaan, kita ubah menjadi melodi gitar yang menghentak.{/cps}"
    mi "{cps=35}Aku ingin sekolah ini bukan hanya tempat belajar rumus, tapi tempat di mana setiap murid punya 'suara' untuk didengar.{/cps}"
    "Kakaknya [m]" "{cps=35}Kamu memang selalu idealis. Tapi... konser seperti apa yang ingin kamu bawakan?{/cps}"
    mi "{cps=35}Konser yang jujur. Konser yang menunjukkan jati diri kita yang sebenarnya{/cps}"
    mi "{cps=35}Aku akan menyebutnya... 'Kitaimirai'.{/cps}"
    "Kakaknya [m]" "{cps=35}Hah?{/cps}"
    "Kakaknya [m]" "{cps=35}Apa itu?{/cps}"
    mi "{cps=35}Ya... sesuai kepanjangannya{/cps}"
    mi "{cps=35}'Harapan Untuk Masa Depan'{/cps}"
    mi "{cps=35}Dan aku ingin kalau para penerus kita bisa untuk melanjutkan proyek ini..{/cps}"
    "Kakaknya [m]" "{cps=35}Heh... seperti yang diharapkan dari ketua{/cps}"
    mi "{cps=35}Kamu mau meneruskannya kan dik?{/cps}"
    m "{cps=35}E-eh? aku kak??{/cps}"
    mi "{cps=35}Yap, karena kemungkinan waktu aku menjabat tidak akan cukup untuk menjalankan proker ini{/cps}"
    "Kakaknya [m]" "{cps=35}Tapi kan belum tentu dia mau [mi]{/cps}"
    mi "{cps=35}Ya.. kamu ajak aja ke sekolah kita, pastikan dia sekolah di sekolah kita{/cps}"
    "Kakaknya [m]" "{cps=35}Kamu ini... egois ada batasnya tahu{/cps}"
    mi "{cps=35}Ehehe{/cps}"
    m "{cps=35}A-aku akan berusaha!{/cps}"
    mi "{cps=35}Gitu dong, tapi tenang saja, adikku juga akan kusuruh sekolah di tempat kita{/cps}"
    "Kakaknya [m]" "{cps=35}Tunggu... bukannya sekolah kita khusus perempuan?{/cps}"
    mi "{cps=35}Ya pasti akan ada waktunya sekolah akan membuka pikirannya{/cps}"
    mi "{cps=35}Dan saat itu tiba, aku ingin adikku berdiri di sini, melanjutkan apa yang kita mulai hari ini.{/cps}"
    "Kakaknya [m]" "{cps=35}Kamu benar-benar visioner yang keras kepala, [mi]. Baiklah, aku akan mendukungmu. Tapi ingat, tantangan dari pihak sekolah kita tidak akan mudah loh.{/cps}"
    mi "{cps=35}Aman kalau itumah{/cps}"
    "{cps=35}Wajah [mi] memandang ke kakakku dengan penuh harapan{/cps}"

    # --- KEMBALI KE MASA SEKARANG ---

    scene bg_council_room_sunset with dissolve
    play music "audio/bgm/tiptoeing around.mp3" fadein 2.0

    "{cps=35}Maya-senpai mengakhiri ceritanya. Keheningan di ruang OSIS terasa jauh lebih berat dari sebelumnya. Cahaya senja yang masuk lewat jendela seolah-olah menjadi saksi bisu kenangan itu.{/cps}"

    m "{cps=40}Namun... prediksi kakakmu benar sekaligus salah.{/cps}"
    
    mc "{cps=40}Apa maksudmu, Senpai? Sekolah ini akhirnya memang menerima laki-laki, kan?{/cps}"

    m "{cps=40}Ya. Tapi kakakmu tidak pernah melihat hari itu tiba.{/cps}"
    m "{cps=40}Tepat seminggu setelah proposal ini diajukan, kakakmu... {w=0.5}dia pergi membawa semua harapan itu bersamanya.{/cps}"
    
    m "{cps=40}Akibat kejadian itu, konser 'Kitaimirai' bukan hanya dibatalkan, tapi dihentikan selamanya.{/cps}"
    m "{cps=40}Kakakku yang seharusnya melanjutkan peninggalan kakakmu keburu lulus sebelum menjalankan proker ini{/cps}"

    v "{cps=40}Jadi... itu alasan kenapa proposal ini disembunyikan?{/cps}"

    m "{cps=40}Benar. Dan alasan aku marah tadi... adalah karena aku takut.{/cps}"
    m "{cps=40}Aku takut jika kamu mencoba menghidupkan 'Kitaimirai', kamu akan berakhir sama seperti dia.{/cps}"

    # --- REAKSI YUUKA ---

    if yuuka_rel > 0:
        y "{cps=40}Kak Maya... ternyata selama ini Kakak memikul janji itu sendirian?{/cps}"
        "{cps=35}Yuuka mendekat ke arah Maya, rasa empatinya kini sepenuhnya menggantikan kecurigaannya.{/cps}"
    else:
        y "{cps=40}Jadi ini beban yang Kakak maksud... {w=0.5} Sebuah harapan yang berubah menjadi kutukan.{/cps}"

    mc "{cps=40}Senpai, terima kasih sudah jujur. Tapi...{/cps}"
    mc "{cps=40}Jika Kakakku ingin aku melanjutkannya, maka aku tidak akan berhenti sekarang.{/cps}"

    m "{cps=40}Terserah kamu, [mc]. Tapi ingat satu hal... {w=0.5} Sastra dan Musik di sekolah ini punya sisi yang belum kamu sentuh.{/cps}"

    m "{cps=40}Ada alasan kenapa melodi itu harus diheningkan, dan kenapa puisi-puisi itu harus dikunci rapat di gudang itu.{/cps}"

    v "{cps=40}Kak Maya... apakah maksudmu soal klub Sastra yang sekarang? Terkait dengan si kembar Shirohana-san?{/cps}"

    m "{cps=40}Biarkan waktu yang menjawabnya. Sekarang, sebaiknya kalian pulang. Hari sudah cukup gelap.{/cps}"

    # --- TRANSISI KELUAR RUANGAN ---

    scene bg_school_corridor_night with fade
    play sound "audio/sfx/door.mp3"

    "{cps=35}Kami melangkah keluar dari ruang OSIS. Suara pintu yang tertutup di belakang kami menggema di koridor yang kini hanya diterangi lampu-lampu temaram.{/cps}"
    "{cps=35}Buku itu terasa hangat di pelukanku, tapi entah kenapa, beban yang kurasakan jauh lebih berat daripada tumpukan kardus di gudang tadi.{/cps}"

    show yuuka_sad at center with dissolve

    y "{cps=40}[mc]...{/cps}"
    mc "{cps=40}Ya?{/cps}"
    y "{cps=40}Jangan paksakan dirimu sendirian. Aku... aku masih marah padamu soal tadi, tapi...{/cps}"
    y "{cps=40}Aku tidak mau kehilangan 'teman masa kecilku' untuk kedua kalinya dalam sejarah sekolah ini.{/cps}"

    "{cps=35}Yuuka mempercepat langkahnya, meninggalkanku yang masih terpaku di tengah koridor gelap. Dia benar, 'Kitaimirai' bukan sekadar konser. Ini adalah perang melawan bayangan masa lalu.{/cps}"

    scene black with fade
    stop music fadeout 3.0

    "{cps=35}Kami meninggalkan ruang OSIS saat lampu koridor mulai menyala satu per satu. Map biru itu masih ada di genggamanku, terasa jauh lebih hangat... dan jauh lebih berat.{/cps}"

    "{cps=35}Rahasia sekolah, kematian kakakku, dan janji Maya-senpai. Semuanya kini berpindah ke pundakku.{/cps}"

    scene black with fade
    stop music fadeout 2.0
    jump chapter_2_end