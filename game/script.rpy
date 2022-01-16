# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define l = Character("[nome_pers]",
                    what_color = "#000")

define p = Character("Professor",
                    who_color = "#00f",
                    what_color = "#000")

define i = Character("[nome_garota]",
                    who_color = "#800080",
                    what_color = "#000")

define t = Character("Tia da Cantina",
                    who_color = "#f00",
                    what_color = "#000")

define x = Character("[nome_garoto]",
                    who_color = "#5e2129",
                    what_color = "#000")

define a = Character("Todos",
                    who_color = "000",
                    what_color = "000")


image fmenu = "menu esquerda.png"
image tmenu = "menu superior.png"
image smenu = "box simulado.png"
image white = Solid("#fff")
image logo = "LogoFoG.png"

image bg sorv = "sorveteria.png"
image bg teste = "escola.jpg"
image bg casa = "casa.jpg"


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
    namorou = 0
    fail = 0
    pro = 0
    jogou = 0
    inst = 0
    saiu = 0
    amigos = 0
    esporte = 0
    simulado = 0
    nome_garota = "Garota Desconhecida"
    nome_garoto = "Xirrark"


# The game starts here

label start:


    scene bg teste:
        xzoom 1.42 yzoom 1.2
        xalign 0.5

    show professor intro:
        xalign 0
        zoom 0.2
        yalign 0.09


    play music musica

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
        zoom 0.4
        yalign 0.3
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
        zoom 0.4
        yalign 0.3
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
        zoom 0.4
        yalign 0.3
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
        zoom 0.4
        yalign 0.3
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
        zoom 0.4
        yalign 0.3
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
        zoom 0.4
        yalign 0.3
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
        yzoom 1.08

    l "Acabou a semana"


    if semana % 5 == 0 and semana != 40:
        jump simulado

    jump fds

label simulado:

    scene bg casa:
        yzoom 1.08

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

    $ simulado += 1

    scene bg teste:
        xzoom 1.42 yzoom 1.2
        xalign 0.5

    l "Parece uma boa ideia fazer o simulado. Será uma boa forma de saber se estou estudando corretamente para fazer o EN."
    jump simulado_calc

label simulado_nao:

    scene bg casa:
        yzoom 1.08

    l "Acho melhor eu descansar neste final de semana, não é bom fazer prova quando não estou com muita vontade de fazer."

    jump fds

label simulado_calc:

    scene bg casa:
        yzoom 1.08

    $ excelentes = 0
    $ boas = 0

    if score_mat > 40 + ((semana/5)-1) * 10:
        $ excelentes += 1
    elif score_mat > 20 + ((semana/5)-1) * 10:
        $ boas += 1

    if score_nat > 40 + ((semana/5)-1) * 10:
        $ excelentes += 1
    elif score_nat > 20 + ((semana/5)-1) * 10:
        $ boas += 1

    if score_hum > 40 + ((semana/5)-1) * 10:
        $ excelentes += 1
    elif score_hum > 20 + ((semana/5)-1) * 10:
        $ boas += 1

    if score_ling > 40 + ((semana/5)-1) * 10:
        $ excelentes += 1
    elif score_ling > 20 + ((semana/5)-1) * 10:
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

    if resultado == 5:
        l "O que estou fazendo aqui? Não aguento essa situação, vou direto para casa."
        l "Preciso de um tempo para pensar no que eu posso fazer."
        jump simulado_fail

    if simulado == 2 and amigos == 0:
        jump evento_amigos_0
        $ amigos = 1
    if amigos == 1:
        jump evento_amigos_1
    if amigos == 2:
        jump evento_amigos_2
    if amigos == 3 and semana > 29:
        jump evento_amigos_3
    jump simulado_fim

label simulado_fim:

    scene bg casa:
        yzoom 1.08

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
    jump semana

label simulado_fail:

    scene white

    centered "{color=#000}Link decidiu dar um tempo e ficou em casa nesta semana.{/color}"
    $ semana += 1
    jump semana

label fds:

    scene bg casa:
        yzoom 1.08


    if semana == 40:
        jump EN

    show tmenu at top:
        zoom 0.7



    show screen stats_screen
    l "Finalmente acabou a semana! O que posso fazer esse final de semana?"

    if namorada == 0 or semana % 5 == 0:
        show fmenu:
            xalign 0 ypos 180
            xzoom 0.85 yzoom 0.9
    else:
        show fmenu:
            xalign 0 ypos 180
            xzoom 1.26 yzoom 0.9
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

    show link mus at top with dissolve:
        zoom 0.4
        yalign 0.3
    l "Devo aproveitar esse fim de semana para continuar treinando as minhas habilidades com violino."
    $ score_mat += 1
    $ score_nat -= 2
    $ score_art += 2
    $ stress -= 2
    $ inst += 1

    jump fds_done

