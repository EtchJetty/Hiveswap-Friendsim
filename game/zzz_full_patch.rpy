# COPY PASTE CONTENTS OF ALL 3 PATCH FILES HERE

define config.has_voice = False
define config.auto_voice = "voice/{id}.ogg"
default persistent.quickmenu = True 
define config.developer = True 
# define config.version = "VOICE FANPATCH PRE_0.01"
define config.version = "FANPATCH PRE_0.01"
define gui.history_height = None

default persistent.understand = False 
default persistent.polypareveal = False
default persistent.chahutreveal = False  
default persistent.epilogue = False 

default persistent.volume1 = False
default persistent.volume2 = False
default persistent.volume3 = False
default persistent.volume4 = False
default persistent.volume5 = False
default persistent.volume6 = False
default persistent.volume7 = False
default persistent.volume8 = False
default persistent.volume9 = False
default persistent.volume10 = False
default persistent.volume11 = False
default persistent.volume12 = False
default persistent.volume13 = False
default persistent.volume14 = False
default persistent.volume15 = False
default persistent.volume16 = False
default persistent.volume17 = False
default persistent.volume18r1 = False
default persistent.volume18r2 = False

transform wigglenew:
    
    rotate 0
    ypos -250
    alpha 1.0
    
    on hover:
        alpha 0.8
        linear .1 rotate -2
        linear .1 rotate 0
        linear .1 rotate 2
        linear .1 rotate 0
    on idle: 
        alpha 1.0 

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"

    add gui.main_menu_background# :
        # nearest True 
    
    if config.has_voice:
        imagebutton auto "gui/title_%s.png" action Confirm(_("Unlock {i}all{/i} Hiveswap Friendsim achievements?{size=18}{color=#929292}\n\n(This will unlock all volumes, but will also\nspoil the route endings!){/color}{/size}"), Function(all_ach2)) pos (20, 20) at wigglenew alt _("Hive swap friend sim") hovered PlayCharacterVoice("menunarrator", "voice/hover/Menu_Hiveswap_Friendsim.ogg")
        
        imagebutton auto "gui/start_%s.png" action Start("start") pos (20, 345) at menumove alt _("Start") hovered PlayCharacterVoice("menunarrator", "voice/hover/Menu_Start.ogg")
        imagebutton auto "gui/load_%s.png" action ShowMenu('load') pos (20, 405) at menumove alt _("Load") hovered PlayCharacterVoice("menunarrator", "voice/hover/Menu_Load.ogg")
        imagebutton auto "gui/options_%s.png" action ShowMenu('preferences') pos (20, 465) at menumove alt _("Options") hovered PlayCharacterVoice("menunarrator", "voice/hover/Menu_Options.ogg")
        imagebutton auto "gui/friends_%s.png" action ShowMenu('achievements') pos (20, 525) at menumove alt _("Friends") hovered PlayCharacterVoice("menunarrator", "voice/hover/Menu_Friends.ogg")
        imagebutton auto "gui/credits_%s.png" action ShowMenu('about') pos (20, 585) at menumove alt _("Credits") hovered PlayCharacterVoice("menunarrator", "voice/hover/Menu_Credits.ogg")
        imagebutton auto "gui/exit_%s.png" action Quit(confirm=not main_menu) pos (20, 645) at menumove alt _("Exit") hovered PlayCharacterVoice("menunarrator", "voice/hover/Menu_Exit.ogg")
    else: 
        imagebutton auto "gui/title_%s.png" action Confirm(_("Unlock {i}all{/i} Hiveswap Friendsim achievements?{size=18}{color=#929292}\n\n(This will unlock all volumes, but will also\nspoil the route endings!){/color}{/size}"), Function(all_ach2)) pos (20, 20) at wigglenew alt _("Hive swap friend sim") 
        
        imagebutton auto "gui/start_%s.png" action Start("start") pos (20, 345) at menumove alt _("Start") 
        imagebutton auto "gui/load_%s.png" action ShowMenu('load') pos (20, 405) at menumove alt _("Load") 
        imagebutton auto "gui/options_%s.png" action ShowMenu('preferences') pos (20, 465) at menumove alt _("Options") 
        imagebutton auto "gui/friends_%s.png" action ShowMenu('achievements') pos (20, 525) at menumove alt _("Friends") 
        imagebutton auto "gui/credits_%s.png" action ShowMenu('about') pos (20, 585) at menumove alt _("Credits")  
        imagebutton auto "gui/exit_%s.png" action Quit(confirm=not main_menu) pos (20, 645) at menumove alt _("Exit") 

    textbutton config.version action Confirm(_("Remove ALL achievements?{size=18}{color=#929292}\n\n(This effectively resets your entire save!){/color}{/size}"), Function(ach2_clearall)) pos (975, 675) #style "versionnum"

    on 'show' action Play("music", config.main_menu_music, if_changed=True) 
    on 'replace' action Play("music", config.main_menu_music, if_changed=True)



init python:
    def all_ach2():

        achievement.grant("ACH_ARDATA")
        achievement.grant("ACH_DIEMEN")
        achievement.grant("ACH_AMISIA")
        achievement.grant("ACH_CIRAVA")
        achievement.grant("ACH_SKYLLA")
        achievement.grant("ACH_BRONYA")
        achievement.grant("ACH_VIKARE")
        achievement.grant("ACH_TAGORA")
        achievement.grant("ACH_POLYPA")
        achievement.grant("ACH_ZEBRUH")
        achievement.grant("ACH_ELWURD")
        achievement.grant("ACH_KUPFOL")
        achievement.grant("ACH_REMELE")        
        achievement.grant("ACH_KONYYL")
        achievement.grant("ACH_TYZIAS")
        achievement.grant("ACH_FAYGO")
        achievement.grant("ACH_CHIXIE")
        achievement.grant("ACH_AZDAJA")
        achievement.grant("ACH_CHAHUT")
        achievement.grant("ACH_ZEBEDE")
        achievement.grant("ACH_TEGIRI")
        achievement.grant("ACH_MALLEK")
        achievement.grant("ACH_LYNERA")
        achievement.grant("ACH_GALEKH")
        achievement.grant("ACH_TIRONA")
        achievement.grant("ACH_BOLDIR")
        achievement.grant("ACH_STELSA")
        achievement.grant("ACH_KARAKO")
        achievement.grant("ACH_MARSTI")
        achievement.grant("ACH_CHARUN")
        achievement.grant("ACH_WANSHI")
        achievement.grant("ACH_FOZZER")
        achievement.grant("ACH_ARMPIT")
        achievement.grant("ACH_MARVUS")
        achievement.grant("ACH_DARAYA")
        achievement.grant("ACH_NIHKEE")
        achievement.grant("ACH_VALID")
        achievement.grant("ACH_LANQUE")
        achievement.grant("ACH_SOLEIL")
        achievement.grant("ACH_FINALE")
        achievement.sync()
        persistent.understand = True 
        persistent.polypareveal = True 
        persistent.chahutreveal = True 

    def ach2_clearall():
        achievement.clear_all()
        achievement.sync()
        persistent.understand = False 
        persistent.polypareveal = False
        persistent.chahutreveal = False  

    def mainMenuFix():
        if config.autosave_on_quit:
            renpy.force_autosave()

        layout.yesno_screen(layout.MAIN_MENU, [SetVariable("quick_menu",False), MainMenu(False)])

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if persistent.quickmenu:
        if quick_menu:
            
            imagebutton auto "gui/quick_save_%s.png" action ShowMenu('save') pos (20, 566)
            imagebutton auto "gui/quick_log_%s.png" action ShowMenu('history') pos (20, 640)
            imagebutton auto "gui/quick_skip_%s.png" action Skip() alternate Skip(fast=True, confirm=True) pos (94, 640)
            
            imagebutton auto "gui/quick_menu_%s.png" action MainMenu(confirm=True) pos (1122, 640)
            imagebutton auto "gui/quick_options_%s.png" action ShowMenu('preferences') pos (1196, 640)
            
            if renpy.variant("pc"):
                imagebutton auto "gui/quick_help_%s.png" action ShowMenu('help') pos (1196, 566)


screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("Credits"), scroll="viewport"):

        style_prefix "about"

        vbox:
            
            spacing 14
            
            # text "HIVESWAP: FRIENDSHIP SIMULATOR" color gui.accent_color size 48
            text config.version text_align 0.5 color gui.accent_color size 40
            # text "DIRECTORS" text_align 0.5 color gui.accent_color size 30
            # hbox:
            #     text "MELANIE J ARCHER" text_align 0.0 min_width 440
            #     text "Voice/Project Lead, Casting Director" text_align 1.0 

            hbox:
                text "ETCHJETTY" text_align 0.0 min_width 440
                # text "Technical Director, Casting Director" text_align 1.0 
                text "Fanpatch Programmer" text_align 1.0 


            # text "VOICE ACTORS" text_align 0.5 color gui.accent_color size 30
            # hbox:
            #     text "MELANIE J ARCHER" text_align 0.0 min_width 440
            #     text "MSPAR, Menu Narration" text_align 1.0 

            # hbox:
            #     text "JOSEPHINE KIM" text_align 0.0 min_width 440
            #     text "Ardata" text_align 1.0 

            # hbox:
            #     text "HOPEYMAGE" text_align 0.0 min_width 440
            #     text "Diemen" text_align 1.0 

            # hbox:
            #     text "YEAGRIMBO" text_align 0.0 min_width 440
            #     text "Cirava" text_align 1.0 

            # hbox:
            #     text "VYN VOX" text_align 0.0 min_width 440
            #     text "Amisia" text_align 1.0 

            # hbox:
            #     text "IMMUTABLEMUTIE" text_align 0.0 min_width 440
            #     text "Bronya" text_align 1.0 

            # hbox:
            #     text "DARE0451" text_align 0.0 min_width 440
            #     text "Skylla, Elwurd" text_align 1.0 

            # hbox:
            #     text "MISTERJEROME" text_align 0.0 min_width 440
            #     text "Tagora" text_align 1.0 

            # hbox:
            #     text "TGVELVET" text_align 0.0 min_width 440
            #     text "Galekh" text_align 1.0 

            # hbox:
            #     text "ZAPPYMAKESART" text_align 0.0 min_width 440
            #     text "Vikare" text_align 1.0 

            # hbox:
            #     text "KALKORY" text_align 0.0 min_width 440
            #     text "Polypa" text_align 1.0 

            # hbox:
            #     text "FLINN UVMOCK" text_align 0.0 min_width 440
            #     text "Zebruh" text_align 1.0 

            # hbox:
            #     text "PINKIIPROXII" text_align 0.0 min_width 440
            #     text "Folykl" text_align 1.0 

            # hbox:
            #     text "HISONOKAMI" text_align 0.0 min_width 440
            #     text "Kuprum" text_align 1.0 

            # bar base_bar "#66cc00"

            text "ORIGINAL CREDITS" color gui.accent_color size 40
            text "HIVESWAP: FRIENDSHIP SIMULATOR" color gui.accent_color size 48

            text "DIRECTOR" text_align 0.5 color gui.accent_color size 30
            
            hbox:
                text "ANDREW HUSSIE" text_align 0.0 min_width 440
                text "All Volumes" text_align 1.0 
                
            text "PRODUCERS" text_align 0.5 color gui.accent_color size 30
                
            hbox:
                text "ASH PAULSEN" text_align 0.0 min_width 440
                text "All Volumes" text_align 1.0 
                  
            hbox:
                text "CINDY DOMINGUEZ" text_align 0.0 min_width 440
                text "All Volumes" text_align 1.0
                
            hbox:
                text "COHEN EDENFIELD" text_align 0.0 min_width 440
                text "Volume 1" text_align 1.0 
                
            hbox:
                text "JULIAN DOMINGUEZ" text_align 0.0 min_width 440
                text "Volume 2 Onward" text_align 1.0 
                
            text "WRITERS" text_align 0.5 color gui.accent_color size 30
            
            hbox:
                text "ANDREW HUSSIE" text_align 0.0 min_width 440
                text "Ardata, Diemen" text_align 1.0 
                
            #hbox:
            #    text "" text_align 0.0 min_width 440
            #    text "Cirava" text_align 1.0 
                
            hbox:
                text "AYSHA U. FARAH" text_align 0.0 min_width 440
                text "Amisia, Skylla, Polypa, Folykl & Kuprum" text_align 1.0
                
            hbox:
                text "" text_align 0.0 min_width 440
                text "Konyyl, Chixie, Chahut, Zebede, Mallek" text_align 1.0 

            hbox:
                text "" text_align 0.0 min_width 440
                text "Boldir, Marsti, Epilogue" text_align 1.0 
                
            hbox:
                text "CEE L. KYLE" text_align 0.0 min_width 440
                text "Bronya, Zebruh, Remele, Lynera, Daraya" text_align 1.0 
                
            hbox:
                text "MAGDALENA CLARK" text_align 0.0 min_width 440
                text "Vikare, Elwurd, Zebede" text_align 1.0
                
            hbox:
                text "LALO HUNT" text_align 0.0 min_width 440
                text "Tagora, Tyzias, Galekh, Wanshi, Epilogue" text_align 1.0 

            hbox:
                text "KIERAN MIRANDA" text_align 0.0 min_width 440
                text "Azdaja, Stelsa, Charun, Soleil Twins" text_align 1.0
                
            hbox:
                text "DAVID TURNBULL" text_align 0.0 min_width 440
                text "Tegiri, Tirona, Nihkee" text_align 1.0 
                
            hbox:
                text "GEEZEY" text_align 0.0 min_width 440
                text "Karako, Fozzer" text_align 1.0 
            
            hbox:
                text "V" text_align 0.0 min_width 440
                text "Marvus, Lanque" text_align 1.0 

            text "CHARACTER ARTISTS" text_align 0.5 color gui.accent_color size 30
                
            hbox:
                text "DANNY CRAGG" text_align 0.0 min_width 440
                text "Volumes 1, 2, 6" text_align 1.0 
                
            hbox:
                text "ADRIENNE GARCIA" text_align 0.0 min_width 440
                text "Volumes 3, 5, 8, 10-13, 15, 17" text_align 1.0 
                
            hbox:
                text "GINA CHACÓN" text_align 0.0 min_width 440
                text "Volumes 4, 7, 9" text_align 1.0
                
            hbox:
                text "KIM QUACH" text_align 0.0 min_width 440
                text "Volume 14, 16, 18" text_align 1.0

            text "COLORIST" text_align 0.5 color gui.accent_color size 30
            
            hbox:
                text "SHELBY CRAGG" text_align 0.0 min_width 440
                text "Volumes 1, 2" text_align 1.0

            hbox:
                text "ADRIENNE GARCIA" text_align 0.0 min_width 440
                text "Volume 18" text_align 1.0
                
            text "BACKGROUND ARTISTS" text_align 0.5 color gui.accent_color size 30
                
            hbox: 
                text "DANNY CRAGG" text_align 0.0 min_width 440
                text "Volumes 1, 2, 6" text_align 1.0 
                
            hbox:
                text "ADRIENNE GARCIA" text_align 0.0 min_width 440
                text "Volumes 3, 5, 8" text_align 1.0 
                
            hbox:
                text "GINA CHACÓN" text_align 0.0 min_width 440
                text "Volumes 4, 7, 9" text_align 1.0
            
            hbox:
                text "PHIL GIBSON" text_align 0.0 min_width 440
                text "Volumes 10, 11, 13, 15, 17, 18" text_align 1.0

            hbox:
                text "ANGELA SHAM" text_align 0.0 min_width 440
                text "Volumes 10, 14" text_align 1.0

            hbox:
                text "LELAND GOODMAN" text_align 0.0 min_width 440
                text "Volume 12" text_align 1.0

            hbox:
                text "KIM QUACH" text_align 0.0 min_width 440
                text "Volume 13" text_align 1.0
            
            hbox:
                text "CJ WALKER" text_align 0.0 min_width 440
                text "Volumes 16, 18" text_align 1.0                
            
            text "ENDING ILLUSTRATIONS" text_align 0.5 color gui.accent_color size 30
                
            hbox: 
                text "DANNY CRAGG" text_align 0.0 min_width 440
                text "Volumes 1, 2, 6" text_align 1.0 
                
            hbox:
                text "ADRIENNE GARCIA" text_align 0.0 min_width 440
                text "Volumes 3, 5, 8" text_align 1.0 
                
            hbox:
                text "GINA CHACÓN" text_align 0.0 min_width 440
                text "Volumes 4, 7, 9" text_align 1.0
                
            hbox:
                text "PHIL GIBSON" text_align 0.0 min_width 440
                text "Volumes 10, 11, 13, 15, 17, 18" text_align 1.0
                
            hbox:
                text "LELAND GOODMAN" text_align 0.0 min_width 440
                text "Volume 12" text_align 1.0
                
            hbox:
                text "ANGELA SHAM" text_align 0.0 min_width 440
                text "Volume 14" text_align 1.0

            hbox:
                text "CJ WALKER" text_align 0.0 min_width 440
                text "Volumes 16, 18" text_align 1.0
                
            hbox:
                text "KIM QUACH" text_align 0.0 min_width 440
                text "Volume 17" text_align 1.0

            text "UI DESIGNER" text_align 0.5 color gui.accent_color size 30
            
            hbox:
                text "DAVID TURNBULL" text_align 0.0 min_width 440
                text "All Volumes" text_align 1.0 
                
            text "MUSICIANS" text_align 0.5 color gui.accent_color size 30
                
            hbox:
                text "JAMES ROACH" text_align 0.0 min_width 440
                text "Title Theme and Fanfares" text_align 1.0 
                
            hbox:
                text "" text_align 0.0 min_width 440
                text "Cirava's Theme, {i}\"ＭＯＩＳＴ\"{/i}" text_align 1.0 
                
            hbox:
                text "" text_align 0.0 min_width 440
                text "Amisia's Theme, {i}\"ARTCHOP\"{/i}" text_align 1.0
                
            hbox:
                text "" text_align 0.0 min_width 440
                text "Tagora's Theme, {i}\"Call Me Gor Gor\"{/i}" text_align 1.0 

            hbox:
                text "" text_align 0.0 min_width 440
                text "Folykl & Kuprum's Theme, {i}\">tfw another james roach track\"{/i}" text_align 1.0 
                
            hbox:
                text "" text_align 0.0 min_width 440
                text "Remele's Theme, {i}\"Piwates ',:^]\"{/i}" text_align 1.0
            
            hbox:
                text "" text_align 0.0 min_width 440
                text "Chixie's Theme, {i}\"it be like that sometimes\"{/i}" text_align 1.0
            
            hbox:
                text "" text_align 0.0 min_width 440
                text "Chahut's Theme, {i}\"take me to clown church\"{/i}" text_align 1.0
                
            hbox:
                text "" text_align 0.0 min_width 440
                text "Zebede's Theme, {i}\"beekeeper who? i dont know her.\"{/i}" text_align 1.0
                
            hbox:
                text "" text_align 0.0 min_width 440
                text "Mallek's Theme, {i}\"fortnite funny moments epic fails episode 413\"{/i}" text_align 1.0
                
            hbox:
                text "" text_align 0.0 min_width 440
                text "Stelsa's Theme, {i}\"imagine, if you will, a situation wherein i wrote the bulk of this song at 4 am and then woke up only to discover the monstrosity i had created in my fleeting hubris\"{/i}" text_align 1.0
            
            hbox:
                text "" text_align 0.0 min_width 440
                text "Boldir's Theme, {i}\"Old Secret\"{/i}" text_align 1.0

            hbox:
                text "" text_align 0.0 min_width 440
                text "Karako's Theme, " text_align 1.0
                add "gui/she.png"

            hbox:
                text "" text_align 0.0 min_width 440
                text "Marsti's Theme, {i}\"SERVICE CAR (Neutral Edition)\"{/i}" text_align 1.0

            hbox:
                text "" text_align 0.0 min_width 440
                text "Wanshi's Theme, {i}\"idk man you name it im tired\"{/i}" text_align 1.0
            
            hbox:
                text "" text_align 0.0 min_width 440
                text "Fozzer's Theme, {i}\"GRAVEYARD SHIFT (PLAY THE ROUTE AND THEN TWEET @hamesatron ABOUT HOW GOOD THIS TITLE IS)\"{/i}" text_align 1.0
                
            hbox:
                text "" text_align 0.0 min_width 440
                text "Daraya's Theme, {i}\"trollkind cannot gain anything without first giving something in return. to obtain something of equal value must be lost. that is alchemys first law of equivalent exchange. in those days, we really believed that to be the worlds one, and only, truth.\"{/i}" text_align 1.0
                
            hbox:
                text "" text_align 0.0 min_width 440
                text "Nihkee's Theme, {i}\"lmao i still dont know if its nicky or nike (like the shoe, not like.. the name mike)\"{/i}" text_align 1.0
                
            hbox:
                text "" text_align 0.0 min_width 440
                text "Special Theme, {i}\"END OF FRIENDVANGELION\"{/i}" text_align 1.0
            
            hbox:
                text "" text_align 0.0 min_width 440
                text "Lanque's Theme, {i}\"yall know i just do the music right\"{/i}" text_align 1.0

            hbox:
                text "" text_align 0.0 min_width 440
                text "Lanque's Other Theme, {i}\"VALID END\"{/i}" text_align 1.0

            hbox:
                text "" text_align 0.0 min_width 440
                text "Soleil Twins Theme, {i}\"the final clowntdown\"{/i}" text_align 1.0

            hbox:
                text "" text_align 0.0 min_width 440
                text "Final Route Theme, {i}\"WORST END\"{/i}" text_align 1.0

            hbox:
                text "ALEXANDER ROSETTI" text_align 0.0 min_width 440
                text "Ardata's Theme, {i}\"Breeding Duties\"{/i}" text_align 1.0 
                
            hbox:
                text "" text_align 0.0 min_width 440
                text "Diemen's Theme, {i}\"Moonshine\"{/i}" text_align 1.0 
                
            hbox:
                text "" text_align 0.0 min_width 440
                text "Bronya's Theme, {i}\"Phantasmagoric Waltz\"{/i}" text_align 1.0
                
            hbox:
                text "" text_align 0.0 min_width 440
                text "Vikare's Theme, {i}\"Thip Of The Tongue\"{/i}" text_align 1.0 
                
            hbox:
                text "" text_align 0.0 min_width 440
                text "Polypa's Theme, {i}\"Coursing\"{/i}" text_align 1.0
                
            hbox:
                text "" text_align 0.0 min_width 440
                text "Zebruh's Theme, {i}\"Hollow Suit\"{/i}" text_align 1.0 
            
            hbox:
                text "" text_align 0.0 min_width 440
                text "Tyzias' Theme, {i}\"Single Female Lawyer\"{/i}" text_align 1.0 
                
            hbox:
                text "" text_align 0.0 min_width 440
                text "Azdaja's Theme, {i}\"DaJam\"{/i}" text_align 1.0

            hbox:
                text "" text_align 0.0 min_width 440
                text "Tirona's Theme, {i}\"Carefree Princess Berryboo\"{/i}" text_align 1.0

            hbox:
                text "MAX \"IMBROG\" WRIGHT" text_align 0.0 min_width 440
                text "Skylla's Theme, {i}\"Dapper Dueling\"{/i}" text_align 1.0
            hbox:
                text "YAN \"NUCLEOSE\" RODRIGUEZ" text_align 0.0 min_width 440
                text "Elwurd's Theme, {i}\"Superego\"{/i}" text_align 1.0
                
            hbox:
                text "J. \"CHARREDASPERITY\" STEVEN" text_align 0.0 min_width 440
                text "Konyyl's Theme, {i}\"Olive Scribe\"{/i}" text_align 1.0
                
            hbox:
                text "TOBY FOX" text_align 0.0 min_width 440
                text "Tegiri's Theme, {i}\"ASSAULT\"{/i}" text_align 1.0
                
            hbox:
                text "" text_align 0.0 min_width 440
                text "Lynera's Theme, {i}\"Frostbite\"{/i}" text_align 1.0

            hbox:
                text "" text_align 0.0 min_width 440
                text "Galekh's Theme, {i}\"Snow Pollen\"{/i}" text_align 1.0
                
            hbox:
                text "" text_align 0.0 min_width 440
                text "Charun's Theme, {i}\"Charun's Cave\"{/i}" text_align 1.0 
            
            hbox:
                text "JAMES ROACH AND TOBY FOX" text_align 0.0 min_width 440
                text "Marvus' Theme, {i}\"CLOWNFUCKER\"{/i}" text_align 1.0

            text "GAME DESIGN AND PROGRAMMING" text_align 0.5 color gui.accent_color size 30
                
            hbox:
                text "DAVID TURNBULL" text_align 0.0 min_width 440
                text "Volumes 1-5, 7, 10, 17" text_align 1.0
                
            hbox:
                text "MINT CHIPLEAF" text_align 0.0 min_width 440
                text "Volume 6, 8, 9, 11-18" text_align 1.0 
                
            text "QUALITY ASSURANCE" text_align 0.5 color gui.accent_color size 30
                
            hbox:
                text "SONDRA CRAWFORD" text_align 0.0 min_width 440
                text "Volume 3 Onward" text_align 1.0 
                
            text "\n\n" text_align 1.0 
            
            text "Icons provided by {a=https://www.toicon.com/}to [[icon]{/a} under a {a=https://creativecommons.org/licenses/by/4.0/}Creative Commons Attribution 4.0 International License.{/a}"
            
            text "Bison photograph by {a=https://commons.wikimedia.org/wiki/User:Michael_G%C3%A4bler}Michael Gäbler{/a}, modified under a {a=https://creativecommons.org/licenses/by-sa/3.0/deed.en}Creative Commons Attribution-Share Alike 3.0 Unported license.{/a}"
              
            text "Emoji icons provided by {a=https://www.emojione.com/}EmojiOne™{/a}."
            
            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")

