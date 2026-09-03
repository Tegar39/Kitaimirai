label chapter_2_kesempatan:
    scene bg_front_house_morning with fade
    play music "audio/soft_melancholy.mp3" fadein 2.0

    "{cps=35}Aku melangkah keluar dari pagar rumah. Seperti biasa, sosok dengan kacamata itu sudah berdiri di sana, menendang-nendang kerikil kecil dengan sepatunya.{/cps}"

    y "{cps=60}Pagi, [mc]! Kamu terlihat... {w=0.1} sedikit lebih baik dari kemarin?{/cps}"

    "{cps=35}Yuuka mendekat, menatap wajahku dengan saksama. Ada gurat kekhawatiran yang coba ia sembunyikan di balik senyumnya.{/cps}"

    mc "{cps=40}Pagi, Yuuka. Yah, setidaknya aku sudah bisa tidur semalam.{/cps}"

    y "{cps=60}Syukurlah... {w=0.1} Aku kepikiran terus soal kejadian kemarin. Maaf ya kalau aku kemarin tidak menemanimu ke ruang itu{/cps}"
    y "{cps=60}Kamu tidak diapa-apain kan?{/cps}"
    "{cps=35}Aku menggelengkan kepala, berusaha meyakinkan Yuuka bahwa aku baik-baik saja.{/cps}"
    mc "{cps=40}Tidak kok, aku baik-baik saja. Kamu nggak perlu khawatir.{/cps}"
    "{cps=35}Yuuka menghela napas lega, senyumnya kembali mengembang.{/cps}"
    y "{cps=60}Aku senang mendengarnya. Aku benar-benar khawatir loh...{/cps}"
    y "{cps=60}Memangnya kamu kemarin ngapain saja di ruangan itu?{/cps}"
    "{cps=35}Aku berpikir keras...{/cps}"
    "{cps=35}Apa aku harus memberitahunya?{/cps}"
    y "{cps=60}Memangnya kamu kemarin ngapain saja di ruangan itu?{/cps}"

    menu:
        "Ceritakan semuanya":
            $ jujur = True
            $ yuuka_rel += 5
            "{cps=35}Aku menghela napas panjang. Tidak ada gunanya menyembunyikan ini dari Yuuka. Dia sudah ada di sampingku sejak lama.{/cps}"
            
            mc "{cps=40}Sebenarnya... {w=0.1} Maya-senpai membahas tentang Kakakku yang telah tiada. Ikazaki [mi]. Ternyata dia adalah Ketua OSIS terdahulu, 10 tahun yang lalu.{/cps}"
            
            y "{cps=60}Eh?! Kakakmu... {w=0.1} Ketua OSIS di sekolah ini juga?{/cps}"
            
            mc "{cps=40}Iya. Dan Maya-senpai sepertinya sangat menghormatinya. Dia memintaku untuk memilih organisasi hari ini, sebagai bentuk 'kontribusi'... {w=0.1} atau mungkin agar aku tidak berakhir seperti Kakak.{/cps}"
            
            "{cps=35}Yuuka terdiam lama. Matanya tampak berkaca-kaca di balik kacamatanya, seolah dia baru menyadari beban berat yang kupikul sendirian semalam.{/cps}"
            
            y "{cps=60}Jadi itu alasannya... {w=0.1} Aku tidak tahu kalau masalahnya sedalam itu. Maafkan aku, [mc]...{/cps}"
            y "{cps=60}Lalu... {w=0.1} sekarang bagaimana? Organisasi mana yang akan kamu pilih?{/cps}"
            "{cps=35}Apakah aku harus memberitahunya?{/cps}"

            menu:
                "Kasih jawaban":
                    $ silent = False
                    if club_choice == "osis":
                        $ yuuka_rel += 5
                        mc "{cps=40}Aku memilih OSIS sih{/cps}"
                        y "{cps=60}Wah....{/cps}"
                        "{cps=35}Yuuka tersenyum bahagia setelah mendengarkan pilihanku{/cps}"
                        y "{cps=60}Aku senang [mc], akhirnya kita bersama lagi{/cps}"
                        mc "{cps=40}Aku memilih ini bukan karena kamu juga ya?{/cps}"
                        y "{cps=60}Lalu?{/cps}"
                        mc "{cps=40}Karena disuruh ayahku juga sih{/cps}"
                        y "{cps=60}Hee....{/cps}"
                        "{cps=35}Aku nggak mungkin bilang alasanku yang sebenarnya...{/cps}"
                        "{cps=35}Karena....{/cps}"
                        "{cps=35}Aku masih memikirkan satu hal...{/cps}"
                        "{cps=35}Kenapa [m] bersikeras untuk mengajakku masuk ke organisasi?{/cps}"
                        "{cps=35}Apa hanya karena aku satu-satunya anak laki di sekolah ini?{/cps}"
                        y "{cps=60}Moh... {w=0.1} kamu ini melamum lagi...{/cps}"
                        "{cps=35}Yuuka bergumam dengan wajah yang sedikit kesal{/cps}"
                        mc "{cps=30}Maaf ya [y]... {w=0.1} soalnya aku lagi banyak pikiran...{/cps}"
                        y "{cps=60}Gapapa kok [mc], kan kamu telah mengalami masa-masa sulit{/cps}"
                        y "{cps=60}Tidak semua orang bisa kuat ketika ada di posisimu{/cps}"


                    elif club_choice == "sastra":
                        $ yuuka_rel -= 3
                        mc "{cps=40}Aku memilih klub sastra{/cps}"
                        y "{cps=60}...Kenapa kamu memilih klub itu?{/cps}"
                        y "{cps=60}Padahal disana tidak ada yang menarik{/cps}"
                        mc "{cps=40}Aku... ada urusan pribadi disana{/cps}"
                        y "{cps=60}Urusan pribadi? Apa maksudmu?{/cps}"
                        mc "{cps=40}Maaf, aku tidak bisa cerita sekarang{/cps}"
                        "{cps=35}Yuuka menatapku dengan tatapan penuh curiga.{/cps}"
                        y "{cps=60}Apa karena si kembar itu?{/cps}"
                        y "{cps=60}Dari kemarin kamu memperhatikan mereka terus, apakah kamu masih terobsesi sama mereka?{/cps}"
                        mc "{cps=40}Bukan... {w=0.1} bukan itu{/cps}"
                        y "{cps=60}Kalau bukan karena mereka, lalu kenapa?{/cps}"
                        mc "{cps=40}Aku cuma... {w=0.1} merasa ada sesuatu yang harus aku selesaikan disana{/cps}"
                        y "{cps=60}Itu belum menjawab apapun [mc]{/cps}"
                        "{cps=35}Yuuka tampak semakin kesal{/cps}"
                        "{cps=35}Yuuka menghentikan langkahnya sejenak. Suasana di antara kami menjadi sangat dingin.{/cps}"
                        mc "{cps=40}Um....{/cps}"
                        "{cps=35}Bagaimana aku harus menjawabnya...{/cps}"
                        y "{cps=60}Terserahlah. Lakukan saja apa yang menurutmu benar.{/cps}"
                        "{cps=35}Yuuka melanjutkan langkahnya dengan wajah yang masih kesal.{/cps}"

                    elif club_choice == None:
                        $ yuuka_rel -= 2
                        mc "{cps=40}Aku tidak gabung ke organisasi manapun{/cps}"
                        y "{cps=60}Hah!?{/cps}"
                        "{cps=35}Yuuka terkejut mendengar jawabanku.{/cps}"
                        y "{cps=60}Kenapa kamu tidak mau gabung? Apa kamu nggak peduli sama masa depanmu?{/cps}"
                        mc "{cps=40}Bukan nggak peduli, aku cuma... {w=0.1} merasa kalau tidak perlu untuk saat ini{/cps}"
                        y "{cps=60}Padahal kamu bisa menambah relasi dan sebagainya{/cps}"
                        y "{cps=60}Aku benar-benar nggak mengerti dengan keputusanmu ini, [mc]{/cps}"
                        mc "{cps=40}Maaf ya, Yuuka. Aku harap kamu bisa mengerti.{/cps}"
                        "{cps=35}Yuuka menatapku dengan tatapan kecewa.{/cps}"
                        y "{cps=60}Entahlah... {w=0.1} aku harap kamu tahu apa yang kamu lakukan.{/cps}"
                        y "{cps=60}Asal nanti kalau aku ataupun dari osis perlu bantuan, kamu bisa bantu ya, [mc]!{/cps}"
                        "{cps=35}Aku mengangguk pelan, berusaha menyembunyikan rasa bersalahku.{/cps}"
                        mc "{cps=40}Tentu saja, Yuuka.{/cps}"
                        "{cps=35}Yuuka melanjutkan langkahnya dengan wajah yang sedikit sedih.{/cps}"


                "Diam saja":
                    $ Silent = True
                    $ yuuka_rel -= 3
                    "{cps=35}Aku terdiam sejenak, tidak tahu harus berkata apa. Aku merasa bersalah karena menyembunyikan sesuatu yang besar dari Yuuka.{/cps}"
                    y "{cps=60}Kenapa kamu diam saja? Apa kamu tidak mau cerita?{/cps}"
                    mc "{cps=40}Entahlah... {w=0.1} aku belum bisa mengatakannya sekarang.{/cps}"
                    "{cps=35}Yuuka menatapku dengan tatapan kecewa.{/cps}"
                    y "{cps=60}Kamu selalu aja....{/cps}"
                    y "{cps=60}Membuatku penasaran setiap kamu ngomong{/cps}"
                    mc "{cps=40}Bukan begitu...{/cps}"
                    mc "{cps=40}Nanti kamu tahu sendiri kok{/cps}"
                    y "{cps=60}Hmm... {w=0.1} ya sudah, terserah kamu deh{/cps}"
                    "{cps=35}Yuuka menghela napas panjang, lalu melanjutkan langkahnya dengan wajah yang sedikit sedih.{/cps}"

        "Tidak perlu (Ceritakan sebagian kecil)":
            $ jujur = False
            $ yuuka_rel -= 5
            mc "{cps=40}Hanya soal peraturan sekolah, Yuuka. Dia memintaku untuk segera menentukan pilihan hari ini atau aku akan kena masalah.{/cps}"
            
            y "{cps=60}Hanya itu? Tapi kenapa wajahmu terlihat pucat sekali? Kamu tidak sedang bohong kan?{/cps}"
            
            mc "{cps=40}Aku serius. Sudahlah, jangan dibahas lagi.{/cps}"
            
            "{cps=35}Yuuka menatapku dengan tatapan curiga. Dia tidak bodoh. Dia tahu ada sesuatu yang besar yang sengaja aku tutup-tutupi darinya.{/cps}"
            y "{cps=60}Kalau kamu tidak mau cerita, ya sudah. Tapi aku harap kamu tahu apa yang kamu lakukan.{/cps}"
            y "{cps=60}Dan jangan sampai kamu menyesal nanti...{/cps}"
            mc "{cps=40}Tentu saja, Yuuka.{/cps}"
            "{cps=35}Yuuka menghela napas panjang, lalu melanjutkan langkahnya dengan wajah yang sedikit sedih.{/cps}"
            "Dalam hati [y]" "{cps=35}Apa yang sebenarnya terjadi dengan [mc]? Kenapa dia terlihat sangat berbeda hari ini...{/cps}"
            "{cps=35}Jarak di antara langkah kami terasa sedikit lebih jauh dari biasanya.{/cps}"

    scene bg_school_gate with fade
    "{cps=35}Sesampainya di gerbang sekolah, aku melihat beberapa gadis sedang berjalan bersama-sama{/cps}"
    if club_choice == "osis":
        "{cps=35}[y] berjalan di depanku{/cps}"
        "{cps=35}Kemudian dia berbalik{/cps}"
        y "{cps=60}Oh iya, [mc]. Kamu duluan ke kelas ya{/cps}"
        y "{cps=60}Nanti aku nyusul, soalnya aku ada urusan{/cps}"
        mc "{cps=40}Oke, hati-hati ya{/cps}"

    elif club_choice == "sastra":
        "{cps=35}[y] berjalan di depanku{/cps}"
        "{cps=35}Tanpa sepatah kata dia sebutkan{/cps}"
        "{cps=35}[y] langsung meninggalkanku{/cps}"
        "{cps=35}Aku ingin mengejarnya... {w=0.1} tapi entah kenapa kaki ini tidak mau bergerak untuk mengejarnya{/cps}"

    elif club_choice == None:
        "{cps=35}[y] berjalan di depanku{/cps}"
        "{cps=35}Kemudian dia berbalik{/cps}"
        y "{cps=60}Oh iya, [mc]. Kamu duluan ke kelas ya{/cps}"
        y "{cps=60}Nanti aku nyusul, soalnya aku ada urusan{/cps}"
        mc "{cps=40}Urusan apa?{/cps}"
        y "{cps=60}Biasa lah, OSIS{/cps}"
        mc "{cps=40}Heh, babu sekolah{/cps}"
        y "{cps=60}A-apa sih! Intinya nanti kamu harus bantu-bantu aku ya!{/cps}"
        "{cps=35}[y] mengatakan itu dengan nada yang sedikit kesal{/cps}"
        mc "{cps=40}Ehehe... {w=0.1} iya iya, nanti kalau aku senggang ya{/cps}"
        y "{cps=60}Hmph, dasar... {w=0.1} aku pergi dulu{/cps}"
        y "{cps=60}Sampai jumpa di kelas, [mc]!{/cps}"
        mc "{cps=40}Oke, hati-hati ya{/cps}"

    elif silent:
        "{cps=35}[y] berjalan di depanku{/cps}"
        "{cps=35}Tanpa sepatah kata dia sebutkan{/cps}"
        "{cps=35}Kenapa jadi canggung gini...{/cps}"
        y "{cps=60}......[mc]{/cps}"
        mc "{cps=40}Ya?{/cps}"
        y "{cps=60}Kamu duluan ke kelas aja{/cps}"
        y "{cps=60}Nanti aku nyusul{/cps}"
        mc "{cps=40}Memangnya kenapa?{/cps}"
        y "{cps=60}Memangnya urusanmu?{/cps}"
        "{cps=35}Aku terdiam sejenak{/cps}"
        "{cps=35}Sial... {w=0.1} kenapa situasinya berbalik{/cps}"
        "{cps=30}[y] Memandangku dengan wajah yang sedikit ngeselin{/cps}"
        mc "{cps=40}Oh gitu ya cara mainnya...{/cps}"
        y "{cps=60}Hah? Apa maksudmu?{/cps}"
        mc "{cps=40}Ah nggak, aku hanya berbicara sendiri{/cps}"
        mc "{cps=40}Kamu kalau mau pergi gapapa, hati-hati ya{/cps}"
        y "{cps=60}Cih! dasar{/cps}"

    elif jujur == False :
        "{cps=35}[y] berjalan di depanku{/cps}"
        "{cps=35}Tanpa sepatah kata dia sebutkan{/cps}"
        mc "{cps=40}Ano.....{/cps}"
        y "{cps=60}Aku ada urusan...{/cps}"
        y "{cps=60}Sampai jumpa{/cps}"
    "{cps=35}[y] langsung meninggalkanku sendirian di lapangan ini{/cps}"

    "{cps=35}Aku hanya bisa menatap punggung Yuuka yang semakin menjauh di koridor. Perasaan tidak tenang ini masih bergelayut di dadaku.{/cps}"

    play sound "audio/shoes_tap.mp3" # Suara langkah kaki sepatu pantofel yang tegas
    "{cps=35}*Tap... Tap... Tap...*{/cps}"

    stop music fadeout 1.5
    "{cps=35}Suara langkah kaki itu berhenti tepat di belakangku. Hawa dingin tiba-tiba menyelimuti tengkukku.{/cps}"

    if jujur and club_choice == "sastra":
        m "{cps=40}Menyedihkan sekali. Ditinggalkan oleh teman masa kecil hanya karena satu kertas keputusan?{/cps}"
    elif jujur and club_choice == "osis":
        m "{cps=40}Menyedihkan sekali. Ditinggalkan oleh teman masa kecil hanya karena dia ada urusan{/cps}"
    elif jujur and club_choice == None:
        m "{cps=40}Heee... {w=0.1}. kamu bilang babu sekolah ya...{/cps}"
    elif jujur == False:
        m "{cps=40}Menyedihkan sekali. Ditinggalkan oleh teman masa kecil hanya karena tidak mau cerita{/cps}"
    play music "audio/maya_theme.mp3" fadein 2.0 # Musik yang lebih formal/tegang
    
    show maya s05 with dissolve
    "{cps=35}Aku berbalik. Maya berdiri di sana, melipat tangan di dadanya dengan tatapan yang seolah bisa menembus pikiranku.{/cps}"

    mc "{cps=40}Maya-senpai... {w=0.1} Sudah sejak kapan kamu di sana?{/cps}"
    show maya s03 with dissolve
    m "{cps=40}Cukup lama untuk melihat drama pagi yang membosankan.{/cps}"
    show maya s02 with dissolve 
    m "{cps=40}Jadi, Ikazaki [mc]... {w=0.1} Mana jawabanmu? Kamu tahu aku tidak suka menunggu, terutama untuk sesuatu yang sudah aku beri waktu semalaman.{/cps}"

    "{cps=35}Aku meraba saku seragamku, mengeluarkan kertas yang sudah sedikit lecek itu.{/cps}"
    
    # Maya mengambil kertas tersebut
    "{cps=35}Tanpa menunggu aku menyerahkannya, dia mengambil kertas itu dari tanganku dengan gerakan cepat.{/cps}"

    m "{cps=40}Baiklah, mari kita lihat pilihanmu.{/cps}"
    if club_choice == "osis":
        "{cps=35}Maya menatap kertas itu sejenak, lalu melipatnya kembali dengan rapi.{/cps}"
        m "{cps=40}Hmph! Pilihan yang aman... {w=0.1} dan membosankan. Tapi setidaknya kamu tahu di mana tempatmu seharusnya berada.{/cps}"
        mc "{cps=40}Kan kakak yang menyuruh{/cps}"
        m "{cps=40}Sejak kapan aku yang menyuruhmu masuk ke OSIS?{/cps}"
        "{cps=35}Maya mengangkat sebelah alisnya, menatapku dengan tatapan tajam.{/cps}"
        "{cps=35}Hue- sial... {w=0.1} kenapa seperti ini...{/cps}"
        m "{cps=40}Ah, sudahlah. Tidak penting.{/cps}"
        m "{cps=40}Intinya... {w=0.1} datanglah ke ruanganku setelah bel pulang. Jangan sampai telat, atau aku akan menganggapmu mengundurkan diri.{/cps}"
        mc "{cps=40}Ba-baik kak{/cps}"
        "{cps=35}Aku mengangguk cepat, berusaha menahan rasa gugup yang tiba-tiba menyerang dadaku.{/cps}"
        "{cps=35}[m] menatapku dengan tatapan dingin beberapa saat sebelum akhirnya berbalik dan berjalan pergi.{/cps}"

    elif club_choice == "sastra":
        "{cps=35}Maya menaikkan sebelah alisnya. Ada kilat ketidaksetujuan di matanya.{/cps}"
        m "{cps=40}Klub Sastra? Kamu yakin?{/cps}"
        m "{cps=40}Padahal kegiatannya tidak terlalu banyak.{/cps}"
        mc "{cps=40}Oleh karena itu aku masuk ke sana{/cps}"
        mc "{cps=40}Daripada aku tidak memilih satu pun kan?{/cps}"
        m "{cps=40}Cih....{/cps}"
        m "{cps=40}Terserahlah. Aku akan memprosesnya, tapi jangan harap aku akan melepaskan pengawasanku darimu.{/cps}"
        m "{cps=40}Aku akan sering-sering mengunjungi klub sastra itu untuk memastikan kamu tidak melakukan hal bodoh.{/cps}"
        mc "{cps=40}Baik kak{/cps}"
        m "{cps=40}Baiklah, mungkin itu dulu untuk saat ini{/cps}"
        m "{cps=40}Kamu sebaiknya ke kelas dan nanti sore kamu harus ke ruangan klub{/cps}"
        mc "{cps=40}Ya kak{/cps}"
        "{cps=35}[m] pergi meninggalkanku setelah mengatakan itu{/cps}"

    elif club_choice == None:
        "{cps=35}Maya terdiam cukup lama setelah membaca kertas yang kukosongkan itu (atau bertuliskan penolakan).{/cps}"
        "{cps=35}Hening. Angin pagi bertiup kencang di antara kami.{/cps}"
        m "{cps=40}...{/cps}"
        m "{cps=40}Kamu benar-benar memilih untuk berdiri sendirian, ya?{/cps}"
        "{cps=35}Tiba-tiba, sudut bibir Maya terangkat sedikit. Bukan senyum sinis, tapi sesuatu yang menyerupai apresiasi.{/cps}"
        m "{cps=40}Menarik... tapi jangan harap hidupmu akan tenang nanti{/cps}"
        "{cps=35}Maya menatapku dengan tatapan serius.{/cps}"
        mc "{cps=35}Maksudnya kak?{/cps}"
        m "{cps=40}Tunggu saja{/cps}"
        "{cps=35}Maya berbalik dan berjalan pergi tanpa menunggu jawabanku.{/cps}"
        "{cps=35}Membuatku penasaran...{/cps}"

    # --- AKHIR PERTEMUAN ---
    mc "{cps=40}Hah... benar-benar wanita yang mengerikan.{/cps}"
    
    "{cps=35}Bel masuk berbunyi. Aku pun bergegas menuju kelas, menyadari bahwa hari-hari tenangku di sekolah ini benar-benar telah berakhir.{/cps}"

    scene black with fade
    stop music fadeout 2.0

    if masuk_club and club_choice == "osis":
        jump chapter_2_osis_kesempatan
    elif masuk_club and club_choice == "sastra":
        jump chapter_2_sastra_kesempatan
    else:
        jump chapter_2_solo