label fds_vid:

    show link gamer at top with dissolve:
        zoom 0.4
        yalign 0.3

    l "Acho que não faz mal jogar um pouco de vez em quando"
    $ score_mat += 2
    $ score_ling += 1
    $ score_spt -= 1
    $ score_art += 1
    $ stress -= 3
    $ jogou += 1

    jump fds_done

label fds_des:

    show link des at top with dissolve:
        zoom 0.4
        yalign 0.3

    l "Desenhar vai ser bem importante para me manter em prática mesmo durante o ano do EN"
    $ score_nat += 1
    $ score_ling -= 2
    $ score_spt -= 2
    $ score_art += 4
    $ stress -= 1

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
    if amigos >= 1:
        $ saiu += 1
    if saiu == 8:
        jump inicio_namoro
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

    show link spt at top with dissolve:
        zoom 0.4
        yalign 0.3
    l "Também é importante praticar esportes para manter minha saúde"
    $ score_spt += 5
    $ stress -= 3
    $ esporte += 1

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
    $ namorou += 1

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

    jump semana

label EN:

    l "Finalmente chegou o dia do EN, agora preciso me concentrar e dar o meu melhor na prova"
    jump curso_calc

label curso_calc:

    if esporte >= 30 and score_mat > 50 and score_nat > 50 and score_ling > 50 and score_hum > 50 and stress < 40:
        jump final_spt

    if jogou >= 30 and score_mat > 50 and score_nat > 50 and score_ling > 50 and score_hum > 50 and stress < 40:
        jump final_espt

    scene white
    centered "{color=#000}Depois de 3 semanas da prova do EN, o dia da divulgação do resultado chegou.{/color}"

    if score_mat > 100 and score_ling > 100 and score_hum > 70 and score_nat > 70 and jogou >= 15 and stress < 60:
        jump final_bcc

    if score_art > 110 and score_hum > 80 and score_mat > 70 and score_ling > 50 and score_nat > 50 and inst >= 20 and stress < 60:
        jump final_mus

    if score_mat > 90 and score_nat > 100 and score_hum > 80 and score_ling > 100 and stress < 60:
        jump final_med

    if score_mat > 110 and score_nat > 110 and score_hum > 60 and score_ling > 60 and stress < 60:
        jump final_eng

    if score_hum > 110 and score_ling > 110 and score_hum > 60 and score_ling > 60 and stress < 60:
        jump final_dir

    if score_spt > 120 and score_mat > 60 and score_nat > 60 and score_ling > 60 and score_hum > 60 and stress < 60:
        jump final_edf

    if score_art > 130 and score_mat > 60 and score_nat > 60 and score_hum > 60 and score_ling > 60 and stress < 60:
        jump final_artcen

    if score_mat > 150 and score_nat > 50 and score_hum > 50 and score_ling > 50 and stress < 60:
        jump final_mat

    if score_hum > 150 and score_nat > 50 and score_mat > 50 and score_ling > 50 and stress < 60:
        jump final_fil

    elif stress >= 60:
        jump stress_fail

    else:
        jump nota_fail

label nota_fail:
    l "Não obtive a nota mínima nem para me candidatar a uma vaga. Por causa do meu péssimo desempenho, terei que começar a trabalhar a fim de bancar um cursinho melhor, já que meus pais não irão pagar um outro cursinho."

    scene white
    centered "{color=#000}[nome_pers] não obteve um bom desempenho neste ano, a decisão de trocar de cursinho pode não ser a melhor possível, porém ele agora possui o objetivo de tentar novamente em um futuro próximo. Talvez o trabalho de meio período seja uma boa experiência para ele. Somente o destino irá dizer.{/color}"
    $ fail = 1
    jump ending

label stress_fail:
    l "Minhas notas foram bem medianas, porém não foram suficientes para garantir uma vaga.  No último dia do cadastro de interesse de vaga, minha posição ficou de fora do limite do número de vagas e há uma dezena de pessoas na minha frente que podem entrar na próxima chamada."
    l "O destino resolveu não me deixar passar neste ano. Pelo menos percebo que tenho a capacidade de passar em um curso, estarei preparado para o próximo EN!!"
    $ fail = 1
    scene white

    if amigos > 0:
        centered "[nome_pers] pode não ter conseguido uma vaga na faculdade, porém os amigos continuam o apoiando nessa dura batalha da sociedade. Agora [nome_pers] já não está tão indeciso quanto estava no ano anterior, mostrando seu amadurecimento durante esse longo ano de estudos."
    else:
        centered "[nome_pers] não conseguiu passar na faculdade, porém ele sabe que o ano não foi em vão, agora ele conhece suas fraquezas e está empenhado em superá-las e ir bem no próximo EN."

    jump ending

