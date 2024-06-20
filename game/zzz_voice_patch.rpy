define config.has_voice = True
define config.auto_voice = "voice/{id}.ogg"
default persistent.quickmenu = True 
define config.developer = True 
define config.version = "VOICE FANPATCH PRE_0.01"
define gui.history_height = None

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
    
    imagebutton auto "gui/title_%s.png" action Confirm(_("Unlock {i}all{/i} Hiveswap Friendsim achievements?{size=18}{color=#929292}\n\n(This will unlock all volumes, but will also\nspoil the route endings!){/color}{/size}"), Function(all_ach2)) pos (20, 20) at wigglenew alt _("Hive swap friend sim") hovered PlayCharacterVoice("menunarrator", "voice/hover/Menu_Hiveswap_Friendsim.ogg")
    
    imagebutton auto "gui/start_%s.png" action Start("start") pos (20, 345) at menumove alt _("Start") hovered PlayCharacterVoice("menunarrator", "voice/hover/Menu_Start.ogg")
    imagebutton auto "gui/load_%s.png" action ShowMenu('load') pos (20, 405) at menumove alt _("Load") hovered PlayCharacterVoice("menunarrator", "voice/hover/Menu_Load.ogg")
    imagebutton auto "gui/options_%s.png" action ShowMenu('preferences') pos (20, 465) at menumove alt _("Options") hovered PlayCharacterVoice("menunarrator", "voice/hover/Menu_Options.ogg")
    imagebutton auto "gui/friends_%s.png" action ShowMenu('achievements') pos (20, 525) at menumove alt _("Friends") hovered PlayCharacterVoice("menunarrator", "voice/hover/Menu_Friends.ogg")
    imagebutton auto "gui/credits_%s.png" action ShowMenu('about') pos (20, 585) at menumove alt _("Credits") hovered PlayCharacterVoice("menunarrator", "voice/hover/Menu_Credits.ogg")
    imagebutton auto "gui/exit_%s.png" action Quit(confirm=not main_menu) pos (20, 645) at menumove alt _("Exit") hovered PlayCharacterVoice("menunarrator", "voice/hover/Menu_Exit.ogg")

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
            
            text "HIVESWAP: FRIENDSHIP SIMULATOR" color gui.accent_color size 48
            text config.version text_align 0.5 color gui.accent_color size 40
            text "DIRECTORS" text_align 0.5 color gui.accent_color size 30
            hbox:
                text "MELANIE J ARCHER" text_align 0.0 min_width 440
                text "Voice/Project Lead, Casting Director" text_align 1.0 

            hbox:
                text "ETCHJETTY" text_align 0.0 min_width 440
                text "Technical Director, Casting Director" text_align 1.0 


            text "VOICE ACTORS" text_align 0.5 color gui.accent_color size 30
            hbox:
                text "MELANIE J ARCHER" text_align 0.0 min_width 440
                text "MSPAR, Menu Narration" text_align 1.0 

            hbox:
                text "JOSEPHINE KIM" text_align 0.0 min_width 440
                text "Ardata" text_align 1.0 

            hbox:
                text "HOPEYMAGE" text_align 0.0 min_width 440
                text "Diemen" text_align 1.0 

            hbox:
                text "YEAGRIMBO" text_align 0.0 min_width 440
                text "Cirava" text_align 1.0 

            hbox:
                text "VYN VOX" text_align 0.0 min_width 440
                text "Amisia" text_align 1.0 

            hbox:
                text "IMMUTABLEMUTIE" text_align 0.0 min_width 440
                text "Bronya" text_align 1.0 

            hbox:
                text "DARE0451" text_align 0.0 min_width 440
                text "Skylla, Elwurd" text_align 1.0 

            hbox:
                text "MISTERJEROME" text_align 0.0 min_width 440
                text "Tagora" text_align 1.0 

            hbox:
                text "TGVELVET" text_align 0.0 min_width 440
                text "Galekh" text_align 1.0 

            hbox:
                text "ZAPPYMAKESART" text_align 0.0 min_width 440
                text "Vikare" text_align 1.0 

            hbox:
                text "KALKORY" text_align 0.0 min_width 440
                text "Polypa" text_align 1.0 

            hbox:
                text "FLINN UVMOCK" text_align 0.0 min_width 440
                text "Zebruh" text_align 1.0 

            hbox:
                text "PINKIIPROXII" text_align 0.0 min_width 440
                text "Folykl" text_align 1.0 

            hbox:
                text "HISONOKAMI" text_align 0.0 min_width 440
                text "Kuprum" text_align 1.0 

            bar base_bar "#66cc00"

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