label chapter_2_osis_kesempatan:
    scene bg_classroom with fade
    play music "audio/school_life.mp3" fadein 2.0

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
    
    play sound "audio/school_bell.mp3"
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

    
    play sound "audio/steps_light.mp3"
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

    play sound "audio/door_open_bang.mp3"
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
    play music "audio/maya_theme.mp3" fadein 2.0

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
    play music "audio/afternoon_ambient.mp3" fadein 2.0

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

    play sound "audio/school_bell_long.mp3"
    "{cps=40}Ting... Tong...{/cps}"
    "{cps=40}Bel pulang akhirnya berbunyi. Murid-murid lain mulai berhamburan keluar dengan riang, tapi aku...{/cps}"

    "{cps=35}Aku menyentuh armband biru OSIS di bahuku. Armband itu seolah mengingatkanku bahwa 'waktu bermainku' sudah berakhir.{/cps}"
    "{cps=35}Aku harus segera menuju ruang rapat, meninggalkan kesunyian kelas ini menuju 'medan perang' yang sebenarnya.{/cps}"

    jump chapter_2_osis_kfm

label chapter_2_osis_kfm:
    # Mengatur suasana sore hari yang dramatis
    scene bg_council_room_sunset with fade
    play music "audio/office_ambience.mp3" fadein 2.0

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
    
    play sound "audio/door_heavy_open.mp3"
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
    play sound "audio/phone_vibrate.mp3"
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
    play music "audio/tension_ambient.mp3" fadein 2.0

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

    play sound "audio/folder_thud.mp3"
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

    play sound "audio/table_bang.mp3"
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
    play music "audio/tension_ambient.mp3" fadein 2.0

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
    play sound "audio/door_close_echo.mp3"

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

    

    
label chapter_2_sastra_kesempatan:
    scene bg_classroom_morning with fade
    play music "audio/school_ambience.mp3" fadein 2.0

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
    
    play sound "audio/school_bell.mp3"
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
    play sound "audio/heavy_breathing.mp3" # SFX napas tersengal

    "{cps=35}Hah... hah...{/cps}"
    "{cps=35}Pikiran buruk mulai memenuhi kepalaku. Loteng selalu dikunci karena pagar pengamannya sudah tua dan berbahaya.{/cps}"
    "{cps=35}Kenapa dia memilih tempat sesunyi itu?{/cps}"

    play sound "audio/door_rattle.mp3" # Suara pintu digoyang
    "{cps=35}*Kriet...*{/cps}"
    
    "{cps=35}Pintunya... tidak terkunci?{/cps}"

    scene bg_rooftop_morning with fade
    play music "audio/sad_piano_emotional.mp3" fadein 2.0

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

    play sound "audio/school_bell_long.mp3"
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
    play music "audio/tension_ambient.mp3" fadein 2.0

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
    play sound "audio/box_crash.mp3"
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

    play sound "audio/door_knock.mp3"
    "{b}*Tok! Tok! Tok!*{/b}"

    mc "{cps=35}Permisi...{/cps}"

    play sound "audio/door_open.mp3"
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