label final_eng:
    l "Fechou ontem o período de inscrição, hoje já deve sair o resultado final."
    l "{cps=1}....."
    l "PASSEI!!!"
    l "E pensar que eu conseguiria passar em engenharia."
    l "A área só irei escolher depois de fazer o ciclo básico da faculdade, porém já tenho uma noção sobre cada uma delas que são oferecidas. Mal posso esperar para começar as aulas."

    scene white
    centered "{color=#000}O ano árduo de estudos mostrou seus frutos, Link começará a cursar engenharia com grande entusiasmo nas próximas semanas. Mesmo sendo um curso exaustivo, Link mostrou, durante o preparatório para o EN, a capacidade de superar qualquer barreira para se tornar um ótimo engenheiro."
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

    if jogou >= 1:
        l "E pensar que eu me interessei em direito por causa daquele jogo de advogados gritando objection. Bem, não  que isso seja o único motivo, já que eu fui conversar com ex alunos do cursinho que foram fazer o curso de direito. Eles esclareceram várias das minhas dúvidas sobre a área, ajudando a me decidir em qual curso me candidatar."

    else:
        l "Os ex alunos do cursinho foram de grande ajuda, esclareceram minhas dúvidas sobre o curso. Se não fosse por eles, eu não teria escolhido direito."

    scene white
    centered "Depois de um ano no cursinho Kirameki, o desejado final feliz é concretizado. Percebendo a importância da comunicação, Link mantém contatos com o pessoal do cursinho e com os colegas da faculdade. Dizem que ele tornou-se um famoso advogado anos depois."
    jump ending

label final_edf:

    l "Mantive uma rotina saudável durante o meus dias de estudos, os exercícios físicos que fiz foram de grande ajuda para controlar minha saúde física e mental porque ficar sentado na cadeira toda hora pode estressar muito."
    l "Hoje é o dia do resultado do EN, daqui a alguns minutos sai os resultados."
    l "{cps=1}....."
    l "PASSEI!!!"
    l "Eu realmente não esperava escolher educação física, porém decidi seguir nessa área porque aprendi a importância dos exercícios físicos."

    scene white
    centered "Link aprendeu a importância da rotina saudável durante seus estudos no cursinho Kirameki. A carreira de Educação Física é ampla, indo além do trabalho em academia. Agora Link estudará sobre as atividades físicas que ele tanto fez nesses últimos meses."


    jump ending

label final_artcen:
    l "Fiquei tão interessado em arte neste último ano que comecei a estudar essa área mesmo que não seja muito cobrada no EN. Porém eu não sabia que existia cursos dessa área, já que não são muito comentadas pelo pessoal."
    l " Hoje é o dia do resultado do EN, daqui a alguns minutos sai os resultados."
    l "{cps=1}....."
    l "PASSEI!!!"
    l "Fiquei muito feliz por ter descoberto que existe o curso de Artes Cênicas quando fui fazer a inscrição, agora poderei estudar mais profundamente as produções artísticas."

    scene white
    centered " Link descobriu a área dos seus sonhos. Com a sua grande dedicação, ele tornou-se um grande diretor de vídeos, incentivando a produção nacional com suas obras."

    jump ending

label final_mat:
    l "Hoje vai sair o resultado do EN."
    l "{cps=1}....."
    l "PASSEI no curso de Bacharelado em Matemática."
    l "O professor X foi um dos melhores professores que eu já tive. Ele se importa bastante com o desenvolvimento do raciocínio lógico em vez de lotar as aulas de conteúdo para decorar resolução, graças a ele, fiquei bastante interessado em Matemática."
    scene white
    centered "Link descobriu a beleza da Matemática durante seus estudos no cursinho Kirameki. O seu entusiasmo nos estudos tornou-se famoso no mundo acadêmico, com pesquisas excelentes e aulas bastante adoradas pelos alunos de graduação."
    jump ending

label final_fil:
    l "Hoje vai sair o resultado do EN."
    l "{cps=1}....."
    l "PASSEI no curso de Filosofia."
    l "As aulas de redação e de Filosofia e Sociologia me motivaram a questionar e a argumentar. Depois de uma conversa com os professores, decidi que o curso de Filosofia seria o melhor para mim."

    scene white
    centered "[nome_pers] começou a desenvolver o seu lado crítico neste último ano. O curso de Filosofia é onde ele aprofundará no estudo de filósofos de várias eras, além de desenvolver a sua lógica e argumentação. Tempos depois, ele tornou-se um grande analista de várias obras, além de escritor de artigos nas revistas."

    jump ending

