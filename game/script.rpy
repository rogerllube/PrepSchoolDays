# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define l = Character("Link")
define p = Character("Professor",
                    who_color = "00f")
image fmenu = "menu esquerda.png"
image tmenu = "menu superior.png"
image white = Solid("#fff")


init python:
    score_mat = 35
    score_nat = 35
    score_ling = 100
    score_spt = 100
    score_hum = 100
    score_art = 100
    stress = 0
    semana = 5

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

    l "O que será que eu posso fazer essa semana?"

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
    $ score_mat += 4
    $ score_hum += 1
    $ score_nat += 3
    $ score_ling += 1
    $ score_spt -= 3
    $ stress += 5
    jump semana_done

label semana_ling:

    show link lin at top with dissolve:
        zoom 0.6
    l "Estudei Linguagens"
    $ score_mat += 0
    $ score_hum += 2
    $ score_nat += 0
    $ score_ling += 4
    $ score_spt -= 2
    $ stress += 3
    jump semana_done

label semana_nat:

    show link nat at top with dissolve:
        zoom 0.6
    l "Estudei Ciencias da Natureza"
    $ score_mat += 3
    $ score_hum += 1
    $ score_nat += 4
    $ score_ling += 1
    $ score_spt -= 3
    $ stress += 5
    jump semana_done

label semana_spt:

    show link spt at top with dissolve:
        zoom 0.6
    l "Fiz Exercícios"
    $ score_mat -= 1
    $ score_hum -= 1
    $ score_nat -= 1
    $ score_ling -= 1
    $ score_art -= 1
    $ score_spt += 5
    $ stress += 1
    jump semana_done

label semana_hum:

    show link hum at top with dissolve:
        zoom 0.6
    l "Estudei Humanidades"
    $ score_mat += 0
    $ score_hum += 4
    $ score_nat += 0
    $ score_ling += 1
    $ score_spt -= 2
    $ stress += 3
    jump semana_done

label semana_art:

    show link art at top with dissolve:
        zoom 0.6
    l "Estudei Artes"
    $ score_mat += 1
    $ score_hum += 1
    $ score_nat += 1
    $ score_ling += 1
    $ score_spt -= 1
    $ score_art += 4
    $ stress -= 2
    jump semana_done


label semana_done:
    if stress < 0:
        $ stress = 0
    if score_mat < 0:
        $ score_mat = 0
    if score_nat < 0:
        $ score_nat = 0
    if score_hum < 0:
        $ score_hum = 0
    if score_ling < 0:
        $ score_ling = 0
    if score_art < 0:
        $ score_art = 0
    if score_spt < 0:
        $ score_spt = 0
    scene bg casa

    l "Acabou a semana"


    if semana % 5 == 0:
        jump simulado

    $ semana += 1
    jump semana

label simulado:

    scene bg casa

    l "Neste final de semana o cursinho realizará um simulado."
    l "Os professores recomendam fazer o simulado não só como forma de medir o nosso conhecimento acadêmico, mas também como forma de treinar o nosso estado emocional."
    l "Devo fazer o simulado?"

    call screen simulado_screen

    if _return == 0:
        $ semana += 1
        jump simulado_sim

    if _return == 1:
        $ semana += 1
        jump simulado_nao

label simulado_sim:

    scene bg teste

    l "Parece uma boa ideia fazer o simulado. Será uma boa forma de saber se estou estudando corretamente para fazer o EN."
    jump simulado_calc


label simulado_nao:

    scene bg casa

    l "Acho melhor eu descansar neste final de semana, não é bom fazer prova quando não estou com muita vontade de fazer."

    jump semana

label simulado_calc:

    scene bg casa

    $ excelentes = 0
    $ boas = 0

    if score_mat > 50:
        $ excelentes += 1
    elif score_mat > 30:
        $ boas += 1

    if score_nat > 50:
        $ excelentes += 1
    elif score_nat > 30:
        $ boas += 1

    if score_hum > 50:
        $ excelentes += 1
    elif score_hum > 30:
        $ boas += 1

    if score_ling > 50:
        $ excelentes += 1
    elif score_ling > 30:
        $ boas += 1

    if excelentes == 4 and stress < 50:
        $ resultado = 0

    elif (boas + excelentes) == 4 and stress < 50:
        $ resultado = 1

    elif (boas + excelentes) >= 2 and stress < 50:
        $ resultado = 2

    elif (boas + excelentes) >= 2 and stress >= 50:
        $ resultado = 3

    elif (boas + excelentes) <= 1 and stress < 50:
        $ resultado = 4

    elif (boas + excelentes) <= 1 and stress >= 50:
        $ resultado = 5


    if resultado <= 2:
        l "Bem legal o cursinho já disponibilizar o gabarito no mesmo dia do simulado, já posso verificar meus acertos agora mesmo."

        if resultado == 0:
            l "Consegui! Só preciso manter esse desempenho que estarei preparado para o EN."

        if resultado == 1:
            l "Até que fui bem no simulado, consigo passar em alguns cursos com essa nota."

        if resultado == 2:
            l "Estou indo bem em certas áreas, porém eu ainda possuo fraquezas. Posso focar nas matérias que domino para concorrer a uma vaga em cursos mais especializados ou posso focar nas matérias que não me dou bem e tentar uma vaga para um curso mais concorrido."
        l "O resultado de hoje me mostrou que estou estudando bem, mas não posso relaxar, devo manter esse ritmo até o dia do EN"

    elif resultado == 3:
        l "Já distribuíram o gabarito aqui na saída do cursinho, irei verificar aqui mesmo."
        l "Ué, errei varias por bobeira, vi aqui que pensei na resolução correta, porém marquei errado porque não prestei atenção na pergunta e nas alternativas."
        l "Foi bom ter feito esse simulado, se não fosse por isso eu teria ido mal no EN por falta de atenção. Devo controlar bem minha rotina para não passar por essa situação de novo."

    elif resultado == 4:
        l "Não sinto que fui bem, mas irei dar uma olhada no gabarito já que o funcionário daqui está distribuindo o papel com as respostas certas."
        l "Fui mal, eu realmente errei um monte de questões por não saber o conteúdo. Devo verificar o meu método de estudo caso eu queira passar no EN."
        l "Meus pais estão bancando meus estudos, não posso continuar nesse estado, devo mudar minha rotina de estudo a fim de aproveitar que tenho o privilégio de estudar no cursinho Kirameki."

    elif resultado == 5:
        l "O que estou fazendo aqui? Não aguento essa situação, vou direto para casa."
        l "Preciso de um tempo para pensar no que eu posso fazer."
        jump simulado_fail

    jump semana

label simulado_fail:

    scene white

    centered "{color=#000}Link decidiu dar um tempo e ficou em casa nesta semana.{/color}"
    $ semana += 1
    jump semana

    return
