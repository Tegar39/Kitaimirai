label chapter_2_kesempatan:
    scene bg_front_house_morning with fade
    play music "audio/bgm/last meet.mp3" fadein 2.0

    "{cps=35}I stepped out past the front gate. As usual, the girl with the glasses was already there, kicking small pebbles with her shoe.{/cps}"

    y "{cps=60}Morning, [mc]! You look... {w=0.1} a little better than yesterday?{/cps}"

    "{cps=35}Yuuka came closer, studying my face carefully. There was a trace of worry she tried to hide behind her smile.{/cps}"

    mc "{cps=40}Morning, Yuuka. Well, at least I managed to sleep last night.{/cps}"

    y "{cps=60}Thank goodness... {w=0.1} I kept thinking about what happened yesterday. Sorry I couldn't go with you to that room.{/cps}"
    y "{cps=60}They didn't do anything to you, right?{/cps}"
    "{cps=35}I shook my head, trying to reassure Yuuka that I was fine.{/cps}"
    mc "{cps=40}No, I'm fine. You don't have to worry.{/cps}"
    "{cps=35}Yuuka let out a relieved breath, and her smile returned.{/cps}"
    y "{cps=60}I'm glad to hear that. I was really worried...{/cps}"
    y "{cps=60}So what did you even do in that room yesterday?{/cps}"
    "{cps=35}I thought hard...{/cps}"
    "{cps=35}Should I tell her?{/cps}"
    y "{cps=60}So what did you even do in that room yesterday?{/cps}"

    menu:
        "Tell her everything":
            $ jujur = True
            $ yuuka_rel += 5
            "{cps=35}I let out a long breath. There was no point hiding this from Yuuka. She'd been by my side for a long time.{/cps}"

            mc "{cps=40}Actually... {w=0.1} Senior Maya brought up my late older sister. Ikazaki [mi]. Turns out she was the Student Council President here ten years ago.{/cps}"

            y "{cps=60}What?! Your sister... {w=0.1} was the Student Council President at this school too?{/cps}"

            mc "{cps=40}Yeah. And Senior Maya seems to respect her a lot. She asked me to choose an organization today, as some kind of 'contribution'... {w=0.1} or maybe so I wouldn't end up like my sister.{/cps}"

            "{cps=35}Yuuka fell silent for a long moment. Her eyes looked glassy behind her glasses, as if she'd only just realized how heavy a burden I'd been carrying alone last night.{/cps}"

            y "{cps=60}So that's why... {w=0.1} I had no idea it went that deep. I'm sorry, [mc]...{/cps}"
            y "{cps=60}So... {w=0.1} what now? Which organization are you going to pick?{/cps}"
            "{cps=35}Should I tell her?{/cps}"

            menu:
                "Give her an answer":
                    $ silent = False
                    if club_choice == "osis":
                        $ yuuka_rel += 5
                        mc "{cps=40}I'm joining the Student Council.{/cps}"
                        y "{cps=60}Oh....{/cps}"
                        "{cps=35}Yuuka smiled happily after hearing my choice.{/cps}"
                        y "{cps=60}I'm so glad, [mc]. We're finally together again.{/cps}"
                        mc "{cps=40}I'm not choosing this just because of you, you know.{/cps}"
                        y "{cps=60}Then why?{/cps}"
                        mc "{cps=40}My dad told me to as well.{/cps}"
                        y "{cps=60}I see....{/cps}"
                        "{cps=35}There's no way I could tell her my real reason...{/cps}"
                        "{cps=35}Because....{/cps}"
                        "{cps=35}There's still one thing stuck in my head...{/cps}"
                        "{cps=35}Why was [m] so insistent that I join an organization?{/cps}"
                        "{cps=35}Is it only because I'm the only guy at this school?{/cps}"
                        y "{cps=60}Hey... {w=0.1} you're zoning out again...{/cps}"
                        "{cps=35}Yuuka muttered with a slightly annoyed look.{/cps}"
                        mc "{cps=30}Sorry, [y]... {w=0.1} I've just got a lot on my mind...{/cps}"
                        y "{cps=60}It's okay, [mc]. You've been through a lot.{/cps}"
                        y "{cps=60}Not everyone could stay strong in your position.{/cps}"


                    elif club_choice == "sastra":
                        $ yuuka_rel -= 3
                        mc "{cps=40}I'm joining the Literature Club.{/cps}"
                        y "{cps=60}...Why that club?{/cps}"
                        y "{cps=60}There's nothing interesting there.{/cps}"
                        mc "{cps=40}I... have personal business there.{/cps}"
                        y "{cps=60}Personal business? What do you mean?{/cps}"
                        mc "{cps=40}Sorry. I can't talk about it right now.{/cps}"
                        "{cps=35}Yuuka stared at me with a look full of suspicion.{/cps}"
                        y "{cps=60}Is it because of those twins?{/cps}"
                        y "{cps=60}You've been watching them since yesterday. Are you still obsessed with them?{/cps}"
                        mc "{cps=40}No... {w=0.1} it's not that.{/cps}"
                        y "{cps=60}If it's not them, then why?{/cps}"
                        mc "{cps=40}I just... {w=0.1} feel like there's something I have to settle there.{/cps}"
                        y "{cps=60}That doesn't answer anything, [mc].{/cps}"
                        "{cps=35}Yuuka looked more and more annoyed.{/cps}"
                        "{cps=35}She stopped walking for a moment. The air between us went cold.{/cps}"
                        mc "{cps=40}Um....{/cps}"
                        "{cps=35}How am I supposed to answer her...{/cps}"
                        y "{cps=60}Whatever. Just do whatever you think is right.{/cps}"
                        "{cps=35}Yuuka started walking again, still looking upset.{/cps}"

                    elif club_choice == None:
                        $ yuuka_rel -= 2
                        mc "{cps=40}I'm not joining any organization.{/cps}"
                        y "{cps=60}What?!{/cps}"
                        "{cps=35}Yuuka was shocked by my answer.{/cps}"
                        y "{cps=60}Why won't you join? Don't you care about your future?{/cps}"
                        mc "{cps=40}It's not that I don't care. I just... {w=0.1} don't feel like I need to right now.{/cps}"
                        y "{cps=60}You could build connections and all that, though.{/cps}"
                        y "{cps=60}I really don't get this decision of yours, [mc].{/cps}"
                        mc "{cps=40}Sorry, Yuuka. I hope you can understand.{/cps}"
                        "{cps=35}Yuuka looked at me with disappointment.{/cps}"
                        y "{cps=60}I don't know... {w=0.1} I just hope you know what you're doing.{/cps}"
                        y "{cps=60}As long as later, if I or the Student Council need help, you can pitch in, okay, [mc]!{/cps}"
                        "{cps=35}I nodded lightly, trying to hide the guilt I felt.{/cps}"
                        mc "{cps=40}Of course, Yuuka.{/cps}"
                        "{cps=35}Yuuka kept walking, her face a little sad.{/cps}"


                "Stay quiet":
                    $ Silent = True
                    $ yuuka_rel -= 3
                    "{cps=35}I went quiet for a moment, not knowing what to say. I felt guilty for hiding something this big from Yuuka.{/cps}"
                    y "{cps=60}Why are you so quiet? Don't you want to talk about it?{/cps}"
                    mc "{cps=40}I don't know... {w=0.1} I just can't say it right now.{/cps}"
                    "{cps=35}Yuuka looked at me with disappointment.{/cps}"
                    y "{cps=60}You're always like this....{/cps}"
                    y "{cps=60}Making me curious every time you open your mouth.{/cps}"
                    mc "{cps=40}It's not like that...{/cps}"
                    mc "{cps=40}You'll find out eventually.{/cps}"
                    y "{cps=60}Hmm... {w=0.1} fine, whatever you say.{/cps}"
                    "{cps=35}Yuuka sighed deeply, then kept walking with a slightly sad look.{/cps}"

        "No need (Tell her only a little)":
            $ jujur = False
            $ yuuka_rel -= 5
            mc "{cps=40}It was just about school rules, Yuuka. She told me I have to decide today or I'll be in trouble.{/cps}"

            y "{cps=60}That's all? But why do you look so pale? You're not lying, are you?{/cps}"

            mc "{cps=40}I'm serious. Drop it. Let's not talk about this anymore.{/cps}"

            "{cps=35}Yuuka watched me with suspicion. She wasn't stupid. She knew something big was being kept from her on purpose.{/cps}"
            y "{cps=60}If you don't want to talk, fine. But I hope you know what you're doing.{/cps}"
            y "{cps=60}And don't end up regretting it later...{/cps}"
            mc "{cps=40}Of course, Yuuka.{/cps}"
            "{cps=35}Yuuka sighed deeply, then kept walking with a slightly sad look.{/cps}"
            "Yuuka (thinking)" "{cps=35}What is actually going on with [mc]? Why does he seem so different today...{/cps}"
            "{cps=35}The space between our steps felt a little wider than usual.{/cps}"

    scene bg_school_gate with fade
    "{cps=35}When we reached the school gate, I saw a few girls walking together.{/cps}"
    if club_choice == "osis":
        "{cps=35}[y] walked ahead of me.{/cps}"
        "{cps=35}Then she turned around.{/cps}"
        y "{cps=60}Oh, right, [mc]. You go to class first.{/cps}"
        y "{cps=60}I'll catch up later — I've got something to do.{/cps}"
        mc "{cps=40}Okay. Be careful.{/cps}"

    elif club_choice == "sastra":
        "{cps=35}[y] walked ahead of me.{/cps}"
        "{cps=35}Without saying a single word.{/cps}"
        "{cps=35}[y] left me behind.{/cps}"
        "{cps=35}I wanted to go after her... {w=0.1} but for some reason my legs refused to move.{/cps}"

    elif club_choice == None:
        "{cps=35}[y] walked ahead of me.{/cps}"
        "{cps=35}Then she turned around.{/cps}"
        y "{cps=60}Oh, right, [mc]. You go to class first.{/cps}"
        y "{cps=60}I'll catch up later — I've got something to do.{/cps}"
        mc "{cps=40}Something to do?{/cps}"
        y "{cps=60}The usual. Student Council stuff.{/cps}"
        mc "{cps=40}Heh. School errand girl.{/cps}"
        y "{cps=60}H-hey! Anyway, you better help me out later!{/cps}"
        "{cps=35}[y] said that in a slightly annoyed tone.{/cps}"
        mc "{cps=40}Ehehe... {w=0.1} yeah, yeah. If I've got free time.{/cps}"
        y "{cps=60}Hmph, you jerk... {w=0.1} I'm going.{/cps}"
        y "{cps=60}See you in class, [mc]!{/cps}"
        mc "{cps=40}Okay. Be careful.{/cps}"

    elif silent:
        "{cps=35}[y] walked ahead of me.{/cps}"
        "{cps=35}Without saying a single word.{/cps}"
        "{cps=35}Why did this get so awkward...{/cps}"
        y "{cps=60}......[mc]{/cps}"
        mc "{cps=40}Yeah?{/cps}"
        y "{cps=60}Just go to class first.{/cps}"
        y "{cps=60}I'll catch up later.{/cps}"
        mc "{cps=40}Why, though?{/cps}"
        y "{cps=60}Is that any of your business?{/cps}"
        "{cps=35}I went quiet for a second.{/cps}"
        "{cps=35}Damn... {w=0.1} the tables turned on me.{/cps}"
        "{cps=30}[y] looked at me with a slightly smug face.{/cps}"
        mc "{cps=40}Oh, so that's how we're playing this...{/cps}"
        y "{cps=60}Huh? What do you mean?{/cps}"
        mc "{cps=40}Ah, nothing. Just talking to myself.{/cps}"
        mc "{cps=40}If you want to go, it's fine. Be careful.{/cps}"
        y "{cps=60}Tch! Jerk.{/cps}"

    elif jujur == False:
        "{cps=35}[y] walked ahead of me.{/cps}"
        "{cps=35}Without saying a single word.{/cps}"
        mc "{cps=40}Um.....{/cps}"
        y "{cps=60}I've got something to do...{/cps}"
        y "{cps=60}See you.{/cps}"
    "{cps=35}[y] left me alone out here on the grounds.{/cps}"

    "{cps=35}I could only watch Yuuka's back as she got farther down the corridor. That uneasy feeling still sat heavy in my chest.{/cps}"

    play sound "audio/sfx/walk.mp3" # Firm formal shoe footsteps
    "{cps=35}*Tap... Tap... Tap...*{/cps}"

    stop music fadeout 1.5
    "{cps=35}Those footsteps stopped right behind me. A cold air suddenly settled on the back of my neck.{/cps}"

    if jujur and club_choice == "sastra":
        m "{cps=40}How pitiful. Abandoned by your childhood friend over one decision form?{/cps}"
    elif jujur and club_choice == "osis":
        m "{cps=40}How pitiful. Abandoned by your childhood friend just because she had somewhere to be.{/cps}"
    elif jujur and club_choice == None:
        m "{cps=40}Hmm... {w=0.1} so you called her a school errand girl, huh...{/cps}"
    elif jujur == False:
        m "{cps=40}How pitiful. Abandoned by your childhood friend just because you wouldn't talk.{/cps}"
    play music "audio/bgm/emptyroom.mp3" fadein 2.0 # More formal/tense music

    show maya s05 with dissolve
    "{cps=35}I turned around. Maya stood there, arms folded, with a look that felt like it could see straight through my thoughts.{/cps}"

    mc "{cps=40}Senior Maya... {w=0.1} How long have you been standing there?{/cps}"
    show maya s03 with dissolve
    m "{cps=40}Long enough to watch a boring morning drama.{/cps}"
    show maya s02 with dissolve
    m "{cps=40}So, Ikazaki [mc]... {w=0.1} Where's your answer? You know I don't like waiting — especially for something I already gave you a whole night to think about.{/cps}"

    "{cps=35}I reached into my uniform pocket and pulled out the form, already a little crumpled.{/cps}"

    # Maya takes the paper
    "{cps=35}Without waiting for me to hand it over, she took the paper from my hand in one quick motion.{/cps}"

    m "{cps=40}Alright. Let's see what you chose.{/cps}"
    if club_choice == "osis":
        "{cps=35}Maya looked at the paper for a moment, then folded it neatly again.{/cps}"
        m "{cps=40}Hmph. A safe choice... {w=0.1} and a boring one. But at least you know where you belong.{/cps}"
        mc "{cps=40}You were the one who told me to.{/cps}"
        m "{cps=40}Since when did I tell you to join the Student Council?{/cps}"
        "{cps=35}Maya raised one eyebrow, staring at me sharply.{/cps}"
        "{cps=35}Ugh— damn... {w=0.1} why is it like this...{/cps}"
        m "{cps=40}Ah, forget it. It doesn't matter.{/cps}"
        m "{cps=40}The point is... {w=0.1} come to my office after the final bell. Don't be late, or I'll take it as you resigning.{/cps}"
        mc "{cps=40}Y-yes, Senior.{/cps}"
        "{cps=35}I nodded quickly, trying to hold down the sudden nervousness in my chest.{/cps}"
        "{cps=35}[m] stared at me coldly for a few seconds before finally turning and walking away.{/cps}"

    elif club_choice == "sastra":
        "{cps=35}Maya raised one eyebrow. There was a flash of disapproval in her eyes.{/cps}"
        m "{cps=40}The Literature Club? Are you sure?{/cps}"
        m "{cps=40}They barely do anything.{/cps}"
        mc "{cps=40}That's exactly why I'm joining.{/cps}"
        mc "{cps=40}Better than picking nothing at all, right?{/cps}"
        m "{cps=40}Tch....{/cps}"
        m "{cps=40}Whatever. I'll process it — but don't expect me to take my eyes off you.{/cps}"
        m "{cps=40}I'll be dropping by that literature club often to make sure you don't do anything stupid.{/cps}"
        mc "{cps=40}Understood, Senior.{/cps}"
        m "{cps=40}Fine. That'll be all for now.{/cps}"
        m "{cps=40}You should get to class. This afternoon, go to the club room.{/cps}"
        mc "{cps=40}Yes, Senior.{/cps}"
        "{cps=35}[m] left after saying that.{/cps}"

    elif club_choice == None:
        "{cps=35}Maya stayed quiet for a long time after reading the blank form (or the one marked with a refusal).{/cps}"
        "{cps=35}Silence. The morning wind blew hard between us.{/cps}"
        m "{cps=40}...{/cps}"
        m "{cps=40}So you're really choosing to stand alone, huh?{/cps}"
        "{cps=35}Suddenly the corner of Maya's mouth lifted a little. Not a mocking smile — something closer to approval.{/cps}"
        m "{cps=40}Interesting... but don't expect your life to stay peaceful after this.{/cps}"
        "{cps=35}Maya looked at me seriously.{/cps}"
        mc "{cps=35}What do you mean, Senior?{/cps}"
        m "{cps=40}Just wait and see.{/cps}"
        "{cps=35}Maya turned and walked away without waiting for my reply.{/cps}"
        "{cps=35}Leaving me curious...{/cps}"

    # --- END OF MEETING ---
    mc "{cps=40}Hah... she really is terrifying.{/cps}"

    "{cps=35}The entrance bell rang. I hurried toward class, realizing my quiet days at this school were truly over.{/cps}"

    scene black with fade
    stop music fadeout 2.0

    if masuk_club and club_choice == "osis":
        jump chapter_2_osis_kesempatan
    elif masuk_club and club_choice == "sastra":
        jump chapter_2_sastra_kesempatan
    else:
        jump chapter_2_solo