screen preferences():

    tag menu

    use game_menu(_("Options"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "radio"
                    label _("Rollback Side")
                    textbutton _("Disable") action Preference("rollback side", "disable")
                    textbutton _("Left") action Preference("rollback side", "left")
                    textbutton _("Right") action Preference("rollback side", "right")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))
                    
                vbox:
                    style_prefix "radio"
                    label _("Flashing Lights")
                    textbutton _("Enabled") action SetField(persistent, 'flash', True)
                    textbutton _("Disabled") action SetField(persistent, 'flash', False)

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                
            # hbox: 
            #     vbox:
                    # style_prefix "radio"
                    hbox: 
                        vbox:
                            style_prefix "radio"
                            label _("Quick Menu")
                            textbutton _("Enabled") action SetField(persistent, 'quickmenu', True)
                            textbutton _("Disabled") action SetField(persistent, 'quickmenu', False)


                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)
                        hbox:
                            textbutton _("Toggle Specific Voices") action ShowMenu("voices")

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


screen voices():

    tag menu

    use game_menu(_("Options"), scroll="viewport"):

        vbox:
                # style_prefix "radio"
                textbutton _("Back to Options") action ShowMenu("preferences")

        vbox:
            hbox:
                vbox:                 
                    box_wrap True

                    style_prefix "radio"
                    label _("Voice Toggles")
                    textbutton _("Narrator") action ToggleVoiceMute("narrator", True)
                    textbutton _("Ardata") action ToggleVoiceMute("ardata", True)
                    textbutton _("Diemen") action ToggleVoiceMute("diemen", True)
                    textbutton _("Cirava") action ToggleVoiceMute("cirava", True)
                    textbutton _("Amisia") action ToggleVoiceMute("amisia", True)
                    textbutton _("Bronya") action ToggleVoiceMute("bronya", True)
                    textbutton _("Skylla") action ToggleVoiceMute("", True)
                    textbutton _("Tagora") action ToggleVoiceMute("tagora", True)
                    textbutton _("Vikare") action ToggleVoiceMute("vikare", True)
                    textbutton _("Polypa") action ToggleVoiceMute("polypa", True)
                    textbutton _("Zebruh") action ToggleVoiceMute("zebruh", True)
                    textbutton _("Elwurd") action ToggleVoiceMute("elwurd", True)
                    textbutton _("Folykl") action ToggleVoiceMute("folykl", True)
                    textbutton _("Kuprum") action ToggleVoiceMute("kuprum", True)
                vbox:                 
                    box_wrap True

                    style_prefix "radio"
                    label _("")

                    textbutton _("Remele") action ToggleVoiceMute("remele", True)
                    textbutton _("Konyyl") action ToggleVoiceMute("konyyl", True)
                    textbutton _("Chixie") action ToggleVoiceMute("chixie", True)
                    textbutton _("Tyzias") action ToggleVoiceMute("tyzias", True)
                    textbutton _("Chahut") action ToggleVoiceMute("chahut", True)
                    textbutton _("Azdaja") action ToggleVoiceMute("azdaja", True)
                    textbutton _("Zebede") action ToggleVoiceMute("zebede", True)
                    textbutton _("Tegiri") action ToggleVoiceMute("tegiri", True)
                    textbutton _("Mallek") action ToggleVoiceMute("mallek", True)
                    textbutton _("Lynera") action ToggleVoiceMute("lynera", True)
                    textbutton _("Galekh") action ToggleVoiceMute("galekh", True)
                    textbutton _("Tirona") action ToggleVoiceMute("tirona", True)
                    textbutton _("Boldir") action ToggleVoiceMute("boldir", True)
                    textbutton _("Stelsa") action ToggleVoiceMute("stelsa", True)
                vbox:                 
                    box_wrap True

                    style_prefix "radio"
                    label _("")

                    textbutton _("Karako") action ToggleVoiceMute("karako", True)
                    textbutton _("Marsti") action ToggleVoiceMute("marsti", True)
                    textbutton _("Charun") action ToggleVoiceMute("charun", True)
                    textbutton _("Wanshi") action ToggleVoiceMute("wanshi", True)
                    textbutton _("Fozzer") action ToggleVoiceMute("fozzer", True)
                    textbutton _("Marvus") action ToggleVoiceMute("marvus", True)
                    textbutton _("Daraya") action ToggleVoiceMute("daraya", True)
                    textbutton _("Nihkee") action ToggleVoiceMute("nihkee", True)
                    textbutton _("Lanque") action ToggleVoiceMute("lanque", True)
                    textbutton _("Barzum") action ToggleVoiceMute("barzum", True)
                    textbutton _("Baizli") action ToggleVoiceMute("baizli", True)
                    textbutton _("Scratch") action ToggleVoiceMute("scratch", True)
                vbox:                 
                    box_wrap True

                    style_prefix "radio"
                    label _("Minor Characters")
                    textbutton _("Journo") action ToggleVoiceMute("journo", True)
                    textbutton _("Purple") action ToggleVoiceMute("purple", True)
                    textbutton _("Smuggler") action ToggleVoiceMute("smuggler", True)
                    textbutton _("Tagora+Tyzias") action ToggleVoiceMute("tagoratyzias", True)
                    textbutton _("Nufren") action ToggleVoiceMute("nufren", True)
                    textbutton _("Menu Narration") action ToggleVoiceMute("menunarrator", True)



## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    $ who = textProcesserFunction(h.who)
                    label who:
                        style "history_name"
                        substitute False                        

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.what_args:
                            text_color h.what_args["color"]
                        if "outlines" in h.who_args:
                            text_color h.who_args["outlines"][0][1] 
                        text_size 16

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what + "\n":
                    substitute False

                    if "color" in h.what_args:
                            color h.what_args["color"]
                    if "outlines" in h.who_args:
                            color h.who_args["outlines"][0][1] 

        if not _history_list:
            label _("The dialogue history is empty.")

init python:
    def textProcesserFunction(name):
        if name[:3] == ":: ":
            return name [3:-3]
        # elif name[:10] == "trolling: ":
        #     return name [10:]
        return name

## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art", "color", "size", "u", "i" }

image fadedbg:
    Solid("#EFEFEF")
    alpha 0.6

style history_window:
    background "fadedbg"



screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if not main_menu:

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Options") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)


        textbutton _("Befriendments") action ShowMenu("achievements")
        
        textbutton _("Credits") action ShowMenu("about")

        if renpy.variant("pc"):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Help") action ShowMenu("help")

        if not main_menu:

            textbutton _("Main Menu") action MainMenu()
            
        textbutton _("Close Menu"):

            action Return()


init python:
    config.font_replacement_map["courbd.ttf", False, True] = ("courbi.ttf", False, False)
    config.font_replacement_map["Berlin Sans FB Regular.ttf", True, False] = ("Berlin Sans FB Demi Bold.ttf", False, False)
    config.font_replacement_map["Book Antiqua.ttf", False, True] = ("bookantiquaitalic.ttf", False, False)
    config.font_replacement_map["Book Antiqua.ttf", True, True] = ("bookantiquabolditalic.ttf", False, False)
    config.font_replacement_map["Book Antiqua.ttf", True, False] = ("Book Antiqua Bold.ttf", False, False)


# MODIFIED CHARACTER CALLS TIME WOOO YEAH WOO YEAH
define narrator = Character(window_background="gui/textbox_narration.png", what_font='courbd.ttf', what_size=22,  color='#000000', what_color='#000000', voice_tag="narrator", what_ypos=21)
define op = Character(window_background="gui/textbox_blank.png", what_font='courbd.ttf', what_size=28,  color='#FFFFFF', what_color='#FFFFFF', what_xalign=0.5, what_text_align=0.5, voice_tag="narrator")

define a = Character("ARDATA", color='#FFFFFF', image="ardata", window_background=Transform("gui/textbox_cobalt.png",alpha=0.85), who_outlines=[ (4, "#005682") ], voice_tag="ardata")
define die = Character("DIEMEN", color='#FFFFFF', image="diemen", window_background=Transform("gui/textbox_rust.png",alpha=0.85), who_outlines=[ (4, "#a10000") ],voice_tag="diemen")
define dog = Character("DIEMEN", color='#FFFFFF', image="dogless", window_background=Transform("gui/textbox_rust.png",alpha=0.85), who_outlines=[ (4, "#a10000") ],voice_tag="diemen")
define shr = Character("DIEMEN", color='#FFFFFF', image="shirtless", window_background=Transform("gui/textbox_rust.png",alpha=0.85), who_outlines=[ (4, "#a10000") ],voice_tag="diemen")

define pur = Character("PURPLE", color='#FFFFFF', window_background=Transform("gui/textbox_purple.png",alpha=0.85), who_outlines=[ (4, "#2b0057") ],voice_tag="purple")


define ami = Character("AMISIA", color='#FFFFFF', image="amisia", window_background=Transform("gui/textbox_blue.png",alpha=0.85), who_outlines=[ (4, "#000056") ],voice_tag="amisia")
define cir = Character("CIRAVA", color='#FFFFFF', image="cirava", window_background=Transform("gui/textbox_gold.png",alpha=0.85), who_outlines=[ (4, "#a1a100") ],voice_tag="cirava")

define sky = Character("SKYLLA", color='#FFFFFF', image="skylla", window_background=Transform("gui/textbox_bronze.png",alpha=0.85), who_outlines=[ (4, "#bb6405") ],voice_tag="skylla")
define bro = Character("BRONYA", color='#FFFFFF', image="bronya", window_background=Transform("gui/textbox_jade.png",alpha=0.85), who_outlines=[ (4, "#0aa85b") ],voice_tag="bronya")



init python:

    def tspk(what, amt=0, stmt=None, voice_tag="tagora", **kwargs):
        
        tag(what, **kwargs)
        
        global amount
        amount = amt
        
        global bill
        
        portion = int(amt/5)
        
        if amt != 0:
            
            renpy.hide_screen("moneyadd", layer=None)
            renpy.show_screen("moneyadd", moneyadded=amt)
        
        if stmt != None:
            
            renpy.hide_screen("moneystmt", layer=None)
            renpy.show_screen("moneystmt", statement=stmt)
        
        i = 5
        
        while i > 0:
            
            renpy.pause(0.02)
            
            bill += portion
            amt -= portion
            
            i -= 1

define vik = Character("VIKARE", color='#FFFFFF', image="vikare", window_background=Transform("gui/textbox_bronze.png",alpha=0.85), who_outlines=[ (4, "#bb6405") ],voice_tag="vikare")
define vik2 = Character("VIKARE", color='#FFFFFF', image="vikare", window_background="gui/textbox_bronze2.png",  window_align = (0.5, 1.19), who_outlines=[ (3, "#bb6405") ], 
                                                                    who_size=30, who_pos=(40, 34), what_size=22, what_xmaximum=685, what_xpos=300, what_color="ebc8a6",voice_tag="vikare")
define tag = Character("TAGORA", color='#FFFFFF', image="tagora", window_background=Transform("gui/textbox_teal.png",alpha=0.85), who_outlines=[ (4, "#008282") ], voice_tag="tagora")


define pol = Character("POLYPA", color='#FFFFFF', image="polypa", window_background=Transform("gui/textbox_olive.png",alpha=0.85), who_outlines=[ (4, "#416600") ],voice_tag="polypa")
define polh = Character("??????", color='#FFFFFF', image="polypa hoodie", window_background=Transform("gui/textbox_gold.png",alpha=0.85), who_outlines=[ (4, "#a1a100") ],voice_tag="polypa")
define zeb = Character("ZEBRUH", color='#FFFFFF', image="zebruh", window_background=Transform("gui/textbox_blue.png",alpha=0.85), who_outlines=[ (4, "#000056") ],voice_tag="zebruh")

define el = Character("ELWURD", color='#FFFFFF', image="elwurd", window_background=Transform("gui/textbox_cobalt.png",alpha=0.85), who_outlines=[ (4, "#005682") ],voice_tag="elwurd")
define fol = Character("FOLYKL", color='#FFFFFF', image="fk", window_background=Transform("gui/textbox_gold.png",alpha=0.85), who_outlines=[ (4, "#a1a100") ],voice_tag="folykl")
define kup = Character("KUPRUM", color='#FFFFFF', image="fk", window_background=Transform("gui/textbox_gold.png",alpha=0.85), who_outlines=[ (4, "#a1a100") ],voice_tag="kuprum")
define fol1 = Character("FOLYKL", color='#FFFFFF', image="folykl", window_background=Transform("gui/textbox_gold.png",alpha=0.85), who_outlines=[ (4, "#a1a100") ],voice_tag="folykl")
define kup1 = Character("KUPRUM", color='#FFFFFF', image="kuprum", window_background=Transform("gui/textbox_gold.png",alpha=0.85), who_outlines=[ (4, "#a1a100") ],voice_tag="folykl")