label chapter_2_solo:
    scene bg_classroom with fade
    play music "audio/school_life.mp3" fadein 2.0

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
    v "{cps=60}Yo! [mc]. Wajahmu seperti orang yang baru saja lolos dari pengadilan akhirat, memangnya ada apa?{/cps}"

    mc "{cps=40}Kamu ini selalu muncul tiba-tiba ya, [v].{/cps}"

    v "{cps=60}Fufufu, nggak juga kok. Oh iya, kemarin [m]-senpai membawamu pergi ke mana?.{/cps}"
    v "{cps=60}Apakah dia membuangmu ke gudang belakang, atau kamu berhasil melakukan 'negosiasi' dengannya?{/cps}"
    
    # TAMBAHAN START
    "{cps=35}Vina menumpukan dagunya di atas tangannya yang terlipat di sandaran kursiku. Matanya yang tajam seolah sedang memindai setiap inci reaksiku.{/cps}"
    
    mc "{cps=40}Negosiasi? Apa maksudmu?{/cps}"
    
    v "{cps=60}Ayolah [mc], coba ceritakan. Dia pasti menyebutkan nama 'Ikazaki [mi]', kan?{/cps}"
    "{cps=35}Loh? Kok dia tahu terkait kakakku?{/cps}"
    v "{cps=35}Hm? Kenapa wajahmu berubah jadi sepucat kertas begitu?{/cps}"
    
    mc "{cps=40}Kamu... nguping?{/cps}"
    
    v "{cps=60}Ya... anggap saja aku punya 'telinga' di mana-mana... lagipula sekolah ini punya dinding yang cukup tipis untuk telinga yang terlatih{/cps}"
    "{cps=35}Jadi, apa pilihanmu?{/cps}"
    # TAMBAHAN END
    mc "{cps=40}Aku... {w=0.1}tidak masuk ke organisasi manapun.{/cps}"
    mc "{cps=40}Aku baru saja menyerahkan kertasnya pada [m]-senpai tadi di gerbang.{/cps}"
    if jujur == False:
        "[y] dan [v]" "{cps=35}HAH!?{/cps}"
        "{cps=35}Terdengar suara kursi yang terjatuh dari depanku{/cps}"
        "{cps=35}Kemudian [y] datang menghampiriku{/cps}"
    else:
        "{cps=35}Terdengar suara kursi di depanku{/cps}"
        "{cps=35}Kemudian [y] datang menghampiriku{/cps}"
        "{cps=35}Sepertinya pembicaraan intens akan dimulai...{/cps}"
    y "{cps=35}Kamu serius tidak gabung ke organisasi manapun?{/cps}"
    mc "{cps=35}Yap, aku sudah menetapkan pilihanku{/cps}"
    "{cps=35}Beneran nih?{/cps}"
    mc "{cps=35}Masa iya aku bohong{/cps}"
    if jujur == False:
        mc "{cps=35}Maaf ya aku telat memberitahumu, [y]...{/cps}"
        "{cps=35}Karena aku tahu, jika aku memberitahumu dari awal, pasti kamu tidak terima{/cps}"
    else:
        mc "{cps=35}Kalian tidak keberatan kan?{/cps}"
    v "{cps=35}Gimana ya... dibilang keberatan sih nggak{/cps}"
    v "{cps=35}Namun... kalau kamu gabung ke osis pasti suasananya semakin asik!{/cps}"
    v "{cps=35}Kamu setuju kan [y]?{/cps}"
    y "{cps=35}Benar tuh! Kenapa kamu nggak gabung ke osis aja sih [mc]?{/cps}"
    v "{cps=35}Padahal kakakmu juga dari osis juga kan?{/cps}"
    "{cps=35}*BRAK{/cps}"
    mc "{cps=35}Kamu jangan pernah membawa kakakku ke dalam topik pembicaraan ini{/cps}"
    v "{cps=35}Hue- apa sih?{/cps}"
    "{cps=35}Aku... mau ke kamar mandi dahulu{/cps}"
    "{cps=35}Aku berdiri, meninggalkan mereka berdua di kelas itu{/cps}"
    v "{cps=35}Apaan sih dia itu?{/cps}"
    v "{cps=35}Padahal kan aku hanya ingin mengajaknya gabung{/cps}"
    y "{cps=35}Nggak gitu caranya [v]!{/cps}"
    v "{cps=35}Lantas?{/cps}"
    y "{cps=35}Kalau kita mengungkit kakaknya, dia pasti gitu{/cps}"
    y "{cps=35}Dari SMP pun begitu...{/cps}"
    "{cps=35}Suasana lorong yang dingin sedikit mendinginkan kepalaku. Aku bersandar di dinding, menatap ujung sepatuku yang sudah mulai kusam.{/cps}"
    "{cps=40}Sial... Kenapa aku harus semarah itu? Vina hanya... dia hanya tidak tahu apa-apa.{/cps}"
    "{cps=35}Aku berhenti di depan jendela besar yang menghadap ke halaman depan. Aku mengepalkan tangan, mencoba menahan emosi yang meluap.{/cps}"
    "???" "{cps=35}Kamu ngapain berdiri di situ?{/cps}"
    mc "{cps=35}Hah?{/cps}"
    "{cps=35}Aku tersentak. Di ujung koridor, bersandar di tembok, seorang gadis yang sangat familiar...{/cps}"
    mc "{cps=40}Kamu... siapa?{/cps}"
    "???" "{cps=35}HAH? Kamu serius nggak kenal aku?{/cps}"
    mc "{cps=35}Sebentar... coba aku ingat-ingat...{/cps}"
    "{cps=35}Siapa ya namanya?{/cps}"
    menu:
        "Kisaragi [f]":
            $ tebak = True
            $ fumi_rel += 5
            mc "{cps=40}Kak [f]?{/cps}"
            f "{cps=35}Benar sekali!{/cps}"
            f "{cps=35}Ternyata kamu punya ingatan yang bagus ya?{/cps}"
            mc "{cps=35}Nggak juga..{/cps}"
            f "{cps=35}Ah! gini saja{/cps}"
            f "{cps=35}Akan aku lakukan perkenalan ulang{/cps}"

        "Pembawa acara saat penyambutan?":
            $ tebak = False
            mc "{cps=40}Kakak pembawa acara saat penerimaan?{/cps}"
            "???" "{cps=40}Ya... nggak salah sih...{/cps}"
            "???" "{cps=40}Tapi masa kamu tidak tahu namaku{/cps}"
            "???" "{cps=40}Padahal aku perkenalan loh waktu itu{/cps}"
            mc "{cps=40}Maaf kak aku tidak terlalu ingat...{/cps}"
            "???" "{cps=40}Cih! yaudah, aku ulangi lagi{/cps}"

    f "{cps=35}Namaku adalah Kisaragi [f], pembawa acara penerimaan kemarin dan juga ketua klub sastra{/cps}"
    f "{cps=35}Namamu ikazaki [mc] kan?{/cps}"
    "{cps=35}Kenapa dia tahu namaku?{/cps}"
    mc "{cps=35}I-iya kak, kenapa?{/cps}"
    f "{cps=35}Kamu kenapa keluyuran di lorong? Padahal sekarang kan sudah mau jam pertama...{/cps}"
    mc "{cps=35}Entahlah kak.. aku merasa telah melakukan banyak hal buruk...{/cps}"
    f "{cps=35}Heee... memangnya apa saja?{/cps}"
    mc "{cps=35}Memangnya aku perlu menceritakan semua?{/cps}"
    f "{cps=35}Ceritain garis besarnya nggak apa-apa sih, lagipula kan sepertinya kamu perlu teman curhat{/cps}"
    mc "{cps=40}Hah... aku lelah, Kak. Semua orang menatapku seolah aku adalah replika dari kakakku yang sudah tiada.{/cps}"

    mc "{cps=40}Mereka ingin aku masuk OSIS, mereka ingin aku menjadi 'hebat' seperti dia. Tapi saat aku menolak, aku justru dianggap sebagai pengecut yang melarikan diri.{/cps}"

    f "{cps=35}Berdiri di bawah bayangan pohon yang besar memang sejuk, tapi kamu tidak akan pernah mendapatkan sinar matahari untuk dirimu sendiri, kan?{/cps}"

    "{cps=35}Aku terdiam. Kalimat itu... rasanya terlalu tepat sasaran.{/cps}"

    "{cps=35}Fumi menatapku dengan tatapan yang sangat tenang. Tidak ada rasa kasihan di matanya, hanya sebuah pemahaman yang mendalam.{/cps}"
    f "{cps=35}Aku mengerti perasaanmu, [mc]...{/cps}"
    "{cps=35}Kakak memangnya tahu apa?{/cps}"
    "{cps=35}Di nama keluargaku ada nama Kisaragi kan?, dan di sekolah ini, nama itu punya 'beban' tersendiri karena kakakku.{/cps}"
    mc "{cps=40}Iya kak, memangnya kenapa?{/cps}"
    f "{cps=40}Kamu tahu idol yang terkenal, Kisaragi [sa]?{/cps}"

    mc "{cps=40}Aku tahu kak, kalau tidak salah dia itu berada di satu era dengan Ogata [ri] dan Morikawa [yu] kan?{/cps}"
    f "{cps=35}Benar sekali{/cps}"
    mc "{cps=35}Lantas?{/cps}"
    f "{cps=35}Aku adalah adiknya{/cps}"
    mc "{cps=35}Hah? {w=0.1} Yang bemar kak?{/cps}"
    f "{cps=35}Kalau kamu berpikir aku hanya membual tidak masalah, nanti kamu ketika istirahat coba ke ruang klub sastra{/cps}"
    f "{cps=35}Akan aku ceritakan semua{/cps}"
    mc "{cps=35}Ummm....{/cps}"
    f "{cps=35}Sampai nanti{/cps}"
    mc "{cps=35}Tunggu ka-{/cps}"
    "{cps=35}[f] pergi tanpa meninggalkan jejak{/cps}"
    mc "{cps=35}Kak...{/cps}"

    "{cps=35}*TENG TENG TENG{/cps}"
    "{cps=35}Bunyi bell jam pertama sudah berbunyi{/cps}"
    mc "{cps=35}Sial.. kenapa jadi menggantung gini...{/cps}"
    "{cps=35}Aku harus bertemu dengannya nanti{/cps}"

    scene bg_classroom with fade
    play music "audio/tension_ambient.mp3" fadein 2.0

    "{cps=35}Langkah kakiku terasa berat saat memasuki kelas. Suara gesekan kursi dan gumaman murid-murid lain seolah menjadi hakim atas kepergianku yang tiba-tiba tadi.{/cps}"

    "{cps=35}Aku duduk di kursiku tanpa berani melirik ke arah Yuuka. Aku bisa merasakan tatapannya yang tajam dari samping, tapi aku memilih untuk menatap lurus ke papan tulis yang masih kosong.{/cps}"

    v "{cps=60}(Berbisik pelan dari belakang) Wah, si Specimen sudah kembali. Wajahmu terlihat lebih... 'penuh rahasia' daripada sepuluh menit yang lalu.{/cps}"

    mc "{cps=40}(Berbisik) Diamlah, Vin.{/cps}"

    "{cps=35}Suasana kelas yang biasanya bising kini terasa mencekam. Meskipun murid-murid lain mulai kembali berbisik, ada dinding tak kasat mata yang terbangun di sekeliling mejaku, meja Yuuka, dan meja Vina.{/cps}"

    "{cps=35}Aku hanya bisa menatap nanar ke arah papan tulis yang masih bersih. Di kepalaku, kalimat Fumi terus berputar: 'Adik dari Kisaragi Sayoko'. Bagaimana mungkin seorang idol itu punya hubungan darah dengan seniorku?{/cps}"

    play sound "audio/door_slide_hard.mp3"
    "{cps=35}*SRAAAK!*{/cps}"

    "{cps=35}[t] melangkah masuk dengan aura yang sanggup membekukan seisi ruangan. Beliau tidak membawa tas, hanya setumpuk buku tebal dan sebatang kapur yang digenggam kuat.{/cps}"
    t "{cps=40}Selamat pagi anak-anak, sekarang letakkan smartphone kalian, kita akan segera memulai pelajaran{/cps}"

    t "{cps=35}Sekarang kita akan mempelajari mata pelajaran yang cukup sulit, jadi saya harap kalian bisa fokus mengikuti pelajarannya{/cps}"
    "murid" "{cps=35}Baik bu{/cps}"
    "{cps=35}Beliau melirik ke arahku sejenak. Tatapannya tajam, seolah beliau tahu aku baru saja membuat keributan di lorong.{/cps}"
    t "{cps=35}Terutama kamu, [mc]{/cps}"
    mc "{cps=35}Lah kok saya bu?{/cps}"
    t "{cps=40}Karena wajahmu terlihat lagi banyak pikiran, [mc]. Apa pikiranmu sedang tertinggal di suatu tempat di luar sana?{/cps}"
    mc "{cps=35}Eh? N-nggak kok, Bu...{/cps}"
    t "{cps=35}Kalau begitu usahakan kamu untuk tetap fokus mengikuti pelajaran hari ini{/cps}"
    mc "{cps=35}Baik bu!{/cps}"
    "{cps=35}Kelas pun dilanjutkan dengan suasana yang sedikit canggung{/cps}"
    "{cps=35}Walau aku masih bisa mengikuti materinya sih{/cps}"
    "{cps=35}Namun entah kenapa... {w=0.1} Kalimat yang diucapkan oleh kak [f] masih nyangkut di pikiranku{/cps}"
    mc "{cps=35}'Nanti kamu ketika istirahat coba ke ruang klub sastra, akan aku ceritakan semua' ya...{/cps}"
    "{cps=35}Aku bergumam memikirkan itu{/cps}"
    "{cps=35}Memangnya apa sih yang akan dia ceritakan{/cps}"
    "{cps=35}Palingan juga cerita terkait keluarganya yang lengkap itu{/cps}"
    "{cps=35}Ditambah dia adalah pembawa acara kemarin... sudah pasti dia itu terlatih{/cps}"
    "{cps=35}Dibandingkan diriku yang saat ini saja melakukan apa-apa sendiri dan tidak memiliki koneksi yang cukup..{/cps}"
    "{cps=35}Itu bukan jalan yang cocok{/cps}"
    "{cps=35}Kalimat yang diucapkan [mom] kembali mengganggu pikiranku{/cps}"
    "{cps=35}'Kamu harus jadi orang sukses!'{/cps}"
    "{cps=35}Dikira gampang apa mah...{w=0.1} minimal perhatikan dahulu kualitas anakmu ini...{/cps}"
    "{cps=35}Memang sih dimana-mana itu banyak orang tua yang mengharapkan anaknya itu lebih sukses dibanding dirinya{/cps}"
    "{cps=35}Namun ada juga yang tidak bisa memenuhi ekspetasinya{/cps}"
    "{cps=35}Dan aku tidak mau menjadi orang gagal...{/cps}"
    mc "{cps=35}Hah...{/cps}"
    "{cps=35}Disaat aku sedang melamun memikirkan hal itu{/cps}"
    "{cps=40}BRAK!{/cps}"
    mc"{cps=40}Hue! Apa yan-{/cps}"
    "{cps=40}[t] melempar buku ke mejaku dengan cukup keras{/cps}"
    t "{cps=40}Hah.... gini ya [mc]{/cps}"
    t "{cps=40}Meskipun kamu sedang banyak pikiran...{/cps}"
    t "{cps=40}{b}MINIMAL MEMPERHATIKAN!{/b}{/cps}"
    mc "{cps=50}Baik bu...{/cps}"
    "{cps=50}Sial... {w=0.1}kenapa jadi begini...{/cps}"
    v "{cps=35}Pfffftttt{/cps}"
    "{cps=50}Terdengar suara [v] yang tertawa kecil di belakangku. Dia pasti menikmati pemandangan ini.{/cps}"

    t "{cps=40}Karena kamu sepertinya punya dunia sendiri di dalam kepala itu, coba selesaikan soal yang ada di papan.{/cps}"
    
    # Soal yang lebih manusiawi
    t "{cps=40}Jika 3x + 5 = 20, berapakah nilai dari x?{/cps}"

    "{cps=35}Aduh... kepalaku mendadak kosong. Angka-angka itu seolah menari-nari di depan mataku.{/cps}"
    if jujur:
        "{cps=35}Yuuka di depanku terlihat panik, dia mengangkat lima jarinya di bawah meja sebagai isyarat.{/cps}"
    else:
        "{cps=35}Yuuka di depanku terlihat biasa saja, dia bahkan tidak memberi isyarat apapun.{/cps}"
    "{cps=35}Aku juga melihat ke arah si kembar...{/cps}"
    "{cps=35}Mereka tidak memberi respon{/cps}"
    mc "{cps=35}Cih{/cps}"
    "{cps=40}Aku harus menjawab apa...{/cps}"
    menu:
        "5":
            $ correct_answer = True
            mc "{cps=40}Jawabannya... 5, Bu.{/cps}"
            
            "{cps=35}Ibu [t] terdiam sejenak, lalu menurunkan kacamatanya.{/cps}"
            
            t "{cps=40}Tepat. Sederhana, bukan?{/cps}"
            t "{cps=40}Ingat, dalam Aljabar, tujuan kita adalah mencari 'Nilai yang Hilang' (x) dengan cara menyeimbangkan kedua sisi.{/cps}"
            
            "{cps=35}Ibu [t] menuliskan coretan di papan dengan cepat.{/cps}"
            t "{cps=40}Jika kamu punya masalah besar (20) dan ada gangguan kecil (+5), hilangkan gangguannya dulu (20-5). Baru kemudian bagi beban sisa (15) dengan kapasitasmu (3).{/cps}"
            
            "{cps=35}Entah kenapa, penjelasan Bu [t] barusan tidak hanya terdengar seperti matematika, tapi seperti cara menghadapi hidup yang sedang berantakan ini.{/cps}"
            t "{cps=35}Sudah paham?{/cps}"
            mc "{cps=35}Sudah bu{/cps}"
            t "{cps=40}Lain kali, perhatikan penjelasan saya. Duduk dan fokus!{/cps}"
            t "{cps=35}Sekarang kembali ke tempat dudukmu{/cps}"
            mc "{cps=35}Ba-baik bu{/cps}"
            
            show yuuka_smile with dissolve
            if jujur:
                "{cps=35}Yuuka menghela napas lega dan tersenyum kecil ke arahku. Di belakang, Vina tampak sedikit kecewa karena tidak bisa menertawakanku.{/cps}"
            v "{cps=60}Cih... ternyata si Specimen Langka ini bisa berhitung juga.{/cps}"

        "15":
            $ correct_answer = False
            mc "{cps=40}Jawabannya... 15, Bu?{/cps}"
            
            "{cps=35}Seketika seisi kelas tertawa. Bahkan Vina di belakangku sampai harus menutup mulutnya agar tidak terdengar terlalu keras.{/cps}"
            t "{cps=40}Lima belas? Kamu ini sedang menghitung nilai x atau harga gorengan di kantin? Salah!{/cps}"
            t "{cps=40}Berdiri di depan sampai jam pelajaran saya selesai!{/cps}"
            
            show yuuka_sad with dissolve
            "{cps=35}Yuuka menepuk jidatnya. Dia sudah memberiku kode, tapi aku malah salah tangkap.{/cps}"

        "3":
            $ correct_answer = False
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
    "{cps=35}Sisa pelajaran terasa seperti siksaan yang lambat. Suara kapur yang beradu dengan papan tulis terdengar seperti detak jam yang menghitung mundur keberanianku.{/cps}"
    "{cps=35}Aku melirik ke arah [y]. Punggungnya tegak, fokusnya seolah tak tergoyahkan.{/cps}"
    "{cps=35}Namun sepertinya dia masih sedikit kesal dengan pilihanku tadi.{/cps}"
    "{cps=35}Ya... mau gimana lagi. Pilihanku sudah bulat{/cps}"
    play sound "audio/school_bell_long.mp3"
    "{cps=40}*Ting... Tong... Ting... Tong...*{/cps}"

    t "{cps=40}Cukup untuk jam ini. Pekerjaan rumah kalian adalah mengerjakan latihan halaman 45 sebagai pendalaman.{/cps}"
    t "{cps=40}[mc], pastikan kamu mencuci wajahmu, kamu terlihat sangat pucat.{/cps}"
    t "{cps=40}Kita ketemu lagi nanti setelah istirahat dengan mata pelajaran Sejarah, jadi siapkan buku kalian nanti{/cps}"

    "{cps=35}Begitu Bu [t] melangkah keluar, suasana kelas yang tadinya sunyi mendadak pecah. Suara tawa dan obrolan mulai memenuhi ruangan, tapi bagiku, suara itu terasa seperti derau statis yang jauh.{/cps}"

    # --- REAKSI YUUKA & VINA (AS BESTIES) ---
    show yuuka_neutral at left
    show vina_smile at right
    with dissolve

    "{cps=35}[y] langsung berdiri. Dia merapikan bukunya dengan gerakan cepat, seolah ingin segera menghilang dari sini. Vina, yang duduk di belakangku, langsung berpindah ke samping Yuuka, merangkul bahunya dengan akrab.{/cps}"

    if correct_answer:
        v "{cps=60}Wah, lihat Yuuka... ternyata si Specimen kita ini otaknya masih sinkron dengan dunia nyata. Aku kira dia sudah lupa cara menghitung x.{/cps}"
        
        y "{cps=40}(Menghela napas) Baguslah kalau begitu. Aku tidak perlu repot-repot mencarikan guru les untuk orang yang keras kepala.{/cps}"
        
        "{cps=35}Yuuka melirikku sejenak. Ada sedikit rasa lega di matanya, tapi dia segera membuang muka saat menyadari aku balik menatapnya.{/cps}"
    else:
        v "{cps=60}Duh, Yuuka... sepertinya kita harus memberi pahlawan kita ini kalkulator sebagai hadiah ulang tahun ke 17? Benar-benar jawaban yang 'berani'.{/cps}"
        
        y "{cps=40}Sudah kuberi kode, tapi dia malah melamun...{/cps}"
        
        "{cps=35}Yuuka menatapku dengan tatapan yang sulit diartikan—campuran antara kesal dan rasa kasihan yang mendalam. Vina hanya menyeringai puas.{/cps}"

    # --- PERSIAPAN PERGI KE KANTIN ---
    v "{cps=60}Sudahlah, Yuu. Ayo ke kantin, aku lapar sekali. Nanti jajanan favoritmu habis kalau kita terus berdiri di sini.{/cps}"
    y "{cps=35}Ah iya juga{/cps}"
    v "{cps=35}[mc], kamu mau ke kantin juga?{/cps}"
    mc "{cps=35}Sepertinya nggak dulu deh, ada kegiatan lain juga{/cps}"
    v "{cps=35}Kegiatan? Padahal kamu ga ada organisasi?{/cps}"
    mc "{cps=35}Dikira aku nggak bisa punya kegiatan apa?{/cps}"
    v "{cps=35}Ehehe, yaudah. sampai jumpa [mc]{/cps}"
    mc "{cps=35}Sampai jumpa...{/cps}"
    "{cps=35}[v] dan [y] pun ke kantin meninggalkanku{/cps}"
    mc "{cps=35}Baiklah... sudah waktunya{/cps}"
    "{cps=35}Aku pun berjalan menuju ke ruangan yang dijanjikan oleh kak [f]{/cps}"
    "{cps=35}Ditengah lorong yang aku lewati{/cps}"
    "{cps=35}Aku mencoba mengingat nama ruangan yang tadi dibahas{/cps}"
    f "{cps=35}nanti kamu ketika istirahat coba ke ruang klub sastra{/cps}"
    mc "{cps=35}Ruang klub sastra ya...{/cps}"
    mc "{cps=35}Dimana?{/cps}"
    "{cps=35}Aku tidak tahu ruangan itu berada dimana...{/cps}"
    mc "{cps=35}Hmmmm....{/cps}"
    "???" "{cps=35}Hei [mc]{/cps}"
    mc "{cps=35}Hah?{/cps}"
    "{cps=35}Aku menengok ke belakang{/cps}"
    yk "{cps=35}Kamu terlihat bingung sekali, ada apa?{/cps}"
    mc "{cps=35}Ummnn....{/cps}"
    mc "{cps=35}Gini [yk]... kamu tahu nggak ruangan klub sastra?{/cps}"
    yk "{cps=35}Tentu saja aku tahu! Aku kan anggota klub itu{/cps}"
    yk "{cps=35}Memangnya kenapa?{/cps}"
    mc "{cps=35}Aku mau kesana{/cps}"
    yk "{cps=35}Heeee.... mau ketemu Onee-san ya?{/cps}"
    mc "{cps=35}Maksudmu?{/cps}"
    yk "{cps=35}Eh? Bukan?? Lalu kamu ngapain ke sana?{/cps}"
    mc "{cps=35}Aku mau ketemu dengan kak [f]{/cps}"
    yk "{cps=35}Hmmm.... kayaknya kak [f] ada di ruang klub..{/cps}"
    yk "{cps=35}Tapi masa kamu nggak mau ketemu dengan Onee-san?{/cps}"
    mc "{cps=35}Kakakmu itu [sh] kan?{/cps}"
    yk "{cps=35}Tentu saja, masa kamu nggak tahu sih, padahal pas perkenalan aku sudah menunjukkan itu dari awal{/cps}"
    mc "{cps=35}Ya... kalau diingat memang sih{/cps}"
    yk "{cps=35}Padahal Onee-san itu benar-benar menunggumu loh, [mc]{/cps}"
    mc "{cps=35}Ngapain dia nungguin aku?{/cps}"
    yk "{cps=35}Ya... kan dia masih ingat dengan janji denganmu{/cps}"
    mc "{cps=35}Membahas itu lagi? Dibilang dia itu mungkin salah orang{/cps}"
    mc "{cps=35}Karena jujur saja aku tidak ingat dengan kejadian itu sama sekali{/cps}"
    yk "{cps=35}Hue- parah banget{/cps}"
    mc "{cps=35}Jadi? Kamu mau menunjukan jalannya?{/cps}"
    yk "{cps=35}Tentu saja! Sini, ikut aku{/cps}"
    "{cps=35}Aku pun mengikuti [yk] menuju ke ruang klub sastra{/cps}"

    scene bg_club_corridor with fade
    play music "audio/mystery_soft.mp3" fadein 2.0

    "{cps=35}Aku berjalan di belakang [yk]. Berbeda dengan [y] yang langkahnya selalu terburu-buru, [yk] melangkah dengan sangat ringan, seolah dia sedang menari di atas lantai koridor ini.{/cps}"

    yk "{cps=35}Nah, kita sampai!{/cps}"

    "{cps=35}[yk] berhenti di depan sebuah pintu hijau dengan papan nama kecil bertuliskan 'Klub Sastra'. Pintu ini terlihat sedikit kusam, namun memberikan kesan tenang yang kontras dengan hiruk-pikuk sekolah.{/cps}"
    yk "{cps=35}Selamat siang! Teman-teman, lihat siapa yang aku bawa!{/cps}"
    sh "{cps=35}Kamu selalu berisik ya, [yk]{/cps}"
    f "{cps=35}Memangnya siapa yang kamu bawa?{/cps}"
    "{cps=35}Sini [mc], ayo masuk{/cps}"
    mc "{cps=35}Permisi...{/cps}"
    "{cps=35}Begitu masuk, bau buku tua dan teh melati menyapa hidungku. Ruangan ini penuh dengan rak buku yang menjulang tinggi hingga ke langit-langit.{/cps}"
    f "{cps=35}Oho! Tamu kehormatan kita akhirnya datang juga, kerja bagus, [yk]{/cps}"
    sh "{cps=35}...{/cps}"
    sh "{cps=35}Ternyata orang yang kakak bilang tadi itu dia ya...{/cps}"
    f "{cps=35}Ya... begitulah{/cps}"
    f "{cps=35}Karena aku lihat tadi dia terlihat kesulitan, jadi sebagai senior yang baik ya aku coba bantu dia{/cps}"
    f "{cps=35}Kamu juga ada urusan denganya kan [sh]{/cps}"
    sh "{cps=35}Nggak begitu...{/cps}"
    "{cps=35}Shoko sedang duduk di sudut ruangan, memegang sebuah buku tebal. Dia menatapku sejenak—tatapannya masih sama, dalam dan sulit diartikan—sebelum kembali menunduk ke bukunya.{/cps}"
    f "{cps=35}Jadi, kamu kesini mau mendengar ceritanya kan?{/cps}"
    mc "{cps=35}I-iya kak!{/cps}"
    f "{cps=35}Sayang sekali!{/cps}"
    mc "{cps=35}Eh?{/cps}"
    f "{cps=35}Kamu aslinya aku ajak kesini biar kamu jadi anggota klub sastra!{/cps}"
    mc "{cps=35}HAH?{/cps}"
    mc "{cps=35}Tapi kan aku tidak mau gabung ke klub manapun kak{/cps}"
    f "{cps=35}*ckckck Nggak seperti itu konsepnya [mc]{/cps}"
    f "{cps=35}[yk], jelaskan{/cps}"
    yk "{cps=35}Ahem! Jadi begini [mc]. Klub Sastra itu bukan cuma soal baca buku atau bikin puisi yang bikin ngantuk.{/cps}"

    yk "{cps=35}Di sekolah ini, setiap murid harus terdaftar di satu 'wadah' kalau tidak mau dianggap sebagai 'titik buta' oleh sistem OSIS. Kamu tahu kan, Kak Maya itu perfeksionis?{/cps}"

    f "{cps=35}Benar. Dan rasionya sederhana: Kalau kamu tetap 'Solo', Maya akan terus mengincarmu untuk masuk OSIS sampai kamu menyerah.{/cps}"

    f "{cps=35}Tapi, kalau kamu terdaftar di sini... setidaknya kamu punya 'alibi' hukum untuk menolak dia. Kita ini semacam... zona netral.{/cps}"
    mc "{cps=40}Zona netral? Tapi tetap saja itu namanya gabung organisasi, Kak.{/cps}"

    f "{cps=35}Fufufu. Anggap saja ini 'keanggotaan pasif'. Kamu tidak perlu ikut rapat, tidak perlu ikut proker. Cukup taruh namamu di sini, dan sebagai gantinya...{/cps}"

    "{cps=35}Fumi mencondongkan tubuhnya ke depan. Tatapannya berubah menjadi sangat serius, membuatku refleks menahan napas.{/cps}"

    f "{cps=35}Aku akan menceritakan apa yang sebenarnya terjadi dari hubunganku dengan Kisaragi [sa] dan juga kasus Ikazaki [mi]. Sesuatu yang bahkan tidak tercatat di arsip resmi sekolah ini meski kamu mencarinya dimana pun.{/cps}"

    "{cps=35}Aku terdiam. Tawaran ini terlalu berisiko, tapi rasa ingin tahuku tentang Kakak seolah-olah ditarik paksa keluar.{/cps}"

    sh "{cps=35}(Tanpa menoleh dari bukunya) Jangan dipaksa, Kak. Biarkan dia memilih 'kebebasan' yang dia banggakan itu.{/cps}"

    sh "{cps=35}Meskipun kebebasan itu hanya akan membawanya pada kebingungan yang lebih dalam.{/cps}"

    mc "{cps=40}Shirohana-san...{/cps}"
    f "{cps=35}Jadi gimana [mc]? Tawaranku tidak terlalu buruk kan?{/cps}"
    mc "{cps=35}Ummnnn nggak sih kak..{/cps}"
    f "{cps=35}Jadi kamu mau bergabung?{/cps}"
    mc "{cps=35}Tidak{/cps}"
    f "{cps=35}Hah?{/cps}"
    "{cps=35}[f] terdiam beberapa saat{/cps}"
    f "{cps=35}Kamu nggak salah ngomong kan [mc]?{/cps}"
    mc "{cps=35}Nggak kok, aku memang tetap tidak mau gabung ke organisasi manapun{/cps}"
    f "{cps=35}Sumpah?{/cps}"
    f "{cps=35}Padahal aku sudah effort sejauh ini demi kamu... bahkan aku sampai mengundang [sh] ke sini...{/cps}"
    f "{cps=35}Walau dia memang anggota klub sih{/cps}"
    mc "{cps=35}Apa hubungannya?{/cps}"
    "{cps=35}[sh] Menutup bukunya dengan suara keras{/cps}"
    sh "{cps=35}Hah... sudah kubilang kan, Kak. Dia itu tipe orang yang kuat pendiriannya.{/cps}"
    "{cps=35}Shoko berdiri, menatapku dengan tatapan yang tajam, namun kali ini ada sedikit rasa... sedih?{/cps}"
    sh "{cps=35}Ikazaki-kun, aku tahu kamu itu tidak tertarik dengan organisasi manapun saat ini..{/cps}"
    sh "{cps=35}Namun, kamu harus ingat...{/cps}"
    sh "{cps=35}Jika kamu perlu apapun, kamu bisa datang ke klub ini, anggap saja ini adalah rumah kedua milikmu{/cps}"
    mc "{cps=35}Kenapa sih kalian sampai segitunya demi aku?{/cps}"
    yk "{cps=35}Kalau ditanya kenapa ya...{/cps}"
    yk "{cps=35}Kenapa ya, [sh] nee?{/cps}"
    sh "{cps=35}Seperti 10 tahun yang lalu{/cps}"
    mc "{cps=35}Apa sih... itu lagi yang dibahas..{/cps}"
    mc "{cps=35}Jujur saja ya [sh]... aku tidak terlalu ingat dengan kejadian itu, bahkan bertemu denganmu saja aku tidak ingat{/cps}"
    sh "{cps=35}Aku paham kok, namun...{/cps}"
    sh "{cps=35}Kalau kamu mau mengingat masa itu kembali, kamu bisa melihat album foto yang ada dirumahmu{/cps}"
    sh "{cps=35}Mungkin foto itu masih ada{/cps}"
    mc "{cps=35}Foto?{/cps}"
    sh "{cps=35}Sebelum aku pindah, kita sempat berfoto..{/cps}"
    sh "{cps=35}Dan seharusnya masih ada foto itu di album{/cps}"
    mc "{cps=35}Kenapa kamu seyakin itu?{/cps}"
    sh "{cps=35}Karena kita berdua yang memasangnya{/cps}"
    mc "{cps=35}Aku... tidak mengerti{/cps}"
    mc "{cps=35}Mungkin nanti ketika dirumah akan aku coba cari{/cps}"
    f "{cps=35}Heloo... aku masih ada di sini loh?{/cps}"
    mc "{cps=35}Ah aku sampai lupa kalau ada kak [f]{/cps}"
    f "{cps=35}Kamu beneran ga mau gabung ya [mc]? Akan aku beri 'servis' deh~{/cps}"
    "{cps=35}[f] terus menempel diriku agar aku mau bergabung{/cps}"
    "{cps=35}Namun maaf.. aku sudah kuat menghadapi ini{/cps}"
    mc "{cps=35}Maaf kak, sekali lagi aku bilang, aku tidak tertarik dengan organisasi, namun kalau memang aku diharuskan gabung..{/cps}"
    f "{cps=35}Kamu gabung dengan kita?{/cps}"
    mc "{cps=35}Aku akan berusaha membantu banyak organisasi tanpa harus terlibat secara langsung{/cps}"
    f "{cps=35}Dengan cara?{/cps}"
    m "{cps=35}Menjadi volunteer{/cps}"
    "{cps=35}Suara tak asing datang dari depan pintu, dengan langkah yang tegas{/cps}"
    "{cps=35}Siluet rambut hitam dengan aksen kuning yang berkilau, berdiri di depan pintu klub sastra{/cps}"
    f "{cps=35}Wah wah wah...{/cps}"
    f "{cps=35}Tak ku sangka kamu akan datang ke ruangan klub milikku{/cps}"
    f "{cps=35}[m]{/cps}"
    mc "{cps=35}Kak [m], ngapain kakak disini?{/cps}"
    m "{cps=35}Kebetulan aku sedang lewat dan mendengar pembicaraan kalian{/cps}"
    f "{cps=35}Kamu mendengarkan dari kapan?{/cps}"
    m "{cps=35}Semenjak [mc] masuk ke ruangan{/cps}"
    f "{cps=35}Bukannya itu sama aja dengan penguntit?{/cps}"
    m "{cps=35}Aku tidak menguntit kok, hanya saja aku penasaran dengan pilihan yang diambil oleh [mc]{/cps}"
    mc "{cps=35}Kenapa sih aku yang selalu jadi pusat perhatian oleh kalian?{/cps}"
    m "{cps=35}Karena seperti yang kamu tahu, [mc]{/cps}"
    m "{cps=35}Kamu adalah satu-satunya murid laki yang ada di sini{/cps}"
    m "{cps=35}Jadi kami selalu mengawasi gerak-gerikmu dan memastikan kalau kamu tidak akan melanggar norma yang berlaku di sekolah ini{/cps}"
    f "{cps=35}Mengawasi? Atau memang kamu nggak mau kehilangan penerusmu di OSIS, [m]?{/cps}"
    m "{cps=35}Pikirkan apa pun yang kamu mau, Kisaragi. Tapi yang jelas, Ikazaki [mc] sudah membuat pilihannya untuk tidak bergabung denganmu.{/cps}"
    "{cps=35}Maya melangkah masuk, aroma parfumnya yang tajam langsung mendominasi ruangan, mengalahkan bau teh melati milik klub sastra.{/cps}"
    m "{cps=35}Jadi, [mc]. Kamu bilang ingin menjadi 'Volunteer'?{/cps}"
    mc "{cps=35}Iya, Kak. Dengan begitu aku bisa membantu siapa pun tanpa harus menyakiti salah satu pihak{/cps}"
    "{cps=35}Menyakiti? memangnya siapa yang disakiti, [mc]?{/cps}"
    "{cps=35}Aku tidak begitu mengerti, tapi aku tetap ingin menjadi volunteer{/cps}"
    m "{cps=35}Menarik. Tapi volunteer pun butuh pengawasan. Bagaimana kalau kita buat kesepakatan?{/cps}"
    mc "{cps=35}Kesepakatan apa lagi?{/cps}"
    m "{cps=35}Kamu bebas tidak masuk klub mana pun. Tapi, setiap program kerja dari klub manapun atau osis, kamu harus ikut serta{/cps}"
    mc "{cps=35}Bukannya itu terlalu banyak?{/cps}"
    m "{cps=35}Kamu keberatan?{/cps}"
    mc "{cps=35}Sudah jelas kak!{/cps}"
    m "{cps=35}Kalau begitu, kamu bisa memilih{/cps}"
    f "{cps=35}Cih lembek banget kamu [m]{/cps}"
    m "{cps=35}Diam lah [f], jadi pilihanmu?{/cps}"
    mc "{cps=35}Aku memilih 2 saja, OSIS dan Sastra{/cps}"
    mc "{cps=35}Apakah itu tidak masalah?{/cps}"
    m "{cps=35}Tidak terlalu buruk, karena klub lain juga tidak sesibuk ini{/cps}"
    m "{cps=35}Aku terima, dan sebagai bayarannya...{/cps}"
    m "{cps=35}Aku akan memberimu akses ke arsip data kesiswaan jika kamu butuh mencari 'sesuatu'.{/cps}"
    "{cps=35}Aku tersentak. Akses arsip? Itu berarti aku bisa mencari data tentang Kakakku secara legal.{/cps}"
    sh "{cps=35}Jangan terlalu percaya padanya, [mc].{/cps}"
    sh "{cps=35}Sepertinya dia memiliki rencana lain...{/cps}"
    m "{cps=35}Aku tidak ada rencana lain kok{/cps}"
    m "{cps=35}Jadi jawabanmu?{/cps}"
    mc "{cps=35}Ummnn.... Kalau aku jadi volunteer apakah akan sendirian saja?{/cps}"
    m "{cps=35}Tentu saja tidak, akan aku berikan salah satu anggotaku untuk membantu?{/cps}"
    m "{cps=35}Namun kamu tidak perlu tahu siapa orangnya{/cps}"
    mc "{cps=35}Kalau begitu... aku setuju. Aku akan menjadi volunteer untuk OSIS dan Klub Sastra.{/cps}"
    m "{cps=35}Keputusan yang bijak, [mc].{/cps}"
    "{cps=35}Maya menyeringai tipis. Kemenangan kecil terpancar dari tatapannya. Dia mengeluarkan sebuah buku saku kecil bersampul perak dari sakunya dan meletakkannya di atas meja.{/cps}"
    m "{cps=35}Ini adalah buku catatan kegiatanmu. Setiap bantuan yang kamu berikan harus ditandatangani oleh penanggung jawab kegiatan.{/cps}"
    f "{cps=35}Dan jangan lupa, [mc]. 'Servis' dariku tetap berlaku kalau kamu bosan dengan aturan kaku Maya. Fufufu.{/cps}"
    sh "{cps=35}...{/cps}"
    "{cps=35}[sh] menatap buku itu dengan tatapan dingin, lalu beralih menatapku. Seolah dia ingin mengatakan sesuatu, tapi tertahan oleh kehadiran [m]{/cps}"
    play sound "audio/school_bell.mp3"
    "{cps=40}*Ting... Tong... Ting... Tong...*{/cps}"

    m "{cps=35}Waktu istirahat sudah habis. Kembalilah ke kelas. Ingat, [mc], statusmu sekarang adalah 'Volunteer Terawasi'. Jangan sampai aku mendengar laporan buruk tentangmu.{/cps}"

    mc "{cps=35}Iya, Kak. Aku mengerti.{/cps}"

    "{cps=35}Aku mengambil buku itu. Rasanya lebih berat daripada kelihatannya. Aku segera berpamitan dan melangkah keluar dari ruangan yang penuh dengan aroma persaingan itu.{/cps}"
    scene bg_school_corridor with fade
    play music "audio/tension_ambient.mp3" fadein 2.0

    "{cps=35}Aku berjalan menyusuri koridor. Pikiranku berkecamuk. Volunteer? Arsip kesiswaan? Dan siapa 'anggota' yang dimaksud Maya untuk membantuku?{/cps}"
    mc "{cps=35}Hah... sepertinya aku baru saja menukar kebebasanku dengan ini...{/cps}"
    mc "{cps=35}Tidak masalah lah, daripada nanti kehidupanku terlalu biasa{/cps}"
    "{cps=35}Aku ingin kembali ke kehidupan normalku{/cps}"
    play sound "audio/bell_chime_soft.mp3"
    play sound "audio/shoes_tap_fast.mp3"
    "{cps=35}*Tap. Tap. Tap.*{/cps}"
    
    "{cps=35}Langkah kaki yang tegas berhenti tepat di depanku. Aku mendongak dan melihat seorang siswi berdiri mematung di tengah jalan, menghalangi jalurku sepenuhnya.{/cps}"
    show abby_stern at center with dissolve
    "???" "{cps=40}Kamu terlambat tiga puluh detik untuk kembali ke kelas, Ikazaki [mc].{/cps}"
    "{cps=35}Kamu siapa?{/cps}"
    "???" "{cps=35}Hooo... kamu tidak tahu aku siapa?{/cps}"
    "???" "{cps=35}Padahal sudah kelihatan jelas jabatanku ini..{/cps}"
    mc "{cps=35}Sudahlah, aku tidak ada urusan denganmu.{/cps}"
    "{cps=35}HAHHH?{/cps}"
    mc "{cps=35}Mohon menepi{/cps}"
    "???" "{cps=35}Apa yan-{/cps}"
    "{cps=35}Aku memegang bahunya dan mendorongnya dengan perlahan agar dia berpindah{/cps}"
    "???" "{cps=35}Heee!?{/cps}"
    "???" "{cps=35}Dasar tidak sopan! Apa-apaan kamu ini!?{/cps}"
    mc "{cps=35}Aku tidak ada waktu untuk berbicara denganmu{/cps}"
    "???" "{cps=35}Setidaknya kamu bertanya dong namaku siapa?{/cps}"
    mc "{cps=35}Aku tadi sudah bertanya namun kamu belum menjawab{/cps}"
    mc "{cps=35}Dan aku tidak ingin kehilangan waktuku cuman demi itu{/cps}"
    "???" "{cps=35}Cih...{/cps}"
    ab "{cps=35}[ab].{/cps}"
    ab "{cps=35}Itu namaku{/cps}"
    mc "{cps=35}Oh gitu{/cps}"
    "{cps=35}Aku langsung melanjutkan langkahku ke kelas{/cps}"
    ab "{cps=35}Masa itu saja responmu!?{/cps}"
    mc "{cps=35}Aku tidak dengar~{/cps}"
    ab "{cps=35}Awas saja kamu, [mc]...{/cps}"
    ab "{cps=35}Aku tidak terima dengan penghinaan ini...{/cps}"
    scene bg_classroom with fade
    play music "audio/tension_ambient.mp3" fadein 2.0

    "{cps=35}Aku melangkah masuk ke kelas tepat saat bel jam pelajaran Sejarah berhenti bergema. Napasku sedikit memburu, bukan karena lelah, tapi karena rasa sesak yang aneh di dadaku.{/cps}"

    "{cps=35}Aku mencoba bersikap biasa saja saat melewati meja [y]. Namun, tanpa menoleh pun, aku bisa merasakan hawa dingin yang memancar dari sana.{/cps}"

    show vina_smile at right with dissolve
    v "{cps=60}Wah, wah... lihat siapa yang baru saja kembali dari 'petualangan' di luar sana. Wajahmu terlihat seperti orang yang baru saja menantang maut, [mc].{/cps}"

    mc "{cps=35}Jangan sekarang, Vin. Aku sedang tidak ingin bercanda.{/cps}"

    "{cps=35}Aku duduk dan langsung memasukkan buku pemberian [m] ke dalam laci meja. Namun, bunyi benturan kecil buku itu dengan laci kayu seolah terdengar sangat keras di tengah kesunyian kelas.{/cps}"
    show yuuka_stern at left with dissolve
    y "{cps=40} Buku apa itu [mc]? Sepertinya aku tidak pernah melihat buku seperti itu?{/cps}"
    v "{cps=35}Aku juga tidak pernah melihatnya...{/cps}"
    v "{cps=35}Kamu maling ya?{/cps}"
    mc "{cps=35}Hei! Bukan begitu... ini bagian dari kesepakatan volunteer...{/cps}"
    v "{cps=35}Volunteer? Kamu jadi volunteer?{/cps}"
    mc "{cps=35}Yap{/cps}"
    v "{cps=35}Heee... oke kalau begitu, nanti bantuin aku nugas ya{/cps}"
    mc "{cps=35}Enak aja! nggak begitu{/cps}"
    v "{cps=35}Hei [y], kita bisa menyuruh dia nih, kamu nggak mau?{/cps}"
    y "{cps=40}Terserahlah, mending kita siapin alat tulis kita{/cps}"
    y "{cps=35}Karena [t] sudah mau masuk ke kelas{/cps}"
    v "{cps=35}Ah iya juga!{/cps}"
    "{cps=35}Mereka kembali ke tempat duduk mereka{/cps}"
    mc "{cps=35}Hah...{/cps}"
    "{cps=35}Aku kembali memandang kondisi sekitar{/cps}"
    "{cps=35}Dan tidak sengaja bertatapan dengan [sh]{/cps}"
    "{cps=35}Namun dia langsung membuang wajahnya{/cps}"
    "{cps=35}Aku gak tahu apa yang terjadi barusan...{/cps}"
    yk "{cps=35}Cieee...{/cps}"
    sh "{cps=35}Apaan sih, [yk]{/cps}"
    yk "{cps=35}Nggak ada apa-apa kok nee-san...{/cps}"
    yk "{cps=35}Hanya saja aku sedang memikirkan skenario terlucu{/cps}"
    sh "{cps=35}Simpan saja ide mu itu{/cps}"
    yk "{cps=35}Baik{/cps}"
    "{cps=35}Suasana kelas mendadak hening total. Hanya ada suara gesekan kursi yang ditarik dan bunyi detak jam dinding yang entah kenapa terdengar lebih keras dari biasanya.{/cps}"

    play sound "audio/door_slide_hard.mp3"
    "{cps=35}*SRAAAK!*{/cps}"

    "{cps=35}Pintu depan terbuka lebar. [t] masuk dengan langkah yang sanggup membuat murid paling berisik sekalipun langsung tegak duduknya. Beliau membawa setumpuk buku yang diletakkan di meja dengan dentuman pelan.{/cps}"

    t "{cps=40}Selamat siang. Simpan semua barang yang tidak berkaitan dengan Sejarah. Sekarang.{/cps}"
    "{cps=35}Aku segera memasukkan alat tulis lain, memastikan buku pemberian Maya itu benar-benar tersembunyi jauh di dalam laci. Aku bisa merasakan tatapan Yuuka masih sesekali melirik ke arah tanganku.{/cps}"

    t "{cps=40}Hari ini kita akan membahas tentang 'Tragedi dan Pengkhianatan' dalam sejarah.{/cps}"
    "{cps=35}[t] menuliskan sebuah istilah besar di papan tulis dengan kapur yang berderit nyaring.{/cps}"

    t "{cps=40}{b}'Falsus in Uno, Falsus in Omnibus'{/b}. Ada yang tahu artinya?{/cps}"
    t "{cps=40}[mc], coba kamu jawab. Sepertinya kamu punya 'wawasan baru' setelah kejadian di lorong tadi.{/cps}"
    "{cps=35}Seketika suara kelas langsung penuh suara bisikan{/cps}"
    "{cps=35}Tentu saja yang mereka bicarakan itu aku{/cps}"
    v "{cps=35}Hue- kamu habis ngapain memangnya [mc]?{/cps}"
    mc "{cps=35}Bukan apa-apa kok...{/cps}"
    v "{cps=35}Ah masa... sepertinya mencurigakan..{/cps}"
    "{cps=35}[v] menatapku dengan wajah yang penasaran{/cps}"
    t "{cps=35}Sudah cukup!{/cps}"
    "{cps=35}Suasana kelas seketika diam{/cps}"
    t "{cps=35}Jadi, apa jawabanmu, [mc]?{/cps}"
    if correct_answer == False:
        t "{cps=35}Jangan sampai kamu salah jawab lagi seperti tadi pagi{/cps}"
    "{cps=35}Hmmmm... apa ya jawabannya{/cps}"
    "{cps=35}Aku tidak terlalu tahu bahasa latin sih.{/cps}"
    menu:
        "Satu kebohongan merusak segalanya":
            $ correct_answer_2 = True
            mc "{cps=40}Kalau tidak salah... artinya 'Satu kebohongan dalam satu hal, maka akan dianggap bohong dalam segala hal', Bu.{/cps}"
            
            t "{cps=40}Tepat sekali. Sebuah prinsip hukum lama yang menekankan pada kredibilitas individu.{/cps}"
            
            "{cps=35}Bu Nanami mengetukkan kapurnya ke papan tulis, tepat di bawah tulisan tersebut.{/cps}"

            t "{cps=40}Sekali kamu merusak kepercayaan seseorang dengan satu ketidakjujuran, maka seluruh kata-katamu setelahnya akan dipandang sebagai debu. Tidak berharga.{/cps}"

            "{cps=35}Aku merasakan hawa dingin dari arah Yuuka [y]. Dia tidak mengatakan apa-apa, tapi suara bolpoinnya yang menggores kertas terdengar sangat keras.{/cps}"

        "Kesalahan satu orang adalah kesalahan semua":
            $ correct_answer_2 = False
            mc "{cps=40}Artinya... kesalahan satu orang akan ditanggung oleh semua orang dalam kelompok itu, Bu?{/cps}"
            
            t "{cps=40}Salah. Itu pemikiran yang terlalu sempit, [mc]. Fokus kita hari ini adalah integritas pribadi.{/cps}"
            
            v "{cps=35}Duh, [mc]... sepertinya kamu benar-benar harus les bahasa asing sama aku nanti.{/cps}"
            
            t "{cps=40}Falsus in Uno, Falsus in Omnibus berarti ketidakjujuran dalam satu poin akan meruntuhkan seluruh kredibilitasmu di poin lainnya.{/cps}"

        "Aku benar-benar tidak tahu":
            $ correct_answer_2 = False
            mc "{cps=40}Maaf, Bu. Saya benar-benar tidak tahu. Bahasa Latin bukan keahlian saya.{/cps}"
            
            t "{cps=40}Setidaknya kamu jujur dengan ketidaktahuanmu. Itu lebih baik daripada berpura-pura tahu.{/cps}"
            
            t "{cps=40}Artinya adalah: Satu kebohongan akan merusak seluruh kebenaran yang kamu bangun.{/cps}"

    # --- KELANJUTAN PELAJARAN ---

    t "{cps=40}Ingatlah ini baik-baik, murid-murid. Dalam sejarah, banyak kekaisaran runtuh bukan karena musuh dari luar, tapi karena pengkhianatan kecil di dalam yang dibiarkan tumbuh.{/cps}"

    t "{cps=40}Perhatikan papan tulis. Sejarah bukan hanya tentang siapa yang menang perang, tapi tentang siapa yang 'menjual' saudaranya demi kemenangan itu.{/cps}"

    t "{cps=40}Mari kita ambil contoh klasik: {b}Marcus Junius Brutus{/b}.{/cps}"

    t "{cps=40}Brutus adalah orang paling dipercaya oleh Julius Caesar. Tapi pada Idus Maret 44 SM, dia menjadi salah satu penikam Caesar. Kenapa?{/cps}"

    v "{cps=35}Karena dia ingin jadi pahlawan, Bu?{/cps}"

    t "{cps=40}Bukan sekadar itu, Vina. Dia melakukannya atas nama 'kebaikan bersama'. Tapi sejarah mencatatnya sebagai simbol pengkhianatan tertinggi.{/cps}"

    t "{cps=40}Dante Alighieri bahkan menempatkan Brutus di lingkaran neraka terdalam, tepat di mulut iblis. Bagi Dante, tidak ada dosa yang lebih besar daripada mengkhianati orang yang mempercayaimu.{/cps}"

    "{cps=35}Aku merasa kursi yang kududuki mendadak panas. Di depanku, Yuuka [y] sedang mencoret-coret buku catatannya dengan gerakan kasar.{/cps}"

    t "{cps=40}Mari kita lihat buktinya dalam sejarah modern: {b}Kasus Benedict Arnold{/b} di Revolusi Amerika.{/cps}"

    t "{cps=40}Dia adalah jenderal hebat, tapi karena merasa tidak dihargai, dia mencoba menjual benteng West Point ke Inggris. Namanya sekarang identik dengan kata 'pengkhianat' di Amerika.{/cps}"

    t "{cps=40}Satu keputusan salah, satu rahasia yang disimpan rapat, cukup untuk menghapus ribuan jasa baik yang pernah dia lakukan sebelumnya.{/cps}"

    "{cps=35}Bu Nanami berhenti tepat di samping meja Yuuka. Yuuka langsung menunduk dalam.{/cps}"

    t "{cps=40}Apakah menurutmu kepercayaan itu seperti kaca, Yuuka?{/cps}"

    y "{cps=35}...Iya, Bu. Sekali retak, bayangannya tidak akan pernah utuh lagi.{/cps}"

    t "{cps=40}Jawaban yang filosofis. Bagus.{/cps}"

    "{cps=35}Selama dua jam berikutnya, Bu Nanami membedah berbagai kasus intelijen masa perang. Tentang bagaimana kode-kode rahasia dihancurkan karena satu orang yang 'bernyanyi' kepada musuh.{/cps}"

    "{cps=35}Aku hanya bisa menatap buku perak pemberian Maya di dalam laci. Buku itu sekarang terasa seperti bom waktu yang bisa meledak kapan saja.{/cps}"

    scene black with fade
    stop music fadeout 4.0

    "{cps=35}Dua jam yang penuh siksaan mental itu akhirnya berakhir seiring bunyi bel pulang.{/cps}"

    play sound "audio/school_bell.mp3"
    "{cps=40}*Ting... Tong... Ting... Tong...*{/cps}"

    scene bg_classroom_sunset with fade
    play music "audio/afternoon_ambient.mp3" fadein 2.0

    "{cps=35}Warna oranye matahari senja menembus jendela kelas, menciptakan bayangan panjang di lantai. Suasana yang seharusnya romantis ini justru terasa sangat canggung.{/cps}"

    show vina_smile at right with dissolve
    v "{cps=35}Ugh... kepalaku mau pecah. Bu Nanami kalau ngasih contoh sejarah kok nakutin banget ya? Kayak lagi nyidang narapidana.{/cps}"

    v "{cps=35}[y], ayo ke kafe! Aku butuh asupan gula biar nggak stres.{/cps}"
    y "{cps=35}Hei.. kita kan ada audit gudang penyimpanan{/cps}"
    v "{cps=35}Ah iya juga...{/cps}"
    v "{cps=35}Arrrrhhhh aku ingin bersantai...{/cps}"
    v "{cps=35}Ah!{/cps}"
    "{cps=35}[v] menatapku{/cps}"
    v "{cps=35}Kenapa kita tidak menyuruh ini anak aja?{/cps}"
    mc "{cps=35}Kenapa aku?{/cps}"
    v "{cps=35}Kan kamu volunteer, jadi kamu yang ngerjain yak{/cps}"
    v "{cps=35}Plisss{/cps}"
    mc "{cps=35}Yaa.... aku tidak keberatan sih...{/cps}"
    mc "{cps=35}Asal ada yang mau membantu aja{/cps}"
    v "{cps=35}Kalau itu maaf, aku tidak bisa{/cps}"
    y "{cps=35}Aku bisa sih, namu-{/cps}"
    v "{cps=35}Aku ada kegiatan lain sama [y] jadi... sampai jumpa, [mc]!{/cps}"
    v "{cps=35}Untuk listnya kamu ambil di ruang osis ya!{/cps}"
    "{cps=35}Mereka langsung meninggalkanku di ruang kelas{/cps}"
    mc "{cps=35}Hah... kegiatan lain yang akan menguras tenaga{/cps}"
    mc "{cps=35}Apa boleh buat, sebagai volunteer yang baik, harus siap dengan segala kemungkinan{/cps}"
    scene bg_school_corridor_sunset with fade
    "{cps=35}Aku berjalan menuju ruang OSIS. Tanganku meraba saku, memastikan buku itu masih ada. Rasanya aneh, aku baru saja resmi jadi volunteer dan sudah diberi tugas audit.{/cps}"
    mc "{cps=35}Hmmm.... ruang OSIS... kalau tidak salah di ujung koridor ini.{/cps}"

    "{cps=35}Begitu sampai di depan ruangan itu, aku menyadari sesuatu yang janggal. Pintunya tidak tertutup rapat, menyisakan sedikit celah.{/cps}"

    mc "{cps=35}Halo? Permisi?{/cps}"

    "{cps=35}Tidak ada jawaban. Aku mendorong pintunya perlahan. Suara engsel pintu yang berderit pelan seolah memperingatiku untuk tidak masuk, tapi aku butuh daftar audit itu sekarang.{/cps}"
    play sound "audio/door_open.mp3"
    scene bg_council_room_interior with dissolve
    "{cps=35}Ruangan itu sunyi. Harum aroma teh melati dan kertas baru memenuhi udara. Aku melangkah mendekati meja besar di tengah ruangan, mencari tumpukan kertas yang dimaksud Vina.{/cps}"

    mc "{cps=35}Mana ya... ah, itu dia di meja belakang.{/cps}"

    "{cps=35}Aku berjalan ke arah meja di sudut ruangan. Namun, langkahku mendadak membeku saat mendengar suara kain yang bergesekan dari balik sekat lemari arsip.{/cps}"

    play sound "audio/clothing_rustle.mp3"
    "???" "{cps=40}Ugh... kenapa susah sekali dilepas...{/cps}"

    mc "{cps=35}Suara itu... bukannya suara kak [m]?{/cps}"

    "{cps=35}Rasa penasaran mengalahkan logikaku. Aku mengintip sedikit dari balik celah lemari. Dan di sana...{/cps}"

    "{cps=35}Bukan hanya kak [m] yang ada di sana. Ternyata ada [ab] yang sedang berlutut di belakangnya, mencoba menarik ritsleting rok Maya yang tersangkut dengan serius.{/cps}"

    ab "{cps=40}Ketua, diam sebentar. Kalau ditarik paksa, kainnya bisa robek. Kenapa sih anda ceroboh sekali?{/cps}"

    m "{cps=40}Ugh... maaf, [ab]. Aku tadi terburu-buru.{/cps}"
    ab "{cps=40}Hah... masih untung ada aku, coba aja yang dateng malah anak itu{/cps}"

    "{cps=35}Pemandangan itu... benar-benar pemandangan yang langka.{/cps}"
    "{cps=35}Seorang komandan kedisiplinan sekolah yang menjadi sangat protektif terhadap pimpinannya{/cps}"
    "{cps=35}Dan juga seorang ketua osis yang selalu terlihat tegak, dingin, dan penuh kendali, sekarang terlihat begitu... rapuh.{/cps}"
    "{cps=35}Jujur saja, pemandangan ini jauh dari kata 'disiplin'{/cps}"

    "{cps=35}Oke, [mc]. Pilihannya dua: pergi sekarang dan anggap tidak pernah terjadi, atau...{/cps}"

    menu:
        "Berusaha menyapa":
            $ maya_rel -= 5
            $ trobos = True
            "{cps=35}Sebagai pria harus berperilaku jujur, apapun yang terjadi{/cps}"
            "{cps=35}Meski akan dibenci{/cps}"
            "{cps=35}Aku kembali mengetuk lemari yang ada di depanku{/cps}"
            play sound "audio/knock_wood.mp3"
            mc "{cps=40}Permisi...{/cps}"
            m "{cps=35}Hm?{/cps}"
            "{cps=35}[m] terlihat sedikit bingung{/cps}"
            "{cps=35}Wajahnya langsung memerah dan seperti yang kita tahu apa yang akan terjadi selanjutnya{/cps}"
            show maya_shocked with vpunch
            m "{cps=40}KYAAAAA!!{/cps}"
            "{cps=35}Maya refleks berbalik sambil menutupi dadanya. Matanya menatapku dengan campuran antara amarah dan malu yang luar biasa.{/cps}"
            ab "{cps=40}I-IKAZAKI?! Sejak kapan kamu di sana?! Keluar! KELUAR SEKARANG!!{/cps}"
            ab "{cps=40}Beraninya kamu masuk tanpa izin dan melihat kondisi Ketua yang seperti ini! Dasar mesum!{/cps}"
            mc "{cps=40}Maaf! Aku cuma mau ambil list audit!{/cps}"
            ab "{cps=35}Cepat keluar!{/cps}"
            mc "{cps=35}Ba-baik{/cps}"
            m "{cps=35}Sial... kenapa aku sampai lupa menutup pintu..{/cps}"
            "{cps=35}Aku langsung berbalik dan menunggu kak [m] berganti pakaian di luar{/cps}"

        "Pergi secara diam-diam":
            $ trobos = False
            $ maya_rel -= 3
            "{cps=35}Aku mencoba melangkah mundur dengan sangat pelan. Tapi malangnya, kakiku menyenggol sebuah tempat sampah besi.{/cps}"
            play sound "audio/trashcan_clatter.mp3"
            "{cps=35}*PRANG!*{/cps}"
            ab "{cps=40}Siapa itu?!{/cps}"
            m "{cps=35}[ab], coba kamu cek{/cps}"
            "{cps=35}Baik!{/cps}"
            "{cps=35}[ab] langsung keluar dari balik lemari dan langsung melihatku{/cps}"
            "{cps=35}Keheningan yang sangat canggung menyelimuti ruangan selama beberapa detik.{/cps}"
            ab "{cps=40}...Kamu. Berapa banyak yang kamu lihat?{/cps}"
            mc "{cps=40}Hampir semua sih...{/cps}"
            m "{cps=35}[ab], siapa yang ada di de-{/cps}"
            m "{cps=35}Pan....{/cps}"
            "{cps=35}Wajah kak [m] langsung memerah dan seperti yang kita tahu apa yang akan terjadi selanjutnya{/cps}"
            m "{cps=35}KYAAAAAAAAAA{/cps}"
            ab "{cps=35}Ngapain kamu muncul sekarang!?{/cps}"
            ab "{cps=35}KENAPA KAMU NGGAK BILANG DARI TADI!{/cps}"
            m "{cps=35}CEPAT KAMU KELUAR!{/cps}"
            "{cps=35}Ba-baik!{/cps}"
            m "{cps=35}Sial... kenapa aku sampai lupa menutup pintu..{/cps}"
            "{cps=35}Aku langsung pergi ke luar ruangan{/cps}"

    "{cps=35}Sial... apa yang terjadi...{/cps}"
    "{cps=35}Padahal aku hanya ingin mengambil list barang..{/cps}"
    "{cps=35}Walau hal itu tidak bisa langsung aku lupakan sih...{/cps}"
    "{cps=35}Tak lama kemudian...{/cps}"
    m "{cps=35}Ahem! [mc], silahkan masuk{/cps}"
    mc "{cps=35}Ba-baik!{/cps}"
    "{cps=35}Aku langsung masuk ke ruangan itu lagi{/cps}"
    mc "{cps=35}Permisi...{/cps}"
    "{cps=35}Suasana di ruangan itu langsung berubah 180 derajat. Awalnya cukup hangat, namun sekarang menjadi dingin...{/cps}"
    "{cps=35}Bahkan lebih dingin dibandingkan kulkas. Mungkin akibat kejadian barusan.{/cps}"
    m "{cps=35}Aku harap kamu tidak mengingat semua hal yang kamu lihat barusan{/cps}"
    mc "{cps=35}Semoga aja sih begitu..{/cps}"
    "{cps=35}Walau itu sulit untuk dilupakan begitu saja{/cps}"
    ab "{cps=40}Kalau kamu tidak melupakannya, akan aku pastikan reputasimu di sekolah ini lebih buruk daripada nilai ujianmu, [mc].{/cps}"
    mc "{cps=35}Jangan mengancam diriku terus dong! Aku kan tidak sengaja.{/cps}"
    ab "{cps=40}Tidak sengaja atau tidak, kamu sudah melihat hal yang terlarang. Bahkan hampir seluruh murid di sini pun tidak pernah melihat sisi 'kurang rapi' dari Ketua.{/cps}"
    mc "{cps=35}Hah?{/cps}"
    mc "{cps=35}Padahal ini sekolah khusus perempuan?{/cps}"
    "{cps=35}Walau sekarang sudah tidak sih...{/cps}"
    ab "{cps=35}Memangnya kamu pikir ini sekolah apa hah!?{/cps}"
    "{cps=35}*bonk{/cps}"
    mc "{cps=35}Aduh!{/cps}"
    ab "{cps=40}Memangnya kamu pikir Ketua itu orang sembarangan!?{/cps}"
    "{cps=35}Setelah sekian lama, aku akhirnya mendapatkan pukulan{/cps}"
    "{cps=35}Terakhir kakakku sih{/cps}"
    m "{cps=35}Sudah cukup, [ab]. Kita punya tugas yang lebih penting.{/cps}"
    ab "{cps=35}Baik ketua...{/cps}"
    "{cps=35}Wajah [ab] seakan masih tidak puas dengan pilihan yang diambil ketua{/cps}"
    m "{cps=35}Memang sih kejadian tadi tidak bisa dihindari, ditambah kan aku lupa mengunci pintu{/cps}"
    m "{cps=35}Lokerku juga sedang rusak sih kuncinya{/cps}"
    mc "{cps=35}Memangnya rusak kenapa kak?{/cps}"
    ab "{cps=35}Kamu ini masih bertanya ya padahal sudah tau salah!{/cps}"
    "{cps=35}*bonk{/cps}"
    mc "{cps=35}Aduh!{/cps}"
    "{cps=35}Aku dipukul, lagi{/cps}"
    m "{cps=35}Cukup [ab]!{/cps}"
    ab "{cps=35}Tapi ketu-{/cps}"
    m "{cps=35}Kamu bisa melakukan itu lain kali, kan sudah aku bilang kita ada tugas yang lebih penting{/cps}"
    "{cps=35}Suara kak [m] langsung berubah, wibawanya sebagai ketua kembali muncul dan menghangatkan ruangan ini{/cps}"
    ab "{cps=35}Baik...{/cps}"
    m "{cps=35}Jadi, apa yang ingin kamu lakukan?{/cps}"
    mc "{cps=35}Begini kak, kata anak osis tadi aku disuruh melakukan audit gudang{/cps}"
    mc "{cps=35}Dan kata kakak juga aku akan ditemani seseorang{/cps}"
    m "{cps=35}Ah! Kebetulan banget{/cps}"
    m "{cps=35}Jadi orang yang aku maksud itu ada di depanmu{/cps}"
    mc "{cps=35}Depanku? Maksud kakak...{/cps}"
    "{cps=35}Aku memadang [ab] yang berusaha untuk mengelak{/cps}"
    ab "{cps=35}Ketua? Kamu tidak salah pilih kan?{/cps}"
    ab "{cps=35}Masa ketua ingin aku satu kelompok sama orang ini?{/cps}"
    mc "{cps=35}Memangnya aku juga mau denganmu?{/cps}"
    ab "{cps=35}HAH?{/cps}"
    ab "{cps=35}Aku juga ga sudi denganmu!{/cps}"
    m "{cps=35}Cukup kalian berdua!{/cps}"
    m "{cps=35}Simpan sifat kekanak-kanakan kalian{/cps}"
    m "{cps=35}Ini itu tugas yang harus penuh ketelitian{/cps}"
    m "{cps=35}Aku melihat [ab] dan kamu itu adalah orang yang teliti sekaligus bisa menyelesaikan tugas ini dengan tepat waktu{/cps}"
    mc "{cps=35}Tapi kan belum tentu bisa dipasangkan begitu saja kak{/cps}"
    mc "{cps=35}Harus ada persetujuan dari kedua belah pihak{/cps}"
    m "{cps=35}Kamu sudah menandatangani surat itu kan?{/cps}"
    mc "{cps=35}Memang sih...{/cps}"
    m "{cps=35}Kalau kamu sudah menandatangani, itu sudah cukup untuk persetujuanmu{/cps}"
    ab "{cps=35}Tapi ketua, kan aku belum menj-{/cps}"
    m "{cps=35}Ssssttttt{/cps}"
    m "{cps=35}Aku yang punya otoritas{/cps}"
    m "{cps=35}Kalau aku melihat kalian berdua bisa bekerjasama, berarti aku bisa memasangkan kalian berdua{/cps}"
    ab "{cps=35}Nggak gitu konsepnya ketua{/cps}"
    m "{cps=35}Keputusanku itu mutlak, kamu mau melawan perintahku{/cps}"
    ab "{cps=35}Selama ini aku memang selalu setuju dengan pilihanmu.. tapi untuk kali ini..{/cps}"
    ab "{cps=35}Aku menolak{/cps}"
    m "{cps=35}Padahal kamu ingin berbincang dengan anak laki?{/cps}"
    "{cps=35}Wajah [ab] langsung memerah, seakan-akan rahasia dia dibongkar langsung{/cps}"
    ab "{cps=35}A-apa maksud ketua!?{/cps}"
    ab "{cps=35}Sejak kapan aku bilang begitu!?{/cps}"
    m "{cps=35}Padahal dulu pas kamu daftar ngomongnya beg-{/cps}"
    mc "{cps=35}Aku.. tidak paham{/cps}"
    ab "{cps=35}Kamu jangan beri komentar!{/cps}"
    m "{cps=35}Sudahlah [ab], anggap saja ini sebuah latihan{/cps}"
    ab "{cps=35}Uhhm...{/cps}"
    "{cps=35}[ab] menatapku dengan tatapan yang sangat tajam, tapi kali ini ada sedikit rona merah di pipinya yang tidak bisa dia sembunyikan.{/cps}"
    m "{cps=35}Nah, [mc]. Ini daftar barang yang harus diaudit. Dan ini kunci gudang penyimpanan basement.{/cps}"
    play sound "audio/keys_clinking.mp3"
    "{cps=35}Maya menyerahkan seikat kunci berat dan sebuah buku audit kepadaku.{/cps}"
    mc "{cps=35}Hmmm.... sepertinya tidak terlalu banyak{/cps}"
    m "{cps=35}Sebaiknya kamu jangan menyepelekan sesuatu hal{/cps}"
    m "{cps=35}Bisa saja dikit namun nanti malah menyebar{/cps}"
    mc "{cps=35}Iya kak...{/cps}"
    m "{cps=35}Tapi kamu bisa kan?{/cps}"
    mc "{cps=35}Tentu saja kak{/cps}"
    m "{cps=35}Kalau ada pertanyaan bisa ditanyakan ke [ab]{/cps}"
    ab "{cps=35}Sebaiknya jangan banyak bertanya{/cps}"
    "{cps=35}Sepertinya [ab] masih belum bisa menerimaku untuk hadir di lingkungan ini{/cps}"
    m "{cps=35}Hah... sepertinya kamu harus mulai terbiasa dengan sifatnya ya, [mc]{/cps}"
    m "{cps=35}Dia memang begitu namun semakin lama pasti akan membaik kok{/cps}"
    mc "{cps=35}Baik....{/cps}"
    m "{cps=35}Kamu ada pertanyaan?{/cps}"
    mc "{cps=35}Untuk saat ini sih belum... mungkin ini kak, arah ke ruangan itu{/cps}"
    m "{cps=35}Kalau itu [ab] akan memandumu. Dan ingat...{/cps}"
    m "{cps=35}Apa yang terjadi di ruangan ini, tetap di ruangan ini. Mengerti?{/cps}"
    "{cps=35}[m] kembali memegang bahuku, tangannya yang lembut seakan-akan membuat diriku tenang{/cps}"
    mc "{cps=35}Mengerti, Kak...{/cps}"
    "{cps=35}Namun disaat yang sama...{/cps}"
    "{cps=35}Ada masalah yang harus aku hadapi{/cps}"
    "{cps=35}Aku tidak ingin bilang ini masalah... Namun...{/cps}"
    "{cps=35}Aku punya firasat buruk{/cps}"
    m "{cps=35}Sebaiknya kamu bergegas, [mc]. Karena [ab] sudah berada di depan ruangan{/cps}"
    "{cps=35}Eh? Sejak kap-{/cps}"
    ab "{cps=35}Ayo cepat jalan! Lama banget jadi orang!{/cps}"
    "{cps=35}Entah kenapa aku merasa sedang mengalami MOS{/cps}"
    mc "{cps=35}Baik...{/cps}"
    m "{cps=35}Semoga kegiatan kalian lancar{/cps}"
    "{cps=35}*Clek{/cps}"
    mc "{cps=35}Jadi, kita kemana?{/cps}"
    ab "{cps=35}Kamu gausah banyak ngomong, cukup ikuti aku{/cps}"
    scene bg_school_corridor_sunset with fade
    play music "audio/tension_walking.mp3" fadein 2.0

    "{cps=35}Aku berjalan di belakang [ab]. Suara denting lonceng di lehernya terdengar setiap kali dia melangkah dengan cepat. Dia tampak sangat terburu-buru, mungkin karena malu.{/cps}"

    mc "{cps=35}Hei, jalannya pelan-pelan sedikit. Aku bawa buku ini juga.{/cps}"
    ab "{cps=35}Diam! Kamu itu lambat sekali!{/cps}"
    ab "{cps=35}Dan soal yang dikatakan Ketua tadi... jangan pernah kamu pikirkan, apalagi kamu tanyakan!{/cps}"
    mc "{cps=35}Maksudmu soal kamu yang ingin berbincang dengan laki-laki?{/cps}"
    "{cps=35}[ab] mendadak berhenti berjalan. Dia berbalik dan menatapku dengan wajah yang benar-benar merah padam.{/cps}"
    ab "{cps=35}JANGAN {w=0.1} BAHAS {w=0.1} ITU {w=0.1} LAGI{/cps}"
    ab "{cps=35}Mengerti?{/cps}"
    mc "{cps=35}U-uh...{/cps}"
    "{cps=35}Kenapa dia sampai segitunya?{/cps}"
    "{cps=35}Perjalanan kami kembali sangat sunyi, dan langkah kaki kami sangat berbeda{/cps}"
    mc "{cps=35}Anu... memangnya ada apa sih?{/cps}"
    ab "{cps=35}K-K-KAMU!{/cps}"
    ab "{cps=35}Itu cuma taktik Ketua untuk mengerjaiku! Aku sama sekali... tidak tertarik... dengan makhluk sepertimu!{/cps}"
    mc "{cps=35}Iya, iya. Aku paham. Tidak perlu sampai berteriak di lorong.{/cps}"
    "{cps=35}Aku hanya bisa menghela napas. Sepertinya audit ini akan menjadi sesi 'penyiksaan' mental bagiku.{/cps}"
    "{cps=35}Kami sampai di depan pintu besi tua menuju gudang. Udara dingin dan aroma debu mulai tercium.{/cps}"
    ab "{cps=35}Buka pintunya. Dan ingat, jangan sentuh apapun kecuali barang yang ada di daftar.{/cps}"
    mc "{cps=35}Baik...{/cps}"
    "{cps=35}Aku membuka pintunya{/cps}"
    "{cps=35}Ruangan itu penuh sekali dengan debu{/cps}"
    scene bg_storage_room_dark with fade
    play sound "audio/dust_cough.mp3"
    "{cps=35}*Uhuk! Uhuk!*{/cps}"
    mc "{cps=35}Debunya tebal sekali... Sepertinya tempat ini tidak pernah disentuh selama bertahun-tahun.{/cps}"
    ab "{cps=35}Tentu saja. Ini gudang arsip lama dan barang-barang yang sudah tidak terpakai.{/cps}"
    mc "{cps=35}Masa untuk sekelas sekolah khusus perempuan sampai sekotor ini?{/cps}"
    ab "{cps=35}Jangan bertanya ke aku! Aku kan hanya komandan kedisiplinan!{/cps}"
    mc "{cps=35}Disini ada tukang bersih-bersih kan?{/cps}"
    mc "{cps=35}Kenapa tidak minta tolong mereka?{/cps}"
    ab "{cps=35}Kamu ini banyak bertanya ya, [mc]...{/cps}"
    ab "{cps=35}Sebaiknya kamu menanyakan itu semua ke [m], jangan ke aku{/cps}"
    ab "{cps=35}Ditambah disini kan banyak berkas penting{/cps}"
    mc "{cps=35}Padahal kebanyakan peralatan olahraga? apa disini tidak pernah ada kegiatan olahraga?{/cps}"
    ab "{cps=35}CUKUP!{/cps}"
    ab "{cps=35}Kalau kamu bertanya sekali lagi, aku kurung kamu disini{/cps}"
    mc "{cps=35}Kalau aku dikurung di sini, kamu melapor ke kak [m] gimana?{/cps}"
    ab "{cps=35}Moh... kamu nyalain lampu dulu sana, daripada ngomong aja{/cps}"
    ab "{cps=35}Barang-barang disini tidak akan mengaudit dirinya sendiri{/cps}"
    mc "{cps=35}Memangnya mereka punya nyawa?{/cps}"
    ab "{cps=35}BERISIK!{/cps}"
    mc "{cps=35}Iya, iya. Galak amat...{/cps}"
    "{cps=35}Aku meraba-raba dinding di dekat pintu, mencari sakelar yang dimaksud.{/cps}"
    play sound "audio/light_switch_stuck.mp3" # Suara sakelar agak macet
    "{cps=35}*Klik... Klik...*{/cps}"
    mc "{cps=35}Kok nggak nyala?{/cps}"
    ab "{cps=35}Tekan yang keras! Sakelarnya memang agak rewel.{/cps}"
    play sound "audio/light_switch_on.mp3"
    # Gunakan efek flash putih singkat sebelum ganti background
    show white with flash
    scene bg_storage_room_bright with dissolve
    "{cps=35}Lampu neon di langit-langit berkedip-kedip sebentar, mengeluarkan suara mendengung yang menyakitkan telinga sebelum akhirnya menerangi seisi ruangan.{/cps}"
    mc "{cps=35}Wah...{/cps}"
    mc "{cps=35}Masih redup{/cps}"
    ab "{cps=35}Ya... mau gimana lagi... ayo [mc]{/cps}"
    ab "{cps=35}Kita audit barang disini{/cps}"
    mc "{cps=35}Hm!{/cps}"
    ab "{cps=35}Ingat ya jangan sampai kamu menyentuh barang apapun yang ada disini{/cps}"
    mc "{cps=35}Oke, oke. Aku mulai ya. Jangan kaget kalau nanti aku malah menemukan harta karun.{/cps}"
    ab "{cps=35}Jangan mimpi. Palingan cuma tikus atau kecoak. Sudah, cepat kerjakan bagianmu di rak sana!{/cps}"
    "{cps=35}Aku melangkah ke pojok kiri, ke arah tumpukan dokumen yang terlihat seperti menara miring. Jariku mulai menelusuri map-map usang yang warnanya sudah memudar.{/cps}"
    "{cps=35}Satu per satu aku mengecek daftar di buku audit. Peralatan pramuka... berkas absensi 7 tahun yang lalu.{/cps}"
    mc "{cps=35}Kenapa buku absensi masih ada disini padahal mereka sudah lulus lama?{/cps}"
    ab "{cps=35}Jangan tanya ke aku, tanya saja ke [m]{/cps}"
    mc "{cps=35}Hmmmm.... ok{/cps}"
    "{cps=35}Kami melanjutkan audit di ruangan ini{/cps}"
    "{cps=35}Sampai 15 menit kemudian...{/cps}"
    "{cps=35}Aku menemukan suatu hal yang menarik perhatianku{/cps}"
    mc "{cps=35}Apa ini?{/cps}"
    "{cps=35}Aku melihat tumpukan buku yang tergeletak di rak paling bawah{/cps}"
    "{cps=35}Buku itu seakan-akan memanggilku dengan nada hangat{/cps}"
    "{cps=35}Walau aku tahu kalau buku itu tidak bisa berbicara{/cps}"
    "{cps=35}Namun aku ingin menyentuh buku itu{/cps}"
    ab "{cps=35}Jangan kamu sentuh!{/cps}"
    mc "{cps=35}Eh?{/cps}"
    ab "{cps=35}Tugas kita disini hanya melakukan audit, tidak lebih{/cps}"
    mc "{cps=35}Tapi-{/cps}"
    ab "{cps=35}Tidak ada tapi-tapi!{/cps}"
    mc "{cps=35}Kamu aslinya juga penasaran kan?{/cps}"
    ab "{cps=35}Nggak juga kok{/cps}"
    "{cps=35}Tapi dari reaksimu sepertinya iya sih..{/cps}"
    "{cps=35}Aku menghiraukan pendapatnya dan langsung mengambil buku itu{/cps}"
    ab "{cps=35}Ja-{/cps}"
    "{cps=35}'Proposal kegiatan'{/cps}"
    mc "{cps=35}Kenapa proposal seperti itu ada disini?{/cps}"
    "{cps=35}'Ikazaki'{/cps}"
    mc "{cps=35}Loh? Kok ada namaku?{/cps}"
    ab "{cps=35}Berarti milikmu itu, [mc]{/cps}"
    mc "{cps=35}Nggak mungkin sih, kan aku baru masuk sekitar 3 hari{/cps}"
    mc "{cps=35}Lagipula aku nggak pernah masuk ke ruangan ini{/cps}"
    ab "{cps=35}Apa kamu ada kerabat yang pernah sekolah disini?{/cps}"
    mc "{cps=35}Ummm{/cps}"
    "{cps=35}Aku mencoba mengingat perkataan kak [m] terkait kakakku{/cps}"
    mc "{cps=35}Ah.... benar juga...{/cps}"
    mc "{cps=35}Kakakku pernah sekolah disini{/cps}"
    ab "{cps=35}Hah?{/cps}"
    ab "{cps=35}Yang benar?{/cps}"
    mc "{cps=35}Yap, aku tidak terlalu ingat detailnya, tapi kak [m] pernah menunjukkan fotonya{/cps}"
    ab "{cps=35}Kamu yakin itu foto kakakmu? Bukan hasil editan?{/cps}"
    mc "{cps=35}Aku ingin bilang begitu... namun dengan ditemukannya proposal ini{/cps}"
    mc "{cps=35}Sepertinya itu memang beneran{/cps}"
    ab "{cps=35}Terus kakakmu kemana?{/cps}"
    mc "{cps=35}Dia telah tiada, tepat 10 tahun yang lalu{/cps}"
    ab "{cps=35}Aku.. turut berduka cita, [mc]{/cps}"
    ab "{cps=35}Semoga beliau tenang disisinya...{/cps}"
    mc "{cps=35}Iya..{/cps}"
    "{cps=35}[ab] terdiam. Wajah galaknya sedikit melunak, berganti dengan tatapan penuh selidik ke arah buku di tanganku.{/cps}"
    ab "{cps=35}Coba buka... pelan-pelan. Kertasnya sudah sangat rapuh.{/cps}"
    play sound "audio/paper_creak.mp3"
    "{cps=35}Aku membuka lembaran pertama dengan hati-hati. Aroma kertas tua yang khas langsung tercium, bercampur dengan bau debu ruangan.{/cps}"
    mc "{cps=35}**'Proposal Festival Budaya Gabungan - Penanggung Jawab: Ikazaki [mi]'**.{/cps}"
    mc "{cps=35}Tahunnya... 10 tahun yang lalu.{/cps}"
    ab "{cps=35}10 tahun? bukannya itu tahun dimana kakakmu tiada?{/cps}"
    mc "{cps=35}Sepertinya sih...{/cps}"
    ab "{cps=35}Bagaimana kalau ini kita bawa ke [m]{/cps}"
    mc "{cps=35}Untuk apa?{/cps}"
    ab "{cps=35}Sudah jelas bukan? Untuk melanjutkan program ini lah!{/cps}"
    ab "{cps=35}Kamu tidak ingin kakakmu memiliki penyesalan bukan?{/cps}"
    mc "{cps=35}Memang sih... tapi kan...{/cps}"
    "{cps=35}*grep{/cps}"
    "{cps=35}Aku bisa merasakan jarinya yang lembut{/cps}"
    ab "{cps=35}Tenang saja, aku akan membantumu{/cps}"
    mc "{cps=35}Kenapa... kamu mau membantuku?{/cps}"
    ab "{cps=35}Memangnya perlu alasan untuk membantu teman?{/cps}"
    "{cps=35}Wajahnya penuh dengan tekad yang kuat{/cps}"
    "{cps=35}Padahal kamu sebelumnya menjaga jarak...{/cps}"
    mc "{cps=35}Ano...{/cps}"
    ab "{cps=35}Kenapa, [mc]?{/cps}"
    mc "{cps=35}Sampai kapan kamu memegang tanganku..{/cps}"
    ab "{cps=35}Hweee!?{/cps}"
    "{cps=35}[ab] tiba-tiba menarik diri, wajahnya memerah karena sadar posisi kami tadi sangat dekat{/cps}"
    ab "{cps=35}Bukan berarti aku ingin mendekatimu loh, jangan geer!{/cps}"
    mc "{cps=35}Oke...{/cps}"
    ab "{cps=35}Baiklah, list barang yang sudah di audit masih kurang atau belum?{/cps}"
    mc "{cps=35}Seharusnya sih sudah...{/cps}"
    ab "{cps=35}Kalau belum lengkap mending kamu periksa lagi deh{/cps}"
    ab "{cps=35}Bagianku juga belum selesai...{/cps}"
    ab "{cps=35}Cih, kenapa sih bagianku selalu banyak...{/cps}"
    "{cps=35}Sepertinya dia perlu bantuan...{/cps}"
    "{cps=35}Apa perlu aku membantunya?{/cps}"
    menu:
        "Bantu Abby":
            $ apatis = False
            $ abby_rel += 10
            "{cps=35}Melihatnya menggerutu sambil mengatur tumpukan kardus sendirian, aku tidak tega juga.{/cps}"
            mc "{cps=35}Sini, biar aku bantu. Bagian atas itu terlalu tinggi untukmu, kan?{/cps}"
            ab "{cps=35}Kamu menghinaku ya?!{/cps}"
            ab "{cps=35}Padahal kamu lebih pendek dariku?{/cps}"
            mc "{cps=35}Bukan begitu. Kalau kita kerjakan berdua, kita bisa lebih cepat keluar dari gudang berdebu ini.{/cps}"
            ab "{cps=35}Ugh... ya sudah{/cps}"
            mc "{cps=35}Sisa bagian mana?{/cps}"
            ab "{cps=35}Bagian atas{/cps}"
            mc "{cps=35}Hmmm itu cukup tinggi{/cps}"
            ab "{cps=35}Oleh karena itu aku pakai tangga{/cps}"
            "{cps=35}[ab] menempatkan tangga itu tepat di depan lemari{/cps}"
            ab "{cps=35}Aku akan naik, kamu pegangin tangganya{/cps}"
            mc "{cps=35}Kenapa nggk aku aja?{/cps}"
            ab "{cps=35}Ini kan bagianku, sudah kamu tetap dibawah saja{/cps}"
            mc "{cps=35}Baik...{/cps}"
            "{cps=35}[ab] mulai menaiki anak tangga satu per satu. Tangga kayu tua itu berderit pelan, seolah memprotes beban yang diterimanya.{/cps}"
            mc "{cps=35}Hati-hati, tangganya agak goyang.{/cps}"
            ab "{cps=35}Diamlah, fokus saja pegangi tangganya! Jangan sampai matamu melirik ke mana-mana ya!{/cps}"
            "{cps=35}Aku hanya bisa menghela napas sambil mencengkeram sisi tangga dengan erat. Posisi ini... sebenarnya agak canggung.{/cps}"
            "{cps=35}Aku berdiri tepat di bawahnya, dan aroma sampo apel dari rambutnya tercium jelas saat dia bergerak mengecek barang di rak paling atas.{/cps}"
            ab "{cps=35}Ok... barang ini juga sudah....{/cps}"
            ab "{cps=35}[mc], sebelah mana lagi yang belum?{/cps}"
            mc "{cps=35}Di sebelah kananmu, [ab]{/cps}"
            ab "{cps=35}Baik{/cps}"
            "{cps=35}[ab] melanjutkan auditnya dengan serius, dia selalu menunjukkan wibawanya, entah bagaimana caranya{/cps}"
            "{cps=35}Meski telah mengalami berbagai kesulitan sejak bertemu denganku{/cps}"
            "{cps=35}Namun entah kenapa...{/cps}"
            "{cps=35}Aku merasa seperti memiliki kakak{/cps}"
            ab "{cps=35}[mc], masih ada lagi?{/cps}"
            mc "{cps=35}Eh? Sudah sih...{/cps}"
            ab "{cps=35}Yang benar? Nadamu tidak meyakinkan pun{/cps}"
            mc "{cps=35}Beneran{/cps}"
            ab "{cps=35}Ok{/cps}"
            "{cps=35}*BRAK{/cps}"
            mc "{cps=35}Aduh! Apa-apaan itu!?{/cps}"
            mc "{cps=35}Kenapa kamu melempar buku auditmu kewajahku?{/cps}"
            ab "{cps=35}Biar cepat saja sih{/cps}"
            ab "{cps=35}Sekarang kamu cepat menepi dari tempat turunku!{/cps}"
            mc "{cps=35}Baik{/cps}"
            "{cps=35}Aku langsung melepas tanganku dari tangga yang dia naiki{/cps}"
            ab "{cps=35}Hei! Jangan dilepas juga dong!{/cps}"
            mc "{cps=35}Ehehe maaf{/cps}"
            mc "{cps=35}Nah cepat turun, nanti aku lepas nih{/cps}"
            ab "{cps=35}Iya-iya...{/cps}"
            "{cps=35}*sreeet{/cps}"
            ab "{cps=35}Nah, karena bagianku sudah selesai.. sekarang apa?{/cps}"

        "Fokus pada Proposal":
            $ apatis = True
            $ abby_rel -= 2
            "{cps=35}Ah nanti aja deh{/cps}"
            "{cps=35}Toh dia sudah besar juga, ngapain aku membantunya{/cps}"
            "{cps=35}Aku juga masih sangat penasaran dengan isi proposal ini, jadi lebih baik aku membaca dan menelaah ini lebih dalam selagi dia sibuk.{/cps}"
            mc "{cps=35}Semangat ya, [ab]. Aku lagi ada urusan{/cps}"
            mc "{cps=35}Jangan panggil aku kalau ada apa-apa loh{/cps}"
            ab "{cps=35}Cih! Benar-benar tidak punya inisiatif ya...{/cps}"
            "{cps=35}[ab] terus menggerutu sambil memposisikan tangga untuk mencegek rak bagian atas{/cps}"
            "{cps=35}Sementara aku lanjut membaca proposal itu{/cps}"
            mc "{cps=35}Heee pentas seni ya...{/cps}"
            "{cps=35}*Bletak{/cps}"
            mc "{cps=35}Aduh! Kalo ngarahin tangga yang bener dong!{/cps}"
            ab "{cps=35}Ya maaf, aku kan cuma sendiri{/cps}"
            ab "{cps=35}Lagipula kamu nggak membantu{/cps}"
            mc "{cps=35}Mau gimana lagi? Aku aja sibuk{/cps}"
            "{cps=35}Situasi kembali menjadi hening{/cps}"
            "{cps=35}Aku lanjut membaca proposal itu, dan [ab] masih berusaha menempatkan tangga{/cps}"
            ab "{cps=35}Yosh, sepertinya sudah pas{/cps}"
            "Dalam hati [ab]" "{cps=35}Tapi nanti gimana kalau aku jatuh ya...{/cps}"
            ab "{cps=35}Hei, [mc]!{/cps}"
            mc "{cps=35}Apalagi?{/cps}"
            ab "{cps=35}Pegangin tangga, aku mau ngecek atas{/cps}"
            mc "{cps=35}Hah... yaudah{/cps}"
            mc "{cps=35}Nah, cepat kamu naik{/cps}"
            ab "{cps=35}Iya-iya{/cps}"
            ab "{cps=35}Jangan lihat atas loh!{/cps}"
            mc "{cps=35}Ngapain juga aku lihat atas{/cps}"
            "{cps=35}[ab] melanjutkan kegiatannya dalam melakukan audit{/cps}"
            "{cps=35}Disisi lain, aku mencoba membaca sedikit proposal yang ditulis oleh kakakku{/cps}"
            ab "{cps=35}Ok... barang ini juga sudah....{/cps}"
            ab "{cps=35}[mc], sebelah mana lagi yang belum?{/cps}"
            mc "{cps=35}Jangan tanya aku, itu kan pekerjaanmu{/cps}"
            ab "{cps=35}Masa aku harus kerja 2 kali?{/cps}"
            mc "{cps=35}Ya itu mah deritamu{/cps}"
            ab "{cps=35}Hmph, dasar{/cps}"
            "{cps=35}[ab] melakukan audit bagian atas untuk kedua kalinya{/cps}"
            "{cps=35}Wajahnya masih terlihat sedikit kesal karena aku tidak membantu banyak{/cps}"
            "{cps=35}Tapi ya mau gimana lagi, ada yang lebih penting soalnya{/cps}"
            ab "{cps=35}Sip, sudah selesai{/cps}"
            ab "{cps=35}[mc], menyingkirlah{/cps}"
            "{cps=35}Aku langsung menyingkir sesuai arahan dari [ab]{/cps}"
            "{cps=35}Dan tentu saja tanganku tetap memegang tangga itu{/cps}"
            ab "{cps=35}Nah, bagianku juga sudah selesai, sekarang apa?{/cps}"

    mc "{cps=35}Sudah sih... tinggal laporan ke kak [m]{/cps}"
    "{cps=35}[ab] kembali memperhatikan proposal itu{/cps}"
    ab "{cps=35}Kamu nggak bawa itu?{/cps}"
    "{cps=35}[ab] menunjuk ke arah proposal yang aku pegang{/cps}"
    mc "{cps=35}Ini? Tentu saja lah, kan kamu sendiri yang bilang mau membawa ini ke osis{/cps}"
    ab "{cps=35}Memangnya aku bilang begitu?{/cps}"
    mc "{cps=35}Yakali ingatanku cuman 30 menit{/cps}"
    ab "{cps=35}Ternyata ingatanmu bagus juga ya, aku salut kepadamu{/cps}"
    "{cps=35}[ab] mengelus kepalaku dengan lembut{/cps}"
    mc "{cps=35}Ngapain kamu ngelus kepala orang{/cps}"
    ab "{cps=35}Apa salahnya?{/cps}"
    mc "{cps=35}Padahal tadi kamu jaga jarak{/cps}"
    ab "{cps=35}Sudahlah, ayo kita bawa{/cps}"
    ab "{cps=35}Jangan lupa kunci ruangannya{/cps}"
    mc "{cps=35}Baik{/cps}"
    play sound "audio/heavy_door_close.mp3"
    "{cps=35}Aku memutar kunci gudang itu. Suara gerendel besi yang mengunci seolah menandakan berakhirnya petualangan singkat kami di dalam kegelapan yang berdebu.{/cps}"
    ab "{cps=35}Sip, ayo kita berangkat{/cps}"
    "{cps=35}Hari yang melelahkan ini sepertinya akan berakhir{/cps}"
    "{cps=35}Jujur saja, aku tidak menyangka akan seperti ini{/cps}"
    "{cps=35}Bisa bertemu dengan [ab]...{/cps}"
    "{cps=35}Meski menjengkelkan sih karena dia selalu marah{/cps}"
    "{cps=35}Tapi untuk sementara aku merasa tenang{/cps}"
    ab "{cps=35}Nah.. [mc], kamu sudah siap?{/cps}"
    mc "{cps=35}Tentu saja{/cps}"
    "{cps=35}Aku menggenggam buku proposal yang kami temukan di gudang{/cps}"
    "{cps=35}Dengan harapan bahwa aku bisa tahu apa yang terjadi sebenarnya{/cps}"
    "{cps=35}[ab] mengetuk ruang osis itu{/cps}"
    ab "{cps=35}Permisi...{/cps}"
    m "{cps=35}Silahkan masuk, aku sudah menunggu kalian{/cps}"
    ab "{cps=35}Baik{/cps}"
    m "{cps=35}Jadi... bagimana kondisi di sana, lalu hasil dari kegiatan kalian?{/cps}"
    ab "{cps=35}Kondisi ditempat itu penuh dengan debu{/cps}"
    ab "{cps=35}Namun hasilnya seperti yang bisa kamu lihat{/cps}"
    "{cps=35}Hmmmm barangnya masih pada lengkap... baguslah{/cps}"
    ab "{cps=35}Terus [mc] tadi menemukan sesuatu{/cps}"
    m "{cps=35}Heee... apa itu?{/cps}"
    "{cps=35}Aku meletakan buku proposal yang tadi ditemukan{/cps}"
    m "{cps=35}Ini...{/cps}"
    m "{cps=35}Kalian menemukannya dimana?{/cps}"
    mc "{cps=35}Dalam kardus, dan entah kenapa penuh dengan debu{/cps}"
    ab "{cps=35}Terus kenapa proposal itu tidak direalisasikan?{/cps}"
    ab "{cps=35}Mungkin kamu tahu sesuatu{/cps}"
    "{cps=35}Maya terdiam. Jemarinya yang lentik perlahan menyentuh sampul buku proposal yang kusam itu. Keheningan yang menyesakkan tiba-tiba menyelimuti ruangan.{/cps}"
    m "{cps=35}Proposal ini... sudah sangat lama sekali.{/cps}"
    "{cps=35}Maya menatap nama 'Ikazaki [mi]' di sampul itu dengan tatapan yang sulit diartikan. Ada sedikit kilatan di matanya yang tidak pernah aku lihat sebelumnya.{/cps}"
    m "{cps=35}Sudah 10 tahun ya..{/cps}"
    mc "{cps=35}10 tahun?{/cps}"
    "{cps=35}[ab] melirik ke arahku sejenak, wajahnya menunjukkan kebingungan yang sama, sebelum kembali menatap Maya dengan penuh tekad.{/cps}"
    ab "{cps=35}Ketua... Apa Anda tahu sesuatu tentang ini? Maksudku, proposal ini dibuat dengan sangat detail. Rasanya tidak masuk akal jika hanya berakhir jadi sarang debu di rak paling bawah.{/cps}"
    "{cps=35}Maya menarik napas panjang. Dia menutup buku itu dan langsung menatap kami berdua.{/cps}"
    m "{cps=35}Sepuluh tahun yang lalu, sekolah ini tidak senyaman sekarang. Aturannya jauh lebih ketat, dan... ada hal-hal yang tidak boleh dipertanyakan.{/cps}"
    mc "{cps=35}Termasuk alasan kenapa proposal kakakku ditolak?{/cps}"
    m "{cps=35}Bukan ditolak sih... lebih tepatnya ada kejadian yang membuat proposal ini tidak direalisasikan{/cps}"
    ab "{cps=35}Apa kamu tahu?{/cps}"
    m "{cps=35}Kalau pun aku menceritakan ke kalian juga, kalian belum tentu mengerti{/cps}"
    ab "{cps=35}Tidak apa-apa, selagi kami tahu apa yang terjadi pada kakaknya [mc]{/cps}"
    mc "{cps=35}Kenapa kamu sampai sebegitunya demi kakakku?{/cps}"
    ab "{cps=35}Karena kenangan itu penting kan?{/cps}"
    ab "{cps=35}Jadi cepat kamu beritahu kami, [m]{/cps}"
    m "{cps=35}Hah.... pada akhirnya pasti aku akan menceritakan ini{/cps}"
    m "{cps=35}Kejadiannya tepat pada tanggal yang sama dengan hari ini{/cps}"
    m "{cps=35}Namun terjadi pada 10 tahun yang lalu{/cps}"
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
    scene bg_council_room_sunset with dissolve
    play music "audio/tension_ambient.mp3" fadein 2.0
    "{cps=35}Maya-senpai mengakhiri ceritanya. Keheningan di ruang OSIS terasa jauh lebih berat dari sebelumnya. Cahaya senja yang masuk lewat jendela seolah-olah menjadi saksi bisu kenangan itu.{/cps}"
    m "{cps=40}Namun... prediksi kakakmu benar sekaligus salah.{/cps}"
    mc "{cps=40}Apa maksudmu, Senpai? Sekolah ini akhirnya memang menerima laki-laki, kan?{/cps}"
    m "{cps=40}Ya. Tapi kakakmu tidak pernah melihat hari itu tiba.{/cps}"
    m "{cps=40}Tepat seminggu setelah proposal ini diajukan, kakakmu... {w=0.5}dia pergi membawa semua harapan itu bersamanya.{/cps}"
    m "{cps=40}Akibat kejadian itu, konser 'Kitaimirai' bukan hanya dibatalkan, tapi dihentikan selamanya.{/cps}"
    m "{cps=40}Kakakku yang seharusnya melanjutkan peninggalan kakakmu keburu lulus sebelum menjalankan proker ini{/cps}"
    ab "{cps=40}Jadi... itu alasan kenapa proposal ini disembunyikan?{/cps}"
    m "{cps=40}Benar. Dan alasan aku belum menceritakan itu semua... adalah karena aku takut.{/cps}"
    m "{cps=40}Aku takut jika kamu mencoba menghidupkan 'Kitaimirai', kamu akan berakhir sama seperti dia, [mc].{/cps}"
    ab "{cps=35}Tapi kan itu kejadian 10 tahun yang lalu, sekarang sudah berbeda era{/cps}"
    ab "{cps=35}Pasti kita bisa mewujudkannya{/cps}"
    ab "{cps=35}Kamu berpikir hal yang sama kan, [mc]?{/cps}"
    mc "{cps=35}U-uh....{/cps}"
    ab "{cps=35}Kenapa dari nada bicaramu seakan tidak yakin?{/cps}"
    ab "{cps=35}Padahal kamu sudah mengetahui kebenarannya sampai saat ini{/cps}"
    mc "{cps=35}Aku... perlu mencerna semua informasi ini..{/cps}"
    mc "{cps=35}Apakah aku boleh keluar sebentar kak?{/cps}"
    m "{cps=35}Silahkan{/cps}"
    "{cps=35}Aku langsung meninggalkan ruang osis itu{/cps}"
    "{cps=35}Dengan banyak informasi yang aku terima{/cps}"
    "{cps=35}Serta kenyataan bahwa kakakku meninggalkan program yang belum dijalankan{/cps}"
    mc "{cps=35}Andai aku ada otoritas...{/cps}"
    "{cps=35}Entah kenapa aku merasa kalau tidak gabung ke organisasi merupakan pilihan yang sedikit keliru{/cps}"
    "{cps=35}Karena aku tidak memiliki wewenang untuk proker ini{/cps}"
    mc "{cps=35}Cih...{/cps}"
    "{cps=35}Kenapa sih...{/cps}"
    "???" "{cps=35}Kamu nggak apa-apa?{/cps}"
    "{cps=35}Seseorang memanggilku{/cps}"
    "{cps=35}Aku tidak bisa memandang wajahnya{/cps}"
    "{cps=35}Jiwaku sudah terlalu lelah untuk ini semua...{/cps}"
    "???" "{cps=35}Ooi...{/cps}"
    mc "{cps=35}Hmmm..?{/cps}"
    "{cps=35}Aku mendongak pelan.{/cps}"
    "{cps=35}Di depanku berdiri seorang murid perempuan yang bersandar santai di tembok.{/cps}"
    "{cps=35}Wajahnya terlihat tenang, seolah beban dunia yang baru saja aku dengar hanyalah dongeng pengantar tidur baginya.{/cps}"
    "???" "{cps=35}Kamu lemas banget, memangnya ada apa?{/cps}"
    mc "{cps=35}Kamu.... siapa?{/cps}"
    ry "{cps=35}Habuki [ry]. Kelas 2-A.{/cps}"
    mc "{cps=35}Habuki....[ry]?{/cps}"
    ry "{cps=35}Yap{/cps}"
    mc "{cps=35}Kenapa kamu kesini?{/cps}"
    "{cps=35}[ry] melipat tangannya, menatapku dengan sorot mata yang sulit dibaca. Tidak ada rasa kasihan di sana, hanya ketenangan yang ganjil.{/cps}"
    ry "{cps=35}Biasanya jam segini di koridor ini sudah sepi. Tapi aku melihatmu duduk disini{/cps}"
    ry "{cps=35}Jadi daripada kamu tidak ada teman, mending aku temani{/cps}"
    mc "{cps=35}Aku... tidak apa-apa...{/cps}"
    ry "{cps=35}Wajahmu itu tidak bisa berbohong loh{/cps}"
    mc "{cps=35}Itu bukan urusanmu kan?{/cps}"
    ry "{cps=35}Memang sih, tapi kan tetap saja kamu itu perlu seorang pendengar{/cps}"
    mc "{cps=35}Pendengar ya...{/cps}"
    mc "{cps=35}Aku masih ada pendengar kok, namun hanya saja..{/cps}"
    ry "{cps=35}Hanya?{/cps}"
    mc "{cps=35}Aku membuatnya sedikit kecewa{/cps}"
    ry "{cps=35}Membuatnya kecewa, ya?{/cps}"

    "{cps=35}[ry] ikut duduk di lantai koridor, tidak jauh dariku. Gerakannya sangat santai, seolah lantai yang dingin itu adalah sofa yang empuk.{/cps}"

    ry "{cps=35}Kadang orang merasa kecewa bukan karena apa yang kamu lakukan, tapi karena mereka peduli pada apa yang sedang kamu hadapi.{/cps}"

    mc "{cps=35}Dia sudah bertekad untuk membantuku mewujudkan mimpi yang bahkan aku sendiri tidak tahu bisa kulakukan atau tidak.{/cps}"
    ry "{cps=35}Gini ya... kamu kelas 1 kan?{/cps}"
    mc "{cps=35}Iya{/cps}"
    ry "{cps=35}Selagi kamu masih kelas 1, wajar jika kamu masih bimbang{/cps}"
    ry "{cps=35}Namun ingat, usahakan untuk tidak mengecewakan orang lain{/cps}"
    ry "{cps=35}Kalau kamu mau membahas terkait masalahmu yang lain atau terkait ini, kamu bisa mencariku di loteng ketika istirahat{/cps}"
    ry "{cps=35}Namun itu untuk lain hari{/cps}"
    ry "{cps=35}Sampai jumpa{/cps}"
    "{cps=35}Dia bangkit berdiri dan mulai melangkah menjauh. Suara langkah kakinya yang pelan perlahan menghilang di ujung koridor yang gelap.{/cps}"
    mc "{cps=35}Loteng saat istirahat, ya...{/cps}"
    "{cps=35}Oh iya!{/cps}"
    "{cps=35}Aku lupa untuk perkenalan...{/cps}"
    "{cps=35}Tapi lain kali saja deh, kan aku juga besok akan ke loteng{/cps}"
    ab "{cps=35}Hayo! kamu habis ngapain!?{/cps}"
    mc "{cps=35}Hue!? A-[ab]!?{/cps}"
    mc "{cps=35}Sejak kapan kamu disini!?{/cps}"
    ab "{cps=35}Baru keluar dari ruangan sih...{/cps}"
    ab "{cps=35}Kamu kenapa tadi keluar tiba-tiba?{/cps}"
    mc "{cps=35}Umn.... entahlah{/cps}"
    mc "{cps=35}Aku tadi keluar karena belum tahu tujuanku yang sebenarnya{/cps}"
    mc "{cps=35}Namun sekarang aku sudah membulatkan tekad{/cps}"
    mc "{cps=35}Dengan mewujudkan impian kakak{/cps}"
    ab "{cps=35}Nah, gitu dong!{/cps}"
    ab "{cps=35}Jangan kayak gitu lagi ya, [mc]{/cps}"
    ab "{cps=35}Sekarang ayo kembali ke ruang osis, [m] masih menunggumu{/cps}"
    mc "{cps=35}Iya{/cps}"
    ab "{cps=35}Tapi serius ya, [mc]. Kalau kamu butuh waktu buat mikir lagi nanti, bilang saja. Jangan langsung kabur begitu.{/cps}"
    ab "{cps=35}Ketua tadi sampai terlihat sedikit... cemas.{/cps}"
    mc "{cps=35}Maaf. Aku janji tidak akan begitu lagi.{/cps}"
    scene bg_council_room_sunset with dissolve
    play music "audio/office_ambience.mp3" fadein 1.0
    "{cps=35}Begitu pintu terbuka, aku melihat kak [m] masih duduk di posisi yang sama. Dia menatapku, dan kali ini senyumnya terasa lebih tulus, seolah dia sudah tahu apa jawabanku.{/cps}"
    m "{cps=35}Sudah merasa lebih baik, [mc]?{/cps}"
    mc "{cps=35}Sudah, Kak. Maaf tadi aku tiba-tiba keluar.{/cps}"
    m "{cps=35}Jadi... keputusanmu?{/cps}"
    mc "{cps=35}Aku sudah memutuskan. Aku ingin menghidupkan kembali 'Kitaimirai'.{/cps}"
    m "{cps=35}Keputusan yang berani. Tapi seperti yang kubilang, kamu tidak punya otoritas di sini. Dan [ab]... dia punya tugas lain.{/cps}"
    m "{cps=35}Mungkin bisa saja kamu tetap menjalankan ini{/cps}"
    mc "{cps=35}Caranya gimana kak?{/cps}"
    m "{cps=35}Ajak klub sastra{/cps}"
    mc "{cps=35}Sas...tra?{/cps}"
    m "{cps=35}Karena kan kakakmu yang punya ide untuk mengajak mereka, namun seperti yang kamu tahu{/cps}"
    m "{cps=35}Jadi aku minta kamu besok bicara dengan anak dari klub sastra, entah ketua atau anggota{/cps}"
    m "{cps=35}Itu terserah padamu{/cps}"
    "{cps=35}Klub sastra ya...{/cps}"
    "{cps=35}Aku masih sedikit trauma dengan ajakan yang dilakukan secara tiba-tiba oleh kak [f]{/cps}"
    mc "{cps=35}Aku besok akan coba ajak bicara salah satu anggotanya kak{/cps}"
    m "{cps=35}Baiklah, [ab].{/cps}"
    ab "{cps=35}Iya ketua{/cps}"
    m "{cps=35}Kamu temani dia besok, karena kemungkinan besar dia akan diajak masuk sastra lagi{/cps}"
    ab "{cps=35}Kenapa saya ketua? saya kan juga mengurus kedisiplinan siswi disini{/cps}"
    ab "{cps=35}Ga mungkin saya juga ikut mengurus [mc]{/cps}"
    m "{cps=35}Tidak masalah, untuk itu aku sudah mengaturnya{/cps}"
    m "{cps=35}Kamu tidak keberatan kan?{/cps}"
    ab "{cps=35}Tidak sih...{/cps}"
    m "{cps=35}Baiklah, aku anggap setuju{/cps}"
    m "{cps=35}Aku harap kalian berdua bisa bekerja sama kembali dan bisa melancarkan kegiatan ini{/cps}"
    "[mc] & [ab]" "{cps=35}Baik{/cps}"
    "{cps=35}Dengan ini... aku sudah memiliki tujuan{/cps}"
    "{cps=35}Aku tidak akan mengulangi kesalahan yang sama denganmu, kak{/cps}"
    m "{cps=35}Baiklah, pertemuan hari ini cukup sampai di sini. Hari sudah semakin gelap, sebaiknya kalian segera pulang.{/cps}"
    m "{cps=35}Aku tunggu kabar baiknya{/cps}"
    "[mc] & [ab]" "{cps=35}Baik{/cps}"
    "{cps=35}*ceklek{/cps}"
    ab "{cps=35}Besok... jam istirahat pertama, temui aku di depan ruang klub sastra. Jangan telat, atau aku akan menyeretmu ke ruang kedisiplinan.{/cps}"
    mc "{cps=35}Iya, iya. Galak sekali.{/cps}"
    ab "{cps=35}Aku serius! Mengingat pengalamanmu dengan klub itu rasanya... mereka sangat intimidatif{/cps}"
    mc "{cps=35}Iya... tenang saja, [ab]{/cps}"
    mc "{cps=35}Aku tidak akan jatuh ke lubang yang sama kok{/cps}"
    ab "{cps=35}Baiklah kalau begitu.... sampai jumpa{/cps}"
    "{cps=35}[ab] langsung meninggalkanku{/cps}"
    "{cps=35}Namun...{/cps}"
    "{cps=35}dia berhenti sejenak, kemudian berbalik dan menatapku dengan ekspresi yang lebih tenang.{/cps}"
    ab "{cps=35}Tapi... aku senang kamu memutuskan untuk lanjut. Terima kasih sudah tidak menyerah, [mc].{/cps}"
    mc "{cps=35}E-eh? Iya...{/cps}"
    "{cps=35}Dia langsung berjalan mendahuluiku dengan langkah cepat, mungkin untuk menutupi rasa malunya.{/cps}"
    scene bg_school_gate_night with fade 
    play music "audio/walking_home_theme.mp3" fadein 2.0
    "{cps=35}Angin malam berhembus pelan saat aku melangkah keluar dari gerbang sekolah. Suasana sangat sunyi, hanya terdengar suara langkah kakiku.{/cps}"
    "{cps=35}Dari kejauhan terlihat ada yang menunggu diriku{/cps}"
    "{cps=35}Dan sepertinya dia terlihat kesal{/cps}"
    y "{cps=35}Kamu ini... kenapa sampai malam?{/cps}"
    y "{cps=35}Aku kan nungguin kamu daritadi{/cps}"
    mc "{cps=35}Perasaan aku nggak minta untuk tungguin aku deh, [y]{/cps}"
    y "{cps=35}Memang apa salahnya? {/cps}"
    y "{cps=35}Sebagai teman yang baik, aku kan khawatir kamu kenapa-kenapa{/cps}"
    mc "{cps=35}Yang ada aku yang khawatir denganmu{/cps}"
    mc "{cps=35}Sampai-sampai nungguin aku{/cps}"
    mc "{cps=35}Orang tua mu dirumah nyariin nanti{/cps}"
    y "{cps=35}Mereka sedang ada acara diluar kota{/cps}"
    y "{cps=35}Kemungkinan mereka pulang pada akhir semester{/cps}"
    mc "{cps=35}Acara apa sampai selama itu?{/cps}"
    y "{cps=35}Entahlah, aku tidak dijelaskan secara rinci oleh mereka...{/cps}"
    mc "{cps=35}Hee....{/cps}"
    mc "{cps=35}Berarti kamu sendirian di rumah selama itu?{/cps}"
    y "{cps=35}Ya begitulah...{/cps}"
    mc "{cps=35}Terus apa untungnya kamu cerita ke aku?{/cps}"
    y "{cps=35}Ya... nggak ada untungnya sih....{/cps}"
    y "{cps=35}Tapi kan aku cuman cerita{/cps}"
    y "{cps=35}Kenapa sih kamu jadi dingin akhir-akhir ini..{/cps}"
    mc "{cps=35}Nggak juga kok, lagipula kan aku sudah membantumu{/cps}"
    y "{cps=35}Iya sih...{/cps}"
    mc "{cps=35}Yaudah, ayo kita pulang, [y]{/cps}"
    y "{cps=35}Hmm!{/cps}"

    "{cps=35}Kami pun pulang bersama. Tentu saja, hanya dengan berjalan kaki.{/cps}"

    "{cps=35}Lampu jalan yang kekuningan membiaskan bayangan kami yang memanjang di atas trotoar. Suara langkah kaki kami yang beradu dengan kesunyian malam menjadi satu-satunya melodi yang menemani perjalanan ini.{/cps}"

    "{cps=35}[y] sempat terdiam cukup lama, mungkin dia masih memikirkan kata-kataku tadi. Namun, dasarnya dia memang tidak bisa diam, dia akhirnya mulai bertanya soal apa yang terjadi di ruang OSIS.{/cps}"

    "{cps=35}Aku menceritakan sedikit... tentang gudang itu, dan berkas kakakku yang berdebu.{/cps}"

    y "{cps=35}Heee... ada berkas kakakmu disana ya...{/cps}"
    mc "{cps=35}Ya... begitulah.{/cps}"

    "{cps=35}Aku tidak menceritakan soal 'Kitaimirai'. Belum saatnya. Rasanya beban itu terlalu berat jika harus dibagi dengan [y] yang selalu ceria.{/cps}"

    y "{cps=35}Tenang saja [mc], nanti kalau kamu perlu bantuan tinggal beritahu aku ya! Aku kan ahli dalam urusan... hmmm... menghiburmu!{/cps}"

    "{cps=35}Dia tertawa kecil, mencoba mencairkan suasana dingin yang tadi sempat aku buat.{/cps}"

    y "{cps=35}Sampai jumpa besok, [mc]!{/cps}"
    y "{cps=35}Oh iya! Jangan begadang loh! Kalau kamu telat besok, aku nggak mau kasih contekan PR lagi!{/cps}"

    mc "{cps=35}Iya iya, bawel.{/cps}"

    "{cps=35}[y] melambaikan tangannya dengan semangat sebelum akhirnya menghilang di balik gerbang rumahnya.{/cps}"

    "{cps=35}Aku berdiri sejenak di depan pagar rumahku sendiri. Udara malam yang dingin mulai menembus seragamku.{/cps}"

    mc "{cps=35}Akhirnya hari yang panjang ini berakhir...{/cps}"

    "{cps=35}Aku meraba tas selempangku. Di sana, proposal kusam itu masih tersimpan rapi. Sebuah beban masa lalu yang sekarang menjadi tujuanku.{/cps}"

    mc "{cps=35}Semoga besok... aku bisa memberikan jawaban yang lebih baik.{/cps}"

    stop music fadeout 2.0
    scene black with fade
    jump chapter_2_end

