# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define l = Character("Link")
image fmenu = "menu esquerda.png"
image tmenu = "menu superior.png"


style texto_semana is text:
    size 40
    color "#000"

style texto_stats is text:
    size 20
    color "#000"



init python:
    score_mat = 0
    score_nat = 0
    score_ling = 0
    score_spt = 0
    score_hum = 0
    score_art = 0
    stress = 0
    semana = 1

# The game starts here.

label start:


    scene bg teste

    # These display lines of dialogue.

    l "texto de teste"

    l "TesteTesteTeste"
    jump semana

label semana:

    scene bg teste

    show tmenu at top:
        zoom 0.7
    show screen stats_screen

    l "O que será que eu posso fazer hoje?"

    show fmenu:
        xalign 0 ypos 180
        xzoom 0.85 yzoom 0.7

    call screen semana_screen

    hide fmenu
    hide tmenu
    hide screen stats_screen


    if _return == 0:
        jump semana_mat
    elif _return == 1:
        jump semana_ling
    elif _return == 2:
        jump semana_nat
    elif _return == 3:
        jump semana_spt
    elif _return == 4:
        jump semana_hum
    else:
        jump semana_art

label semana_mat:

    show link mat at top with dissolve
    l "Estudei Matematica"
    $ score_mat += 5
    jump semana_done

label semana_ling:

    show link lin at top with dissolve
    l "Estudei Linguagens"
    $ score_ling += 5
    jump semana_done

label semana_nat:

    show link nat at top with dissolve
    l "Estudei Ciencias da Natureza"
    $ score_nat += 5
    jump semana_done

label semana_spt:

    l "Fiz Exercícios"
    $ score_spt += 5
    jump semana_done

label semana_hum:

    show link hum at top with dissolve
    l "Estudei Humanidades"
    $ score_hum += 5
    jump semana_done

label semana_art:

    show link art at top with dissolve
    l "Estudei Artes"
    $ score_art += 5
    jump semana_done


label semana_done:
    scene bg casa
    l "Acabou a semana"
    jump semana

    return
