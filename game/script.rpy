# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define l = Character("[nome_pers]",
                    what_color = "#000")


define p = Character("Professor",
                    who_color = "#00f",
                    what_color = "#000")

image fmenu = "menu esquerda.png"
image tmenu = "menu superior.png"
image smenu = "box simulado.png"
image white = Solid("#fff")

image bg teste = "escola.jpg"
image bg casa = "casa.png"


init python:
    score_mat = 30
    score_nat = 30
    score_ling = 30
    score_spt = 30
    score_hum = 30
    score_art = 30
    stress = 0
    semana = 1
    namorada = 0
    jogou = 0


# The game starts here

label start:


    scene bg teste:
        xzoom 1.42 yzoom 1.2
        xalign 0.5

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

    p "Agora, vamos às apresentações"
    "O professor passa pela sala perguntando o nome de cada aluno, até que finalmente chega a sua vez"

    python:
        nome_pers = renpy.input("Qual o seu nome?", length=32)
        nome_pers = nome_pers.strip()

        if not nome_pers:
            nome_pers = "Link"
        with open(os.path.join(renpy.config.gamedir, "relatorio" + nome_pers + ".txt"), 'a') as f:
            f.write( 'Inicio do relatorio\n\n\n' )
        f.close()
    hide professor

    jump semana

label semana:

    scene bg teste:
        xzoom 1.42 yzoom 1.2
        xalign 0.5

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
    scene bg casa:
        zoom 0.36

    l "Acabou a semana"


    if semana % 5 == 0 and semana != 40:
        jump simulado

    jump fds

label simulado:

    scene bg casa:
        zoom 0.36

    l "Neste final de semana o cursinho realizará um simulado."
    l "Os professores recomendam fazer o simulado não só como forma de medir o nosso conhecimento acadêmico, mas também como forma de treinar o nosso estado emocional."
    l "Devo fazer o simulado?"

    show smenu:
        xalign 0.5 yalign 0.5
        xzoom 0.85 yzoom 0.85
    call screen simulado_screen

    if _return == 0:
        $ semana += 1
        jump simulado_sim

    if _return == 1:
        jump simulado_nao

label simulado_sim:

    scene bg teste:
        xzoom 1.42 yzoom 1.2
        xalign 0.5

    l "Parece uma boa ideia fazer o simulado. Será uma boa forma de saber se estou estudando corretamente para fazer o EN."
    jump simulado_calc

label simulado_nao:

    scene bg casa:
        zoom 0.36

    l "Acho melhor eu descansar neste final de semana, não é bom fazer prova quando não estou com muita vontade de fazer."

    jump fds

label simulado_calc:

    scene bg casa:
        zoom 0.36

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
    jump write_log

label simulado_fail:

    scene white

    centered "{color=#000}Link decidiu dar um tempo e ficou em casa nesta semana.{/color}"
    $ semana += 1
    jump write_log

label fds:

    scene bg casa:
        zoom 0.36


    if semana == 40:
        jump EN

    show tmenu at top:
        zoom 0.7



    show screen stats_screen
    l "Finalmente acabou a semana! O que posso fazer esse final de semana?"

    show fmenu:
        xalign 0 ypos 180
        xzoom 0.85 yzoom 0.9
    call screen fds_screen

    hide tmenu
    hide fmenu
    hide screen stats_screen

    if _return == 0:
        jump fds_rev
    elif _return == 1:
        jump fds_mus
    elif _return == 2:
        jump fds_vid
    elif _return == 3:
        jump fds_des
    elif _return == 4:
        jump fds_sair
    elif _return == 5:
        jump fds_fes
    elif _return == 6:
        jump fds_esp
    elif _return == 7:
        jump fds_desc
    else:
        jump fds_nam

label fds_rev:

    l "Estou bem cansado, mas preciso revisar os conteúdos da semana."
    $ score_mat += 1
    $ score_hum += 1
    $ score_nat += 1
    $ score_ling += 1
    $ score_art += 1
    $ stress += 3

    jump fds_done