label final_bcc:
    l "Vou jogar aqui uma visual novel até sair o resultado do EN. Melhor relaxar lendo do que ficar ansioso com o resultado."
    l "{cps=1}....."
    l "Parece que chegou a hora do resultado ficar disponível no site, vou lá ver"
    l "PASSEI!!!"
    l "Depois de ter jogado bastante videogame nesse último ano, percebi que fiquei interessado em como programar, passei a ficar vendo como funciona sites e aplicativos."
    l "Ciência da Computação é o curso perfeito para eu entender toda a base de como funciona o computador e de como utilizá-lo para criar programas."

    scene white
    centered "Link passou a ter bastante interesse na lógica por trás dos programas durante seus estudos para o EN. Agora ele poderá focar os estudos nessa área enquanto desenvolve jogos como hobby."
    jump ending

label final_mus:
    l "Neste último ano percebi o quão importante a música é para mim, por isso decidi me inscrever em Música. Daqui a pouco sai o resultado do EN, espero que eu seja aprovado."
    l "{cps=1}....."
    l "PASSEI!!!"
    l "Foi bem concorrida essa vaga, porque, mesmo não possuindo muitos inscritos como medicina, o número de vagas é bem pequeno. Bem, agora que passei, poderei me dedicar em estudar a parte teórica da música nas aulas além de praticar violino."

    scene white
    centered "Link descobriu que pode utilizar o hobby como carreira. Durante o curso de Música, ele fez vários trabalhos freelancer para ganhar experiência, agora ele é famoso pelo seu trabalho como compositor e participa em vários tipos de mídia, desde filmes até videogames"

    jump ending

label final_spt:

    scene white
    centered "[nome_pers] não obteve boas notas no EN, porém...."
    scene bg casa:
        yzoom 1.08
    l "Esse ano foi bem estranho. Entrei no cursinho para me preparar para o EN, porém acabei despertando meu lado atleta."
    l "Frequentei bastante a academia para nadar e o professor me sugeriu entrar na equipe de natação."
    l "Eu consegui acompanhar os treinos puxados a ponto de ir bem em várias competições estaduais. Além disso, passei no curso técnico em gestão pública já que meu treinador sugeriu continuar os estudos."

    scene white
    centered "[nome_pers] curiosamente se tornou um atleta nos próximos anos. A sugestão de continuar os estudos foi importante para estender a sua carreira no esporte, já que depois de se aposentar da competição, [nome_pers] criou o programa regional de apoio à vida esportiva, auxiliando os jovens a seguirem na carreira do esporte."
    $ pro = 1
    jump ending

label final_espt:

    scene white
    centered "[nome_pers] não obteve boas notas no EN, porém...."
    scene bg casa:
        yzoom 1.08

    l "Não achei que fui bem no EN, porém os amigos que fiz na comunidade do jogo Engrenagem Acusada e do Bó Bleiz me alertaram de um ensino técnico em análise de sistemas."
    scene white
    centered "Uma semana depois do EN, [nome_pers] fez a prova do curso técnico."
    scene bg casa:
        yzoom 1.08

    l "Olha só, parece que meu plano B deu certo, não precisarei fazer o cursinho novamente. Ainda bem que fiquei bastante ativo na comunidade de anime fighters, graças ao pessoal de lá, descobri que o EN não é a única prova que existe."
    l "Agora que passei no vestibular do ensino técnico, poderei focar nos torneios online."
    scene white
    centered "[nome_pers] aprendeu a importância do plano B graças à comunidade dos anime fighters."
    centered "Com sua dedicação, ele começou a ir bem em vários torneios nacionais, mas ele não largou o curso técnico a fim de ter um emprego para bancar as viagens internacionais."
    centered "[nome_pers] se tornou um grande jogador e conheceu vários países ao longo de sua carreira."
    $ pro = 1
    jump ending