define o = Character("", color='#FFFFFF', what_color="#000000", image="scratch", window_background=im.MatrixColor(im.Grayscale("/gui/textbox_purple.png"), im.matrix.invert()),voice_tag="scratch")
define s = Character("", kind=narrator, color='#FFFFFF', what_color="#FFFFFF", image="scratch", window_background=im.MatrixColor("/gui/textbox_narration.png", im.matrix.invert()),voice_tag="scratch")

define reader = Character("", color='#FFFFFF', image="reader", window_background=im.Grayscale("/gui/textbox_purple.png"), voice_tag="narrator")

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
                    imagebutton auto "gui/epilogue_%s.png" action Jump("epilogue") alt "Epilogue: Of Hosts, Excellent" sensitive persistent.epilogue hovered PlayCharacterVoice("menunarrator", "voice/hover/Volume_Epilogue_Title.ogg")


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
    
    imagebutton auto "images/charselect/ardata_button_%s.png" action Jump("ardata") pos (0, 0) alt _("Ardata Carmia") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/ardata.ogg")# "voice/hover/Volume_1_Ardata_Select.ogg")
    imagebutton auto "images/charselect/diemen_button_%s.png" action Jump("diemen") pos (640, 0) alt _("Diemen Xicali") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/diemen.ogg")# "voice/hover/Volume_1_Diemen_Select.ogg")
    
screen troll_select2():
    
    imagebutton auto "volumes/volume2/images/charselect/amisia_button_%s.png" action Jump("amisia") pos (0, 0) alt _("Amisia Erdehn") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/amisia.ogg")
    imagebutton auto "volumes/volume2/images/charselect/cirava_button_%s.png" action Jump("cirava") pos (640, 0) alt _("Cirava Hermod") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/cirava.ogg")
    
screen troll_select3():
    
    imagebutton auto "volumes/volume3/images/charselect/skylla_button_%s.png" action Jump("skylla") pos (0, 0) alt _("Skylla Koriga") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/skylla.ogg")
    imagebutton auto "volumes/volume3/images/charselect/bronya_button_%s.png" action Jump("bronya") pos (640, 0) alt _("Bronya Ursama") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/bronya.ogg")
    
screen troll_select4():
    
    imagebutton auto "volumes/volume4/images/charselect/tagora_button_%s.png" action Jump("tagora") pos (0, 0) alt _("Tagora Gorjek") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/tagora.ogg")
    imagebutton auto "volumes/volume4/images/charselect/vikare_button_%s.png" action Jump("vikare") pos (640, 0) alt _("Vikare Ratite") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/vikare.ogg")
    
screen troll_select5():
    
    if persistent.polypareveal:
        imagebutton auto "volumes/volume5/images/charselect/polypa2_button_%s.png" action Jump("polypa") pos (0, 0) alt _("Polypa Goezee") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/polypa.ogg")
    else:
        imagebutton auto "volumes/volume5/images/charselect/polypa1_button_%s.png" action Jump("polypa") pos (0, 0) alt _("??????")   
        
    imagebutton auto "volumes/volume5/images/charselect/zebruh_button_%s.png" action Jump("zebruh") pos (640, 0) alt _("Zebruh Codakk") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/zebruh.ogg")

screen troll_select6():
    imagebutton auto "volumes/volume6/images/charselect/elwurd_button_%s.png" action Jump("elwurd") pos (0, 0) alt _("Elwurd") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/elwurd.ogg")
    imagebutton auto "volumes/volume6/images/charselect/kuprum_button_%s.png" action Jump("folyklkuprum") pos (640, 0) alt _("Kuprum and Folykl") # hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/kuprumfolykl.ogg")
    
screen troll_select7():
    imagebutton auto "volumes/volume7/images/charselect/remele_button_%s.png" action Jump("remele") pos (0, 0) alt _("Remele Namaaq") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/remele.ogg")
    imagebutton auto "volumes/volume7/images/charselect/konyyl_button_%s.png" action Jump("konyyl") pos (640, 0) alt _("Konyyl Okimaw") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/konyyl.ogg")

screen troll_select8():
    imagebutton auto "volumes/volume8/images/charselect/tyzias_button_%s.png" action Jump("tyzias") pos (0, 0) alt _("Tyzias Entykk") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/tyzias.ogg")
    imagebutton auto "volumes/volume8/images/charselect/chixie_button_%s.png" action Jump("chixie") pos (640, 0) alt _("Chixie Roixmr") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/chixie.ogg")