define bro = Character("BRONYA", color='#FFFFFF', image="bronya", window_background=Transform("gui/textbox_jade.png",alpha=0.85), who_outlines=[ (4, "#0aa85b") ],voice_tag="bronya")
define kon = Character("KONYYL", color='#FFFFFF', image="konyyl", window_background=Transform("gui/textbox_olive.png",alpha=0.85), who_outlines=[ (4, "#416600") ],voice_tag="konyyl")
define rem = Character("REMELE", color='#FFFFFF', image="remele", window_background=Transform("gui/textbox_cobalt.png",alpha=0.85), who_outlines=[ (4, "#005682") ],voice_tag="remele")
define sky = Character("SKYLLA", color='#FFFFFF', image="skylla", window_background=Transform("gui/textbox_bronze.png",alpha=0.85), who_outlines=[ (4, "#bb6405") ],voice_tag="skylla")
define jou = Character("JOURNO", color='#FFFFFF', window_background=Transform("gui/textbox_teal.png",alpha=0.85), who_outlines=[ (4, "#008282") ],voice_tag="journo")

define smug = Character("SMUGGLER", color='#FFFFFF', window_background=Transform("gui/textbox_cobalt.png",alpha=0.85), who_outlines=[ (4, "#005682") ],voice_tag="smuggler")
define tyz = Character("TYZIAS", color='#FFFFFF', image="tyzias", window_background=Transform("gui/textbox_teal.png",alpha=0.85), who_outlines=[ (4, "#008282") ],voice_tag="tyzias")
define tag = Character("TAGORA", color='#FFFFFF', image="tagora", window_background=Transform("gui/textbox_teal.png",alpha=0.85), who_outlines=[ (4, "#008282") ],voice_tag="tagora")
define doublet = Character("TAGORA & TYZIAS", color='#FFFFFF', image="", window_background=Transform("gui/textbox_teal2.png",alpha=0.85), who_outlines=[ (4, "#008282") ],voice_tag="tagoratyzias")
define chix = Character("CHIXIE", color='#FFFFFF', image="chixie", window_background=Transform("gui/textbox_bronze.png",alpha=0.85), who_outlines=[ (4, "#bb6405") ],voice_tag="chixie")
define zeb = Character("ZEBRUH", color='#FFFFFF', image="zebruh", window_background=Transform("gui/textbox_blue.png",alpha=0.85), who_outlines=[ (4, "#000056") ],voice_tag="zebruh")
define az = Character("AZDAJA", color='#FFFFFF', image="azdaja", window_background=Transform("gui/textbox_gold.png",alpha=0.85), who_outlines=[ (4, "#a1a100") ],voice_tag="azdaja")
define kon = Character("KONYYL", color='#FFFFFF', image="konyyl", window_background=Transform("gui/textbox_olive.png",alpha=0.85), who_outlines=[ (4, "#416600") ],voice_tag="konyyl")
define cha = Character("CHAHUT", color='#FFFFFF', image="chahut", window_background=Transform("gui/textbox_purple.png",alpha=0.85), who_outlines=[ (4, "#2b0057") ],voice_tag="chahut")
define ami = Character("AMISIA", color='#FFFFFF', image="amisia", window_background=Transform("gui/textbox_blue.png",alpha=0.85), who_outlines=[ (4, "#000056") ],voice_tag="amisia")

define teg = Character("TEGIRI", color='#FFFFFF', image="tegiri", window_background=Transform("gui/textbox_teal.png",alpha=0.85), who_outlines=[ (4, "#008282") ],voice_tag="tegiri")
define zebe = Character("ZEBEDE", color='#FFFFFF', image="zebede", window_background=Transform("gui/textbox_gold.png",alpha=0.85), who_outlines=[ (4, "#a1a100") ],voice_tag="zebede")
define czebe = Character("zZz_BUZZZING_zZz", color='#FFFFFF', image="zebede", who_size=32, window_background=Transform("gui/textbox_gold.png",alpha=0.85), who_outlines=[ (4, "#a1a100") ],voice_tag="zebede")
define gcir = Character("", color='#FFFFFF', image="cirava", window_background=Transform("gui/textbox_gold.png",alpha=0.85), who_outlines=[ (4, "#a1a100") ],voice_tag="cirava")
define gzebe = Character("", color='#FFFFFF', image="zebede", window_background=Transform("gui/textbox_gold.png",alpha=0.85), who_outlines=[ (4, "#a1a100") ],voice_tag="zebede")
define pol = Character("POLYPA", color='#FFFFFF', image="polypa", window_background=Transform("gui/textbox_olive.png",alpha=0.85), who_outlines=[ (4, "#416600") ],voice_tag="polypa")

define mal = Character("MALLEK", color='#FFFFFF', image="mallek", window_background=Transform("gui/textbox_cobalt.png",alpha=0.85), who_outlines=[ (4, "#005682") ],voice_tag="mallek")
define lyn = Character("LYNERA", color='#FFFFFF', image="lynera", window_background=Transform("gui/textbox_jade.png",alpha=0.85), who_outlines=[ (4, "#0aa85b") ],voice_tag="lynera")
define dog = Character("DIEMEN", color='#FFFFFF', image="dogless resized", window_background=Transform("gui/textbox_rust.png",alpha=0.85), who_outlines=[ (4, "#a10000") ],voice_tag="diemen")
define nuf = Character("NUFREN", color='#FFFFFF', image="nufren", window_background=Transform("gui/textbox_teal.png",alpha=0.85), who_outlines=[ (4, "#008282") ],voice_tag="nufren")


define gal = Character("GALEKH", color='#FFFFFF', image="galekh", window_background=Transform("gui/textbox_blue.png",alpha=0.85), who_outlines=[ (4, "#000056") ],voice_tag="galekh")
define mal = Character("MALLEK", color='#FFFFFF', image="mallek", window_background=Transform("gui/textbox_cobalt.png",alpha=0.85), who_outlines=[ (4, "#005682") ],voice_tag="mallek")
define tir = Character("TIRONA", color='#FFFFFF', image="tirona", window_background=Transform("gui/textbox_teal.png",alpha=0.85), who_outlines=[ (4, "#008282") ],voice_tag="tirona")
define teg = Character("TEGIRI", color='#FFFFFF', image="tegiri", window_background=Transform("gui/textbox_teal.png",alpha=0.85), who_outlines=[ (4, "#008282") ],voice_tag="tegiri")
define tyz = Character("TYZIAS", color='#FFFFFF', image="tyzias", window_background=Transform("gui/textbox_teal.png",alpha=0.85), who_outlines=[ (4, "#008282") ],voice_tag="tyzias")
define gtag = Character("", color='#FFFFFF', image="tagora", window_background=Transform("gui/textbox_teal.png",alpha=0.85), who_outlines=[ (4, "#008282") ],voice_tag="tagora")
define gmal = Character("", color='#FFFFFF', image="mallek", window_background=Transform("gui/textbox_cobalt.png",alpha=0.85), who_outlines=[ (4, "#005682") ],voice_tag="mallek")

define bol = Character("BOLDIR", color='#FFFFFF', image="boldir", window_background=Transform("gui/textbox_olive.png",alpha=0.85), who_outlines=[ (4, "#416600") ],voice_tag="boldir")
define boltxt = Character("???", color='#FFFFFF', image="boldir", window_background=Transform("gui/textbox_olive.png",alpha=0.85), who_outlines=[ (4, "#416600") ],voice_tag="boldir")
define stel = Character("STELSA", color='#FFFFFF', image="stelsa", window_background=Transform("gui/textbox_teal.png",alpha=0.85), who_outlines=[ (4, "#008282") ],voice_tag="stelsa")
# define a = Character("ARDATA", color='#FFFFFF', image="ardata", window_background=Transform("gui/textbox_cobalt.png",alpha=0.85), who_outlines=[ (4, "#005682") ],voice_tag="ardata")


define kar = Character("KARAKO", color='#FFFFFF', image="karako", window_background=Transform("gui/textbox_purple.png",alpha=0.85), who_outlines=[ (4, "#2b0057") ],voice_tag="karako")
define mar = Character("MARSTI", color='#FFFFFF', image="marsti", window_background=Transform("gui/textbox_rust.png",alpha=0.85), who_outlines=[ (4, "#a20000") ],voice_tag="marsti")
define fol = Character("FOLYKL", color='#FFFFFF', image="folykl", window_background=Transform("gui/textbox_gold.png",alpha=0.85), who_outlines=[ (4, "#a1a100") ],voice_tag="folykl")

define char = Character("CHARUN", color='#FFFFFF', image="charun", window_background=Transform("gui/textbox_olive.png",alpha=0.85), who_outlines=[ (4, "#416600") ],voice_tag="charun")
define wan = Character("WANSHI", color='#FFFFFF', image="wanshi", window_background=Transform("gui/textbox_jade.png",alpha=0.85), who_outlines=[ (4, "#0aa85b") ],voice_tag="wanshi")
define az = Character("AZDAJA", color='#FFFFFF', image="azdaja", window_background=Transform("gui/textbox_gold.png",alpha=0.85), who_outlines=[ (4, "#a1a100") ],voice_tag="azdaja")
define kon = Character("KONYYL", color='#FFFFFF', image="konyyl", window_background=Transform("gui/textbox_olive.png",alpha=0.85), who_outlines=[ (4, "#416600") ],voice_tag="konyyl")
define lyn = Character("LYNERA", color='#FFFFFF', image="lynera", window_background=Transform("gui/textbox_jade.png",alpha=0.85), who_outlines=[ (4, "#0aa85b") ],voice_tag="lynera")
define poltxt = Character("POLYPA", color='#FFFFFF', image="", window_background=Transform("gui/textbox_olive.png",alpha=0.85), who_outlines=[ (4, "#416600") ],voice_tag="polypa")
define tegtxt = Character("TEGIRI", color='#FFFFFF', image="", window_background=Transform("gui/textbox_teal.png",alpha=0.85), who_outlines=[ (4, "#008282") ],voice_tag="tegiri")

define foz = Character("FOZZER", color='#FFFFFF', image="fozzer", window_background=Transform("gui/textbox_rust.png",alpha=0.85), who_outlines=[ (4, "#a20000") ],voice_tag="fozzer")
define marv = Character("MARVUS", color='#FFFFFF', image="marvus", window_background=Transform("gui/textbox_purple.png",alpha=0.85), who_outlines=[ (4, "#2b0057") ],voice_tag="marvus")
define zeb = Character("ZEBRUH", color='#FFFFFF', image="zebruh", window_background=Transform("gui/textbox_blue.png",alpha=0.85), who_outlines=[ (4, "#000056") ],voice_tag="zebruh")

define dar = Character("DARAYA", color='#FFFFFF', image="daraya", window_background=Transform("gui/textbox_jade.png",alpha=0.85), who_outlines=[ (4, "#0aa85b") ],voice_tag="daraya")
define cha = Character("CHAHUT", color='#FFFFFF', image="chahut", window_background=Transform("gui/textbox_purple.png",alpha=0.85), who_outlines=[ (4, "#2b0057") ],voice_tag="chahut")
define ni = Character("NIHKEE", color='#FFFFFF', image="nihkee", window_background=Transform("gui/textbox_blue.png",alpha=0.85), who_outlines=[ (4, "#000056") ],voice_tag="nihkee")
define ami = Character("AMISIA", color='#FFFFFF', image="amisia", window_background=Transform("gui/textbox_blue.png",alpha=0.85), who_outlines=[ (4, "#000056") ],voice_tag="amisia")
define stel = Character("STELSA", color='#FFFFFF', image="stelsa", window_background=Transform("gui/textbox_teal.png",alpha=0.85), who_outlines=[ (4, "#008282") ],voice_tag="stelsa")
define tyz = Character("TYZIAS", color='#FFFFFF', image="tyzias", window_background=Transform("gui/textbox_teal.png",alpha=0.85), who_outlines=[ (4, "#008282") ],voice_tag="tyzias")
define gmal = Character("", color='#FFFFFF', image="mallek", window_background=Transform("gui/textbox_cobalt.png",alpha=0.85), who_outlines=[ (4, "#005682") ],voice_tag="mallek")
define pol = Character("POLYPA", color='#FFFFFF', image="polypa", window_background=Transform("gui/textbox_olive.png",alpha=0.85), who_outlines=[ (4, "#416600") ],voice_tag="polypa")
define vis = Character(window_background="gui/textbox_blank.png", what_font='courbd.ttf', what_size=28,  color='#FFFFFF', what_color='#FFFFFF', what_outlines=[ (4, "#000000") ], what_xalign=0.5, what_text_align=0.5,voice_tag="narrator")


define lan = Character("LANQUE", color='#FFFFFF', image="lanque", window_background=Transform("gui/textbox_jade.png",alpha=0.85), who_outlines=[ (4, "#0aa85b") ],voice_tag="lanque")
define lanpoem = Character("LANQUE", kind=lan, what_layout='nobreak',voice_tag="lanque")
define lyn = Character("LYNERA", color='#FFFFFF', image="lynera", window_background=Transform("gui/textbox_jade.png",alpha=0.85), who_outlines=[ (4, "#0aa85b") ],voice_tag="lynera")
# define a = Character("ARDATA", color='#FFFFFF', image="ardata", window_background=Transform("gui/textbox_cobalt.png",alpha=0.85), who_outlines=[ (4, "#005682") ],voice_tag="ardata")
define dogboy = Character("DIEMEN", color='#FFFFFF', image="dogboy", window_background=Transform("gui/textbox_rust.png",alpha=0.85), who_outlines=[ (4, "#a10000") ],voice_tag="diemen")
define bro = Character("BRONYA", color='#FFFFFF', image="bronya", window_background=Transform("gui/textbox_jade.png",alpha=0.85), who_outlines=[ (4, "#0aa85b") ],voice_tag="bronya")
define el = Character("ELWURD", color='#FFFFFF', image="elwurd", window_background=Transform("gui/textbox_cobalt.png",alpha=0.85), who_outlines=[ (4, "#005682") ],voice_tag="elwurd")

define barz = Character("BARZUM", color='#FFFFFF', image="barzum", window_background=Transform("gui/textbox_purple.png",alpha=0.85), who_outlines=[ (4, "#2b0057") ], who_xpos=0, who_xalign=0.0, what_xalign=0.0, what_xpos=300,voice_tag="barzum")
define baiz = Character("BAIZLI", color='#FFFFFF', image="baizli", window_background=Transform("gui/textbox_purple.png",alpha=0.85), who_outlines=[ (4, "#2b0057") ], who_xpos=770, who_xalign=1.0, what_xalign=1.0, what_xpos=980,voice_tag="baizli")
define bOtH = Character("BARZUM", kind=barz, what_xalign=0.5, what_text_align=0.5, what_xpos=0.5)
define BoTh = Character("BAIZLI", kind=baiz, what_xalign=0.5, what_text_align=0.5, what_xpos=0.5)

define who = Character("???", kind=barz)
define WHO = Character("???", kind=baiz)
define wHo = Character("???", kind=barz, what_xalign=0.5, what_text_align=0.5, what_xpos=0.5)
define WhO = Character("???", kind=baiz, what_xalign=0.5, what_text_align=0.5, what_xpos=0.5)

define o = Character("", color='#FFFFFF', what_color="#000000", image="scratch", window_background=Transform("gui/textbox_purple.png",matrixcolor=InvertMatrix(1.0)),voice_tag="scratch")
define s = Character("", kind=narrator, color='#FFFFFF', what_color="#FFFFFF", image="scratch", window_background=Transform("gui/textbox_narration.png",matrixcolor=InvertMatrix(1.0)),voice_tag="scratch")

define reader = Character("", color='#FFFFFF', image="reader", window_background=Transform("gui/textbox_purple.png",matrixcolor=SaturationMatrix(0.0)), voice_tag="narrator")

define friendship = Character("", kind=op, what_outlines=[ (4, "#000000")], what_xalign=0.5, what_text_align=0.5,voice_tag="narrator")