label evento_amigos_0:

    scene bg sorv:
    show sorvete:
        xalign 0.4 yalign 0.7
    l "Depois de fazer esse simulado, já comecei a bolar estratégias de provas. Não adianta nada eu estudar muito se eu não responder as questões dentro do tempo."
    l "Irei comprar uma coxinha na cantina antes de ir para casa. Só tem uma pessoa na minha frente, não ficarei tanto tempo aqui e"
    l "{cps=1}....."
    l "Aquela garota está comprando uma taça gigante de sorvete!"
    l "Nunca vi essa opção no menu, como sabia que existe esse sundae gigante?"
    i "Ah, ficou curioso com essa sobremesa divina? Depois de eu pedir sorvete com os mesmos complementos várias vezes ano passado, a tia da cantina até decorou os sabores e até batizou com meu nome."
    l "Incrível, vou até pedir um pra mim."
    l "Tia, quanto custa aquela taça de sorvete?"
    t "Parece que ficou curioso com uma de minhas obras primas. Bem, o preço é 15 reais."
    l "Ok, vou querer um, preciso matar minha vontade."
    t "Vai demorar um pouco, mas logo estará pronto."
    "{cps=1}........"
    t "Aqui está, o sorvete da Iliana para o gato curioso."
    $ nome_garota = "Iliana"
    l "Muito obrigado, mal posso esperar pra comer."
    show iliana at left:
        zoom 0.2
        yalign 0.0
    i "{size=32}OOOOOI GATO CURIOSO,{/size} vem aqui na mesa comer seu sorvete."
    l "Gato curioso..."
    l "Não posso negar, sou bastante curioso quando o assunto é comida."
    l "Pelo menos terei companhia enquanto como esse sorvete gigante."
    i "Olá, mais um companheiro do sorvete Iliana, presumo que já deva saber meu nome."
    i "Esse aqui é meu irmão mais novo, Xirrark. Ele não gosta tanto de doces muito doces, sabe como é, pessoas com gosto muito refinado que só comem doces de chá verde."
    show xirrark at right:
        zoom 0.2
        yalign 0.0
    x "Olá, sou Xirrark. Só avisando que também gosto de sorvete, porém não sou fã de colocar um monte de calda, confeitos, chocolate, paçoca, entre outras opções."
    x "Prefiro uma combinação simples sem muito exagero, ao contrário da minha irmã, como você pode ter notado."
    i "Prefiro comer doce com bastante doce e com um bom custo benefício."
    i "Meu irmãozinho gosta daquele sorvete de neve que fica perto daqui. O potinho tem uma cara fofinha, mas o preço é praticamente igual ao daqui e com menos conteúdo."
    x "Parece que alguém não sabe apreciar o sabor refinado do sorvete com mochi, aquilo sim é uma combinação divina que vale o preço a ser pago."
    x "..."
    x "Ah, peço desculpas pela longa conversa sobre sorvete."
    l "Foi muito bom esse papo, deu até vontade de comer esse sorvete de neve."
    l "Desculpe por demorar a me apresentar, mas sou [nome_pers]. Prazer em conhecê-los, Iliana e Xirrark."
    x "Sem problemas."
    i "Já que terminamos as apresentações, o que está achando do meu sorvete?"
    l "Muito bom e muito doce, só não sei se vou conseguir terminar essa montanha de sorvete."
    hide xirrark
    show professor intro:
        xalign 1.0
        zoom 0.2
        yalign 0.09
    p "Olha só, parece que alguém tentou se desafiar com o sorvete Iliana."
    l "Olá professor. Pelo visto você conhece essa enorme taça."
    p "É um famoso desafio aqui no cursinho Kirameki, mesmo que tenha menos de um ano de existência. Pelo visto já conhece a origem da lenda."
    l "E foi por causa dela que estou sofrendo com esse desafio congelante."
    i "Comer meu sorvete não é pra fazer as pessoas sofrerem, mas parece que sou a única que come tudo sem esforço."
    p "Enquanto vocês estão comendo sorvete, irei deixar aqui o gabarito do simulado de hoje. Qualquer dúvida só chamar os professores que eles estarão preparados para atendê-los."
    l "Já estava até esquecendo que fizemos simulado hoje. Antes de eu ir embora com a barriga cheia, podem passar o contato de vocês?"
    hide professor intro
    show xirrark at right:
        zoom 0.2
        yalign 0.0
    x "Claro. O número é esse aqui."
    i "Terminei de comer. Deixa eu digitar o número no seu celular e..."
    i "Pronto. E se prepare para a conversa por sticker com meu irmão. Ele ama mandar stickers fofinhos pelo teregran."
    l "Opa, mais uma fonte de sticker pra mim então."
    l "Obrigado pelos contatos vou indo agora para conferir em casa o gabarito, até mais."
    "{color=#000}Xirrark e Iliana" "Até mais."
    $ amigos = 1

    jump simulado_fim