label fds_mus:

    l "Não posso esquecer de praticar meus instrumentos"
    $ score_mat += 1
    $ score_nat -= 2
    $ score_art += 2
    $ stress -= 2

    jump fds_done

label fds_vid:

    l "Acho que não faz mal jogar um pouco de vez em quando"
    $ score_mat += 2
    $ score_ling += 1
    $ score_spt -= 1
    $ score_art += 1
    $ stress -= 3
    $ jogou = 1

    jump fds_done

label fds_des:

    l "Desenhar vai ser bem importante para me manter em prática mesmo durante o ano do EN"
    $ score_mat += 1
    $ score_hum += 1
    $ score_nat += 1
    $ score_ling += 1
    $ score_spt -= 1
    $ score_art += 4
    $ stress -= 2

    jump fds_done

label fds_sair:

    l "Preciso sair de casa para relaxar um pouco"
    $ score_mat -= 1
    $ score_hum -= 1
    $ score_nat -= 1
    $ score_ling -= 1
    $ score_spt -= 1
    $ score_art -= 1
    $ stress -= 6

    jump fds_done

label fds_fes:

    l "Vai ter uma festa esse final de semana, acho que seria bem legal ir"
    $ score_mat -= 1
    $ score_hum -= 1
    $ score_nat -= 1
    $ score_ling -= 1
    $ score_spt -= 1
    $ score_art -= 1
    $ stress -= 6

    jump fds_done

label fds_esp:

    l "Também é importante praticar esportes para manter minha saúde"
    $ score_spt += 5
    $ stress -= 3

    jump fds_done

label fds_desc:

    l "Estou exausto, preciso de um descanso esse final de semana"

    $ stress -= 4

    jump fds_done

label fds_nam:

    l "Vou sair com a minha namorada"

    $ score_mat -= 1
    $ score_hum -= 1
    $ score_nat -= 1
    $ score_ling -= 1
    $ score_spt -= 1
    $ score_art -= 1
    $ stress -= 6

    jump fds_done

label fds_done:

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

    l "Acabou o final de semana."
    $ semana += 1

    jump write_log

label write_log:
    python:

        with open( os.path.join(renpy.config.gamedir, "relatorio" + nome_pers + ".txt" ), 'a') as f:
            f.write('Semana: ' + str(semana-1) + '\nMatematica: ' + str(score_mat) + '\nLinguagens: ' + str(score_ling) + '\nNatureza: ' + str(score_nat) + '\nHumanas: ' + str(score_hum) + '\nArte: ' + str(score_art) + '\nEsportes: ' + str(score_spt))
            f.write('\nStress: ' + str(stress) + '\n\n\n')
        f.close()

    jump semana

label EN:

    l "Finalmente chegou o dia do EN, agora preciso me concentrar e dar o meu melhor na prova"

    python:

        with open(os.path.join(renpy.config.gamedir, "relatorio" + nome_pers + ".txt" ), 'a') as f:
            f.write('Semana: ' + str(semana) + '\nMatematica: ' + str(score_mat) + '\nLinguagens: ' + str(score_ling) + '\nNatureza: ' + str(score_nat) + '\nHumanas: ' + str(score_hum) + '\nArte: ' + str(score_art) + '\nEsportes: ' + str(score_spt))
            f.write('\nStress: ' + str(stress) + '\n\n\n')
        f.close()
    scene white
    centered "{color=#000}Depois de 3 semanas da prova do EN, o dia da divulgação do resultado chegou.{/color}"
    jump curso_calc

label curso_calc:

    if (score_mat + score_nat + score_hum + score_ling) < 200:
        jump nota_fail

    if (score_mat + score_nat + score_hum + score_ling) > 200 and stress > 80:
        jump stress_fail

    if score_mat > 100 and score_nat > 100 and score_hum > 80 and score_ling > 80 and stress < 80:
        jump final_med

    if score_mat > 100 and score_nat > 100 and stress < 80:
        jump final_eng

    if score_hum > 100 and score_ling > 100 and stress < 60:
        jump final_dir



