label chapter_2_sastra_kesempatan:
    scene bg_classroom_morning with fade
    play music "audio/bgm/schoolgate.mp3" fadein 2.0

    "{cps=35}Aku duduk di kursiku dengan perasaan campur aduk. Suasana kelas yang biasanya riuh terasa jauh di telingaku.{/cps}"
    "{cps=35}Di depanku, Yuuka sudah duduk diam. Dia tidak menyapaku, tidak juga menoleh. Dia hanya sibuk membolak-balik halaman bukunya dengan gerakan yang kasar.{/cps}"

    # --- INTERAKSI DENGAN YUUKA DI KELAS ---
    mc "{cps=40}[y]...{/cps}"
    
    y "{cps=40}...{/cps}"

    "{cps=35}Hening. Dia benar-benar sedang menunjukkan 'silent treatment' kepadaku karena pilihanku pagi tadi.{/cps}"

    if jujur:
        "{cps=35}Meskipun aku sudah jujur soal Kakakku, dia sepertinya masih tidak terima kenapa aku memilih Sastra daripada OSIS bersamanya.{/cps}"
    else:
        "{cps=35}Apalagi aku tidak memberitahunya alasan yang sebenarnya. Jarak satu meter di antara meja kami terasa seperti satu kilometer.{/cps}"

    # --- KEHADIRAN SHOKO ---
    "{cps=35}Tiba-tiba, sebuah bayangan kecil berdiri di samping mejaku.{/cps}"
    sh "{cps=35}Ikazaki-kun...{/cps}"
    "{cps=35}[sh] menatapku dengan wajah yang sedikit serius{/cps}"
    mc "{cps=35}Eh [sh], ada apa?{/cps}"
    sh "{cps=35}Ng-nggak ada apa-apa kok...{/cps}"
    "{cps=35}Aneh...{/cps}"
    "{cps=35}Tumben dia samperin aku{/cps}"
    "{i}Dalam hati [sh]: \"Adik sialan... kenapa aku harus melakukan ini demi menuruti perintahnya...\"{/i}"
    sh "{cps=35}Kamu nanti siang kosong nggak?{/cps}"
    mc "{cps=35}Umm... iya sih, kenapa memangnya?{/cps}"
    sh "{cps=35}Aku nanti mau ngobrol sama kamu, apakah bisa?{/cps}"
    "{cps=35}[y] memandangku dengan wajah yang sinis{/cps}"
    "{cps=35}Aduh...{/cps}"
    "{cps=35}Kenapa kamu datang di waktu yang tidak pas sih [sh]...{/cps}"
    "{cps=35}[y] langsung membuang wajahnya dariku{/cps}"
    "{cps=35}Seakan-akan berkata 'Bukan urusanku'{/cps}"
    mc "{cps=35}Umn... bisa sih [sh]{/cps}"
    sh "{cps=35}Fyuh... syukurlah..{/cps}"
    sh "{cps=35}Aku tunggu ya nanti{/cps}"
    "{cps=35}[sh] langsung kembali ke tempat duduknya{/cps}"
    v "{cps=35}Cie... nambah lagi nih{/cps}"
    mc "{cps=35}Apaan sih vin{/cps}"
    v "{cps=35}Ehehe...{/cps}"
    "{cps=35}Bel tanda kelas masuk pun berbunyi{/cps}"
    sh "{cps=35}Aku penasaran akan mempelajari apa hari ini...{/cps}"

    scene black with fade
    "{cps=35}Pelajaran pun dimulai. Namun, ajakan [sh] terus terngiang di kepalaku. Apa sebenarnya yang akan terjadi?{/cps}"

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
        "{cps=35}Yuuka terlihat panik, dia mengangkat lima jarinya di bawah meja sebagai isyarat.{/cps}"
        "{cps=35}Kemudian [sh]...{w=0.1} dia memberikan isyarat berupa angka 5{/cps}"
    else:
        "{cps=35}Yuuka terlihat biasa saja, bahkan tidak memberi isyarat apapun.{/cps}"
        "{cps=35}Namun [sh]...{w=0.1} dia memberikan isyarat berupa angka 5{/cps}"
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
            else:
                "{cps=35}Yuuka diam saja, tidak memberikan reaksi apapun, tetapi [sh] terlihat sedikit tenang{/cps}"
            v "{cps=60}Cih... ternyata si Specimen Langka ini bisa berhitung juga.{/cps}"

        "15":
            $ correct_answer = False
            $ yuuka_rel -= 2
            $ shoko_rel -= 2
            mc "{cps=40}Jawabannya... 15, Bu?{/cps}"
            
            "{cps=35}Seketika seisi kelas tertawa. Bahkan Vina di belakangku sampai harus menutup mulutnya agar tidak terdengar terlalu keras.{/cps}"
            t "{cps=40}Lima belas? Kamu ini sedang menghitung nilai x atau harga gorengan di kantin? Salah!{/cps}"
            t "{cps=40}Berdiri di depan sampai jam pelajaran saya selesai!{/cps}"
            
            if jujur:
                "{cps=35}Yuuka menepuk kepalanya seakan tidak percaya kalau aku malah menjawabnya dengan salah. Di belakang, Vina tampak tertawa kecil karena melihat jawabanku.{/cps}"
            else:
                "{cps=35}Yuuka diam saja, tidak memberikan reaksi apapun, tetapi [sh] terlihat sedikit kecewa{/cps}"
        "3":
            $ correct_answer = False
            $ yuuka_rel -= 2
            $ shoko_rel -= 2
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
        v "{cps=35}Tapi... Kenapa kamu bisa salah jawab?{/cps}"
        mc "{cps=35}Entahlah.. sepertinya aku lagi banyak pikiran{/cps}"
        v "{cps=35}Perasaan kamu nggak ngapa-ngapain...{/cps}"
        v "{cps=35}Kamu juga berpikir gitu kan [y]?{/cps}"
        y "{cps=35}Ummm... iya sih..{/cps}"
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
    else:
        "{cps=40}[v] dan [y] langsung menghampiriku.{/cps}"
        "{cps=40}Sepertinya mereka ingin memberiku semacam 'wejangan'.{/cps}"
        
        show yuuka_determined at left
        show vina_smile at right
        with dissolve

        v "{cps=40}Yo! {w=0.1}Si pintar.{/cps}"
        mc "{cps=40}Hei!{/cps}"
        v "{cps=40}Ayolah, aku cuman bercanda. Tapi serius, kamu tadi oke juga ketika maju{/cps}"
        mc "{cps=40}Apa sih...{/cps}"
        v "{cps=35}Kasih tahu dong kenapa kamu bisa menjawab...{/cps}"
        "{cps=35}[y] menempel di sampingku{/cps}"
        mc "{cps=35}Entahlah...{/cps}"
        "{cps=35}Aku memandang ke sekitar sambil memalingkan wajahku dari [v]...{/cps}"
        if jujur:
            "{cps=35}Terlihat [y] yang sedikit kesal{/cps}"
            y "{cps=40}Hah... kalian ini...{/cps}"
            "{cps=35}[v], ayo ke kantin{/cps}"
            v "{cps=40}Ayo! [mc] kamu mau ikut?{/cps}"
            mc "{cps=40}Nggak dulu, masih kenyang{/cps}"
            v "{cps=40}Heee... kamu yakin?{/cps}"
            v "{cps=40}Yap{/cps}"
            v "{cps=40}Oke kalau begitu, sampai nanti{/cps}"
            "{cps=40}[y] dan [v] langsung pergi meninggalkanku sendiri{/cps}"
        else:
            y "{cps=40}Terlihat [y] yang sedang ingin menghindariku. Aku tidak tahu apa yang terjadi padanya{/cps}"
            v "{cps=35}Hei... ada apa sih ka?{/cps}"
            y "{cps=40}Entahlah, kalau kamu mau tahu ya tanya ke [mc] langsung{/cps}"
            "{cps=40}[y] langsung meninggalkan kami tanpa sepatah kata apa pun{/cps}"
            v "{cps=40}Sepertinya ada drama nih..{/cps}"
            v "{cps=40}Kamu habis apain dia?{/cps}"
            mc "{cps=40}Ah nggak gitu{/cps}"
            v "{cps=40}Hah...{w=0.1} [y]!{/cps}"
            "{cps=40}[v] langung mengejar [y]{/cps}"
            "{cps=40}Meninggalkanku sendiri{/cps}"


    sh "{cps=35}Seperti biasa selalu ramai ya [mc]{/cps}"
    "{cps=35}Shoko tiba-tiba sudah berada di dekatku. Suaranya yang tenang terasa kontras dengan keributan Yuuka dan Vina tadi.{/cps}"
    mc "{cps=35}Ya begitulah...{/cps}"
    sh "{cps=35}Kamu tidak ikut ke kantin bersama mereka?{/cps}"
    mc "{cps=35}Untuk saat ini nggak dulu{/cps}"
    "{cps=35}karena lagi ga megang duit sih{/cps}"
    sh "{cps=35}Berarti momennya pas ya..{/cps}"
    mc "{cps=35}Momen? Apa mak-{/cps}"
    "{cps=35}Tanpa peringatan, Shoko menarik tanganku. Genggamannya kecil tapi sangat kuat, memaksaku untuk berdiri dan mengikutinya ke luar kelas.{/cps}"
    mc "{cps=35}He-hei! kamu mau membawaku ke mana{/cps}"
    sh "{cps=35}Ikut saja{/cps}"
    "{cps=35}Aku dibawa dia pergi{/cps}"
    "{cps=35}Aku nggak tau mau dibawa kemana{/cps}"
    "{cps=35}Aku hanya bisa pasrah ditarik menyusuri koridor. Punggung Shoko terlihat sangat tegak, seolah dia sudah merencanakan ini sejak tadi.{/cps}"
    "{cps=35}Semoga saja tidak ke tempat yang aneh...{/cps}"
    "{cps=35}Dan kami berhenti di depan ruangan yang familiar{/cps}"
    "{cps=35}Bau dari ruangan itu... serta kondisi sekitarnya..{/cps}"
    "{cps=35}Seakan-akan aku pernah ada disini...{/cps}"
    sh "{cps=35}Masuklah, [mc]{/cps}"
    mc "{cps=35}*Glek...* Baik.{/cps}"
    "{cps=35}Aku memberanikan diri untuk membuka pintu ruangan ini{/cps}"
    "{cps=35}Dan setelah aku membukanya{/cps}"
    "{cps=35}Terlihat buku yang tertata rapih di rak{/cps}"
    "{cps=35}Serta seorang gadis yang sedang membaca buku{/cps}"
    "{cps=35}Dari rambutnya... {w=0.1} Seperti kembaran [sh] yang kemarin terlambat..{/cps}"
    yk "{cps=35}Hmn?{/cps}"
    yk "{cps=35}Onee-san... Kenapa kamu lama banget untuk membawa dia kesini{/cps}"
    sh "{cps=35}Kan bukan kebiasaanku [yk]{/cps}"
    sh "{cps=35}Kamu juga bisa membawa dia sendiri kesini kan{/cps}"
    yk "{cps=35}Heee padahal lebih cocok onee-san yang membawanya{/cps}"
    sh "{cps=35}Hah...{/cps}"
    "{cps=35}[sh] langsung mengambil buku di rak dan langsung membacanya{/cps}"
    "{cps=35}Tanpa menjelaskan kenapa aku ada di sini{/cps}"
    mc "{cps=35}Ano...{/cps}"
    yk "{cps=35}Ah iya! Selamat datang di klub sastra [mc]{/cps}"
    yk "{cps=35}Sepertinya tidak perlu perkenalan karena kan kita bertiga sekelas{/cps}"
    yk "{cps=35}Jadi.... ya, semoga kamu betah ya disini{/cps}"
    "{cps=35}Senyum hangat Yukie membuat rasa gugupku sedikit mereda. Dia terasa jauh lebih ramah dibandingkan kakaknya.{/cps}"
    mc "{cps=35}Terima kasih, Yukie. Tapi... bagaimana kalian tahu aku akan bergabung ke sini?{/cps}"
    yk "{cps=35}Ummm... kenapa ya...{/cps}"
    yk "{cps=35}Nee-san tahu kan?{/cps}"
    sh "{cps=35}Kalau aku sih tahu dari kak [m]{/cps}"
    "{cps=35}Dia lagi ya...{/cps}"
    mc "{cps=35}Lalu... aku harus ngapain sekarang?{/cps}"
    sh "{cps=35}Untuk saat ini kamu anggap ruangan ini sebagai rumahmu saja{/cps}"
    "{cps=35}[sh] menjawab sambil terus melanjutkan kegiatan membacanya{/cps}"
    yk "{cps=35}Ya ampun... Nee-san sebaiknya kurangin sifat dinginmu itu{/cps}"
    sh "{cps=35}Apaan sih{/cps}"
    "{cps=35}Shoko menutup bukunya pelan, lalu menatapku dengan tatapan yang sulit diartikan.{/cps}"
    yk "{cps=40}Eh [mc], kamu tahu kan kenapa Maya-san bersikeras memintamu masuk organisasi?{/cps}"
    mc "{cps=40}Katanya sih untuk 'kontribusi'. Tapi aku merasa ada alasan lain.{/cps}"
    yk "{cps=35}Memang sih, karena dengan bergabung ke organisasi...{/cps}"
    yk "{cps=35}Kamu bisa meningkatkan banyak {i}soft skill{/i}{/cps}"
    yk "{cps=35}Seperti bicara didepan umum, relasi, dan sebagainya{/cps}"
    mc "{cps=35}Ya... begitulah{/cps}"
    yk "{cps=35}Nah, aku ingin bertanya kepadamu [mc]. Kenapa kamu memilih sastra dibandingkan osis atau organisasi lain?{/cps}"
    mc "{cps=35}Ummmnn....{/cps}"
    "{cps=35}Bagaimana aku memberitahu mereka{/cps}"
    "{cps=35}Kalau tujuanku yang sebenarnya adalah mengembalikan ingatan yang telah hilang...{/cps}"
    "{cps=35}Aku jawab gini aja deh{/cps}"
    mc "{cps=35}Aku hanya tertarik ke sastra kok nggak ada yang lain{/cps}"
    yk "{cps=35}Heee... mencurigakan...{/cps}"
    yk "{cps=35}Kamu berpikir hal yang sama kan, [sh] Nee-san?{/cps}"
    "{cps=35}Sepertinya [yk] tidak bisa dibohongi{/cps}"
    "{cps=35}Aku harus bagaimana...{/cps}"
    sh "{cps=35}Aku tidak terlalu peduli sih [yk]{/cps}"
    yk "{cps=35}Heeee.... membosankan{/cps}"
    sh "{cps=35}Selagi kamu ada disisiku.. itu sudah cukup [mc]{/cps}"
    yk "{cps=35}Ya... lagipula kan memang tujuanmu kita bersama lagi kan, Nee-san{/cps}"
    yk "{cps=35}Seperti 10 tahun yang lalu{/cps}"
    sh "{cps=35}Hmm!{/cps}"
    "{cps=35}Apa sih yang terjadi pada 10 tahun yang lalu?{/cps}"
    mc "{cps=35}Sebentar... aku masih belum bisa mencerna semua kejadian ini yang terjadi begitu cepat..{/cps}"
    mc "{cps=35}Memangnya kita bertiga pernah bermain bersama 10 tahun yang lalu?{/cps}"
    "{cps=35}Suasana mendadak menjadi sangat berat. Senyum Yukie menghilang, berganti dengan tatapan sedih yang mendalam.{/cps}"
    "{cps=35}Di sudut ruangan, Shoko mematung. Tangannya gemetar hebat saat memegang dadanya, seolah ada sesak yang tak tertahankan di sana.{/cps}"
    sh "{cps=35}Kamu... {w=0.5}benar-benar lupa?{/cps}"
    mc "{cps=35}Maaf, Shoko... aku benar-benar—{/cps}"
    sh "{cps=35}[yk].. aku pergi keluar dulu{/cps}"
    yk "{cps=35}Eh? Nee-sa-{/cps}"
    "{cps=35}*BRAK{/cps}"
    "{cps=35}Shoko lari keluar ruangan secepat kilat. Pintu terbanting keras, menyisakan keheningan yang menyesakkan di antara aku dan Yukie.{/cps}"
    "{cps=35}Dari balik koridor, samar-samar terdengar suara isakan kecil yang memilukan...{/cps}"
    "{cps=35}Entah kenapa aku merasa begitu bersalah...{/cps}"
    yk "{cps=35}Hah... sudah ku duga akan seperti ini{/cps}"
    yk "{cps=35}Dia selalu aja seperti ini{/cps}"
    yk "{cps=35}Bahkan terakhir kali sebelum kami berpisah..{/cps}"
    mc "{cps=35}Memangnya kenapa sih, Yukie? Kok dia bisa sampai segitunya? Apa yang terjadi 10 tahun lalu?{/cps}"
    yk "{cps=35}Aku tidak bisa menjelaskannya kepadamu sekarang, [mc]. Itu adalah luka yang hanya Shoko yang bisa ceritakan.{/cps}"
    yk "{cps=35}Cepatlah kejar dia! Dia belum jauh. Jangan biarkan dia sendirian dalam kondisi seperti itu.{/cps}"
    menu:
        "Kejar Shoko sekarang":
            $ shoko_rel += 10
            "{cps=35}Aku tidak punya pilihan lain. Aku harus bertanggung jawab atas rasa sakit yang tidak kusengaja kubuat ini.{/cps}"

        "Tanya Yukie lebih lanjut":
            $ shoko_rel -= 5
            mc "{cps=35}Tapi aku butuh jawaban, Yukie!{/cps}"
            yk "{cps=35}Kamu pria atau bukan sih!?{/cps}"
            yk "{cps=35}Jawaban tidak akan berguna kalau orangnya sudah terlanjur hancur! Kejar dia, [mc]!{/cps}"

    "{cps=35}Aku langsung berusaha mencari [sh]...{w=0.1} namun...{w=0.1} dia dimana?{/cps}"
    "{cps=35}Aku tidak tahu lokasi persisnya...{/cps}"
    mc "{cps=35}Kamu dimana sih... [sh]{/cps}"
    "{cps=35}Waktu terus berjalan mendekati bunyi bell{/cps}"
    "{cps=35}Aku masih terus mencari keberadaan [sh]{/cps}"
    "{cps=35}Sampai aku berada di depan ruang kelas{/cps}"
    "{cps=35}Dan berhadapan dengan [y] dan [v]{/cps}"
    v "{cps=35}Loh, [mc]? Kamu kenapa panik begitu? Seperti baru saja dikejar hantu.{/cps}"
    mc "{cps=35}Kalian berdua... kalian melihat [sh] lewat sini?{/cps}"
    v "{cps=35}[sh]? maksudmu gadis berambut merah itu?{/cps}"
    v "{cps=35}Aku tidak melihatnya sih... kalau kamu [y]?{/cps}"
    if jujur:
        "{cps=35}Yuuka menatapku sejenak. Meskipun ada sedikit kilat cemburu, rasa khawatirnya jauh lebih besar.{/cps}"
        y "{cps=35}Aku kalau tidak salah melihat seorang gadis rambut merah berlari ke loteng deh. Wajahnya tertutup tangan, sepertinya dia sedang menangis...{/cps}"
        mc "{cps=35}Loteng? Memangnya dia mau ngapain?{/cps}"
        y "{cps=35}Kamu ngapain tanya ke aku?{/cps}"
        mc "{cps=35}Kamu kan anggota osis{/cps}"
        y "{cps=35}Ya nggak semua anggota osis bisa tahu semuanya dong!{/cps}"
        v "{cps=35}Sudah-sudah, sebaiknya kamu langsung ke loteng deh [mc], aku takut nanti terjadi hal yang tidak diinginkan...{/cps}"
        mc "{cps=35}Baik kalau begitu.. terimakasih [y], [v]!{/cps}"
        y "{cps=35}Hati-hati, [mc]...{/cps}"
    else:
        "{cps=35}Yuuka menyilangkan tangannya, menatapku dengan tatapan yang sangat dingin.{/cps}"
        y "{cps=35}Hah? Buat apa aku membantumu?{/cps}"
        v "{cps=35}Hei...{/cps}"
        mc "{cps=35}Kamu kan osis [y], pasti kamu tahu sesuatu...{/cps}"
        y "{cps=35}Kamu saja berbohong kepadaku soal pilihan organisasimu... jadi buat apa aku jujur memberitahumu lokasinya?{/cps}"
        "{cps=35}Cih...{/cps}"
        mc "{cps=35}Untuk masalah bohong nanti aku bisa jelaskan{/cps}"
        mc "{cps=35}Tapi sekarang beritahu aku dulu{/cps}"
        y "{cps=35}Sepenting itukah dia dibandingkan hubungan kita?{/cps}"
        v "{cps=35}[y]... sepertinya ini beneran genting deh...{/cps}"
        v "{cps=35}Kalau tidak genting, [mc] tidak akan seperti ini{/cps}"
        v "{cps=35}Mendingan kamu beri tahu, nanti kalau [mc] tidak mau jujur.. aku ikat dia di gudang{/cps}"
        y "{cps=35}Hmmmm....{/cps}"
        "{cps=35}Lama banget berpikirnya... cepat woi{/cps}"
        y "{cps=35}Loteng{/cps}"
        y "{cps=35}Aku beritahu ke kamu karena kasihan, bukan berarti aku peduli dengan dia ya, dan yang penting kamu janji ceritakan semua yang terjadi kepadaku nanti sepulang sekolah{/cps}"
        mc "{cps=35}Ya... aku akan cerita. Terimakasih banyak [y]{/cps}"

    "{cps=35}Aku langsung pergi meninggalkan mereka dan bergegas ke arah loteng{/cps}"
    "{cps=35}Hah... hah...{/cps}"
    "{cps=35}Seingatku loteng selalu dikunci karena terlalu berbahaya disana{/cps}"
    "{cps=35}Namun... kenapa dia pergi kesana{/cps}"
    "{cps=35}Aku langsung memutar arah dan memacu kakiku menuju tangga paling ujung.{/cps}"
    
    scene bg_stairs_to_rooftop with fade
    play sound "audio/sfx/breathing.mp3" # SFX napas tersengal

    "{cps=35}Hah... hah...{/cps}"
    "{cps=35}Pikiran buruk mulai memenuhi kepalaku. Loteng selalu dikunci karena pagar pengamannya sudah tua dan berbahaya.{/cps}"
    "{cps=35}Kenapa dia memilih tempat sesunyi itu?{/cps}"

    play sound "audio/sfx/door.mp3" # Suara pintu digoyang
    "{cps=35}*Kriet...*{/cps}"
    
    "{cps=35}Pintunya... tidak terkunci?{/cps}"

    scene bg_rooftop_morning with fade
    play music "audio/bgm/last bridge.mp3" fadein 2.0

    "{cps=35}Begitu aku membuka pintu, angin kencang langsung menerpa wajahku. Di sana, di dekat pagar pembatas, aku melihat punggung kecil yang bergetar itu.{/cps}"
    mc "{cps=35}[sh]...{/cps}"
    sh "{cps=35}Kenapa kamu mengejarku? Padahal kamu tidak mengingat kenangan itu..{/cps}"
    mc "{cps=35}Aku tidak ingin kamu berbuat aneh [sh]{/cps}"
    sh "{cps=35}Aneh? Aku hanya ingin menenangkan diri disini{/cps}"
    sh "{cps=35}Lagipula orang macam apa yang langsung bunuh diri hanya karena teman masa kecilnya tidak mengingat kenangan terakhirnya...{/cps}"
    sh "{cps=35}Walau itu hampir kejadian..{/cps}"
    mc "{cps=35}Kamu ngomong apa sih... masa depanmu kan masih panjang{/cps}"
    mc "{cps=35}Hanya karena masalah kecil kamu sampai seperti ini...{/cps}"
    "{cps=35}Shoko berbalik perlahan. Matanya yang sembab menatapku dengan tatapan yang sangat menyakitkan.{/cps}"
    sh "{cps=35}Kecil? Berarti kamu menganggap semua kenangan itu tidak berguna ya...{/cps}"
    "{cps=35}[sh] mulai mendekati pembatas{/cps}"
    sh "{cps=35}Sampai jumpa, [mc]{/cps}"
    "{cps=35}Aku tidak ingin kejadian buruk terjadi lagi..{/cps}"
    mc "{cps=35}Sial... SUDAH CUKUP, [sh]!{/cps}"
    "{cps=35}Aku tidak mau kehilangan orang yang aku kenal lagi! Tidak untuk ketiga kalinya!{/cps}"
    "{cps=35}Aku menerjang maju tanpa berpikir panjang. Tanganku meraih lengannya yang dingin.{/cps}"
    "{cps=35}*GREP*{/cps}"
    "{cps=35}Aku menarik tangannya agar dia tidak terjatuh{/cps}"
    sh "{cps=35}[mc]! Apa yang-{/cps}"
    "{cps=35}*BRAK*{/cps}"
    mc "{cps=35}Aduh...{/cps}"
    mc "{cps=35}Kamu tidak apa...{/cps}"
    mc "{cps=35}apa?{/cps}"
    "{cps=35}Aku menariknya terlalu kuat hingga kami berdua kehilangan keseimbangan. Aku terjatuh telentang di lantai beton yang keras, dan Shoko...{/cps}"
    "{cps=35}Dia berada tepat di atasku. Nafasnya yang hangat menerpa leherku. Tubuhnya yang mungil terasa sangat ringan, namun gemetarannya begitu terasa di dadaku.{/cps}"
    "{cps=35}Tangannya yang lembut dan dingin... kini berada di dalam genggamanku.{/cps}"
    sh "{cps=35}Apaan sih [mc]... *hiks-hiks{/cps}"
    "{cps=35}Dia menangis lagi. Kali ini bukan tangisan kemarahan, tapi tangisan kelegaan yang menyesakkan.{/cps}"
    mc "{cps=35}Sudahlah [sh]... Kamu jangan menangis lagi ya{/cps}"
    "{cps=35}Aku terus berusaha menenangkannya{/cps}"
    sh "{cps=35}*hiks.. hiks.. Kamu jahat{/cps}"
    mc "{cps=35}Kenapa aku dicap jahat sih?{/cps}"
    sh "{cps=35}Kamu selalu saja melupakan hal penting seakan-akan itu semua hanya angin lalu saja{/cps}"
    mc "{cps=35}Iya, aku tahu aku salah karena melupakan hal sepenting itu. Sepuluh tahun itu waktu yang lama, [sh]. Aku tidak mungkin mengingat semuanya secara spesifik...{/cps}"
    sh "{cps=35}Tapi aku kan selalu ingat tentangmu...{/cps}"
    "{cps=35}Melihatnya seperti ini, aku tahu aku harus melakukan sesuatu. Aku harus menebus sepuluh tahun yang hilang itu.{/cps}"
    mc "{cps=35}Aku punya ide! Bagaimana kalau kita buat kenangan baru saja? Di sekolah ini, di klub sastra.{/cps}"
    mc "{cps=35}Jika masa lalu itu kabur, mari kita buat masa depan yang lebih jelas.{/cps}"
    sh "{cps=35}Membuat... kenangan baru? Bagaimana caranya?{/cps}"
    mc "{cps=35}Itu... aku belum tahu pastinya. Mungkin kita bisa cari tahu bersama Yukie.{/cps}"
    sh "{cps=35}Mungkin... itu bisa kita lakukan.{/cps}"
    $ shoko_rel += 10
    "{cps=35}*TENG-NONG-NENG-NONG{/cps}"
    "{cps=35}Bel tanda masuk jam kedua telah berbunyi{/cps}"
    mc "{cps=35}Nah... bel sudah bunyi. Ayo kita kembali ke kelas.{/cps}"
    sh "{cps=35}Tidak mau...{/cps}"
    mc "{cps=35}Hei, nilaiku bisa hancur kalau aku bolos jam Bu Nanami lagi!{/cps}"
    sh "{cps=35}Biarkan aku... {w=0.3}tetap seperti ini selama lima menit lagi. Kumohon.{/cps}"
    "{cps=35}Wajahnya yang cemberut namun memerah membuatku tidak bisa menolak. Ada kedamaian aneh yang menyelimuti kami di tengah kebisingan angin loteng ini.{/cps}"
    mc "{cps=35}Hah... iya, iya. Lima menit saja ya.{/cps}"
    "{cps=35}Meski sudah SMA, ternyata dia masih punya sisi kekanak-kanakan yang manis. Dan untuk pertama kalinya setelah sekian lama, aku merasa... benar-benar dibutuhkan.{/cps}"
    scene black with fade
    stop music fadeout 2.0
    "{cps=35}Dan ketika sampai di kelas...{/cps}"
    t "{cps=35}{b}KALIAN BERDUA DARIMANA SAJA!?{/b}{/cps}"
    t "{cps=35}Masa meninggalkan pelajaran saya selama 10 menit! Kalian mau saya beri nilai Alpha?{/cps}"
    mc "{cps=35}Nggak, Bu! Maaf, tadi itu...{/cps}"
    "{cps=35}Aku melirik [sh] di sampingku, berharap dia membantuku mencari alasan. Tapi dia malah... tersenyum tipis?{/cps}"
    "{cps=35}Pahamin situasi dong, [sh]! Kita sedang di ujung tanduk!{/cps}"
    sh "{cps=40}Maafkan kami, Bu Nanami.{/cps}"
    "{cps=35}Shoko melangkah maju dengan tenang. Suaranya yang datar namun merdu langsung membuat seisi kelas terdiam. Bahkan Bu Nanami pun sedikit menurunkan nada bicaranya.{/cps}"
    sh "{cps=40}Tadi kami sedang berada di loteng, ada urusan penting di sana.{/cps}"
    t "{cps=40}Loteng!? {w=0.5}Bukankah area itu dilarang untuk murid tanpa izin khusus? Apa yang kalian lakukan di tempat berbahaya seperti itu?{/cps}"
    "{cps=35}Satu kelas langsung berbisik-bisik. Aku bisa merasakan tatapan tajam dari setiap sudut ruangan, terutama dari meja paling depan.{/cps}"
    sh "{cps=40}Kami sedang mencari 'perspektif' baru, Bu.{/cps}"
    sh "{cps=40}Dan Ikazaki-kun... {w=0.3}dia cukup baik untuk menemaniku memastikan aku tidak 'hanyut' oleh angin di sana.{/cps}"
    "{cps=35}Shoko melirikku sekilas dengan senyum tipis yang masih menempel di bibirnya. Kalimat 'hanyut oleh angin' itu jelas merujuk pada kejadian hampir jatuh tadi, tapi bagi orang lain, itu terdengar seperti kata yang aneh.{/cps}"
    t "{cps=35}Ibu sama sekali tidak mengerti apapun perkataanmu...{/cps}"
    t "{cps=35}Yang penting kali ini aku biarkan, namun kalau kalian mengulangi ini.. awas saja!{/cps}"
    "{cps=35}Sekarang kembali ke tempat duduk kalian{/cps}"
    "{cps=35}Ba-baik bu!{/cps}"
    "{cps=35}Aku berjalan cepat menuju bangkuku dengan kepala tertunduk. Saat melewati meja [y], aku bisa merasakan aura dingin yang membuat bulu kudukku berdiri.{/cps}"
    show yuuka_stern at left with dissolve
    y "{cps=40}(Berbisik sangat pelan) 'Menemaninya', huh? Sampai matanya merah begitu?{/cps}"
    mc "{cps=40}(Berbisik) Nanti kujelaskan, Yuuka...{/cps}"
    y "{cps=40}Tidak perlu. Aku sudah tahu jawabannya hanya dengan melihat wajahmu yang terlihat merasa bersalah itu.{/cps}"
    "{cps=35}Yuuka memalingkan wajahnya ke arah papan tulis, mencoret-coret bukunya dengan sangat kasar.{/cps}"
    show vina_smile at right with dissolve
    v "{cps=40}(Sambil memberikan jempol diam-diam) Hebat juga kamu, Specimen. Ternyata loteng adalah tempat kencan favoritmu, ya?{/cps}"
    mc "{cps=40}Vin, ini bukan waktunya bercanda...{/cps}"
    "{cps=35}Aku duduk dan mencoba fokus, tapi aku tidak bisa berhenti memikirkan Shoko. Di depan sana, dia duduk dengan tenang seolah tidak terjadi apa-apa, tapi aku tahu... mulai hari ini, segalanya akan berubah.{/cps}"
    t "{cps=40}Sekarang buka buku Sejarah kalian. Kita akan membahas tentang 'Tragedi dan Pengkhianatan' dalam sejarah pergerakan organisasi.{/cps}"

    t "{cps=40}Dalam sejarah, banyak tokoh besar yang jatuh bukan karena musuh dari luar, tapi karena rusaknya 'Kepercayaan' dari orang terdekatnya.{/cps}"
    
    # Elemen Ilmu Pengetahuan
    t "{cps=40}Ada sebuah istilah Latin: {b}'Falsus in Uno, Falsus in Omnibus'{/b}. Ada yang tahu artinya?{/cps}"

    "{cps=35}Kelas sunyi. Aku melirik [y], dia sedang mencatat dengan sangat cepat, seolah-olah berusaha mengabaikan keberadaanku.{/cps}"
    "{cps=40}Seperti biasa, dia selalu saja fokus{/cps}"
    "{cps=40}Berbeda denganku...{/cps}"
    "{cps=35}namun [sh]... dia terus memperhatikanku semenjak kejadian tadi{/cps}"
    t "{cps=40}[mc], coba kamu jawab. Kamu sepertinya sedang melamun dari awal pelajaran ini{/cps}"
    mc "{cps=40}Kok saya sih [t]?{/cps}"
    t "{cps=40}Memangnya yang melamun selain kamu siapa lagi?{/cps}"
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
            mc "{cps=40}Artinya... sekali berbohong dalam satu hal, maka seluruh perkataannya akan dianggap bohong, Bu.{/cps}"
            if jujur:
                $ yuuka_rel -= 5
                "{cps=35}Yuuka menghentikan catatannya sesaat. Bahunya sedikit bergetar, tapi dia tetap tidak menoleh.{/cps}"
                "{cps=35}Dia seolah sedang mencerna kata-kata itu, meyakinkan dirinya bahwa keputusanku masuk sastra. Meskipun mendadak...adalah kejujuran yang pahit.{/cps}"
                unknown "{cps=35}Lantas kenapa kamu di loteng dan melakukannya...{/cps}"
                "{cps=35}Terdengar suara gumaman yang sangat lirih di depanku. Begitu pelan, tapi penuh dengan nada kecurigaan.{/cps}"
            else:
                $ yuuka_rel -= 5
                unknown "{cps=35}Pembohong{/cps}"
                "{cps=35}Terdengar suara gumaman yang sangat lirih di depanku. Begitu pelan, tapi penuh dengan nada kecurigaan.{/cps}"
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
    
    t "{cps=40}Sekali kamu merusak kepercayaan, butuh waktu seumur hidup untuk membangunnya kembali.{/cps}"
    
    "{cps=35}Yuuka menghentikan catatannya sesaat. Bahunya sedikit bergetar, tangannya menggenggam pena dengan sangat erat sampai kuku jarinya memutih.{/cps}"
    "{cps=35}Aku tahu dia mendengarkan setiap kata itu. Dan aku tahu, kata-kata Nanami-sensei sedang menghujam tepat di tengah-tengah kecanggungan kami.{/cps}"

    "{cps=35}Nanami-sensei kembali ke papan tulis, kapur di tangannya berderit keras saat beliau menuliskan daftar nama-nama pengkhianat besar dalam sejarah.{/cps}"
    "{cps=35}Suasana kelas menjadi sangat berat. Hanya ada suara gesekan pena di atas kertas dan detak jam dinding yang seolah melambat secara sengaja.{/cps}"

    "{cps=35}Satu jam berlalu...{/cps}"
    "{cps=35}Sinar matahari siang yang menyengat perlahan mulai bergeser, menciptakan bayangan panjang dari kaki meja yang menembus lantai kayu kelas.{/cps}"
    "{cps=35}Beberapa teman sekelasku mulai terlihat mengantuk, kepala mereka terkantuk-kantuk mengikuti irama suara Nanami-sensei yang monoton namun tajam.{/cps}"
    
    "{cps=35}Suara [t] yang menjelaskan tentang runtuhnya kerajaan-kerajaan besar akibat pengkhianatan internal terasa seperti bisikan yang menghakimi setiap helai napasku.{/cps}"

    "{cps=35}Aku melirik ke depan. [y] masih tetap pada posisinya. Dia tidak pernah sekalipun melirik ke arahku, bahkan saat dia mengambil penggaris atau merapikan rambutnya.{/cps}"
    "{cps=35}Namun [sh]... Dia masih saja memperhatikanku{/cps}"
    "{cps=35}Dua jam berlalu...{/cps}"
    "{cps=35}Waktu benar-benar terasa abadi. Kakiku terasa kaku, dan pikiranku mulai melayang pada Shoko, pada klub sastra, dan pada kejadian yang aku alami ketika istirahat..{/cps}"
    if correct_answer:
        "{cps=35}Setiap detik yang kami lalui dalam diam ini terasa lebih menyakitkan daripada hukuman berdiri di depan kelas tadi pagi.{/cps}"
    else:
        "{cps=35}Setiap detik yang kami lalui dalam diam ini terasa lebih menyakitkan daripada tusukan benda tajam.{/cps}"
    "{cps=35}Dinding es yang dibangun [y] di depanku terasa semakin tebal. Aku ingin bicara, tapi tenggorokanku terasa terkunci oleh beban rahasia dan pilihan yang baru saja kuambil.{/cps}"
    "{cps=35}Kehadiranku di sini... di belakang... seolah-olah sudah dihapus sepenuhnya dari dunia kecilnya.{/cps}"
    "{cps=35}Namun saat aku mencoba menoleh sedikit ke arah baris paling belakang...{/cps}"
    "{cps=35}[sh] masih di sana. Di balik Yukie, dia memperhatikanku dengan tatapan yang tenang namun intens. Seolah-olah dia sedang mengawasi 'miliknya' agar tidak menghilang lagi.{/cps}"


    scene black with fade
    stop music fadeout 3.0

    play sound "audio/sfx/school bell.mp3"
    "{cps=40}Ting... Tong...{/cps}"
    "{cps=40}Bel pulang akhirnya berbunyi{/cps}"
    t "{cps=40}Baiklah, pelajaran hari ini saya akhiri sampai di sini. Jangan lupa pelajari bab selanjutnya tentang 'Konsekuensi dari Sebuah Pilihan'.{/cps}"
    "{cps=35}Nanami-sensei merapikan bukunya dan keluar kelas. Suasana kelas yang tadinya sunyi langsung meledak oleh suara murid-murid yang bersiap pulang.{/cps}"

    v "{cps=40}Fwaah... Akhirnya! Otakku rasanya mau meledak dengerin istilah Latin tadi.{/cps}"
    
    "{cps=35}Vina meregangkan tubuhnya di belakangku, lalu dia mencondongkan tubuh ke depan, berbisik di dekat telingaku.{/cps}"

    v "{cps=35}Hei, Specimen... [y] sudah berdiri tuh. Ingat janjimu tadi pagi, atau kamu mau aku seret ke gudang beneran?{/cps}"

    "{cps=35}Aku menoleh ke depan. Yuuka sudah merapikan tasnya. Dia berdiri di depan mejanya, menungguku dengan tatapan yang sulit dibaca. Matanya masih terlihat dingin.{/cps}"

    y "{cps=40}Sepertinya nanti saja deh [v], kan kita ada kegiatan lain bukan?{/cps}"
    v "{cps=35}Ah! iya juga... Hah...{/cps}"
    v "{cps=35}[mc], kamu mau ikut kami?{/cps}"
    mc "{cps=35}Kemana?{/cps}"
    v "{cps=35}Gudang belakang, kami berdua mau melakukan audit inventaris{/cps}"
    mc "{cps=35}Sepertinya tidak..{/cps}"
    v "{cps=35}Ah, kamu juga ada kegiatan sastra ya...{/cps}"
    yk "{cps=35}Wah kebetulan banget! kami dari sastra juga akan ke gudang{/cps}"
    "{cps=35}[yk] datang ke mejaku bersama dengan [sh]{/cps}"
    mc "{cps=35}Loh kalian?{/cps}"
    yk "{cps=35}Kebetulan senior dari klub sastra menyuruh aku dan oneesan untuk ke gudang itu{/cps}"
    yk "{cps=35}Karena kalian berdua dari osis juga ada urusan disana, kenapa kita nggak bersama-sama saja?{/cps}"
    v "{cps=35}Hmmm... Ide bagus! Gimana, [y]? Boleh kan mereka ikut?{/cps}"
    "{cps=35}Yuuka diam seribu bahasa. Dia menatap Shoko sejenak—yang masih menolak membalas tatapannya—lalu beralih menatapku dengan tatapan yang seolah berkata: {i}'Lagi-lagi dia?'{/i}{/cps}"
    y "{cps=40}Terserahlah. Gudang itu milik sekolah, bukan milik OSIS. Ayo berangkat.{/cps}"
    "{cps=35}Yuuka berjalan lebih dulu tanpa menungguku. Langkah kakinya terdengar tegas dan cepat.{/cps}"
    "{cps=35}Kami pun bergegas berjalan ke gudang dengan tujuan masing-masing{/cps}"

    # --- PERJALANAN ---

    scene bg_school_corridor_afternoon with fade
    play music "audio/bgm/tiptoeing around.mp3" fadein 2.0

    "{cps=35}Kami berlima berjalan menyusuri koridor menuju gedung aula. Posisinya benar-benar canggung.{/cps}"
    "{cps=35}[v] dan [yk] di depan, sementara aku berjalan di tengah, 'dikawal' oleh [sh] di sisi kiri dan [y] di sisi kanan.{/cps}"
    "{cps=35}[v] dan [yk] terlihat asik membahas kegiatan yang akan mereka lakukan nanti{/cps}"
    "{cps=35}Sementara itu, aku terjebak di barisan belakang. Aku berjalan di tengah, 'dikawal' oleh [sh] di sisi kiri dan [y] di sisi kanan.{/cps}"
    "{cps=35}Suasananya sangat aneh. Aku bisa merasakan ujung jari [sh] sesekali menarik lengan seragam kiriku. Gerakannya ragu-ragu, seolah dia masih tidak ingin melepaskan apa yang baru saja dia temukan di loteng tadi.{/cps}"
    "{cps=35}Namun, belum sempat aku bereaksi, tiba-tiba aku merasakan tarikan yang jauh lebih tegas di lengan seragam kananku.{/cps}"
    "{cps=35}Aku melirik ke kanan. [y] sedang menggenggam kain seragamku dengan erat. Dia tidak menatapku—dia menatap lurus ke depan dengan wajah cemberut—tapi genggamannya seolah berkata: 'Jangan berani-berani menjauh dariku'.{/cps}"
    mc "{cps=35}Ano... kalian berdua...{/cps}"
    # --- MOMEN UNISON (BARENGAN) ---
    show yuuka_stern at right
    show shoko_neutral at left
    with dissolve
    "[y] dan [sh]" "{cps=35}Diamlah, [mc]!{/cps}"
    with vpunch # Efek layar bergetar karena MC kaget
    "{cps=35}Aku langsung bungkam seribu bahasa. Kalau dua orang ini sudah bicara bersamaan, lebih baik aku tidak mencari penyakit.{/cps}"
    "[v] dan [yk]" "{cps=35}Hm?{/cps}"
    "{cps=35}[v] dan [yk] menoleh ke belakang sebentar, melihat posisiku yang seperti sandwich{/cps}"
    "[v] dan [yk]" "{cps=35}Pfffttt{/cps}"
    "{cps=35}Mereka hanya menyeringai nakal tanpa niat membantu sama sekali.{/cps}"
    "{cps=35}Sialan kalian...{/cps}"
    "{cps=35}Aku pun diam sepanjang perjalanan. Sampai...{/cps}"
    "{cps=35}Kami pun sampai di depan pintu gudang yang berat itu. Tujuan kami berbeda, tapi aku tahu... di dalam sana, hanya akan ada satu kebenaran yang terungkap.{/cps}"
    v "{cps=35}Nah, karena kita sudah sampai disini, mungkin kalian bisa jelaskan tujuan kalian{/cps}"
    yk "{cps=35}Hmmm... Kalau aku sih disini untuk mengambil buku berisikan naskah{/cps}"
    v "{cps=35}Naskah? seperti apa?{/cps}"
    yk "{cps=35}Semacam buku, katanya itu sudah lama sekali.. sekitar 12 tahun yang lalu{/cps}"
    v "{cps=35}Heee... perlu kami bantu?{/cps}"
    yk "{cps=35}Kalau tidak merepotkan sih{/cps}"
    v "{cps=35}Oke kalau begitu, sebagai gantinya kalian bantuin kami untuk melakukan audit ya{/cps}"
    yk "{cps=35}Deal!{/cps}"
    "{cps=35}Kami pun bekerjasama untuk melakukan audit dan juga mencari buku tersebut{/cps}"
    "{cps=35}Dari yang aku dengar, buku itu sudah cukup tua dan kusam{/cps}"
    "{cps=35}Tapi selama pencarian dan audit...{/cps}"
    "{cps=35}Aku tidak menemukan buku itu sama sekali{/cps}"
    v "{cps=35}Hah... auditnya sudah selesai, terimakasih ya karena kalian telah membantu kami{/cps}"
    yk "{cps=35}Tidak masalah.. tapi apa bukunya sudah ditemukan?{/cps}"
    v "{cps=35}Untuk itu aku tidak menemukan sama sekali{/cps}"
    v "{cps=35}Mencari buku di tempat seperti ini sama seperti mencari jarum di tumpukan jerami{/cps}"
    yk "{cps=35}Ehehe iya sih..{/cps}"
    "{cps=35}Dibagian lain..{/cps}"
    "{cps=35}[sh] dan [y] sedang berduaan, dan ingin membahas semua yang terjadi{/cps}"
    sh "{cps=35}Ada apa kamu memanggilku sampai kita berdua disini?{/cps}"
    y "{cps=35}Begini [sh]...{/cps}"
    y "{cps=35}Kamu ngapain tadi lari ke loteng sambil menangis?{/cps}"
    sh "{cps=35}Kamu mau tahu yang sebenarnya?{/cps}"
    y "{cps=35}Iya! Karena aku tidak ingin terjadi hal aneh kepada teman masa kecilku{/cps}"
    sh "{cps=35}Baiklah kalau begitu{/cps}"
    "{cps=35}[sh] menceritakan semua yang terjadi, mulai dari pertemuan kembali setelah 10 tahun sampai kejadian di loteng{/cps}"
    y "{cps=35}Jadi begitu...{/cps}"
    y "{cps=35}Aku tidak menyangka [mc] seperti itu... pasti berat untukmu [sh]{/cps}"
    sh "{cps=35}Begitulah. Menyakitkan saat menyadari bahwa hanya aku yang memegang erat janji itu sendirian.{/cps}"
    "{cps=35}Yuuka terdiam. Dia menatap Shoko dengan tatapan yang tidak lagi sinis. Ada rasa solidaritas yang muncul di antara mereka berdua sebagai sesama orang yang 'dibuat pening' oleh [mc].{/cps}"
    y "{cps=35}Lalu, kenapa kamu tidak membencinya saja?{/cps}"
    sh "{cps=35}Karena... {w=0.5}dia menyelamatkanku tadi. Bukan hanya dari jatuh, tapi dari pikiranku sendiri.{/cps}"
    y "{cps=35}Jadi begitu...{/cps}"
    mc "{cps=35}Ano... kalian sampai kapan ada disana?{/cps}"
    "{cps=35}Aku melihat mereka berbicara dibawah rak yang diatasnya terdapat kardus{/cps}"
    y "{cps=35}Eh [mc]! Sebentar lagi kami seles-{/cps}"
    "{cps=35}*Swing{/cps}"
    "{cps=35}Dan kardus itu mulai bergerak ke bawah{/cps}"
    mc "{cps=35}Kalian berdua, awas!{/cps}"
    "[sh] dan [y]" "{cps=35}Eh?{/cps}"

    "{cps=35}Tanpa pikir panjang, aku menerjang ke arah mereka. Rak tua di atas mereka berderit keras, dan kardus-kardus besar itu meluncur turun dengan cepat.{/cps}"

    with vpunch
    play sound "audio/sfx/jatoh.mp3"
    "{b}*BRAAAK!*{/b}"

    "{cps=35}Debu tebal seketika memenuhi udara, membuatku terbatuk-batuk. Aku merasakan tubuhku menghantam lantai kayu yang keras, rasa sakit menjalar di punggungku.{/cps}"
    "{cps=35}Tapi setidaknya... aku berhasil menarik mereka berdua ke dalam dekapanku sebelum kardus-kardus itu menghantam mereka.{/cps}"
    "{cps=35}Lampu gudang tiba-tiba mati karena guncangan rak tadi. Suasana menjadi sangat gelap, hanya menyisakan sunyi dan debu yang menyesakkan.{/cps}"
    mc "{cps=35}Uhuk... kalian... kalian tidak apa...{/cps}"
    mc "{cps=35}Apa..?{/cps}"
    "{cps=35}Dalam kegelapan total, aku mencoba mencari tumpuan untuk bangkit. Namun, tanganku meraba sesuatu yang terasa... berbeda.{/cps}"
    "{cps=35}apa yang ada di genggamanku?{/cps}"
    "{cps=35}*squish{/cps}"
    "{cps=35}Aku meremas tangan kiriku secara tidak sengaja. Terasa sangat empuk, seperti bantal yang kenyal.{/cps}"
    unknown "{cps=35}Kyah~{/cps}"
    "{cps=35}Aneh...{/cps}"
    "{cps=35}*squish{/cps}"
    "{cps=35}Aku meremas tangan kananku. Rasanya sedikit lebih padat namun tetap sangat lembut.{/cps}"
    unknown "{cps=35}A-auch~... Hei!{/cps}"
    "{cps=35}Sepertinya.. aku menyentuh hal yang sangat empuk di kedua tanganku{/cps}"
    "{cps=35}Dan aku akan mendengar teriakan paling berisik yang membuat gendang telingaku pecah{/cps}"
    "{cps=35}Lampu berkedip sejenak, lalu menyala kembali dengan terang.{/cps}"
    "{cps=35}Dan... sepertinya gendang telingaku akan rusak{/cps}"
    mc "{cps=35}Ya... aku tidak ekspek akan seperti in-{/cps}"
    y "{cps=40}{b}IKAZAKIII!!!!{/b}{/cps}"

    show yuuka_blush at right
    show shoko_blush at left
    with dissolve

    "{cps=35}Cahaya kembali menyinari gudang, dan pemandangan di depanku membuat jantungku hampir berhenti.{/cps}"
    "{cps=35}Aku sedang tengkurap di antara mereka berdua. Tangan kiriku berada tepat di atas dada Shoko, dan tangan kananku... mencengkeram pinggang Yuuka dengan sangat erat.{/cps}"

    y "{cps=40}K-kamu... dasar mesum! Penjahat!{/cps}"
    sh "{cps=40}Ikazaki-kun... {w=0.3}ternyata sisi lainmu... lebih berani dari yang kukira.{/cps}"

    # Penemuan Buku di tengah kekacauan
    "{cps=35}Tepat di saat itu, sebuah buku coklat jatuh dari tumpukan kardus yang robek, mendarat tepat di atas kepala kami{/cps}"
    
    mc "{cps=35}T-tunggu! Ini kecelakaan! Dan lihat... buku itu!{/cps}"
    y "{cps=35}Buku apa yang kamu maksud, dasar cabul!{/cps}"
    "{cps=35}Disaat yang tidak menguntungkan ini{/cps}"
    v "{cps=35}Oi! Kalian nggak apa-apa? Suaranya berisik banget—{/cps}"
    "{cps=35}2 orang yang tidak aku ingin datang ke ruangan ini malah muncul seketika{/cps}"
    v "{cps=35}HUE- kamu ini sepertinya mencari kesempatan dalam kesempitan ya [mc]{/cps}"
    yk "{cps=35}[mc]... tidak aku sangka ternyata kamu..{/cps}"
    mc "{cps=35}BUKAN BEGITU!{/cps}"
    "{cps=35}Aku segera meloncat mundur, menjauh dari Yuuka dan Shoko dengan wajah yang kurasa sudah semerah tomat matang. Suasana gudang mendadak lebih panas daripada oven.{/cps}"
    v "{cps=35}Terus itu tangan tadi lagi ngapain? Hayoo...{/cps}"
    mc "{cps=35}Tadi itu raknya mau jatuh! Aku cuma mau melindungi mereka!{/cps}"
    "{cps=35}Aku menunjuk rak yang miring dan buku cokelat yang tadi menimpa kami{/cps}"
    sh "{cps=35}[mc]... kamu...{/cps}"
    y "{cps=35}Bodoh. Kalau kamu terluka bagaimana?{/cps}"
    "{cps=35}Lebih baik aku terluka dibanding teman masa kecilku yang terluka{/cps}"
    "{cps=35}[sh] dan [y] langsung tersipu malu{/cps}"
    y "{cps=35}Dasar...{/cps}"
    "{cps=35}Kamu ini ya.. dari dulu memang tidak pernah berubah{/cps}"
    "{cps=35}Tapi tetap saja...{/cps}"
    "{cps=35}Aku langsung memungut buku cokelat itu untuk mengalihkan pembicaraan.{/cps}"
    mc "{cps=35}Lihat ini... buku ini keluar dari kardus yang hampir menimpa [y] dan [sh]{/cps}"
    "{cps=35}Melihat buku itu, raut wajah Yukie dan Shoko langsung berubah serius. Godaan mereka terhenti seketika.{/cps}"
    yk "{cps=35}Buku ini...{/cps}"
    yk "{cps=35}Ini yang senior cari! terimakasih ya, kalian bertiga!{/cps}"
    "{cps=35}Sebuah kebetulan macam apa ini?{/cps}"
    "{cps=35}Memangnya buku apa sih itu?{/cps}"
    yk "{cps=35}Kalau tidak salah...{w=0.1} buku itu adalah proposal lama dari klub sastra{/cps}"
    "{cps=35}Sebentar, bukannya itu ada namamu [mc]?{/cps}"
    mc "{cps=35}Sepertinya begitu. Ada nama 'Ikazaki' yang tertulis samar di sampulnya.{/cps}"
    y "{cps=35}Kalau tidak salah ketua pernah bilang kakakmu itu sekolah disini 12 tahun yang lalu kan?{/cps}"
    mc "{cps=35}Iya sih... dari namanya tidak salah lagi, itu adalah kakak{/cps}"
    mc "{cps=35}Kenapa bisa ada disini?{/cps}"
    v "{cps=35}Sebaiknya kita bawa ini ke ruang osis{/cps}"
    yk "{cps=35}Tapi seniorku yang meminta...{/cps}"
    v "{cps=35}Bagaimana kalau kamu hubungi seniormu yang dari sastra untuk berkumpul di ruang osis juga?{/cps}"
    yk "{cps=35}Ide yang bagus!{/cps}"
    "{cps=35}Seketika [yk] langsung menghubungi senior yang ada di ruang sastra{/cps}"
    yk "{cps=35}Sudah aku hubungi, nanti dia ada di ruangan osis{/cps}"
    v "{cps=35}Bagus, sekarang mari kita pindah{/cps}"
    "{cps=35}Kami pun pindah lokasi ke ruangan osis{/cps}"
    "{cps=35}Antara rasa malu yang luar biasa, punggung yang pegal, dan buku misterius di genggamanku...{/cps}"
    "{cps=35}Satu hal yang pasti: Hidupku tidak akan pernah sama lagi.{/cps}"
    scene black with fade
    stop music fadeout 2.0
    "{cps=35}Langkah kaki kami bergema di koridor yang sepi. Matahari sore masuk melalui jendela, memberikan warna oranye yang tajam pada pintu ruang OSIS.{/cps}"

    play sound "audio/sfx/knock door.mp3"
    "{b}*Tok! Tok! Tok!*{/b}"

    mc "{cps=35}Permisi...{/cps}"

    play sound "audio/sfx/door.mp3"
    "{cps=35}Begitu pintu terbuka, aroma teh melati dan kertas baru menyambut kami. Di balik meja besar itu, Maya-senpai sudah duduk dengan posisi yang sangat tegak.{/cps}"

    show maya_neutral at center with dissolve
    m "{cps=40}Kalian terlambat 15 menit dari jadwal audit. Dan kulihat... kalian membawa 'tamu' yang tidak diundang.{/cps}"
    "{cps=35}Maya menatap Shoko dan Yukie dengan tatapan dingin yang belum pernah kulihat sebelumnya.{/cps}"

    y "{cps=35}Maaf, Kak. Tadi ada sedikit insiden di gudang. Dan... kami menemukan ini.{/cps}"

    "{cps=35}Aku melangkah maju dan meletakkan buku cokelat itu di atas meja Maya.{/cps}"

    "{cps=35}Seketika, kulihat raut wajah Maya berubah. Hanya sesaat, tapi aku bisa melihat matanya membelalak lebar. Tangannya yang sedang memegang pena sedikit mengencang.{/cps}"

    m "{cps=40}Di mana... di mana kalian menemukan ini?{/cps}"
    sh "{cps=35}Di bawah rak yang hampir mencelakai kami, Kak.{/cps}"
    m "{cps=35}Mencelakai? Memangnya kalian kenapa sampai seperti itu?{/cps}"
    v "{cps=35}Ya... tidak bisa dijelaskan sih kak{/cps}"
    "{cps=35}Shoko melangkah maju, berdiri di sampingku. Dia tidak lagi terlihat lemah. Dia menatap kak [m] dengan berani.{/cps}"
    m "{cps=35}Shirohana Shoko... sudah kubilang jangan mencampuri urusan ini.{/cps}"
    "{cps=35}Tiba-tiba, suara langkah kaki terdengar dari arah pintu yang masih terbuka.{/cps}"
    unknown "{cps=35}Maaf saya terlambat. Sepertinya diskusinya sudah dimulai ya?{/cps}"
    m "{cps=35}Wah-wah... akhirnya kamu muncul juga ya, setelah pembukaan kemarin{/cps}"
    "{cps=35}Kisaragi [f].{/cps}"
    "{cps=35}Ah... iya juga, aku masuk ke organisasi ini karena penasaran dengan [sh]{/cps}"
    "{cps=35}Namun aku tidak tahu siapa saja anggota yang ada di dalamnya, termasuk ketua.{/cps}"
    "{cps=35}Parah sekali diriku ini{/cps}"
    f "{cps=35}Ya... begitulah{/cps}"
    f "{cps=35}Banyak kegiatan setelah penerimaan murid baru{/cps}"
    f "{cps=35}Padahal itu harusnya pekerjaan osis{/cps}"
    m "{cps=35}Mau gimana lagi [f], kan anggota osis tidak cukup untuk mengurusi semua itu{/cps}"
    "{cps=35}[f] memandang [m] dengan wajah yang sinis, seakan tidak senang dengan suasana saat ini{/cps}"
    f "{cps=35}Jadi? Ada apa memangnya?{/cps}"
    m "{cps=35}Kamu tahu kan proposal ini?{/cps}"
    "{cps=35}[m] menunjukkan proposal itu ke [f]{/cps}"
    f "{cps=35}Ahh! Setelah aku cari selama 1 tahun... akhirnya ketemu juga{/cps}"
    "{cps=35}[f] ingin mengambil proposal itu{/cps}"
    m "{cps=35}Eits! Enak saja, ini itu properti milik osis, ditambah kan ini proposal yang sudah ditolak{/cps}"
    f "{cps=35}Heeee!?{/cps}"
    sh "{cps=35}Ditolak? Atau disembunyikan?{/cps}"
    "{cps=35}[m] terkejut mendengar jawaban dari [sh]{/cps}"
    m "{cps=35}Apa maksudmu?{/cps}"
    sh "{cps=35}Kalau tidak disembunyikan, kenapa proposal itu ada di gudang{/cps}"
    sh "{cps=35}Ditambah di dalam kardus{/cps}"
    "{cps=35}[m] diam seribu bahasa, seakan tidak tahu apa jawaban yang harus dia berikan{/cps}"
    m "{cps=35}Itu... {w=0.5}itu urusan pengurus dua belas tahun yang lalu! Aku hanya menyuruh kalian untuk melakukan audit, tidak lebih{/cps}"
    f "{cps=35}Lantas kenapa kamu takut sekali dengan proposal itu [m]?{/cps}"
    f "{cps=35}Kamu tidak mungkin menyembunyikan sesuatu kan?{/cps}"
    m "{cps=35}Uhm....{/cps}"
    "{cps=35}Para anggota osis menatap wajah [m] dengan wajah yang penuh dengan pertanyaan{/cps}"
    m "{cps=35}Hah.... ujung-ujungnya harus aku yang menjelaskan kembali ya?{/cps}"
    m "{cps=35}Baiklah, akan aku jelaskan terkait proposal itu.{/cps}"
    "{cps=35}[m] langsung berdiri dari kursinya, dan mulai bercerita{/cps}"
    m "{cps=35}Proposal itu memang sudah ada sejak 12 tahun yang lalu, dibuat oleh Ikazaki [mi].{/cps}"
    m "{cps=35}Namun proposal itu tidak pernah direalisasikan oleh pihak sekolah maupun osis{/cps}"
    m "{cps=35}Meskipun dia adalah ketua osis saat itu{/cps}"
    mc "{cps=35}Kenapa kak [m] tahu sampai sedetail itu?{/cps}"
    m "{cps=35}Karena kakakmu yang memberikan mandat untuk merealisasikan kegiatan dalam proposal itu kepadaku{/cps}"
    mc "{cps=35}Sejak kapan? Seingatku kak [m] hanya bilang kalau kakak tahu nama dari kakakku{/cps}"
    "{cps=35}Aku menatap kak [m] dengan serius dan penuh rasa penasaran{/cps}"
    "{cps=35}Kenapa kamu menatapku sampai segitunya? Kamu tidak mempercayaiku?{/cps}"
    "{cps=35}Kalaupun kak [mi] memberikan mandat kepadamu, coba ceritakan{/cps}"
    "{cps=35}[f] juga ikut membuat [m] terasa terdesak{/cps}"
    "{cps=35}Itu semua terjadi sekitar 10 tahun yang lalu... ketika proposal itu selesai dibuat{/cps}"
    
    "Kakaknya [m]" "{cps=35}Haaaaahhhhh... pegalnya{/cps}"
    "Kakaknya [m]" "{cps=35}Kamu yakin mau ngejalanin proker ini [mi]? Kita kekurangan orang loh{/cps}"
    v "{cps=35}Siapa yang bertanya?{/cps}"
    y "{cps=35}Hush! Kak [m] masih bercerita, cukup dengarkan{/cps}"
    v "{cps=35}Ehehe, maaf{/cps}"
    m "{cps=35}Yang bertanya kakakku, dia bernama Kirishima [sz]{/cps}"
    v "{cps=35}Heee...{/cps}"
    m "{cps=35}Bisakah aku lanjut?{/cps}"
    y "{cps=35}Silahkan kak dilanjut{/cps}"
    "{cps=35}Baiklah.{/cps}"
    mi "{cps=35}Hmmm gimana ya...{/cps}"
    mi "{cps=35}Kita tunda proker ini dulu saja{/cps}"
    sz "{cps=35}Kamu yakin?{/cps}"
    mi "{cps=35}Ya... kan belum aku majuin ke guru, ditambah juga kan kita belum tahu anak sastra mau atau tidak untuk diajak kerjasama{/cps}"
    sz "{cps=35}Memang sih{/cps}"
    sz "{cps=35}Namun mau ditunda sampai kapan{/cps}"
    mi "{cps=35}Nah itu... gimana kalau adikmu?{/cps}"
    sz "{cps=35}Hue- dia masih kecil hei! masa iya kita harus nunggu 10 tahun?{/cps}"
    "{cps=35}Ya.. daripada prokernya tidak jalan kan? Nanti aku suruh adikku masuk ke sekolah kita deh{/cps}"
    sz "{cps=35}Dia anak laki tahu{/cps}"
    mi "{cps=35}Ya... siapa tahu nanti ada perubahan peraturan yang mengizinkan anak laki masuk{/cps}"
    sz "{cps=35}Kamu ini... kayak mimpi di siang bolong{/cps}"
    mi "{cps=35}Aku nggak bermimpi kok, pasti kejadian{/cps}"
    mi "{cps=35}Kan kamu yang akan mengurus administrasi sekolah kita nantinya{/cps}"
    sz "{cps=35}Hah? Sejak kapan aku mau jadi admin di sekolah?{/cps}"
    sz "{cps=35}Aku aja ingin jadi dokter{/cps}"
    mi "{cps=35}Siapa tahu kan{/cps}"
    mi "{cps=35}Ah! Adiknya [sz]!{/cps}"
    m "{cps=35}Hm? Kenapa kak?{/cps}"
    mi "{cps=35}Kamu nanti masuk ke sekolah yang sama dengan kakakmu ya!{/cps}"
    m "{cps=35}Memangnya kenapa?{/cps}"
    mi "{cps=35}Nanti kamu yang meneruskan pekerjaan kakakmu{/cps}"
    sz "{cps=35}Hei! memangnya dia mau apa?{/cps}"
    mi "{cps=35}Tenang saja... kamu akan dibantu adikku kok{/cps}"
    m "{cps=35}Adik kakak? Namanya siapa?{/cps}"
    mi "{cps=35}Ikazaki [mc]. Kamu ingat-ingat nama dia ya, soalnya kamu pasti akan bertemu dengannya{/cps}"
    mi "{cps=35}Ditambah dia pasti akan membantumu{/cps}"
    sz "{cps=35}Hei [mi]... jangan mendoktrin adikku yang aneh-aneh!{/cps}"
    mi "{cps=35}Nggak kok, aku cuman memberi masukkan, ditambah kan belum tentu dia mau{/cps}"
    m "{cps=35}Ummm... aku akan berusaha{/cps}"
    "dalam hati [m]" "{cps=35}Aku tidak akan membiarkan perjuangan kakak-kakak sia-sia{/cps}"
    "dalam hati [m]" "{cps=35}Pasti bisa aku jalankan!{/cps}"
    m "{cps=35}Saat itu diriku penuh dengan semangat yang berapi-api{/cps}"
    m "{cps=35}Namun ketika detik-detik terakhir... sebelum mereka mengirim proposal itu ke guru...{/cps}"
    m "{cps=35}Terjadi musibah yang membuat acara ini ditunda dan proposal itu 'dihilangkan'{/cps}"
    m "{cps=35}Aku tidak bisa menceritakan secara detail karena aku tidak tahu apa yang terjadi saat itu{/cps}"
    v "{cps=35}Sial.. kenapa jadi menggantung gini{/cps}"
    "{cps=35}Kalau kalian penasaran, kalian bisa bertanya ke kakakku{/cps}"
    "{cps=35}Kakaknya kak [m] kalau tidak salah namanya [sz] kan?{/cps}"
    "{cps=35}Kedengarannya seperti guru yang ada di ruang kesehatan dan administrasi..{/cps}"
    "{cps=35}Ya memang dia{/cps}"
    "Semua orang" "{cps=35}HEEEEE!?{/cps}"
    mc "{cps=35}Tunggu... Dokter Kirishima yang mana deh orangnya?{/cps}"
    m "{cps=35}Dia yang kamu temui di ruang tata usaha pada hari pertama{/cps}"
    mc "{cps=35}Hmmmm....{/cps}"
    "{cps=35}Jauh banget!{/cps}"
    f "{cps=35}Kenapa penampilan dia jauh banget denganmu?{/cps}"
    m "{cps=35}Ya... aku tidak ingin terlalu mirip sih, ditambah kan beda era{/cps}"
    m "{cps=35}Ada pertanyaan lain?{/cps}"
    v "{cps=35}Mungkin ini... Proposal itu sebaiknya diapain?{/cps}"
    "{cps=35}[f] melangkah maju, tangannya menyentuh sampul kusam buku itu. Tatapannya tidak lagi sinis, melainkan penuh determinasi.{/cps}"
    f "{cps=35}Mungkin biar klub sastra aja yang melakukan revisi, nanti kalian yang menerima, gimana?{/cps}"
    f "{cps=35}Ditambah kan dari cerita tadi memang klub sastra yang ditargetkan{/cps}"
    f "{cps=35}Kalian tidak keberatan kan?{/cps}"
    "{cps=35}[f] memandang kami dengan wajah yang penuh harapan{/cps}"
    mc "{cps=35}Aku tidak masalah sih... kalau kalian?{/cps}"
    yk "{cps=35}Selagi Nee-san setuju, aku tidak masalah{/cps}"
    mc "{cps=35}Kalau kamu [sh]?{/cps}"
    sh "{cps=35}Tidak apa-apa [mc], lagipula kamu ingin membuat kenangan baru kan?{/cps}"
    v "{cps=35}Heeee kenangan apa tuch?{/cps}"
    y "{cps=35}Kamu ini... kebiasaan [v]{/cps}"
    v "{cps=35}Heee apa sih?{/cps}"
    sh "{cps=35}Kamu ga masalah kan [y]?{/cps}"
    y "{cps=35}Hmm! tidak masalah{/cps}"
    if jujur:
        "Dalam hati [y]" "{cps=35}(Selagi ini bisa membantu [mc] menemukan jati dirinya dan memenuhi janji kakaknya... aku akan mendukungnya. Meskipun harus bekerja sama dengan Sastra.){/cps}"
    else:
        y "{cps=35}Namun pastikan kalau [mc] tidak berbohong{/cps}"
        mc "{cps=35}Hei!{/cps}"
        sh "{cps=35}Tenang saja, aku pasti bisa membuat [mc] menjadi orang yang jujur{/cps}"
    m "{cps=35}Baiklah, aku serahkan proposal ini ke kalian, pastikan acara dari proposal itu bisa berjalan ya!{/cps}"
    "{cps=35}Maya menyerahkan buku cokelat itu kepada Fumi. Cahaya matahari sore yang merah masuk melalui jendela, menyinari buku itu seolah-olah sedang memberikan restu.{/cps}"
    "Anggota sastra" "{cps=35}Baik!{/cps}"
    "{cps=35}Sore itu, di ruang OSIS yang sakral, sebuah janji yang terkubur selama 12 tahun akhirnya mulai berdenyut kembali.{/cps}"
    f "{cps=35}Baiklah, kami kembali ke ruangan kami ya [m], sampai jumpa!{/cps}"
    m "{cps=35}Sampai jumpa{/cps}"
    "{cps=35}*clek{/cps}"
    "{cps=35}Kami pun berjalan menuju ruangan kami{/cps}"
    "{cps=35}Di tengah perjalanan, [sh] dan [yk] seperti biasa berada di depanku{/cps}"
    "{cps=35}Dan kak [f] berdiri di sampingku dan mulai membuka pembicaraan{/cps}"
    f "{cps=35}Hunnngggh pegalnya...{/cps}"
    f "{cps=35}Maaf ya [mc], hari pertamamu di klub sastra malah seperti ini...{/cps}"
    mc "{cps=35}Tidak apa-apa kok kak, lagipula kan memang kesalahanku yang terlambat gabung{/cps}"
    f "{cps=35}Tapi aku penasaran deh, soalnya kan di pendaftaran itu cuman [sh] dan [yk] yang beneran mendaftar{/cps}"
    f "{cps=35}Nah kamu kenapa tiba-tiba mau gabung ke klub kita?{/cps}"
    f "{cps=35}Sebagai ketua aku harus tahu tujuan masing-masing anggotaku{/cps}"
    mc "{cps=35}Ummnnn... gimana ya kak..{/cps}"
    mc "{cps=35}Aku cukup tertarik dengan kegiatan klub ini sih, seperti menulis cerita, buat puisi dan sebagainya{/cps}"
    mc "{cps=35}Ditambah dengan proposal yang tadi dibahas itu...{/cps}"
    "{cps=35}Kak [f] menepuk bahuku{/cps}"
    f "{cps=35}Tenang saja! Kita pasti bisa kok, menjalankan proker ini!{/cps}"
    f "{cps=35}Demi kakakmu{/cps}"
    mc "{cps=35}Iya kak, aku akan berusaha.{/cps}"

    f "{cps=35}Nah, begitu dong! Oh iya, berhubung ini sudah sore, kalian bertiga langsung pulang saja ya.{/cps}"
    f "{cps=35}Biar proposal ini aku coba baca dahulu dirumah. Jadi besok kita mulai bedah isinya bersama-sama.{/cps}"
    sh "{cps=35}Baik, Kak [f]. Sampai jumpa besok.{/cps}"
    yk "{cps=35}Daa-daa Kak [f]! Ayo [mc], [sh]-nee, kita ke gerbang bersama!{/cps}"
    "{cps=35}Kami bertiga berpisah dengan Kak [f] di depan ruangan klub. Dia memeluk buku cokelat itu erat-erat, seolah sedang memegang kunci masa depan kami semua.{/cps}"

    "{cps=35}Langkah kaki kami bergema di koridor yang mulai sepi. Cahaya matahari merah padam di balik gedung sekolah, menyisakan bayangan panjang yang seolah-olah sedang menari di dinding kayu.{/cps}"

    "{cps=35}Hari ini dimulai dengan kebingungan, diwarnai dengan insiden di gudang, dan diakhiri dengan sebuah beban janji 12 tahun yang lalu.{/cps}"

    "{cps=35}Aku menyentuh bahuku, tempat di mana armband biru OSIS tadi sempat terpasang. Rasanya masih ada sisa dingin dari kain itu di sana.{/cps}"

    yk "{cps=35}Hei, [mc]!{/cps}"

    mc "{cps=35}Hm?{/cps}"

    yk "{cps=35}Kamu jangan melamun terus dong! Nanti kalau kesambet penunggu perpustakaan lama, aku nggak mau tanggung jawab ya!{/cps}"

    mc "{cps=35}Aku tidak melamun kok. Aku hanya... memikirkan banyak hal.{/cps}"

    yk "{cps=35}Hah... kebiasaan.{/cps}"

    "{cps=35}[yk] berlari ke depanku. Dia berbalik dengan lincah, lalu menarik tangan [sh] yang sedari tadi berjalan pelan di sampingku.{/cps}"

    yk "{cps=35}Nee-san juga jangan diam saja! Ayo, katakan sesuatu padanya!{/cps}"

    sh "{cps=35}Ah! Apa yang— {w=0.3} Yukie, lepaskan!{/cps}"

    "{cps=35}Yukie memberikan sinyal kedipan mata yang sangat jelas kepada Shoko. Shoko terdiam sejenak, wajahnya yang pucat merona tipis di bawah sinar senja.{/cps}"

    sh "{cps=35}Ah... {w=0.5}benar juga.{/cps}"

    "{cps=35}Mereka berdua berhenti tepat di depan gerbang sekolah yang besar. Angin sore meniup rambut merah mereka, menciptakan pemandangan yang entah kenapa terasa sangat familiar... seolah aku pernah melihatnya 10 tahun yang lalu.{/cps}"

    show shoko_smile at left
    show yukie_smile at right
    with dissolve

    "[sh] & [yk]" "{cps=35}Mulai hari ini, mohon kerjasamanya ya, [mc]!{/cps}"

    "{cps=35}Suara mereka yang bersatu terdengar jernih, memecah kesunyian sore itu. Aku tertegun sejenak sebelum akhirnya mengangguk pelan.{/cps}"

    mc "{cps=35}Iya. Mohon kerjasamanya juga.{/cps}"

    scene black with fade
    stop music fadeout 3.0

    "{cps=35}Di antara rasa malu di gudang, rahasia keluarga Kirishima, dan impian [mi]-nee yang berat...{/cps}"

    "{cps=35}Satu hal yang pasti: Mulai besok, melodi yang hilang itu akan mulai terdengar lagi.{/cps}"

    "{cps=35}Dan mulai hari ini... aku bersumpah tidak akan membiarkan siapa pun 'menghilang' lagi.{/cps}"

    jump chapter_2_end