label evento_amigos_1:

    scene bg teste:
        xzoom 1.42 yzoom 1.2
        xalign 0.5
    show xirrark at right:
        zoom 0.2
        yalign 0.0
    x "Olá [nome_pers], tava pensando em te convidar para comer meu sorvete favorito já que na última vez você teve uns problemas para terminar o sorvete gigante."
    l "Aceito sim, mal posso esperar para comer o sorvete com mochi que você falou na última vez."
    l "A Iliana vai também?"
    l "Ela tinha falado que não gosta de porções pequenas."
    x "Ela vai sim, só precisamos esperar ela voltar do banheiro."
    l "Falando nela, aqui está."
    show iliana at left:
        zoom 0.2
        yalign 0.0
    i "Parece que todos estão aqui para comer sorvete. Estou precisando de açúcar depois desse simulado, então vamos logo."
    l "Acha que o sorvete de lá vai te satisfazer por completo?"
    l "Eu sei que você não gosta de porções pequenas."
    i "Eu economizei durante esse mês para comprar a maior porção, não precisa se preocupar comigo, mas é melhor você conseguir comer tudo da porção pequena."
    l "Ok, ok. Não precisa me lembrar que sofri para comer o desafio do Sorvete Iliana."
    x "Vamos indo que a sorveteria fecha em menos de uma hora."
    scene white
    centered "Chegando na sorveteria"
    scene bg sorv:
    show sorvete:
        xalign 0.4 yalign 0.7
    show xirrark at right:
        zoom 0.2
        yalign 0.0
    show iliana at left:
        zoom 0.2
        yalign 0.0
    x "[nome_pers], a minha recomendação é o que tem mochi, azuki e leite condensado. Vou pegar a porção de 250 mL porque não sou que nem a minha irmã."
    i "Como não sou como meu irmão, vou pegar a porção de 750 mL, que custa o dobro do preço, mas eu como o triplo do sorvete."
    l "Vou seguir a recomendação do Xirrark. Não estou preparado para comer muito hoje."
    "Atendente" "Parece que temos um intruso na famosa dupla de irmãos, em que posso ajudar?"
    l "Parece até que estou andando no meio de celebridades, mas antes de perguntar o contexto vou fazer meu pedido. O de mochi com azuki e leite condensado, 250 mL"
    "Atendente" "Obrigada, o pedido sairá por 15 reais. Agora sobre os irmãos, os funcionários daqui conhecem eles porque falam muito sobre sorvete. O irmão gosta bastante do nosso sorvete, enquanto a irmã reclama da porção, porém nunca falou mal da qualidade."
    x "Minha irmã prioriza quantidade, mas ela nunca critica a alta qualidade do sorvete."
    l "Realmente os dois são barulhentos quando o assunto é sorvete."
    "Atendente" "Pois é, né."
    l "Wow, esse sorvete realmente é fantástico, obrigado Xirrark pela recomendação."
    x "De nada"
    i "Mais um pro time do sorvete de neve."
    l "Relaxa Iliana, no próximo simulado vou pegar o seu sorvete. Não é como se eu não gostasse de sorvete muito doce e gigante."
    x "Eu não consigo comer aquele sorvete, então vou comprar apenas uma coxinha."
    i "Esse meu irmão que não aceita comidas muito doces..."
    l "Talvez eu peça uma coxinha em vez do sorvete, parece uma boa ideia."
    i "Traidor.."
    hide iliana
    hide xirrark
    $ amigos = 2
    jump simulado_fim