label nota_fail:
    l "Não obtive a nota mínima nem para me candidatar a uma vaga. Por causa do meu péssimo desempenho, terei que começar a trabalhar a fim de bancar um cursinho melhor, já que meus pais não irão pagar um outro cursinho."

    scene white
    centered "{color=#000}[nome_pers] não obteve um bom desempenho neste ano, a decisão de trocar de cursinho pode não ser a melhor possível, porém ele agora possui o objetivo de tentar novamente em um futuro próximo. Talvez o trabalho de meio período seja uma boa experiência para ele. Somente o destino irá dizer.{/color}"
    jump ending

label stress_fail:
    l "Minhas notas foram bem medianas, porém não foram suficientes para garantir uma vaga.  No último dia do cadastro de interesse de vaga, minha posição ficou de fora do limite do número de vagas e há uma dezena de pessoas na minha frente que podem entrar na próxima chamada."
    l "O destino resolveu não me deixar passar neste ano. Pelo menos percebo que tenho a capacidade de passar em um curso, estarei preparado para o próximo EN!!"
    jump ending

label final_eng:
    l "Fechou ontem o período de inscrição, hoje já deve sair o resultado final."
    l "{cps=1}....."
    l "PASSEI!!!"
    l "E pensar que eu conseguiria passar em engenharia."
    l "A área só irei escolher depois de fazer o ciclo básico da faculdade, porém já tenho uma noção sobre cada uma delas que são oferecidas. Mal posso esperar para começar as aulas."

    scene white
    centered "{color=#000}O ano árduo de estudos mostrou seus frutos, Link começará a cursar engenharia com grande entusiasmo nas próximas semanas. Mesmo sendo um curso exaustivo, Link mostrou ,durante o preparatório para o EN, a capacidade de superar qualquer barreira para se tornar um ótimo engenheiro."
    jump ending

label final_med:

    l "Ahhhh, site, ATUALIZA."
    l "Isso que dá ter me candidatado para medicina, a concorrência extremamente alta com notas absurdas em todas as áreas está me deixando nervoso."
    l "Fico feliz de ter me identificado com a área durante o ano no cursinho Kirameki, eu não pensava inicialmente em seguir a área da saúde, porém as pesquisas que fiz me motivaram a fazer essa escolha."
    l "Opa, parece que o F5 deu certo agora."
    l "{cps=1}....."
    l "PASSEI!!!"
    l "O meu eu do ano passado nunca imaginaria que estaria comemorando a vaga em medicina. O cursinho Kirameki realmente me ajudou na preparação. Minha dedicação aos estudos durante esse ano realmente fez diferença, mas não posso esquecer os domingos de folga, essenciais para o controle da minha saúde mental."

    scene white
    centered "Link, surpreso com o resultado, começará a estudar medicina nas próximas semanas. A rotina de estudos controlada foi efetiva, porém ela não será abandonada na faculdade. Link, sabendo da importância do equilíbrio, continua a sua rotina a fim de aproveitar bem a faculdade e de se tornar um excelente médico."
    jump ending

label final_dir:

    l "PASSEI!!!"

    if jogou == 1:
        l "E pensar que eu me interessei em direito por causa daquele jogo de advogados gritando objection. Bem, não  que isso seja o único motivo, já que eu fui conversar com ex alunos do cursinho que foram fazer o curso de direito. Eles esclareceram várias das minhas dúvidas sobre a área, ajudando a me decidir em qual curso me candidatar."

    else:
        l "Os ex alunos do cursinho foram de grande ajuda, esclareceram minhas dúvidas sobre o curso. Se não fosse por eles, eu não teria escolhido direito."

    scene white
    centered "Depois de um ano no cursinho Kirameki, o desejado final feliz é concretizado. Percebendo a importância da comunicação, Link mantém contatos com o pessoal do cursinho e com os colegas da faculdade. Dizem que ele tornou-se um famoso advogado anos depois."
    jump ending

label final_edf:


    jump ending

label final_artcen:

    jump ending

label final_mat:

    jump ending

label final_fil:

    jump ending

label final_bcc:

    jump ending

label final_mus:

    jump ending

label final_spt:

    jump ending

label final_espt:

    jump ending

label ending:

    scene white

    centered "Acabou o jogo :´("

    return
