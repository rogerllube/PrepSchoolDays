# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define l = Character("Link")
define p = Character("Professor",
                    who_color = "00f")
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

    show professor intro at right


    p "Bom dia estudantes"
    p "A partir de hoje serei seu professor de matemática do curso preparatório para o Exame Nacional, o EN."
    p "Temos 40 semanas de aulas e vocês podem focar em uma matéria por semana para estudarem aqui no cursinho Kirameki."
    p "Os finais de semana são reservados para simulados a cada 5 semanas, recomendo comparecerem porque os simulados servem para verificar o quanto vocês estão treinados tanto academicamente quanto emocionalmente."
    p "Porém, lembrem-se que não precisam fazer todos os simulados, porque também é importante controlarem a saúde mental."
    p "Usem os dias sem aulas para fazerem alguma atividade que gostem como tocar um instrumento ou passear."
    p "Outro assunto que tenho para falar é a decisão de carreira."
    p "Muitos de vocês já sabem o curso que pretendem fazer enquanto outros estão indecisos."
    p "Para os que já decidiram a área, continuem estudando todas as matérias enquanto focam nas que possuem um peso maior no EN dependendo do curso."
    p "Já em relação aos indecisos, fiquem tranquilos que é bastante normal essa insegurança."
    p "Conforme os dias passam vocês adquirem experiência de vida, consequentemente ficarão mais maduros sobre qual curso escolher."
    p "Lembrem-se que essa decisão acontece depois do EN, então estudem todas as matérias a fim de possuírem um leque grande de possibilidades quando chegar a hora."

    hide professor

    jump semana

label semana:

    scene bg teste

    l "O que será que eu posso fazer hoje?"

    show tmenu at top:
        zoom 0.7
    show screen stats_screen

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

    show link mat at top with dissolve:
        zoom 0.6
    l "Estudei Matematica"
    $ score_mat += 5
    $ stress += 5
    jump semana_done

label semana_ling:

    show link lin at top with dissolve:
        zoom 0.6
    l "Estudei Linguagens"
    $ score_ling += 5
    $ stress += 5
    jump semana_done

label semana_nat:

    show link nat at top with dissolve:
        zoom 0.6
    l "Estudei Ciencias da Natureza"
    $ score_nat += 5
    $ stress += 5
    jump semana_done

label semana_spt:

    show link spt at top with dissolve:
        zoom 0.6
    l "Fiz Exercícios"
    $ score_spt += 5
    $ stress -= 5
    jump semana_done

label semana_hum:

    show link hum at top with dissolve:
        zoom 0.6
    l "Estudei Humanidades"
    $ score_hum += 5
    $ stress += 5
    jump semana_done

label semana_art:

    show link art at top with dissolve:
        zoom 0.6
    l "Estudei Artes"
    $ score_art += 5
    $ stress += 5
    jump semana_done


label semana_done:
    scene bg casa
    l "Acabou a semana"
    $ semana += 1

    if semana % 5 == 0:
        jump simulado
    jump semana

label simulado:

    scene bg teste

    l "Neste final de semana o cursinho realizará um simulado."
    l "Os professores recomendam fazer o simulado não só como forma de medir o nosso conhecimento acadêmico, mas também como forma de treinar o nosso estado emocional."
    l "Devo fazer o simulado?"
    call screen simulado_screen

    if _return == 0:
        jump simulado_sim

    if _return == 1:
        jump simulado_nao

label simulado_sim:

    scene bg teste

    l "Parece uma boa ideia fazer o simulado. Será uma boa forma de saber se estou estudando corretamente para fazer o EN."
    jump semana

label simulado_nao:

    scene bg teste

    l "Acho melhor eu descansar neste final de semana, não é bom fazer prova quando não estou com muita vontade de fazer."

    jump semana

    return