label evento_amigos_2:

    show xirrark at right:
        zoom 0.2
        yalign 0.0
    x "Oi [nome_pers], o que achou do simulado de hoje?"
    l "Foi uma prova meio desafiadora, porém estou conseguindo pegar o jeito para resolver a tempo"
    l "Falando em simulado, por que você escolheu filosofia? Com suas notas, poderia almejar um curso mais concorrido."
    x "Eu pensava desse jeito até meu terceiro ano, mas a experiência da minha irmã foi um choque de realidade tanto para mim quanto para ela."
    l "Experiência? Lembro que o sorvete Iliana foi criado ano passado, ela fez alguma coisa entre o fim do ensino médio e o começo dos estudos dela aqui no cursinho Kirameki?"
    x "Você é bem atento aos detalhes de data. Uma coisa que você não sabe é que a Iliana já fez um semestre de Engenharia e algumas semanas de Direito."
    x "Depois de ter saído dos cursos ela retornou para estudar aqui no cursinho Kirameki."
    l "Por que ela saiu desses cursos?"
    x "Bem, o motivo foi...."
    x "Parece que minha irmã acaba de terminar o simulado, melhor deixar ela contar para você o que ela sentiu."
    show iliana at left:
        zoom 0.2
        yalign 0.0
    i "Sobre o que meu irmãozinho e o gato curioso estão falando? O clima aqui não mostra que vocês estavam calados minutos atrás."
    x "O que acha de matar a curiosidade do gato e contar sua experiência na faculdade?"
    x "Especialmente a parte em que descobre que não gosta do curso."
    i "Ah, sim. Primeiro irei falar o motivo de ter escolhido Engenharia."
    l "Qual será o motivo? Parece que é algo bem complexo."
    i "Parecia legal, então escolhi Engenharia. Era uma das opções que vários alunos da minha sala estavam pensando."
    l "Eh????"
    i "Deve ser por isso que eu não continuei o curso. Eu achava desinteressante o ambiente, além de ficar incomodada com a estúpida carga horária, que forçava vários alunos a apenas decorarem resolução de prova porque não havia tempo para estudar e entender o conteúdo."
    i "Depois de perceber que eu não aproveitaria o curso, larguei e vim pro cursinho Kirameki, porém eu não tinha decidido qual curso fazer."
    l "Então escolher um curso por ter muita gente falando não é uma boa ideia afinal?"
    i "Sim, e cometi o mesmo erro escolhendo Direito neste ano. Só fiquei algumas semanas lá e logo voltei pra cá."
    i "O que aprendi foi que faltava maturidade nas minhas escolhas, porém agora já decidi o que cursar depois de pesquisar bastante."
    l "E o que seria?"
    i "Nutrição. Entender o processo fisiológico do corpo humano, os nutrientes dos alimentos, o armazenamento dos ingredientes e o planejamento dos pratos me interessa bastante."
    i "Fico até pensando como não cheguei a essa conclusão antes. Provavelmente por não ter ninguém da minha sala pensando nesse curso isso nem passou pela minha cabeça."
    i "Pelo menos não terei que mexer num programa de desenho, sofrer com aquele negócio e no fim descobrir que quase todo mundo passa sem fazer muita coisa porque se muitos alunos forem reprovados não haveria horários disponíveis para os alunos dos anos seguintes fazerem essa matéria."
    l "Legal que você descobriu algo que encaixa com você. Então é por isso que o Xirrark pretende ir para Filosofia?"
    x "Sim, por causa da minha irmã que eu não fui para medicina depois de terminar o Ensino Médio. Decidi esperar um ano para entender qual curso seria bom para mim, e se eu errasse poderia tentar o EN denovo ou pedir transferência se houvesse alguma similaridade entre os cursos."
    x "No fim, Filosofia foi o que mais me atraiu."
    x "Esperar um ano também não é tão ruim assim, já que conheci uma pessoa louca o suficiente para tentar comer o sorvete Iliana."
    l "Obrigado pelo elogio..."
    x "Depois dessa conversa fiquei com fome. Vou pegar uma coxinha."
    l "Ah sim, vou comer uma coxinha também."
    i "Não ia pedir o sorvete Iliana?"
    l "Verdade, mas dessa vez quero comer uma coxinha."
    i "Traidor..."
    hide iliana
    hide xirrark
    $ amigos = 3
    jump simulado_fim