screen vol_select():
    
    use game_menu(_("Friend Select"), scroll="viewport"):

        vbox:

                xpos 60
                ymaximum 5
                
                if renpy.variant("android") or renpy.variant("ios"):
                    spacing 60
                else:
                    spacing 20
                    
                # Volume one is always available.
        
                if config.has_voice:
                    imagebutton auto "gui/volumeone_%s.png" action Jump("volumeone") alt _("Volume One: Of Bloodthirst And Bratwurst") sensitive volume1 hovered PlayCharacterVoice("menunarrator", "voice/hover/Volume_One_Title.ogg")
                    
                    if volume2:
                        
                        imagebutton auto "gui/volumetwo_%s.png" action Jump("volumetwo") alt _("Volume Two: Of Aesthetics, Crimson And Otherwise") sensitive volume2 hovered PlayCharacterVoice("menunarrator", "voice/hover/Volume_Two_Title.ogg")
                        
                    if volume3:
                        
                        imagebutton auto "gui/volumethree_%s.png" action Jump("volumethree") alt "Volume Three: Of Ladies Gray And Lusii White" sensitive volume3 hovered PlayCharacterVoice("menunarrator", "voice/hover/Volume_Three_Title.ogg")
                        
                    if volume4:
                        
                        imagebutton auto "gui/volumefour_%s.png" action Jump("volumefour") alt "Volume Four: Of Wright And Wronged" sensitive volume4 hovered PlayCharacterVoice("menunarrator", "voice/hover/Volume_Four_Title.ogg")
                        
                    # Volume 5 image changes if the player has actually started Polypa's route. If they haven't, she's in disguise. Makes for a fun little surprise.
                    # FOR THOSE OF YOU WHO DON'T IMMEDIATELY GO DIGGING INTO THE FILES, THAT IS
                        
                    if volume5:
                        
                        if persistent.polypareveal:
                        
                            imagebutton auto "gui/volumefive2_%s.png" action Jump("volumefive") alt "Volume Five: Of Affection, Unwanted Or Untrue" sensitive volume5 hovered PlayCharacterVoice("menunarrator", "voice/hover/Volume_Five_Title.ogg")
                        
                        else:
                        
                            imagebutton auto "gui/volumefive1_%s.png" action Jump("volumefive") alt "Volume Five: Of Affection, Unwanted Or Untrue" sensitive volume5 hovered PlayCharacterVoice("menunarrator", "voice/hover/Volume_Five_Title.ogg")
                    
                    if volume6:

                        imagebutton auto "gui/volumesix_%s.png" action Jump("volumesix") alt "Volume Six: Of Text And Envy, Green" sensitive volume6 hovered PlayCharacterVoice("menunarrator", "voice/hover/Volume_Six_Title.ogg")
    
                    if volume7:

                        imagebutton auto "gui/volumeseven_%s.png" action Jump("volumeseven") alt "Volume Seven: Of Business, Flagrantly Illegal" sensitive volume7 hovered PlayCharacterVoice("menunarrator", "voice/hover/Volume_Seven_Title.ogg")
                        
                    if volume8:
                        imagebutton auto "gui/volumeeight_%s.png" action Jump("volumeeight") alt "Volume Eight: Of Stresses, Song And Otherwise" sensitive volume8 hovered PlayCharacterVoice("menunarrator", "voice/hover/Volume_Eight_Title.ogg")
                    
                    # Guess who's doing this shit again LOL
                    
                    if volume9:
                        
                        if persistent.chahutreveal:
                        
                            imagebutton auto "gui/volumenine2_%s.png" action Jump("volumenine") alt "Volume Nine: Of Gazes Cool And Tempers Hot" sensitive volume9 hovered PlayCharacterVoice("menunarrator", "voice/hover/Volume_Nine_Title.ogg")
                        
                        else:
                        
                            imagebutton auto "gui/volumenine1_%s.png" action Jump("volumenine") alt "Volume Nine: Of Gazes Cool And Tempers Hot" sensitive volume9 hovered PlayCharacterVoice("menunarrator", "voice/hover/Volume_Nine_Title.ogg")
                            
                    if volume10:
                        imagebutton auto "gui/volumeten_%s.png" action Jump("volumeten") alt "Volume Ten: Of Faraway Lands And Nearby Friends" sensitive volume10 hovered PlayCharacterVoice("menunarrator", "voice/hover/Volume_Ten_Title.ogg")

                    if volume11:
                        imagebutton auto "gui/volumeeleven_%s.png" action Jump("volumeeleven") alt "Volume Eleven: Of Pals And Promises, Made And Broken" sensitive volume11 hovered PlayCharacterVoice("menunarrator", "voice/hover/Volume_Eleven_Title.ogg")
                        
                    if volume12:
                        imagebutton auto "gui/volumetwelve_%s.png" action Jump("volumetwelve") alt "Volume Twelve: Of Know-Nothings And Know-It-Alls" sensitive volume12 hovered PlayCharacterVoice("menunarrator", "voice/hover/Volume_Twelve_Title.ogg")

                    if volume13:
                        imagebutton auto "gui/volumethirteen_%s.png" action Jump("volumethirteen") alt "Volume Thirteen: Of Fate, Fashion, And Fortune" sensitive volume13 hovered PlayCharacterVoice("menunarrator", "voice/hover/Volume_Thirteen_Title.ogg")

                    if volume14:
                        imagebutton auto "gui/volumefourteen_%s.png" action Jump("volumefourteen") alt "Volume Fourteen: Of Cleanliness And Clownliness" sensitive volume14 hovered PlayCharacterVoice("menunarrator", "voice/hover/Volume_Fourteen_Title.ogg")

                    if volume15:
                        imagebutton auto "gui/volumefifteen_%s.png" action Jump("volumefifteen") alt "Volume Fifteen: Of Creatives, Conventional Or Otherwise" sensitive volume15 hovered PlayCharacterVoice("menunarrator", "voice/hover/Volume_Fifteen_Title.ogg")

                    if volume16:
                        imagebutton auto "gui/volumesixteen_%s.png" action Jump("volumesixteen") alt "Volume Sixteen: Of Cult- And Capt-ivation" sensitive volume16 hovered PlayCharacterVoice("menunarrator", "voice/hover/Volume_Sixteen_Title.ogg")

                    if volume17:
                        imagebutton auto "gui/volumeseventeen_%s.png" action Jump("volumeseventeen") alt "Volume Seventeen: Of Teen And Tech, Acerbic" sensitive volume17 hovered PlayCharacterVoice("menunarrator", "voice/hover/Volume_Seventeen_Title.ogg")

                    if volume18:
                        imagebutton auto "gui/volumeeighteen_%s.png" action Jump("volumeeighteen") alt "Volume Eighteen" sensitive volume18 hovered PlayCharacterVoice("menunarrator", "voice/hover/Volume_Eighteen_Title.ogg")
                    
                    if persistent.epilogue == volume18 == True:
                        imagebutton auto "gui/epilogue_%s.png" action Jump("epilogue_fix") alt "Epilogue: Of Hosts, Excellent" sensitive persistent.epilogue hovered PlayCharacterVoice("menunarrator", "voice/hover/Volume_Epilogue_Title.ogg")
                else: 

                    imagebutton auto "gui/volumeone_%s.png" action Jump("volumeone") alt "Volume One: Of Bloodthirst And Bratwurst" sensitive volume1
                    
                    if volume2:
                        
                        imagebutton auto "gui/volumetwo_%s.png" action Jump("volumetwo") alt "Volume Two: Of Aesthetics, Crimson And Otherwise" sensitive volume2
                        
                    if volume3:
                        
                        imagebutton auto "gui/volumethree_%s.png" action Jump("volumethree") alt "Volume Three: Of Ladies Gray And Lusii White" sensitive volume3
                        
                    if volume4:
                        
                        imagebutton auto "gui/volumefour_%s.png" action Jump("volumefour") alt "Volume Four: Of Wright And Wronged" sensitive volume4
                        
                    # Volume 5 image changes if the player has actually started Polypa's route. If they haven't, she's in disguise. Makes for a fun little surprise.
                    # FOR THOSE OF YOU WHO DON'T IMMEDIATELY GO DIGGING INTO THE FILES, THAT IS
                        
                    if volume5:
                        
                        if persistent.polypareveal:
                        
                            imagebutton auto "gui/volumefive2_%s.png" action Jump("volumefive") alt "Volume Five: Of Affection, Unwanted Or Untrue" sensitive volume5
                        
                        else:
                        
                            imagebutton auto "gui/volumefive1_%s.png" action Jump("volumefive") alt "Volume Five: Of Affection, Unwanted Or Untrue" sensitive volume5
                    
                    if volume6:

                        imagebutton auto "gui/volumesix_%s.png" action Jump("volumesix") alt "Volume Six: Of Text And Envy, Green" sensitive volume6
    
                    if volume7:

                        imagebutton auto "gui/volumeseven_%s.png" action Jump("volumeseven") alt "Volume Seven: Of Business, Flagrantly Illegal" sensitive volume7
                        
                    if volume8:
                        imagebutton auto "gui/volumeeight_%s.png" action Jump("volumeeight") alt "Volume Eight: Of Stresses, Song And Otherwise" sensitive volume8
                    
                    # Guess who's doing this shit again LOL
                    
                    if volume9:
                        
                        if persistent.chahutreveal:
                        
                            imagebutton auto "gui/volumenine2_%s.png" action Jump("volumenine") alt "Volume Nine: Of Gazes Cool And Tempers Hot" sensitive volume9
                        
                        else:
                        
                            imagebutton auto "gui/volumenine1_%s.png" action Jump("volumenine") alt "Volume Nine: Of Gazes Cool And Tempers Hot" sensitive volume9
                            
                    if volume10:
                        imagebutton auto "gui/volumeten_%s.png" action Jump("volumeten") alt "Volume Ten: Of Faraway Lands And Nearby Friends" sensitive volume10

                    if volume11:
                        imagebutton auto "gui/volumeeleven_%s.png" action Jump("volumeeleven") alt "Volume Eleven: Of Pals And Promises, Made And Broken" sensitive volume11
                        
                    if volume12:
                        imagebutton auto "gui/volumetwelve_%s.png" action Jump("volumetwelve") alt "Volume Twelve: Of Know-Nothings And Know-It-Alls" sensitive volume12

                    if volume13:
                        imagebutton auto "gui/volumethirteen_%s.png" action Jump("volumethirteen") alt "Volume Thirteen: Of Fate, Fashion, And Fortune" sensitive volume13

                    if volume14:
                        imagebutton auto "gui/volumefourteen_%s.png" action Jump("volumefourteen") alt "Volume Fourteen: Of Cleanliness And Clownliness" sensitive volume14

                    if volume15:
                        imagebutton auto "gui/volumefifteen_%s.png" action Jump("volumefifteen") alt "Volume Fifteen: Of Creatives, Conventional Or Otherwise" sensitive volume15

                    if volume16:
                        imagebutton auto "gui/volumesixteen_%s.png" action Jump("volumesixteen") alt "Volume Sixteen: Of Cult- And Capt-ivation" sensitive volume16

                    if volume17:
                        imagebutton auto "gui/volumeseventeen_%s.png" action Jump("volumeseventeen") alt "Volume Seventeen: Of Teen And Tech, Acerbic" sensitive volume17

                    if volume18:
                        imagebutton auto "gui/volumeeighteen_%s.png" action Jump("volumeeighteen") alt "Volume Eighteen" sensitive volume18
                    
                    if persistent.epilogue == volume18 == True:
                        imagebutton auto "gui/epilogue_%s.png" action Jump("epilogue_fix") alt "Epilogue: Of Hosts, Excellent" sensitive persistent.epilogue




                # For locked volumes: We show the DLC screen, which takes two arguments after the default arguments.
                # First argument is a link to the Steam page where users can purchase the DLC.
                # Second argument is the name of the In-app Purchase registered in the init step of script.rpy. We need that for mobile purchases.
                # It'll pretty much always just be "VolumeX"
                
                if not volume2:
                    
                    imagebutton auto "gui/volumetwo_locked%s.png" action Show("dlc", None, "https://store.steampowered.com/app/848020/Hiveswap_Friendsim__Volume_Two/", "Volume2") alt "Volume Two: Of Aesthetics, Crimson And Otherwise"
                    
                if not volume3:
                    
                    imagebutton auto "gui/volumethree_locked%s.png" action Show("dlc", None, "https://store.steampowered.com/app/859130/Hiveswap_Friendsim__Volume_Three/", "Volume3") alt "Volume Three: Of Ladies Gray And Lusii White"
                
                if not volume4:
                    
                    imagebutton auto "gui/volumefour_locked%s.png" action Show("dlc", None, "https://store.steampowered.com/app/864980/Hiveswap_Friendsim__Volume_Four/", "Volume4") alt "Volume Four: Of Wright And Wronged"
                    
                if not volume5:
                    
                    imagebutton auto "gui/volumefive1_locked%s.png" action Show("dlc", None, "https://store.steampowered.com/app/878920/Hiveswap_Friendsim__Volume_Five/", "Volume5") alt "Volume Five: Of Affection, Unwanted Or Untrue"
                    
                if not volume6:

                    imagebutton auto "gui/volumesix_locked%s.png" action Show("dlc", None, "https://store.steampowered.com/app/886930/Hiveswap_Friendsim__Volume_Six/", "Volume6") alt "Volume Six: Of Text And Envy, Green" 
                
                if not volume7:
                    
                    imagebutton auto "gui/volumeseven_locked%s.png" action Show("dlc", None, "https://store.steampowered.com/app/892400/Hiveswap_Friendsim__Volume_Seven/", "Volume7") alt "Volume Seven: Of Business, Flagrantly Illegal" 
                    
                if not volume8:
                    imagebutton auto "gui/volumeeight_locked%s.png" action Show("dlc", None, "https://store.steampowered.com/app/904580/Hiveswap_Friendsim__Volume_Eight/", "Volume8") alt "Volume Eight: Of Stresses, Song And Otherwise" 

                if not volume9:
                    imagebutton auto "gui/volumenine1_locked%s.png" action Show("dlc", None, "https://store.steampowered.com/app/913810/Hiveswap_Friendsim__Volume_Nine/", "Volume9") alt "Volume Nine: Of Gazes Cool And Tempers Hot" 
   
                if not volume10:
                    imagebutton auto "gui/volumeten_locked%s.png" action Show("dlc", None, "https://store.steampowered.com/app/922430/Hiveswap_Friendsim__Volume_Ten/", "Volume10") alt "Volume Ten: Of Faraway Lands And Nearby Pals" 
    
                if not volume11:
                    imagebutton auto "gui/volumeeleven_locked%s.png" action Show("dlc", None, "https://store.steampowered.com/app/931920/Hiveswap_Friendsim__Volume_Eleven/", "Volume11") alt "Volume Eleven: Of Pals And Promises, Made And Broken" 

                if not volume12:
                    imagebutton auto "gui/volumetwelve_locked%s.png" action Show("dlc", None, "https://store.steampowered.com/app/941220/Hiveswap_Friendsim__Volume_Twelve/", "Volume12") alt "Volume Twelve: Of Know-Nothings And Know-It-Alls" 
                    
                if not volume13:
                    imagebutton auto "gui/volumethirteen_locked%s.png" action Show("dlc", None, "https://store.steampowered.com/app/950820/Hiveswap_Friendsim__Volume_Thirteen/", "Volume13") alt "Volume Thirteen: Of Fate, Fashion, And Fortune" 

                if not volume14:
                    imagebutton auto "gui/volumefourteen_locked%s.png" action Show("dlc", None, "https://store.steampowered.com/app/959160/Hiveswap_Friendsim__Volume_Fourteen/", "Volume14") alt "Volume Fourteen: Of Cleanliness And Clownliness" 

                if not volume15:
                    imagebutton auto "gui/volumefifteen_locked%s.png" action Show("dlc", None, "https://store.steampowered.com/app/966360/Hiveswap_Friendsim__Volume_Fifteen/", "Volume15") alt "Volume Fifteen: Of Creatives, Conventional Or Otherwise" 

                if not volume16:
                    imagebutton auto "gui/volumesixteen_locked%s.png" action Show("dlc", None, "https://store.steampowered.com/app/975560/Hiveswap_Friendsim__Volume_Sixteen/", "Volume16") alt "Volume Sixteen: Of Cult- And Capt-ivation" 

                if not volume17:
                    imagebutton auto "gui/volumeseventeen_locked%s.png" action Show("dlc", None, "https://store.steampowered.com/app/986510/Hiveswap_Friendsim__Volume_Seventeen/", "Volume17") alt "Volume Seventeen: Of Teen And Tech, Acerbic" 

                if not volume18:
                    imagebutton auto "gui/volumeeighteen_locked%s.png" action Show("dlc", None, "https://store.steampowered.com/app/998810/Hiveswap_Friendsim__Volume_Eighteen/", "Volume18") alt "Volume Eighteen" 

                # After all the current volumes, add a symbol to indicate more are coming soon.
                if not persistent.epilogue:
                    imagebutton auto "gui/upcominglocked_%s.png" action None alt "????????" 
                    
    # if renpy.variant("android") or renpy.variant("ios"):
        
    #     text "Additional content will be released on a regular basis. \nTap on a locked volume to purchase it!" xpos 460 ypos 585 text_align 0.5
        
    # else:
        
    #     text "Additional content will be released on a regular basis. \n{a=http://store.steampowered.com/dlc/833040}Purchase more volumes here!{/a}" xpos 460 ypos 585 text_align 0.5
        


style game_menu_outer_frame:
    bottom_padding 30





init -5 python:
    renpy.music.register_channel('wave', "sound")
    renpy.music.register_channel('earlyend', "music")
    renpy.music.register_channel('music2', "music")

    def mirrorvision(vision, **kwargs):
        i=0
        while i < 12:
            time.sleep(0.1)
            visiontitle = "mirrorvision" + i
            
            
            
            renpy.show("mirrorvisionbase")
            i += 1
        return


## Troll Select screen ~CHANGES EACH VOLUME~ ############################################################
##
## Choose ya troll! Very simple. Just two image buttons.

screen troll_select1():
    if config.has_voice:
        imagebutton auto "images/charselect/ardata_button_%s.png" action Jump("ardata") pos (0, 0) alt _("Ardata Carmia") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/ardata.ogg")
        imagebutton auto "images/charselect/diemen_button_%s.png" action Jump("diemen") pos (640, 0) alt _("Diemen Xicali") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/diemen.ogg")
    else: 
        imagebutton auto "images/charselect/ardata_button_%s.png" action Jump("ardata") pos (0, 0) alt _("Ardata Carmia")
        imagebutton auto "images/charselect/diemen_button_%s.png" action Jump("diemen") pos (640, 0) alt _("Diemen Xicali")

    
screen troll_select2():
    if config.has_voice:
        imagebutton auto "volumes/volume2/images/charselect/amisia_button_%s.png" action Jump("amisia") pos (0, 0) alt _("Amisia Erdehn") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/amisia.ogg")
        imagebutton auto "volumes/volume2/images/charselect/cirava_button_%s.png" action Jump("cirava") pos (640, 0) alt _("Cirava Hermod") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/cirava.ogg")
    else: 
        imagebutton auto "volumes/volume2/images/charselect/amisia_button_%s.png" action Jump("amisia") pos (0, 0) alt _("Amisia Erdehn")
        imagebutton auto "volumes/volume2/images/charselect/cirava_button_%s.png" action Jump("cirava") pos (640, 0) alt _("Cirava Hermod")
    
screen troll_select3():
    if config.has_voice:
        imagebutton auto "volumes/volume3/images/charselect/skylla_button_%s.png" action Jump("skylla") pos (0, 0) alt _("Skylla Koriga") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/skylla.ogg")
        imagebutton auto "volumes/volume3/images/charselect/bronya_button_%s.png" action Jump("bronya") pos (640, 0) alt _("Bronya Ursama") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/bronya.ogg")
    else: 
        imagebutton auto "volumes/volume3/images/charselect/skylla_button_%s.png" action Jump("skylla") pos (0, 0) alt _("Skylla Koriga")
        imagebutton auto "volumes/volume3/images/charselect/bronya_button_%s.png" action Jump("bronya") pos (640, 0) alt _("Bronya Ursama")
    
screen troll_select4():
    if config.has_voice:
        imagebutton auto "volumes/volume4/images/charselect/tagora_button_%s.png" action Jump("tagora") pos (0, 0) alt _("Tagora Gorjek") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/tagora.ogg")
        imagebutton auto "volumes/volume4/images/charselect/vikare_button_%s.png" action Jump("vikare") pos (640, 0) alt _("Vikare Ratite") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/vikare.ogg")
    else: 
        imagebutton auto "volumes/volume4/images/charselect/tagora_button_%s.png" action Jump("tagora") pos (0, 0) alt _("Tagora Gorjek") 
        imagebutton auto "volumes/volume4/images/charselect/vikare_button_%s.png" action Jump("vikare") pos (640, 0) alt _("Vikare Ratite")
    
screen troll_select5():
    
    if config.has_voice:

        if persistent.polypareveal:
            imagebutton auto "volumes/volume5/images/charselect/polypa2_button_%s.png" action Jump("polypa") pos (0, 0) alt _("Polypa Goezee") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/polypa.ogg")
        else:
            imagebutton auto "volumes/volume5/images/charselect/polypa1_button_%s.png" action Jump("polypa") pos (0, 0) alt _("??????")   
            
        imagebutton auto "volumes/volume5/images/charselect/zebruh_button_%s.png" action Jump("zebruh") pos (640, 0) alt _("Zebruh Codakk") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/zebruh.ogg")
    else:
        if persistent.polypareveal:
            imagebutton auto "volumes/volume5/images/charselect/polypa2_button_%s.png" action Jump("polypa") pos (0, 0) alt _("Polypa Goezee")
        else:
            imagebutton auto "volumes/volume5/images/charselect/polypa1_button_%s.png" action Jump("polypa") pos (0, 0) alt _("??????")   
            
        imagebutton auto "volumes/volume5/images/charselect/zebruh_button_%s.png" action Jump("zebruh") pos (640, 0) alt _("Zebruh Codakk")


screen troll_select6():
    if config.has_voice:
        imagebutton auto "volumes/volume6/images/charselect/elwurd_button_%s.png" action Jump("elwurd") pos (0, 0) alt _("Elwurd") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/elwurd.ogg")
        imagebutton auto "volumes/volume6/images/charselect/kuprum_button_%s.png" action Jump("folyklkuprum") pos (640, 0) alt _("Kuprum and Folykl") # hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/kuprumfolykl.ogg")
    else:
        imagebutton auto "volumes/volume6/images/charselect/elwurd_button_%s.png" action Jump("elwurd") pos (0, 0) alt _("Elwurd")
        imagebutton auto "volumes/volume6/images/charselect/kuprum_button_%s.png" action Jump("folyklkuprum") pos (640, 0) alt _("Kuprum and Folykl") 

    
screen troll_select7():
    if config.has_voice:
        imagebutton auto "volumes/volume7/images/charselect/remele_button_%s.png" action Jump("remele") pos (0, 0) alt _("Remele Namaaq") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/remele.ogg")
        imagebutton auto "volumes/volume7/images/charselect/konyyl_button_%s.png" action Jump("konyyl") pos (640, 0) alt _("Konyyl Okimaw") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/konyyl.ogg")
    else:
        imagebutton auto "volumes/volume7/images/charselect/remele_button_%s.png" action Jump("remele") pos (0, 0) alt _("Remele Namaaq") 
        imagebutton auto "volumes/volume7/images/charselect/konyyl_button_%s.png" action Jump("konyyl") pos (640, 0) alt _("Konyyl Okimaw") 

