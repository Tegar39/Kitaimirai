label chapter_2_kesempatan:
    scene bg_front_house_morning with fade
    play music "audio/bgm/last meet.mp3" fadein 2.0

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

    play sound "audio/sfx/walk.mp3" # Suara langkah kaki sepatu pantofel yang tegas
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
    play music "audio/bgm/emptyroom.mp3" fadein 2.0 # Musik yang lebih formal/tegang
    
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