label evento_amigos_3:

    l "Faltam apenas algumas semanas para o EN. Mesmo depois de fazer vários simulados não estou 100\% seguro."
    show professor intro:
        xalign 1.0
        zoom 0.2
        yalign 0.09
    p "[nome_pers], você parece meio procupado depois de ter feito o simulado de hoje. Pensando em alguma coisa complicada?"
    l "Professor, estou pensando na possibilidade de eu não ir bem no dia da prova. Fico estudando e treinando nos simulados porém sinto que não é o suficiente"
    p "Esse é um sentimento bem comum nas pessoas."
    p "Não necessariamente relacionado ao EN, porém comum quando estamos preocupados com o desempenho em um evento que pode mudar o nosso futuro."
    p "O importante é fazer os 3 seguintes passos: manter a calma, acreditar em si mesmo e aceitar os possíveis resultados."
    l "Não entendi o terceiro passo, qual é a ideia dele?"
    p "Vou começar a explicação com o primeiro e o segundo passos."
    p "Os simulados que realizamos aqui no cursinho Kirameki servem para auxiliar os alunos nesses primeiros dois passos."
    p "Manter a calma a fim de não perder a concentração durante a prova e deixar os estudantes confiantes de que eles conseguem resolver as questões."
    p "Fazemos os simulados em intervalos fixos e elaboramos as provas de modo que a dificuldade seja mais elevada que a do EN"
    l "Não entendo como fico preocupado sendo que estou conseguindo acompanhar os estudos aqui, parece que não é o suficiente apenas entender a matéria."
    p "É aí que está o segredo do terceiro passo. Se a vaga no curso da faculdade fosse garantida com esses dois primeiros passos, o método de estudo que vários cursinhos e vídeos da internet comentam seria o suficiente, porém o número de vagas é limitado."
    p "O que o aluno precisa saber é lidar com a possibilidade de fracassar, o que fazer caso isso ocorra e entender que é normal fracassar."
    p "Tentar denovo no ano seguinte? Se candidatar para a segunda opção em vez da primeira a fim de ingressar na faculdade e fazer transferência caso veja uma oportunidade?"
    p "Dar uma pausa para experienciar outros aspectos importantes da vida além do estudo?"
    p "Esse passo 3 é importante para melhorar a performance dos passos 1 e 2, porque a pressão de ser obrigado a conseguir a vaga desaparece e o estudante pode focar em fazer uma boa prova."
    l "Eu realmente não pensei nesse aspecto de lidar com a possibilidade de não conseguir, porque a Iliana já passou antes na faculdade."
    l "Você pode usar o caso dela como uma outra forma de lidar com o fracasso. Tentar mais uma vez depois de ter escolhido um curso que não gostou é mais uma forma de continuar com a vida."
    p "Portanto, meu conselho é não se cobrar para passar em apenas uma tentativa."
    l "Obrigado professor. Encontrei um jeito de lidar com as minhas preocupações a fim de não prejudicar meu desempenho daqui a algumas semanas."
    $ amigos = 4
    jump simulado_fim

label inicio_namoro:

    scene bg sorv:
    show sorvete:
        xalign 0.4 yalign 0.7
    show xirrark at right:
        zoom 0.2
        yalign 0.0
    x "Pessoal, vou ao banheiro, já volto."
    hide xirrark
    l "Espera, essa é a minha chance de me confessar para a Iliana. Preciso aproveitar essa oportunidade."
    l "Iliana, preciso falar uma coisa para você. Gostaria de {cps=1}..."
    show iliana at left:
        zoom 0.2
        yalign 0.0
    i "Ah, [nome_pers], quer namorar comigo?"
    l "...namorar comigo... espera, eu ia perguntar isso. E você foi tão direta ao ponto que fiquei surpreso."
    i "Então suponho que seja um sim."
    l "Com certeza. Só quero saber como teve essa coragem de se confessar em um instante."
    i "Simples, usei meu irmão como parceiro de treino e fiquei falando com ele várias vezes até eu conseguir dizer sem dificuldades."
    i "Além disso, ele está ali atrás da árvore pra dar uma brecha pra nós."
    x "Parece que tudo correu bem, irmã."
    l "Vocês são a melhor dupla de irmãos que eu já vi."
    $ namorada = 1
    jump fds_done

label ending:

    scene white

    if amigos > 0:
        centered "Xirrark seguiu a carreira de Filosofia e se tornou um ótimo professor incentivando os seus alunos a buscarem o conhecimento."
    if amigos > 0 and namorada == 0:
        centered "Iliana seguiu a carreira de nutricionista depois de decidir o melhor caminho para ela. Seu conhecimento multidisciplinar tornou-se o ponto forte de seu trabalho de controle da qualidade dos alimentos e no planejamento nutricional e econômico nos locais onde trabalhou."
    if namorada == 1 and ( fail == 1 or namorou < 10):
        centered "O relacionamento entre [nome_pers] e Iliana não durou depois do ingresso dela no curso de nutrição, porém eles continuaram grandes amigos seguindo suas próprias carreiras."
        centered "Iliana abriu um consultório e se tornou uma grande profissional"
    if namorada == 1 and fail == 0 and namorou >= 10 and pro == 0:
        centered "Mesmo depois de seguirem carreiras diferentes, Iliana e [nome_pers] mantiveram contato durante os estudos. Após a formatura, os dois foram contratados em sua área de formação."
        centered "Anos depois, se casaram com uma bela cerimônia, é dito que cachoeiras escorriam pelos olhos de Xirrark."

    jump creditos

label creditos:
    centered "Obrigado por jogar PrepSchool Days"
    show logo at center:
        zoom 0.1
        yalign 0.5
    show text "{size=32}Créditos:" at top
    pause 3
    hide logo
    centered "Roteiro: Naoto"
    centered "Programação: Rogério(Sir)"
    centered "Cenário/UI: João Pedro"
    centered "Design de personagem: Henrique Tadashi"
    centerd "Música: Bounce Ball by Twin Musicom (twinmusicom.org)"
    centered "Agradecimentos especiais: thegamelogicist"
    return