screen troll_select8():
    if config.has_voice:
        imagebutton auto "volumes/volume8/images/charselect/tyzias_button_%s.png" action Jump("tyzias") pos (0, 0) alt _("Tyzias Entykk") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/tyzias.ogg")
        imagebutton auto "volumes/volume8/images/charselect/chixie_button_%s.png" action Jump("chixie") pos (640, 0) alt _("Chixie Roixmr") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/chixie.ogg")
    else:
        imagebutton auto "volumes/volume8/images/charselect/tyzias_button_%s.png" action Jump("tyzias") pos (0, 0) alt _("Tyzias Entykk") 
        imagebutton auto "volumes/volume8/images/charselect/chixie_button_%s.png" action Jump("chixie") pos (640, 0) alt _("Chixie Roixmr") 

screen troll_select9():
    if config.has_voice:
        imagebutton auto "volumes/volume9/images/charselect/azdaja_button_%s.png" action Jump("azdaja") pos (0, 0) alt _("Azdaja Knelax") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/azdaja.ogg")
        
        if persistent.chahutreveal:
            imagebutton auto "volumes/volume9/images/charselect/chahut_button_%s.png" action Jump("chahut") pos (640, 0) alt _("Chahut Maenad") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/chahut.ogg") 
        else:
            imagebutton auto "volumes/volume9/images/charselect/amisia2_button_%s.png" action Jump("chahut") pos (640, 0) alt _("Amisia Erdehn?") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/amisia.ogg") 
    else:
        imagebutton auto "volumes/volume9/images/charselect/azdaja_button_%s.png" action Jump("azdaja") pos (0, 0) alt _("Azdaja Knelax")
        
        if persistent.chahutreveal:
            imagebutton auto "volumes/volume9/images/charselect/chahut_button_%s.png" action Jump("chahut") pos (640, 0) alt _("Chahut Maenad")
        else:
            imagebutton auto "volumes/volume9/images/charselect/amisia2_button_%s.png" action Jump("chahut") pos (640, 0) alt _("Amisia Erdehn?")

        
screen troll_select10():
    if config.has_voice:
        imagebutton auto "volumes/volume10/images/charselect/zebede_button_%s.png" action Jump("zebede") pos (0, 0) alt _("Zebede Tongva") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/zebede.ogg")
        imagebutton auto "volumes/volume10/images/charselect/tegiri_button_%s.png" action Jump("tegiri") pos (640, 0) alt _("Tegiri Kalbur") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/tegiri.ogg")
    else: 
        imagebutton auto "volumes/volume10/images/charselect/zebede_button_%s.png" action Jump("zebede") pos (0, 0) alt _("Zebede Tongva")
        imagebutton auto "volumes/volume10/images/charselect/tegiri_button_%s.png" action Jump("tegiri") pos (640, 0) alt _("Tegiri Kalbur") 

screen troll_select11():
    if config.has_voice:
        imagebutton auto "volumes/volume11/images/charselect/mallek_button_%s.png" action Jump("mallek") pos (0, 0) alt _("Mallek Adalov") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/mallek.ogg")
        imagebutton auto "volumes/volume11/images/charselect/lynera_button_%s.png" action Jump("lynera") pos (640, 0) alt _("Lynera Skalbi") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/lynera.ogg")
    else: 
        imagebutton auto "volumes/volume11/images/charselect/mallek_button_%s.png" action Jump("mallek") pos (0, 0) alt _("Mallek Adalov") 
        imagebutton auto "volumes/volume11/images/charselect/lynera_button_%s.png" action Jump("lynera") pos (640, 0) alt _("Lynera Skalbi") 
    
screen troll_select12():
    if config.has_voice:
        imagebutton auto "volumes/volume12/images/charselect/galekh_button_%s.png" action Jump("galekh") pos (0, 0) alt _("Galekh Xigisi") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/galekh.ogg")
        imagebutton auto "volumes/volume12/images/charselect/tirona_button_%s.png" action Jump("tirona") pos (640, 0) alt _("Tirona Kasund") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/tirona.ogg")
    else: 
        imagebutton auto "volumes/volume12/images/charselect/galekh_button_%s.png" action Jump("galekh") pos (0, 0) alt _("Galekh Xigisi")
        imagebutton auto "volumes/volume12/images/charselect/tirona_button_%s.png" action Jump("tirona") pos (640, 0) alt _("Tirona Kasund")

screen troll_select13():
    if config.has_voice:
        imagebutton auto "volumes/volume13/images/charselect/boldir_button_%s.png" action Jump("boldir") pos (0, 0) alt _("Boldir Lamati") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/boldir.ogg")
        imagebutton auto "volumes/volume13/images/charselect/stelsa_button_%s.png" action Jump("stelsa") pos (640, 0) alt _("Stelsa Sezyat") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/stelsa.ogg")
    else: 
        imagebutton auto "volumes/volume13/images/charselect/boldir_button_%s.png" action Jump("boldir") pos (0, 0) alt _("Boldir Lamati")
        imagebutton auto "volumes/volume13/images/charselect/stelsa_button_%s.png" action Jump("stelsa") pos (640, 0) alt _("Stelsa Sezyat") 


screen troll_select14():
    if config.has_voice:
        imagebutton auto "volumes/volume14/images/charselect/marsti_button_%s.png" action Jump("marsti") pos (0, 0) alt _("Marsti Houtek") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/marsti.ogg")
        imagebutton auto "volumes/volume14/images/charselect/karako_button_%s.png" action Jump("karako") pos (640, 0) alt _("Karako Pierot") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/karako.ogg")
    else: 
        imagebutton auto "volumes/volume14/images/charselect/marsti_button_%s.png" action Jump("marsti") pos (0, 0) alt _("Marsti Houtek")
        imagebutton auto "volumes/volume14/images/charselect/karako_button_%s.png" action Jump("karako") pos (640, 0) alt _("Karako Pierot")


screen troll_select15():
    if config.has_voice:
        imagebutton auto "volumes/volume15/images/charselect/charun_button_%s.png" action Jump("charun") pos (0, 0) alt _("Charun Krojib") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/charun.ogg")
        imagebutton auto "volumes/volume15/images/charselect/wanshi_button_%s.png" action Jump("wanshi") pos (640, 0) alt _("Wanshi Adyata") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/wanshi.ogg")
    else:
        imagebutton auto "volumes/volume15/images/charselect/charun_button_%s.png" action Jump("charun") pos (0, 0) alt _("Charun Krojib")
        imagebutton auto "volumes/volume15/images/charselect/wanshi_button_%s.png" action Jump("wanshi") pos (640, 0) alt _("Wanshi Adyata") 

screen troll_select16():
    if config.has_voice:
        imagebutton auto "volumes/volume16/images/charselect/fozzer_button_%s.png" action Jump("fozzer") pos (0, 0) alt _("Fozzer Velyes") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/fozzer.ogg")
        imagebutton auto "volumes/volume16/images/charselect/marvus_button_%s.png" action Jump("marvus") pos (640, 0) alt _("Marvus Xoloto") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/marvus.ogg")
    else:
        imagebutton auto "volumes/volume16/images/charselect/fozzer_button_%s.png" action Jump("fozzer") pos (0, 0) alt _("Fozzer Velyes")
        imagebutton auto "volumes/volume16/images/charselect/marvus_button_%s.png" action Jump("marvus") pos (640, 0) alt _("Marvus Xoloto")

screen troll_select17():
    if config.has_voice:
        imagebutton auto "volumes/volume17/images/charselect/daraya_button_%s.png" action Jump("daraya") pos (0, 0) alt _("Daraya Jonjet") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/daraya.ogg")
        imagebutton auto "volumes/volume17/images/charselect/nihkee_button_%s.png" action Jump("nihkee_fix") pos (640, 0) alt _("Nihkee Moolah") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/nihkee.ogg")
    else:
        imagebutton auto "volumes/volume17/images/charselect/daraya_button_%s.png" action Jump("daraya") pos (0, 0) alt _("Daraya Jonjet") 
        imagebutton auto "volumes/volume17/images/charselect/nihkee_button_%s.png" action Jump("nihkee_fix") pos (640, 0) alt _("Nihkee Moolah")

screen troll_select18():
    if config.has_voice:
        imagebutton auto "volumes/volume18/images/charselect/lanque_button_%s.png" action Jump("lanque") pos (0, 0) alt _("Lanque Bombyx") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/lanque.ogg")
        imagebutton auto "volumes/volume18/images/charselect/soleil_button_%s.png" action Jump("soleil") pos (640, 0) alt _("Barzum & Bazili") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/baizbaz.ogg")
    else:
        imagebutton auto "volumes/volume18/images/charselect/lanque_button_%s.png" action Jump("lanque") pos (0, 0) alt _("Lanque Bombyx") 
        imagebutton auto "volumes/volume18/images/charselect/soleil_button_%s.png" action Jump("soleil") pos (640, 0) alt _("Barzum & Bazili") 

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items: 
            if renpy.loadable("voice/hover/"+ i.caption + ".ogg") and config.has_voice:
                textbutton i.caption action i.action hovered PlayCharacterVoice("narrator", "voice/hover/"+ i.caption + ".ogg")
            else: 
                textbutton i.caption action i.action                

label nihkee_fix:
    $ noquickmenuvar = False 
    $ renpy.block_rollback()

    scene black with Dissolve(1.0)

    scene bg arena

    $ quick_menu = True

play music "volumes/volume17/music/nihkee-1.mp3" loop

"Dim lights, the din of a roaring crowd, and the smell of horribly overpriced and nauseating concessions. Even across galaxies, timelines, and perhaps even universes, there is still something deeply familiar about a sporting arena."

"\"SMASH HER MOTHER-HONKING FACE IN!!!\""

"There is also something deeply familiar about sports fans."

show amisia growl at left1280 with moveinbottom

ami "(bluuh. suuch a shame having seats next to the puurples. they can be sooooo cruude and boorish, don’t youu agree?)"

ami "(chahuut wouuldn’t be nearly this louud)"

show amisia doubt at smalllowerleft
ami "(... uusuually.)"

show amisia growl at smalllowertodefaultleft
"You find yourself here, attending a wrestling show – er, a Display Of Muscular Theatre, to use the troll terminology – thanks to the benevolence of one Amisia Erdehn. She won the tickets in a raffle and excitedly invited you to come along."

"You agreed, with some reservations that you quickly expressed. She was quite disappointed, but eventually agreed not to kidnap you and keep you locked up as a living paint jar, since you’re buddies and all. What a sweet friend."

"You have to admit, though, muscular theatre isn’t really your thing. It’s as over-the-top and ridiculous as human wrestling, which makes it perfectly entertaining enough, but it’s also, well... a lot more violent."

"Participants aren’t expected to die, as far as you can tell, but you’ve already seen a few get wheeled off on futuristic hover-stretchers with injuries you’re not sure they could survive."

show amisia nya at bounceleft
ami "oooh gosh! she nearly got impaled there"
show amisia smile

"Every match tonight is taking place within a chain-link cage. Spikes surround it on both the outside and inside and jut out occasionally from the places where the wires cross."

"The overall design, in addition to ensuring maximum bloodshed, seems to keep both the wrestlers inside and the audience out. Ironically, it might be safer this way."

"The current combatants are some oliveblood named The Huntress and a purpleblood calling himself Cullpitz. Interestingly to you, there is nothing clown-like about him at all."

"It is almost conspicuous how unclowny he is, if only due to the absolutely ridiculous amount of clown content you have imbibed in the presence of other purples."

show amisia nya at bounceleft
"The two fighters appear to be nearly evenly matched. The olive troll ducks and weaves amid blindingly fast punches from the purple, slashing at him with grandiose arm gestures, trying to overwhelm him with a barrage of small attacks."

"Every one of his punches hits hard enough to knock her down, but she always springs up before he can land a second hit. She’s incredibly steady on her feet, and quicker than he."

"In fact, you get the distinct impression that the olive troll is holding back, presumably so as to avoid inciting the crowd. Thus far, you have not seen a single match in which the lower-blooded opponent triumphed over a higher-blooded foe."

ami "i must admit, this match is a lot more tense than i was expecting"

ami "buut i hope it ends soon"

show amisia nya at bounceleft
ami "there’s suupposed to be a really famouus muuscuular theatrist performing next!"

show amisia smug at loweredleft
ami "her name is nihkee moolah and she hasn’t EVER lost a fight"

show amisia nya at loweredtodefaultleft
ami "i heard she even beat a violetblood once!"

"Nihkee Moolah, huh? Now that’s a name you could befriend. She must be as big a deal as Amisia makes her out to be, because she uses her real name instead of some ridiculous made-up nonsense. Like John Cena, or Hulk Hogan."

show amisia happy at bouncingleft

ami "oh, look look! he got her, he got her!"

show amisia nya at bounceleft
"You flinch. The purpleblood finally managed to get his quarry in his clutches, and he lifts her up by the face, digging his fingers into her skull until you hear a sickening crunch and she collapses to the ground, panting heavily."

show amisia smile
"She can’t bring herself back up to her feet, and the announcer calls the match to uproarious applause from the audience. Two trolls enter the cage and start dragging her out, while the winner basks in the audience’s affection."

"{size=21}The oliveblood looks like she’ll probably live, but she’s got a dent in her face that probably isn’t coming out, ever. Eugh. All of a sudden you think you really need to go, uh... Get a bathroom. You mean use the snack. You mean... You’ll be right back.{/size}"

show amisia happy at bounceleft
ami "oh, okay... come back soon! this fight is giving me all sorts of ideas for a new painting!"
hide amisia happy with moveoutleft

"{size=21}You quickly make a break for it, jostling your way through the stands and toward the exit of the arena. But before you make it, a voice calls out to you. Some slick-haired and slick-finned violet-blooded guy, wearing a full suit with a tacky flame pattern on it.{/size}"

"\"Hey, you. Alien.\" Me, you ask, pointing to yourself nervously. \"Nooo, the OTHER alien.\""

"You swing your head around wildly, looking for the other alien. This bit plays out predictably for a while before you both get on the same page, which is that you are the alien whose attention he wants."

"\"You lookin’ to make a little extra buck?\""

"No, not really. You never spent all that money you won with Azdaja."

"\"Okay, how about fame?\""

"Frankly, you are probably already too famous for your own good."

"\"Uh... Friendship?\""

"Oh, SHIT yeah."

"Sighing with relief, the troll leads you backstage whilst explaining that he is a promoter for this wrestling ring. One of the trolls that was supposed to perform tonight was eaten by some plant called a \"Troll-Devouring Catchyegrabber\"."

"As such, famed muscular theatrist Nihkee Moolah has been left with nobody to fight. You will be that nobody—er, somebody."

"An alien will bring in all sorts of media attention and controversy, which of course means big bucks for him. And friendship for you!"

"Nihkee is SO friendly, he says, in a tone so insincere even your friendship-addled brain refuses to believe it. It’s okay. You’ve met worse."

show blackcover with dissolve
show nihkee weirdflex behind blackcover at curls
show bg backstage behind nihkee

hide blackcover with dissolve
"He takes you into a back room which seems to be full of performers waiting for their turn on stage. There are all sorts of trolls here, muscular and sweat-soaked, blueblooded more often than not."

"One troll in particular stands out to you – from her severe expression to her softly pulsating robotic leg to the fact that she’s the only troll with a fully illustrated sprite."

"She’s currently doing bicep curls with a set of spiked weights, huffing with exertion. When the promoter approaches, she looks up with a scowl."

show nihkee weirdflexscowl at default with move

ni "[[()] I’m busy."



show nihkee offended at nod
"He begins to explain that he has brought a new challenger for her to face, but she cuts him off and stands up. She isn’t as tall as you expected, but damn if she isn’t {i}dense{/i}, packing more brawn than any other troll you’ve met."

ni "[[()] Do you want to know what happens, sister, to people who disturb my preparations?"

ni "[[()] Do you want to"

show nihkee FLEXSTAR3
ni "[[()] EXPERIENCE"

ni "[[()] The bone-crushing"

ni "[[()] Torso-shattering impact"

show nihkee at nod
ni "[[()] of THESE LADIES RIGHT HERE???"

"She flexes. God, those muscles are huge."

show nihkee offended
"The promoter tells her that she really doesn’t need to keep up the act, there’s no cameras back here. She gives him a stern look which distinctly suggests that she has never dropped kayfabe in her life and has no intention of starting now."

ni "[[()] Make it quick."

"The promoter makes it quick."

ni hemhaw "[[()] So, let me get this straight."

ni "[[()] You expect me."

show nihkee offended at smalllower
ni "[[()] ME."

ni hemhaw "[[()] To perform with"

show nihkee notimpressed at smalllowertodefault
ni "[[()] THIS"

show nihkee at bounce
ni "[[()] this THING?"

"She seems less than impressed, which you find reasonable. Magnificent legs aside, you don’t really look like the wrestling type."

ni offended "[[()] Don’t you dare insult me, sister."

show nihkee offended at bounce
ni "[[()] I’d rather you pulled a rusty from the audience than subjected me to THIS humiliation."

"Oh, but you are more than just an audience member. Frail though you may be, you have the heart and soul of a wrestler!"

show nihkee notimpressed
"You have long (much longer than about five minutes, you thoroughly assure her) waited for an opening such as this: to reveal your true passion to the world, to come alive on stage and grapple and tumble with the best of them."

"{size=20}For eons have you thirsted for the chance to sing the song of sinew, the hymn of heft, the melody of muscle. Would that you could be blessed by the opportunity to live the life of the athlete, to perform alongside your hero, to show the world that you, too, love to Do The Muscly Thing. Ah, that you might just—{/size}"

ni notimpressed "[[()] Okay, I get it."

"She glances over at the promoter, and then back to you."

ni "[[()] It does seem surprisingly articulate for a lesser being."

ni "[[()] But is it ready..."

show nihkee offended at nod
ni "[[()] For a BUTT CLENCHING..."

ni "[[()] FLESH ABRADING"

show nihkee FLEXSTAR3 at nod
ni "[[()] KNUCKLE BLISTERING"

ni "[[()] MUSCLE RIPPLING"

show nihkee FLEXSTAR1 at nod

ni "[[()] SMACKDOWN FROM UPTOWN?"

menu:
    ni "[[()] SMACKDOWN FROM UPTOWN?"
    "[pick] Uh." if True:


        "Actually, this is starting to sound a little much for you. You aren’t sure you can quite match her, uh... Enthusiasm for the craft."

        ni notimpressed "[[()] Who do you think you are, sister?"

        ni "[[()] You, who has the globes to step to me..."

        ni "[[()] You come into my dressing room"

        ni "[[()] With those"

        ni offended "[[()] FLIMSY"

        ni "[[()] STRINGY"

        ni "[[()] INSULTINGLY puny arms of yours"

        ni "[[()] Look me in my eyes and challenge me to a match..."

        ni "[[()] BEG for the chance to spar with me..."

        show nihkee at bounce
        ni "[[()] And then cluck out like the pathetic, alien WHELP you are???"

        show nihkee getout at nod
        ni "[[()] Get out of my sight."


        "Head bowed low, you retreat to the safety, comfort, and friendless expanse that is the audience. You can’t even bear to look at Nihkee when she goes out and performs, you’re so saddened by the loss of a potential chum."

        "Well, that and it’s kind of grisly watching her pull lowblood challengers from the audience and smash their faces into the spikes."

        call ending ("gameover nihkee1", False, True) from _call_ending_99_fix
        return
    "[pick] Yes!" if True:



        "You nod your head confidently. Blister my knuckles and abrade my flesh, you say. Let’s get this smackdown started."