screen troll_select9():
    
    imagebutton auto "volumes/volume9/images/charselect/azdaja_button_%s.png" action Jump("azdaja") pos (0, 0) alt _("Azdaja Knelax") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/azdaja.ogg")
    
    if persistent.chahutreveal:
        imagebutton auto "volumes/volume9/images/charselect/chahut_button_%s.png" action Jump("chahut") pos (640, 0) alt _("Chahut Maenad") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/chahut.ogg") 
    else:
        imagebutton auto "volumes/volume9/images/charselect/amisia2_button_%s.png" action Jump("chahut") pos (640, 0) alt _("Amisia Erdehn?") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/amisia.ogg") 
        
screen troll_select10():
    imagebutton auto "volumes/volume10/images/charselect/zebede_button_%s.png" action Jump("zebede") pos (0, 0) alt _("Zebede Tongva") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/zebede.ogg")
    imagebutton auto "volumes/volume10/images/charselect/tegiri_button_%s.png" action Jump("tegiri") pos (640, 0) alt _("Tegiri Kalbur") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/tegiri.ogg")

screen troll_select11():
    imagebutton auto "volumes/volume11/images/charselect/mallek_button_%s.png" action Jump("mallek") pos (0, 0) alt _("Mallek Adalov") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/mallek.ogg")
    imagebutton auto "volumes/volume11/images/charselect/lynera_button_%s.png" action Jump("lynera") pos (640, 0) alt _("Lynera Skalbi") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/lynera.ogg")
    
screen troll_select12():
    imagebutton auto "volumes/volume12/images/charselect/galekh_button_%s.png" action Jump("galekh") pos (0, 0) alt _("Galekh Xigisi") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/galekh.ogg")
    imagebutton auto "volumes/volume12/images/charselect/tirona_button_%s.png" action Jump("tirona") pos (640, 0) alt _("Tirona Kasund") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/tirona.ogg")

screen troll_select13():
    imagebutton auto "volumes/volume13/images/charselect/boldir_button_%s.png" action Jump("boldir") pos (0, 0) alt _("Boldir Lamati") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/boldir.ogg")
    imagebutton auto "volumes/volume13/images/charselect/stelsa_button_%s.png" action Jump("stelsa") pos (640, 0) alt _("Stelsa Sezyat") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/stelsa.ogg")

screen troll_select14():
    imagebutton auto "volumes/volume14/images/charselect/marsti_button_%s.png" action Jump("marsti") pos (0, 0) alt _("Marsti Houtek") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/marsti.ogg")
    imagebutton auto "volumes/volume14/images/charselect/karako_button_%s.png" action Jump("karako") pos (640, 0) alt _("Karako Pierot") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/karako.ogg")

screen troll_select15():
    imagebutton auto "volumes/volume15/images/charselect/charun_button_%s.png" action Jump("charun") pos (0, 0) alt _("Charun Krojib") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/charun.ogg")
    imagebutton auto "volumes/volume15/images/charselect/wanshi_button_%s.png" action Jump("wanshi") pos (640, 0) alt _("Wanshi Adyata") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/wanshi.ogg")

screen troll_select16():
    imagebutton auto "volumes/volume16/images/charselect/fozzer_button_%s.png" action Jump("fozzer") pos (0, 0) alt _("Fozzer Velyes") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/fozzer.ogg")
    imagebutton auto "volumes/volume16/images/charselect/marvus_button_%s.png" action Jump("marvus") pos (640, 0) alt _("Marvus Xoloto") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/marvus.ogg")

screen troll_select17():
    imagebutton auto "volumes/volume17/images/charselect/daraya_button_%s.png" action Jump("daraya") pos (0, 0) alt _("Daraya Jonjet") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/daraya.ogg")
    imagebutton auto "volumes/volume17/images/charselect/nihkee_button_%s.png" action Jump("nihkee_fix") pos (640, 0) alt _("Nihkee Moolah") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/nihkee.ogg")

screen troll_select18():
    imagebutton auto "volumes/volume18/images/charselect/lanque_button_%s.png" action Jump("lanque") pos (0, 0) alt _("Lanque Bombyx") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/lanque.ogg")
    imagebutton auto "volumes/volume18/images/charselect/soleil_button_%s.png" action Jump("soleil") pos (640, 0) alt _("Barzum & Bazili") hovered PlayCharacterVoice("narrator", "voice/hover/fsim_names/baizbaz.ogg")

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items: 
            if renpy.loadable("voice/hover/"+ i.caption + ".ogg"):
                textbutton i.caption action i.action hovered PlayCharacterVoice("narrator", "voice/hover/"+ i.caption + ".ogg")
            else: 
                textbutton i.caption action i.action                