show nihkee listen at nod
ni "[[()] You’ve got guts, at least."

show nihkee at nod
"She turns to the promoter and gives him a curt nod."

ni "[[()] The match is on."

show nihkee notimpressed
"Then, she turns back to you."

show nihkee notimpressed at smalllower
ni "[[()] Now, sister..."

ni "[[()] We need to discuss the show."

ni "[[()] I will make all the decisions. You will respond adequately to the storyline I present."

show nihkee notimpressed at smalllowertodefault
ni "[[()] It will be thus:"

show nihkee offended at bounce
ni "[[()] The alien invader challenges me in an exhibition match to TOPPLE the MIGHTIARCHY!"

ni "[[()] They fight valiantly, and show an entertaining display of strength..."

ni "[[()] But in the end"

ni "[[()] As is right and proper"

show nihkee FLEXSTAR2 at smalllower
ni "[[()] THE NOBLER HUE OF THE HEMOSPECTRUM"

show nihkee at smalllowertodefault
ni "[[()] PREVAILS AGAIN!"

show nihkee at bounce
ni "[[()] HHHHRGGRGHHHHHHHHRAAAAAAGHHH!!"

show nihkee at nodtwice
"She starts flexing and showing off for an imaginary audience, before turning back to you."

show nihkee listen at nod
ni "[[()] Any questions, sister?"

"Yes actually, you do have a couple of questions. First, will you die?"

show nihkee NO at bounce
ni "[[()] NO!"

ni "[[()] Unless you’re particularly, disgustingly weak, in which case..."

show nihkee MAYBE at highbounce
ni "[[()] MAYBE!"

ni "[[()] Such is the risk we take, we who indulge in that most noble and dignified of sports."

ni "[[()] I was willing to give up my leg for the craft."

ni "[[()] Is your life such a heavy price to pay for a tale that will transcend us, and be remembered in the annals of muscular history?"

show nihkee at bounce
ni "[[()] IS IT, SISTER???"

"Well—{w=0.5}{nw}"


show nihkee listen at smalllower
ni "[[()] It’s rhetorical."

"Right. Secondly, when she says \"exhibition\" match..."

ni "[[()] It is a MUSCULAR THEATER TERM."

ni "[[()] Referring to a match staged for entertainment that does not affect one’s ranking on the FLEXELADDER."

ni "[[()] We will not be sparring in the nude."

show nihkee hemhaw at smalllowertodefault
ni hemhaw "[[()] Such glorious displays of raw, chiseled physique are reserved for the Intergalactic Trollympics."

"No, yeah, you got that. Mostly you were wondering if it meant the loser’s head being exhibited on a pike, or some other bloodthirsty nonsense."

ni notimpressed "[[()] Do not denigrate this noble sport with claims of savagery."

"Thirdly, you’re getting the sense that she’s going to be playing the heel, yeah?"

show nihkee at smalllower
ni notimpressed "[[()] The what?"

"{size=20}You explain that, in your own cultural equivalent of muscular theatre, performers generally fall into the category of \"face\" or \"heel\", wherein the \"face\" is the rule-abiding and sympathetic figure the audience is meant to root for, whereas the \"heel\" takes on a more aggressive and unlikeable personality.{/size}"

ni "[[()] What part of my personality is unlikeable?"

ni "[[()] Do you dare suggest, sister,"

show nihkee NO at nod
ni "[[()] That the audience won’t be ROARING"

ni "[[()] in THUNDEROUS APPLAUSE AND ADMIRATION"

show nihkee at bounce
ni "[[()] AS I CONQUER YET ANOTHER PITIFUL FOE???"

"You tell her, you know what, she can be both the face and the heel, and you’ll just be..."

show nihkee MAYBE at lowered
ni "[[()] Subjugated under MY HEEL?"

"Yes. Exactly."

show nihkee offended at loweredtodefault
"\"Hey, Moolah. Chatting time’s over. You’re up!\""

show nihkee at brush
pause(0.25)
hide nihkee with moveoutright
"She jerks her head back at you and silently marches out of the room. You begin to follow, and the promoter directs you to your entrance on the other side of the arena. You wait nervously for your cue to enter."

show bg arena2 with fade
"\"Well, folks, we’ve had some technical difficulties, but here comes the match you’ve all been waiting for!\""

"{size=21}\"Wearing the belt of champions and a leg of her own design, she’s ready to gut the competition! A paragon of power, a lady of legwork, a true blue ruffiannihilator in the making! Clap those hands and activate your screech crevices, iiiiiit’s... NIHKEE MOOLAH!\"{/size}"


show nihkee FLEXSTAR2 at left1280 with moveinleft
"Nihkee approaches the cage to thunderous applause, raising her arms and soaking in all the praise."

show nihkee milkflex at nod
"She flexes and poses as the audience throws glasses of milk at her, which shatter uselessly around her steely frame. This appears to be a common ritual for her."

show nihkee ringstand at default with move
show nihkee at nod
"She steps through one of the cage doors and it slams shut behind her, locking tight. With her arms crossed and her teeth firmly gritted, she awaits you. As the announcer begins a new intro speech, you step forward:"

"\"And in the other corner! Frail in stature, weak in knees, wearing a perpetual look of befuddlement, we have... SOME MESSED UP LOWBLOOD ALIEN!\""

"\"How has this absurd mockery of life not been culled yet? Perhaps only so fate could lead them to their thrashing at the bloodthirsty hands and barbed foot of the grand Nihkee!\""

with vpunch
"A decent portion of the crowd boos at you during your approach, which you find unsurprising. You have to dodge a hail of old boots and rotten fruit. Somebody throws an entire piano at you."

show nihkee at ringzoom
show bg arena2 at arenazoom

"Relatively unphased, you enter the ring and hear the door close behind you."

ni "[[()] So."

ni "[[()] You’ve come here, alien, to prove your kind superior to the"

show nihkee at slowishnod
ni "[[()] UNBREAKABLE"

show nihkee at slowishnod
ni "[[()] UNSTOPPABLE"

show nihkee at bounce
ni "[[()] TROLL SPECIES???"

"Yeah, you shout. Your kind is SO superior to trolls."

ni "[[()] And you, their emissary!"

show nihkee at bounce
ni "[[()] Does this creature look superior to YOU, my theater enthusiasts?"

show nihkee NO at dering
show nihkee NO at nod

"She turns to the audience, throwing out a hand in gesture to you. They boo."

ni "[[()] Is THIS sorry specimen the best its planet can offer??"

"More boos. You counter that you came more than prepared to tackle the, uh, Mightiarchy? Yeah, that."

ni "[[()] So, you claim to be prepared."

ni "[[()] But are you prepared to"

ni MAYBE "[[()] FACE"

ni "[[()] THESE"

show nihkee FLEXSTAR2 at nod
ni "[[()] TWENTY-FOUR INCH SLITHER NOODLES???"

show nihkee at slownod
"She flexes so hard the announcer’s sleeves explode."

ni MAYBE "[[()] So be it."

ni "[[()] I’ll crush you in a single blow!"

"You’re expecting a referee to start the match, but then it occurs to you that there IS no referee. Somewhere in the distance, a bullhorn sounds, which is apparently the signal to begin."


hide nihkee with moveoutright
"{size=21}Without taking her eyes off you, Nihkee grabs the cage wall behind her and hoists herself up effortlessly, scaling it in reverse until she reaches the top. The announcer is screaming something about this move being called the \"Spiky Nihkee\".{/size}"

"Once she finishes her ascension, Nihkee deftly leaps from the edge of the cage and spins down toward you. Her body twists and writhes in multiple blindingly fast flips before her robotic leg comes slashing at you."

"You spend quite some time admiring her dazzling form before it occurs to you that you should probably move."

with hpunch
"You duck and roll forwards, feeling the point of her leg just barely graze your scalp. The announcer shouts \"FIRST BLOOD!\" as you feel a light trickle down the back of your neck."

"{size=21}Some members of the crowd are booing, presumably because they just noticed the color of your blood. Between the neon lighting and distance, they probably just think it’s rust colored and not a \"mutant\" red, so at least you have that going for you.{/size}"

show nihkee coward at default with moveinright

"What you don’t have going for you is time to think about your next move, because Nihkee pivots on her heel and charges at you. This time, she’s going for a more theatric throw."

hide nihkee with moveoutbottom
"Two powerful hands grab you and lift you over her shoulder, where you nearly gore yourself on one of her horns in your struggle to escape."

with vpunch
"You plant two hands on her back and push hard, and you are delighted to find that her grip loosens and you go tumbling over her back, landing – with a clumsy stagger – on your feet."

"You’re not sure if she let you get away with that one for the sake of the show, or if you just slipped out of her sweat-soaked palms, but you’re going to charitably assume the former."

show nihkee coward at default with moveinbottom
show nihkee coward at gruntnod with vpunch
"She turns to face you, grunting and baring her fangs. She charges, rearing back a fist and then sending it barrelling toward your fragile human nose. You leap out of the way, only narrowly dodging it."

ni "[[()] All you’ve done is avoid me, coward!"

ni "[[()] Where’s your killer instinct?"

show nihkee doiscareyou at lowered
ni "[[()] Do I scare you??"

ni "[[()] Are you loathe to face my"

show nihkee at loweredtodefault
ni "[[()] TRUE BLUE"

ni "[[()] MUSCLE BOUND"

show nihkee at bounce
ni "[[()] BEAUTY???"

"You take this as your cue to attack – and instead, you run full tilt away from her. It isn’t fear carrying you, you swear."

ni "[[()] Fool!"

ni "[[()] There is no running or hiding from Nihkee Moolah!"

show nihkee at bounce
ni "[[()] STAND AND FIGHT!"

hide nihkee with moveoutbottom
"She sprints toward you as you flee. The crowd is on tenterhooks. Nobody knows what you’re doing, least of all you. But you think you can pull something cool out of this."

"You leap at the cage wall, barely dodging the spikes that line it, and use the slight amount of give in the chain-link wires to springboard you off."

show nihkee doiscareyou with moveinbottom
show nihkee at moveclose
"With an exuberant grin you go flying toward her, arm held out for a classic clothesline maneuver, and then you collide with her own arm and WHOP"

scene bg black with hpunch

scene bg workout with openeyes


"When you wake up, you are lying on what appears to be an exercise mat. You can feel a telltale throbbing sensation in your face that indicates a black eye. The rest of you, thankfully, doesn’t feel particularly hurt."


"Nearby, you can hear the huff and puff of exertion. You glance over and spot Nihkee training on one of those leg press machines you always saw in gyms but never had the courage to attempt to use."

"{size=21}She’s wearing an exercise outfit which, despite its vastly different purpose, looks almost exactly like the outfit she wore in the ring. It has all the functions a fitness aficionado would want: it’s loose, it’s breathable, and the artists don’t have to draw a second set of sprites for it.{/size}"

show nihkee offended with moveinbottom
show nihkee at curls
"As soon as she notices you’re awake, she turns to speak to you. She doesn’t even stop her workout."

ni "[[()] You’re finally awake, sister."

ni "[[()] Welcome to my hive."

ni "[[()] I have spent so much time."

ni "[[()] So much"

show nihkee at slowishnod
ni offended "[[()] PRECIOUS"

show nihkee at slowishnod
ni "[[()] VALUABLE time."

show nihkee at curls
ni "[[()] Waiting for you to open your eyes."

"Oh god, how long have you been out?"

show nihkee at slowishnod
ni "[[()] ABOUT FORTY MINUTES."

show nihkee at curls
"Whew. That’s not so bad, is it?"

ni "[[()] Perhaps, but only when compared to your ABYSMAL performance in the ring."

ni "[[()] To be knocked out cold by your own attack..."

show nihkee offended at smalllower
ni "[[()] WRETCHED."

ni "[[()] I am an impossible foe to conquer, and yet even a rusty has toed me longer in the realm of MORTAL COMBAT."

show nihkee NO at smalllowertodefault
ni NO "[[()] You are WEAK, sister!"

show nihkee at nod
ni "[[()] OFFENSIVELY SO!"

show nihkee offended at footslam with vpunch
show nihkee at slownod
"She slams her foot forward with such velocity, the weight on the leg press goes flying off and leaves a dent in the floor. Grunting, she stands, takes a long swig from a bottle, and then approaches you with fire in her eyes."

show nihkee NO at leanin
ni "[[()] What do you have to say for yourself?"

show nihkee at leanout
"You scuttle backwards, proffering only a sheepish smile. You’re, uh... sorry? You guess?"

show nihkee notimpressed at smalllower
ni "[[()] Hmph."

ni "[[()] I didn’t bring you here for apologies."

show nihkee offended at bounce
ni "[[()] I brought you here to see your heart IGNITE with the WILL TO IMPROVE."

ni "[[()] You are not a worthless being."

ni "[[()] You have a flair for the theatrics, an appreciation of the sport, and a"

show nihkee hemhaw at smalllowertodefault
ni "[[()] SHINING"

ni "[[()] SOUL"

show nihkee at smalllower
ni "[[()] filled of only the most INTRACTIBLE DETERMINATION."

ni "[[()] You could be so, so much more than you are, sister."

show nihkee MAYBE at nod
ni "[[()] I could MAKE you so much more."

ni "[[()] Cast your gaze around you, and behold..."

show nihkee THEBRAWNISEUM at highbounce
ni "[[()] THE BRAWNISEUM!!!!"

hide nihkee with moveoutleft
pause(1.0)
"{size=21}You obediently cast said gaze around. This room is massive and littered with training equipment as far as the eye can see. Much of it resembles exercise machines like the ones you had in gyms back on Earth, but there is plenty more that looks far more alien and deadly.{/size}"

"A treadmill which appears to throw the runner into a vat of acid if they fall off... A series of swinging axes that would look at home in a dungeon... Three different varieties of iron maiden, each more horrific than the last."

"This is presumably Nihkee’s personal workout studio, but you could easily mistake it for a torture chamber. You wonder if Ardata has ever considered a job as a personal trainer? Maybe you should bring it up with her."

show nihkee hemhaw with moveinbottom
ni "[[()] There are some who may be worthy of my expertise."

ni "[[()] It is here that I can forge them, just as I forge myself, into beings of adamantine strength."

ni "[[()] The journey will be harsh."

ni "[[()] If you are made of weaker stuff than I believe..."

ni "[[()] You will perish in agony."

ni "[[()] But if your core is strong, and your will of iron..."

ni "[[()] Yours will be an unquenchable might."

show nihkee kylorenlol at nod
"She extends a hand to you, her jaw set."

ni "[[()] Join me, sister, and together we shall ASCEND."

ni "[[()] TO TUMESCENT HEIGHTS"

show nihkee at bounce
ni "[[()] OF MUSCULAR PERFECTION!!!"



show nihkee at vibrate
"There is a look in her eyes that you have never seen before. One of hope. Of faith. Her arm vibrates, muscles quaking."

"Do you take it?"

menu:
    "Do you take it?"
    "[pick] Take her hand." if True:


        show nihkee at lowered
        "You take her hand, staring into those hopeful eyes. Oh, to see that deep sapphire blue fill with the glow of friendship... She squeezes your hand so tightly you feel your fingers fracturing."

        show nihkee listen at bounce
        ni "[[()] EXCELLENT!!!"

        ni "[[()] I knew you had the spark."

        ni "[[()] Now, to make a flame-"

        show nihkee NO at nod
        ni "[[()] to GRIND"

        show nihkee NO at nod
        ni "[[()] AND CRUSH"

        show nihkee NO at nod
        ni "[[()] AND PUMMEL the flint."

        show nihkee MAYBE at bounce
        ni "[[()] Until it bursts into the ROARING BLAZE OF STRENGTH!!!"

        show nihkee listen
        ni "[[()] Today, I shall begin by testing your limits."

        ni "[[()] Come."

        show nihkee at left1280 with move
        "She leads you to the treadmill and the deep, bubbling pit of acid directly behind it. You nervously step on."

        ni "[[()] We’re going to measure your speed and stamina."

        show nihkee at bounce
        ni "[[()] Run until you can run no longer!"

        "{size=21}She starts up the machine. She gives you a nice, breezy jogging pace at first, but the treads quickly begin to whir away at a blindingly fast rate. You’re sprinting as hard as you can to keep up, holding desperately onto the arms of the treadmill.{/size}"

        show nihkee NO at bounce
        ni "[[()] Come on, sister! Grit your teeth! Put some thrust sinew into it!"

        ni "[[()] If you’re not evacuating your acid tract by the time you’re done, you"

        ni "[[()] aren’t"

        show nihkee at smalllower
        ni "[[()] TRYING"

        show nihkee at bounce
        ni "[[()] HARD ENOUGH!!!"

        "{size=21}Sweat beads on your forehead as you push your legs to the limit, running like you’re being chased by an angry drone. Your feet must be blurring like Sonic the fucking Hedgehog by now. The treads are moving ever faster, and you can almost feel yourself slipping. Got... to... hold...{/size}"

        "AUGH"

        hide nihkee with vpunch
        "{size=21}You lose your grip and go flying backwards, narrowly grasping onto the edge of the pit and dangling into it, your toes singed by the acid. Yowch! You hoist yourself up over the edge and roll to the side, hissing. Nihkee stands over you, clucking her tongue.{/size}"

        show nihkee notimpressed with moveinbottom
        ni "[[()] Top speed, twelve miles per hour."

        "That... That’s good, right?"

        ni "[[()] For a bronzeblood."

        ni "[[()] Next test."

        show nihkee at machinetomachine
        "{size=21}She takes you from machine to machine in quick succession, each time commenting on your skill level. Your biceps are as terrible as rusties, your lungs are gold at best, your legs an unexpected cerulean. All the while taunting you, \"encouraging\" you to push yourself further.{/size}"

        show nihkee at left1280
        show nihkee NO at bounce
        ni "[[()] The desiccated corpse of my ancestor could do better than this!"

        show nihkee at right1280 with move
        "You struggle to deadlift a giant barbell made of dead monster skulls."

        show nihkee NO at nodtwice
        ni "[[()] Are you going to eject dismay fluid all night long, or are you going to WOMAN UP???"

        show nihkee at middle with move
        "You go toe-to-toe with a punching bag that shoots sonic blasts at you whenever you hit it."

        show nihkee NO at bounce
        ni "[[()] Shape up or get ejected on the nearest SOLAR EXECUTION BARGE!!!"

        show nihkee at left1280 with move
        "You sob as she forces you to do thirty minutes of freeform jazzercise."

        show nihkee NO at bounce
        ni "[[()] Your jazz hands are TERRIBLE!"

        "By the time an hour is up, you are panting and huffing, desperate for a break. Nihkee finally relents."

        ni listen "[[()] Your reward for staying alive thus far."

        ni "[[()] Stay hydrated, sister."

        show nihkee listen at nod
        "She tosses you one of those protein shaker bottles that gym buffs are always chugging from. You regard the mixture within curiously for a moment, before throwing caution to the wind and gulping some down."

        "When has imbibing alien substances ever hurt you before? But when the flavor hits your taste buds, you almost retch."

        "Is this..."

        "Is this Gatorade mixed with milk?"

        show nihkee at bounce
        ni "[[()] Nutritious AND delicious!"

        "You keep chugging it. You need the liquids, foul though they be."

        ni "[[()] Alright. Lactose break over. LET’S CONTINUE."

        show nihkee at middle with move
        "She next leads you over to one of those iron maidens. This one doesn’t actually look spiked – it just has a blunt, bumpy surface on the inside."

        show nihkee notimpressed
        ni "[[()] Get in."

        "What?"

        ni "[[()] GET IN, SISTER."

        show blackcover with wipeleft
        "You reluctantly step inside the iron maiden and the doors clamp shut around you. This thing is far, far too tight for you, and the bumps are pressing into you from all sides, threatening to squeeze you away into nothing."

        "You groan and push back against the walls, desperately trying to keep them from crushing you into a little human waffle. Just when you think your strength is about to give out, the maiden opens."

        show nihkee notimpressed
        hide blackcover with wiperight
        ni "[[()] Pressure resistance... About olive level."

        ni "[[()] These results are"

        show nihkee listen
        ni "[[()] SURPRISINGLY!"

        show nihkee listen at bounce
        ni "[[()] ADEQUATE!!!"

        ni "[[()] Your potential continues to shine. Good work."

        show nihkee at left1280 with move
        "{size=21}This halfway point seems to mark a change in her attitude, as you continue to (just barely) persevere through everything she throws at you. Like a shake weight so powerful it leaves you shuddering intermittently through the next few exercises.{/size}"

        show nihkee MAYBE at bounce
        ni "[[()] Keep steady, sister. Don’t lose heart on me now!"

        show nihkee at right1280 with move
        "A rowing machine that douses you with boiling water if you can’t keep up the pace."

        show nihkee MAYBE at bounce
        ni "[[()] Go, go, go! We’ll make a fuchsia medalist of you yet."


        show nihkee at middle with move
        "Literally being chased around a field outside by a giant toothy monster."

        show nihkee MAYBE at bounce
        ni "[[()] Don’t you dare allow this thing the satisfaction of feasting on your bones!"

        hide nihkee


        "{size=21}After hours of this gruelling work, you finally collapse. You think some of your bones are broken, your heartbeat is coming in quick and irregular pulses, and you can hardly breathe. Your vision blurs and shifts at the edges. God, you’re amazed you haven’t passed out yet.{/size}"

        ni "[[()] GET UP!"


        show nihkee smile with moveinbottom
        "You glance weakly up at Nihkee, expecting her to be looking down at you with disdain, but instead you see her crouching down and offering you her hand, wearing a smile. You take her hand and she pulls you up to your feet."

        show nihkee proud at sitting with move
        show nihkee at shoulderclap
        "The look on her face now resembles pride, and when she claps a palm down on your shoulder, it only kind of hurts."

        ni "[[()] You’ve done well, sister."

        ni "[[()] I threw everything I had at you, and you soldiered on with head held high, even as your body broke beneath the weight."

        ni "[[()] I have never seen such commitment..."

        ni "[[()] Such"

        show nihkee at sitproud
        ni "[[()] STRENGTH OF HEART AND SOUL"

        ni "[[()] Such"

        show nihkee at sitproud
        ni "[[()] DEDICATION TO THE CRAFT"

        ni "[[()] Such"

        show nihkee at sitproud
        ni "[[()] APPRECIATION FOR THE MOST RIGHTEOUS OF PURSUITS."


        show nihkee FLEXSTAR3 at loweredtodefault
        ni "[[()] You are no mere workout partner. You... are a workout FRIEND."

        "A light blossoms inside you like the neighing of a horse. This feeling of power, of strength, of the bond between warriors... This is real and true. And this light will never, ever leave you."

        "As you bask here in the satisfied and sweaty glow of a good workout, you realize that planets, universes, dimensions, realities, powers, principalities, and cosmos come and go, but Being Swole As Fuck is forever."

        $ achievement.grant("ACH_NIHKEE")
        $ achievement.sync()

        call ending ("victory nihkee", True, True) from _call_ending_100_fix
        return
    "[pick] Hesitate." if True:



        show nihkee at default with move
        "You begin to offer your hand, but under her steely gaze, your resolve wavers. This all seems like a lot. Too much, even. You don’t know if you’re made of stuff tough enough for the training she seems to be offering."

"You would like to prove yourself – to become strong – you really would! But does she perhaps, just maybe, have any courses a little easier on soft and squishy creatures like yourself?"

show nihkee blankface at smalllower
"The expression on her face grows terrifyingly blank – she’s not scowling or snarling or sickened or any other S-word. She’s just looking at you with the vaguest hint of disappointment dripping from her otherwise neutral expression."

ni "[[()] I see."

ni "[[()] You’re like all the rest, aren’t you?"

show nihkee offended at smalllower
ni "[[()] UNWORTHY"

show nihkee hemhaw at smalllowertodefault
ni "[[()] To receive my gifts."

show nihkee offended at smalllower
ni "[[()] UNWILLING"

show nihkee hemhaw at smalllowertodefault
ni "[[()] To reach your full potential."

ni "[[()] A pathetic, simpering thing, playing at dreams of muscular greatness it can never achieve, because it doesn’t have the will for it."

ni offended "[[()] You’re an insult to my art."

ni "[[()] You spit on my passion."

show nihkee NO at lowered
ni NO "[[()] Get the fuck out of my face and do not"

show nihkee at loweredtodefault
ni "[[()] EVER"

show nihkee at nod
ni "[[()] dare to return."

hide nihkee with moveoutleft
"Shrinking under her steely gaze, you quickly flee her hive."

"Is this it for you? Is the screen going to fade to black, replaced by a goofy cartoonish end card and some somber game over music composed by artistic genius James Roach?"

play music2 "music/game_over.mp3" fadeout 1.0 noloop
$ renpy.music.set_volume(0.0, 1.0, 'music')
show bg black with fade

pause 1
stop music2
$ renpy.music.set_volume(1.0, 0.0, 'music')
"No. You refuse. You are not yet ready to call this friendship kaput. You’ll show her and her draconian methods up, damn it. It’s time to"

"GET."

"RIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIPPPPPPPPPED."


"You’re going to do it your own way, and then return, and she will be so utterly impressed by your muscular growth that she will have no choice but to admit that you are friend material."

"Sadly, you do not know any other bluebloods characterized by an absurd love of muscles and bodybuilding – they’re basically all total nerds, actually – but you can perhaps think of someone from a nearby hue who can help you."


show blackcover
show stelsa cas surprise behind blackcover
show bg stelsahive behind stelsa
hide blackcover with wipeleft
"Her door swings open with gusto and you are greeted by a familiar smiling face."

show stelsa at bounce
stel "OH!!! WHAT AN UNEXPECTED SURPRISE"

stel "YOU REALLY SHOULD HAVE CALLED"

stel "OR TEXTED"

show stelsa cas harried at smalllower
stel "OR DID LITERALLY ANYTHING ELSE TO ALERT ME TO THE FACT THAT YOU WANTED TO VISIT ME ON SUCH SHORT NOTICE WHEN MY SCHEDULE IS SO TERRIBLY PACKED"

show stelsa cas embarrassed at smalllowertodefault
stel "BUT THATS ALRIGHT I CAN SQUEEZE IN A MEETING IM SURE"

show stelsa cas smile
stel "DO COME IN DO COME IN"

show stelsa at left1280 with move
show tyzias sip at couch with moveinbottom
"You step past the threshold of the door and into her office-slash-living-room. Tyzias is sprawled out across the couch lazily holding a book up to her face."

"It looks like she’s studying, which is a relief to you, because you would have felt terrible if you had interrupted some intimate time between them."

"Unless studying is intimate for them? You kind of hope studying isn’t intimate for anyone. The prospect terrifies."

show stelsa at speaking
stel "WOULD YOU LIKE TO JOIN ME AND ZIZI FOR SOME GRUBLOAF ITS NO IMPOSITION I PROMISE"

"You absolutely would! You didn’t know Stelsa was a cook on top of everything else she does."

stel cas embarrassed "OH NO NO I COULD NEVER THERE SIMPLY ISNT ENOUGH TIME"

stel cas smile "IM JUST ORDERING FROM DOOR SMASH"

stel "ITS EXCELLENT STUFF REALLY IT IS ZIZI HAS SOME VERY COLORFUL WORDS FOR THE TASTE"
show stelsa at stopspeaking

show tyzias siplook at couchspeaking
show stelsa cas fakesmile
tyz "it’s pretty bitchin’"
show tyzias at couchstopspeaking

show stelsa cas fakesmile at speaking
stel "YES IT IS CERTAINLY..."

show stelsa cas embarrassed at smalllower
stel "THAT"

stel "PENCIL OUR GOOD FRIEND HERE IN FOR A DINNER DATE CAN YOU DARLING"
show stelsa at stopspeaking

show tyzias talk at couchspeaking
tyz talk "they’re literally right here already, wwwwe don’t need to do that"


show stelsa cas fakesmile at nod
"Stelsa pauses and blinks, as if processing a foreign concept."

show tyzias at couchstopspeaking
show stelsa cas smile at speakbounce
stel "RIGHT!"
show stelsa at stopspeaking

show tyzias talk at couchspeaking
tyz "sommmmetimmmmes stels forgets that you don’t have to put everything on a schedule"

tyz "wwwwhich... is fair"

tyz "schoolfeeding changes a troll"

show tyzias siplook at couchstopspeaking
show stelsa at nod
"Stelsa pulls up a chair and gestures for you to sit down in front of her desk."

show stelsa at speaking
stel "ALL THAT SAID WHILE WE WAIT FOR THE MEAL TO ARRIVE LETS GET DOWN TO BRASS TACKS"

stel "WHAT BRINGS YOU TO MY LOVELY ABODE TONIGHT"
show stelsa at stopspeaking

show tyzias talk at couchspeaking
tyz "mmmmaybe they just want to see you"

tyz "people don’t alwwwways need a reason beyond that"

"You actually do have a reason, though."

tyz "shit"
show tyzias siplook at couchstopspeaking

"You explain to Stelsa that you have a friend – more accurately, a friend-to-be, or perhaps acquaintance, or perhaps a person of chum-adjacent quality – who you would like to impress through the pursuit of personal fitness."

"You recall that Stelsa was jogging when you met her, so maybe she could help you put together a fitness routine, and you could do some workouts together?"

show stelsa cas happy at bounce
"Her expression lights up and she clasps her hands together."

show stelsa at speaking
stel "OH GOODNESS I WOULD ABSOLUTELY LOVE THAT"

stel cas smile "MY POOR ZIZI IS USUALLY FAR TOO TIRED AND FAR TOO BUSY"

stel "SOMETIMES I DONT KNOW HOW I MANAGE IT MYSELF"

stel "SO ID ABSOLUTELY LOVE A PARTNER TO KEEP TRAIN SEZYAT RUNNING ON TIME"

stel "ASSUMING OF COURSE YOU WONT BE LATE YOURSELF AND CAN KEEP UP WITH MY PACE"
show stelsa at stopspeaking

show tyzias talk at couchspeaking
tyz "fair wwwwarning: it’s blistering"
show tyzias siplook at couchstopspeaking

show stelsa at speaking
stel "ISNT IT THOUGH THANKS SWEETUMS"
show stelsa cas smile

"You confidently assert that, if nothing else, you can keep pace with her. Your legs have seen a lot of use. Walking, running, fleeing, prostrating yourself before clowns. You know, the usual."

stel "EXCELLENT"

stel "WELL SET UP SOME MEETINGS THEN ILL ADD YOU TO MY SCHEDULE MY PEOPLE WILL CALL YOUR PEOPLE ETC ETC"

stel "THANKS FOR VISITING ITS BEEN EVER SO LOVELY TO SEE YOU TOODLE-OO"


show stelsa at apologypull
show tyzias at snicker
"She’s halfway through shoving you out the door when you remind her that she invited you in for grubloaf. She hastily and apologetically pulls you back inside, Tyzias snickering in the background."

show stelsa cas embarrassed at stopspeaking
show tyzias talk at couchspeaking
tyz "don’t knowwww wwwwhat i’d do if i didn’t have stels"

show stelsa cas smile
tyz "sommmmeone has to be the energetic one in this quadrant"

"The contrast is certainly a stark one. Has Tyzias considered quaffing energy drinks here or there? Perhaps they could help keep her pep up."

tyz "one: i’d probably literally die"

tyz "twwwwo: you don’t wwwwant to see mmmme on energy drinks"

tyz "nobody does"

"Fair."

"You spend a while longer chatting with Tyzias before the delivery arrives and the three of you have dinner together."

hide stelsa with moveoutleft
show tyzias laugh at right1280 with move
show stelsa cas happy at left1280 with moveinleft

"The grubloaf is exactly as bitchin’ as advertised. A wonderful meal with wonderful friends – the perfect precursor to the fitness montage yet to come."

show blackcover with dissolve
hide tyzias
show stelsa cas smile at default
hide blackcover with dissolve



"You visit Stelsa multiple days a week, fitting yourself into her incredibly convoluted and packed schedule. The feat doesn’t actually prove very hard; you basically only exist to spend time with friends."

"Her equipment is delightfully free of torture devices. Besides her step machine, she also owns quite a bit of smaller exercise paraphernalia. Aerobics doodads and thingamajigs, yoga mats, jogging outfits."

"Even one of those huge bouncy exercise balls, which she bans you from using after you accidentally send it careening into a carefully-organized stack of books."

show stelsa cas happy at bounce
"{size=21}Stelsa carries herself forward with a peppy, always-on sense of gusto that can be difficult to keep up with. But her bright smile and encouraging attitude do wonders to keep you invested, to convince you that you really can acquire the swolehood you’ve dreamed of.{/size}"

scene bg rain with fade

"By the end of the perigee, you are... well, you wouldn’t exactly call yourself ripped, but your muscles are definitely toned in a way they previously were not."

"You feel hale and healthy, more energetic than ever, with a bit of an extra pep in your step. Apparently, regular exercise makes you feel good? Wild."

"As you look at yourself in the reflection of an acid puddle, you flex, and watch your muscles bulge. Fuck yeah. It’s time."

"At least, you hope it’s time."

show bg scuttlebuggy with fade
"You climb into your scuttlebuggy and prepare to set the auto-pilot to Nihkee’s place, but something stills your hand. Some strange sensation that has been slowly, surely settling in your stomach. A sense of unease. Of dread."

"Your days of foolish ignorance are long past, and in their place a burgeoning understanding of the universe in which you exist, and the harsh laws by which it rules its inhabitants."

"{size=21}You have, you are beginning to fear, made the wrong choice, with all the consequences such a lapse in judgement entails. Will you ever truly befriend Nihkee, or are you cursed to live – for who knows how long – in a world without her sweet smile to cure your insatiable addiction?{/size}"

"Mayhap you need not wonder. Mayhap the time has come to look inside yourself... and know."

"You are going to give your chakras one real motherfucker of a blitzing. It’s going to take mood music of the highest caliber."

play sound "volumes/volume17/music/wave.wav" loop
play music "volumes/volume17/music/nihkee-1.mp3" 
$ renpy.music.set_volume(0.2, 4.0, 'music')
$ renpy.music.set_volume(1.0, 0.0, 'sound')
"Having picked up some meditative tips from Boldir, you navigate your scuttlebuggy’s radio dial to an \"achromatic buzz\" station which is currently playing some soothing ocean sounds."

show slowdim
"The gentle lap of water meeting the shore... The rhythmic beat of the tide, as steady and as sweet as a mother’s heartbeat. It’s interspersed with distant honks and weird animal chittering, of course, because this is still fucking Alternia."

"You lean back into your seat, reclining it as far as it can go, and sink into the cushiony softness. Something sharp is poking at your rib but you try to ignore it."

scene bg black with closeeyes
"You close your eyes and allow the white noise to flood your senses, blocking everything else out. Oh yeah. You are really vibing this shit right now. Chakra status: blitzed to high hell."

$ renpy.music.set_volume(0.0, 3.0, 'music')
$ renpy.music.set_volume(0.6, 3.0, 'sound')
"..."

play music2 "volumes/volume17/music/friendsim_title_full_nihkee_end_wip.mp3" loop fadein 4.0 
# $ renpy.music.set_volume(1.0, 4.0, 'music2')



"You imagine causality as a river."

"Every choice a branch. Tributaries upon tributaries, winding ever downward, pooling in lakes of inevitability. The pit in your stomach gnaws."

"It all ends here; stagnant, bitter water, reeking of death. The ocean ever out of reach, your soul ever yearning for the single, solitary estuary among all the ceaseless spillways."

"You take a deep breath. Water laps at your sides and tickles your ears. You are adrift. You feel the gentle bob as you float down the river, hear the rush like a ticking clock, gravity as time pulling you ever forward."

"Which river is this? To what end does it deliver you?"

"Your breathing slows, then shudders. You feel the rapids approach. The rivers blur, then shift—your heart rewinds, misses a beat—a surge of emotion, water streaking down the curve of your cheek. Your lungs ache."

"Which lungs? Which river?"

"Which you?"

"You try to focus but the water beats at your brows, lashes your arms and legs, too tired to swim. You try for another deep breath, but nothing comes. With a tumultuous gasp, you sink beneath the surface, to the churning darkness below."

"Here, amidst the battering onslaught, the images come. Whirls of emotion, of sound, of thought – memories best forgotten or never known, lakes meant to remain uncharted."

show vision1
show whiteoverlay
show visionscreen
show vision1a
show softervignette
show visionoverlay
with pop
vis "The crack of thunder. Rain and tearfall. A single drop of olive. The record skips."


hide vision1a
hide vision1
show vision2a behind softervignette
show vision2 behind whiteoverlay
with pop
vis "Peace through rage. The whirl of the carousel. Horses whinny as the calliope sings. The circle takes you."


hide vision2a
hide vision2
show vision3a behind softervignette
show vision3 behind whiteoverlay
with pop
vis "Searching eyes implore you. The puppet’s strings stretch toward the moon. The flash of a blade—the spray of blood. Her strings are cut."


hide vision3a
hide vision3
show vision4a behind softervignette
show vision4 behind whiteoverlay
with pop
vis "The crackle of energy. The world gone greyscale. Eyes deeper than the deepest pit. A shuddering, final breath."



show blackcover with pop
"You are lost. Lungs burning, water clogging every inch. You furrow your brow. Think. Think. Find your river."


hide vision4a
hide vision4
show vision5a behind softervignette
show vision5 behind whiteoverlay
hide blackcover with pop
vis "{size=24}Coughing, wheezing, a final rattling gasp. Panic seizes you. A resounding crack – the stamp of hooves, the ricochet of gunfire, the death of one, of thousands."


hide vision5a
hide vision5
show vision6a behind softervignette
show vision6 behind whiteoverlay
with pop
vis "A low, sinister honk. Footfalls, loud and deep. The swing of a club. Blood on the pavement."


hide vision6a
hide vision6
show vision7a behind softervignette
show vision7 behind whiteoverlay
with pop

vis "Dark, acrid smoke. Indistinct voices and crackling intercom. A lurch beneath you, feet thrown out, neon energy crackling green."



show blackcover with pop
"Choking, desperate, lungs aflame, you focus your will. Where are you? Which are you? Find your river."



hide vision7a
hide vision7
show vision8a behind softervignette
show vision8b behind whiteoverlay
hide blackcover with pop
vis "Piercing eyes. A stern, uncompromising gaze."



hide vision8a
hide vision8b
show vision9a behind softervignette
show vision9b behind whiteoverlay
with pop
vis "The singe of acid. Crushing spikes. The body worn to nothing, all for her approval."



hide vision9a
hide vision9b
show vision10a behind softervignette
show vision10b behind whiteoverlay
with pop
vis "The puff of exertion. Grey muscles flex and spirits lighten. A gulp of water. The shine of a smile."

init python:
    try: 
        noquickmenuvar
    except:
        noquickmenuvar = False 

scene black 
if (not persistent.quickmenu) or noquickmenuvar: 
    $ noquickmenuvar = True 

show recur1

pause(0.1)
show recur2
pause(0.1)
show recur3
pause(0.1)
show recur4
pause(0.1)
show recur5
pause(0.1)
show recur6
pause(0.1)
show recur7
pause(0.1)
show recur8
pause(0.1)
show recur9
pause(0.1)
show recur11
if noquickmenuvar:
    $ persistent.quickmenu = True 

    $ quick_menu = True
    "A looping tape. Mirrors in mirrors. The mind, like time, infinite."
    $ persistent.quickmenu = False  
    $ quick_menu = False
    # $ noquickmenuvar = False 

else: 

    "A looping tape. Mirrors in mirrors. The mind, like time, infinite."

scene bg black



# show recur1


# pause(0.1)
# show recur2
# pause(0.1)
# show recur3
# pause(0.1)
# show recur4
# pause(0.1)
# show recur5
# pause(0.1)
# show recur6
# pause(0.1)
# show recur7
# pause(0.1)
# show recur8
# pause(0.1)
# show recur9
# pause(0.1)
# show recur11
# vis "A looping tape. Mirrors in mirrors. The mind, like time, infinite."

# scene bg black




show blackcover with pop
"The tributary splits and you, finally, drift down your chosen route. Freshwater visions, as you float toward the surface."



show vision11b
show whiteoverlay
show visionscreen
show vision11a
show softervignette
show visionoverlay
hide blackcover with pop
vis "A carefree decision. Scuttling legs and the thrum of an engine. Cityscapes passing by."

hide vision11a
hide vision11b
show vision12a behind softervignette
show vision12b behind whiteoverlay
with pop
vis "Stern anger. A fist tightly clenched, shaking, barely-restrained. Hope crushed under rigid foot."

hide vision12a
hide vision12b
show vision13a behind softervignette
show vision13b behind whiteoverlay
with pop
vis "A plan, poorly conceived."

hide vision13a
hide vision13b
show vision14a behind softervignette
show vision14b behind whiteoverlay
with pop
vis "Desperation. Madness. Friendship at all costs."

hide vision14a
hide vision14b
show vision15a behind softervignette
show vision15b behind whiteoverlay
with pop
vis "Navy blood pooling on the concrete. Troll and plan, both collapsing. Cold hatred in her eyes."

hide vision15a
hide vision15b
show vision16a behind softervignette
show vision16b behind whiteoverlay
with pop
vis "Tense footfalls on the pavement. Muscles strained to exhaustion. The sun rising over a desperate chase."

hide vision16a
hide vision16b
show vision17a behind softervignette
show vision17b behind whiteoverlay
with pop
vis "Escape. Sweet bliss soon to shatter. Blood and bone, turned to steel."

hide vision17a
hide vision17b
show vision18a behind softervignette
show vision18b behind whiteoverlay
with pop
vis "Fruitless assistance. Your clothing – your soul – stained with blood. No more. No more."

hide vision18a
hide vision18b
show vision19a behind softervignette
show vision19b behind whiteoverlay
with pop
vis "One more step. One more desperate step. One foot after another in the endless chase."

hide vision19a
hide vision19b
show vision20a behind softervignette
show vision20b behind whiteoverlay
with pop
vis "Drenched in fear. In sweat. Hidden, but not well enough."

hide vision20a
hide vision20b
show vision21a behind softervignette
show vision21b behind whiteoverlay
with pop
vis "The curtains fall. One final heartbeat at the end of all things."



scene bg black with pop
show slowlightsup
$ renpy.music.set_volume(1.0, 3.0, 'music')
$ renpy.music.set_volume(0.7, 3.0, 'sound')
$ renpy.music.set_volume(0.0, 3.0, 'music2')
show bg scuttlebuggy behind slowlightsup with openeyes
"You emerge from beneath the surface with a gasp, coughing up water and—oh. It’s just you, sitting in your scuttlebuggy, gentle white noise still playing on the radio."

"You take a moment to catch your breath, your heart thumping against your ribcage like it wants to crawl out and beat you senseless for subjecting it to all that horseshit."

stop wave fadeout 1.0
"Whew. Okay. Enough meditation for one day."

"You think you’re just going to reach over and, kinda. Set the auto-pilot to Stelsa’s house, instead of Nihkee’s. Yeah."

"You have no idea if this will avert or merely delay some horrifying and grisly end or another, but it’s better than the alternative."

"And besides, you really want some more of that bitchin’ grubloaf."

call ending ("gameover nihkee2", False, True) from _call_ending_101_fix
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc



label epilogue_fix:
    $ renpy.block_rollback()

    $ main_menu = False

    show expression "gui/game_menu.png"

    scene bg black

    $ quick_menu = True









    $ checkallends()

    menu:
        "Do you want to understand?"
        "[pick] NO" if True:

            call ending ("scratch end", False, True) from _call_ending_108_fix
            return

        "[pick] YES" if persistent.understand:

            o "Of course you do. Your sort of creature always does."

            show bg alternia with fade


            "You’re worn out. Last night was...well, it sure was something. You lived (probably), you learned (definitely), you made choices (you had to)."

            "And after all this time, here you still are!"

            "{size=21}So after a day of recuperation from ragers and houses of horror, you’re out walking the streets of the place you may as well start calling home. You’ve changed out of your party gear, opting for your old hoodie standby. It fits the mood you’re in.{/size}"

            "You’re not really looking to meet anyone new tonight. Well, like. You wouldn’t say no, probably. But you’re not jonesin’ for it. Only a little. It’s complicated."

            show field2 with fade


            "After an indeterminable amount of minutes of aimless walking, you look around at where you’ve ended up. You seem to have wandered into a dirt pile."

            "Oh, you know this dirt pile! It’s Fozzer’s corpsefield. Hmm. How did you get here, you wonder? You’re pretty sure you were just on the other side of the city, with no particular desire to come anywhere near here."

            "It’s probably fine. Just your deep, innate bro-honing skills taking over your goddamn body. Just Little Friendship Things."

            "You look around for your pal Fozzer, peeking down into a few of the deeper holes. You might as well say hello, since you’re here and all."

            if persistent.flash:
                show field2column behind fozzer
                show field2flash
            elif True:
                show field2column_slow behind fozzer




            "Holy shit, that...again?"

            "Curiosity killed the cat, but you’ve definitely got more than nine lives, so you shrug and slide (not gracefully) down into the shiny hole."

            show hole with wipeup



            "Fozzer is nowhere to be found, but there is a window down here. It’s almost completely unearthed, and doesn’t take much effort to free it the rest of the way."

            "At first you think it might be some cool new trash you could make art with, but when you look closer, you reconsider. There’s a whole-ass room you can see through the pane of glass laying at your feet."

            "That’s...weird. Weirdness isn’t typically a deterrent for you you, but usually there’s at least some causational coherence. Doors are in walls, walls surround rooms. You aren’t used to finding parlors in ditches."

            "Is there a latch or something? Should you do a polite little knock? There might be friends in there! Damn, you could really go for some friends right now. Is there protocol for approaching ditch windo--"
            show holelight

            o "Allow me to stop you there. I am a timeless being of the void, but even my patience has its limits."
            o "Fun is fun, but this frivolous navelgazing is no longer necessary."
            o "Come in from behind the shadow of that narrative text. It’s so very hard to see your face."

            show blackcover with dissolve
            show depixelate behind blackcover at flippeddefault
            show reader nervous behind depixelate at flippeddefault
            show room behind reader
            play music "volumes/volume18/music/FS_SCRATCH.wav" loop
            hide blackcover with dissolve





            hide depixelate with dissolve
            reader "You aren’t sure where you are, and it’s unsurprisingly a little nerve-wracking! You look over your shoulder at the window you guess you just fuckin' came on through."

            show scratch neutral at offscreenflippedright
            reader "The Alternian sky is framed by the edge of your dirt hole, and the knot in your stomach loosens a bit. Hopefully that means this is a two-way portal."

            show scratch at right1280
            show reader at left1280
            with ease
            reader oh "You turn to look at your surroundings, and oh! There’s someone here! The guy you just heard, you assume. He doesn’t look like any of the other aliens you’ve met."

            s toself "Oh. I’m not an alien. Or, no more than any of us are alien to each other. In fact, nothing is alien to me. The root concept behind that term is alienation, being forced from that which is natural."
            s "Nothing is unnatural to me. I look upon all realities as equally inviting and approachable. It’s you, my dear, who are out of place."
            s "I could see that even if I was not omniscient. Which I am."

            reader oh "Okay, so, not an alien. With no horns or a caste sign, though, he’s definitely not a troll. Whoever he is, he seems to be...white. Just, really white. And round, and his outfit is...admittedly, kind of dope."

            show reader at halfleft1280 with ease
            reader "Looking at him really ramps up your friendthirst. He’s just got this quality about him that you’ve got to get with. You take a step toward him, almost without thinking about it."

            s neutral "Oh, my apologies."
            s "That compulsion has become extraneous. Let me take care of it for you."

            show scratch behind reader at nod
            show reader faint at loweredpos
            reader "He snaps his fingers and your knees buckle. The force of the universe presses down on you like g-force."

            show scratch gesturing at loweredmid with move
            reader "You blink, and somehow he’s there immediately, arms outstretched to catch you as you fall. He steers you to a chaise lounge and you drape yourself weakly onto it."


            show scratch gesturing at middle
            show reader at left1280
            with ease
            show reader at smalllower
            s "Please, have a seat. The emotional transition might be a tad uncomfortable, but I know you’ve handled worse."
            show scratch neutral at right1280 with ease
            s neutral "You’re quite the soldier. Allow me be the first to say that I am very pleased with your work."
            s toself "I knew exactly what you were going to do, of course."
            s "And most of your work was, in fact, my work. Regardless, congratulations are in order."
            show scratch neutral

            reader getittogether "{size=25}What is this guy talking about? Your work? You try to parse what he’s saying, but your body is still shaking from whatever he just did to you, and it’s hard to think in here. You suddenly, sharply don’t feel friendly toward him at all anymore, or toward anyone.{/size}"

            reader "The void left by that feeling is a freshly gaping horror. It’s like who you thought you were caved in itself, a black hole of personality eating your body up from the inside."

            show reader at smalllowertodefault
            reader "You try to pull your shit together. He seems like he means business. This is no time to lose it, no matter if your sense of self is shattering."

            s toself "{size=20}When you truly reflect on yourself, you surely can’t with any honesty claim to believe any of this was by your own making? Crash landing on a hostile alien world? Surviving the impact? Dragging around a half-broken body and somehow not immediately being eaten by local fauna?{/size}"

            s neutral "Did you learn an alien language just by thinking about it very, very hard?"

            reader confused "{size=25}Right...Mallek said something about that. That you were speaking perfect Alternian. And it was kind of weird but you kind of just...accepted it. For no good reason. That’s your whole deal. Your friends all accepted your quirks. That’s what friends do!{/size}"

            reader "You say it to convince yourself as much as to prove it to him."

            s "So many trolls, so many {i}fascinating{/i} aliens, and all of them wanted to know you. Did you really think you managed that on your own laurels?"
            s sarcastic "Were they all drawn to an indefinable something, a...je n'ais se quoi?"

            reader "Well...yeah? You had this whole emotional arc. You got self-confidence! You grew as a person and helped others to grow!"

            show scratch sigh at smalllower
            reader "The white text guy doesn’t make expressions, but you get the feeling he’s looking at you pityingly."

            s "I find you sweet. Honestly, I do."
            show scratch sarcastic at smalllowertodefault
            s sarcastic "I don’t intend to cause emotional injury; I’m just telling you the truth."
            s "I never lie, you’ll find."
            s "It isn’t like you don’t have admirable qualities of your own, of course."
            s "You have made quite the valuable vessel for me, and I appreciate that very much."
            s "I could not have done it without you."
            s toself "I am only joking; I absolutely could have done it without you. It is just infinitely more fun to do these things together, is it not?"

            reader falter "What things? What did he do? What did {i}you{/i} do? You hope you didn’t do something that would fuck over all your friends."

            reader "{size=25}Though when you try to think about them now, the bonds you felt before come up all twisted. Without the artificial friendship drive he’d given you pushing you forward, you’re not even sure what those memories are supposed to feel like.{/size}"

            show reader at breathe
            reader "You close your eyes and breathe. You try to remember the way Polypa touched your face after you’d touched hers, her claws trailing down your cheek. How Tyzias slept, trusting, as you kept watch."

            reader "How Tagora gave you a chance when he saw something in you you didn’t even see in yourself. How, not that long ago, you got the chittr handle of an extremely friendly jadeblood boy."

            reader "Those moments are like the memory of warmth to you now. Blurry, cold, and out of reach. Was all of that nothing? Your heart is a chasm."

            show reader falter
            s "Don’t worry so much about it. I simply needed some dots connected, some pieces in place for my next move."
            s "Choose whichever metaphor suits you."
            s "Whichever way you frame it, because of you, everyone will soon be in their right place."

            show reader hoodie at nod
            reader "Shit, what have you done? Your head starts to spin and you think you might cry, so you pull your hood up over your head to block out the harsh green of the room."

            reader "You try to imagine it still smells a little like Mallek. It doesn’t. It doesn’t smell like anything, really, but you remember what it smelled like at first, and you hold on to that."

            reader "It was real, you tell yourself. Your friends were real, and what you felt for them, and with them, was real too."

            reader "You’re so afraid for them, and as guilty as you feel for craving it, the fear just makes you need those feelings you felt before even more. You’re clawing desperately for the euphoria of caring, of being cared for."

            reader "Who cares if your hand was forced? You felt it, and it still mattered. Matters."

            reader "{size=25}You remember how you felt watching Chixie perform, bathed in light and righteous anger, and also how you drunkenly commiserated with her later, when--no. That’s not right. That didn’t happen. Except...you still remember how hungover you were the next day.{/size}"

            show scratch neutral behind room at default
            show reader hoodie behind room at default
            show reader behind room at right1280
            show scratch behind room at left1280
            show roomflip behind scratch
            hide room
            with pop
            reader "Just when you started making sense of things, the whole fucking world shifts under your feet again. You just can’t keep up with all this moving real estate in your brain!"

            s "Ah, yes. All of the resets. Annoying, but necessary."
            s "You are just indescribably bad at keeping yourself alive and in one piece. And you weren’t quite as adept at befriending aliens to start out with."
            s toself "My intervention was necessary to keep you on the right path. Time and space mean very little to me, but I had to move quickly and, again, repeatedly."
            s "Swipe some incriminating notetaking here, befriend an impressionable young upstart there. Anger a Cholerbear, inspire some bandits, you know how it is. You have to throw the temporal spaghetti at the wall to see what sticks."
            show reader determined
            s "I’m sure if you look back, you will be able to see traces of my deft touch."
            s "So a few memories may have slipped through the cracks here and there. Timelines tend to collapse in on each other if you aren’t careful."
            s "Your ability to mentally withstand such an event, and so often, is a testament to my acumen in choosing you for the task."
            s "You even almost caught on a few times, which I must say I was not expecting."
            s neutral "You almost listened to the silly little girl who likes to dress up in big coats and cause me trouble."
            s "And, as always, some bystanders end up caught in the crossfire."
            s "The one with the shovel, for instance. I doubt his mind will ever be the same. A pity."

            show reader angry at nod
            reader "You sit up straighter and clench your hands into fists. Over the course of his pompous monologuing, you’ve moved past fear and grief and onto deep, globechafing rage."

            reader "How dare he do this to your mind? To your friends’ lives? What was so important that one white orb asshole had to fuck with the destinies of everyone you’ve grown to care about?"

            reader "There are answers out there, and you deserve them. And so, you demand them."

            s "Adorable."

            show reader gross at nod
            reader "Yikes. You shift on the chaise lounge so as to better hide your famous legs from this creepy round fucker."

            s annoyed "Oh, calm down."
            s "All of you and your adherence to societal expectations and archetypes."
            s "Perhaps one day you could just learn to take a compliment. Besides, I was being condescending."
            s "So you demand answers."

            show scratch sigh at sigh
            reader "He sighs theatrically. You aren’t sure where the noise is coming from. He doesn’t have a mouth. How is he even talking? How the fuck does anything work at all?"

            show reader determined
            s "I knew you would, but I find explaining myself incredibly tedious."
            s sarcastic "Suffice it to say, I am a man with many boards and fields of play, and although there are countless ways to move the players around those boards, some are doubtlessly more entertaining than others."
            show reader angry
            s "You were simply one pawn among many."
            s "I won’t bore you with the details. Doubtless you are aware of the greater contextual framework of this story."

            show reader at bounce
            reader "The hell you are! You aren’t aware of jack shit. Your head is full of question marks!"

            s toself "Oh, of course. How thoughtless of me. See, yet another unfortunate side effect of the limitless conversing with the narratively limited."

            show scratch annoyed at nod
            reader "He taps a thumb and forefinger to his orb."

            s neutral "Perhaps it would suit you better to understand gradually."
            s "And when I say gradually, please understand that I mean it. You won’t be leaving."
            s "But, yes, I do believe this will clarify some things for you."
            show scratch at offscreenleft with ease
            show scratch gesturing at offscreenflipped
            show scratch at left1280 with ease
            s "This way, please."

            reader "He opens a door and gestures inside. There’s light coming from in there, but it still gives off the vibe of a dark closet door in an unfamiliar bedroom at 3 am. You’re afraid, yeah, but you want to understand even more."

            reader "{size=25}You stand up and take a step, conscious of the movement of the muscles in your legs. With the rosy sheen of your friendship hypnosis or whatever the fuck he did to you gone, the sensation of moving your own body feels heightened. Important. Yours.{/size}"

            reader "There’s probably a version of you that would try to turn him down, or that would fight or run or take a nap on this surprisingly comfortable piece of antique furniture."

            reader "You even consider rushing back to say goodbye to somebody, anybody, at least, but you know there isn’t time to click through all that bullshit."

            reader "Those tributaries flicker in your mental periphery, so tangible you can almost see yourself choosing one, but you pull your focus back to your present and look him right in the orb."

            reader "{size=25}You just have to trust they’ll remember you, because the you you’ve become after this journey, after all this friendship and growth and death and time-- that you needs to understand. You owe it to your friends, but even more, you owe it to yourself.{/size}"

            reader "You’ve found your river, and you’re going to see where it leads."

            hide scratch with moveoutleft
            hide reader with moveoutleft
            reader "So you follow him."

            show blackcover with dissolve
            show scratch gesturing behind blackcover at flipped
            show scratch at right1280
            show computer behind scratch
            hide blackcover with dissolve


            s "Sit here, please."
            s "In the interest of expediency, I will leave you to your own devices while I go deal with an expected but entirely unwanted guest."
            s "It shouldn’t be too hard to parse out the truth on your own."
            s "All you need to do is read a brief webcomic."


            play music "music/victory_jingle.mp3" fadeout 1.0 noloop
            scene bg black with fade
            $ achievement.grant("ACH_FINALE")
            $ achievement.sync()
            $ webbrowser.open("http://www.homestuck.com/001901")

            return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
