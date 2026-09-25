"""Ajustes editoriais encontrados pelos leitores simulados (idempotentes)."""
from pathlib import Path
import json
P=Path(__file__).resolve().parent
bp=P/'context/conteudo-base.json'; dp=P/'context/aulas-editoriais.json'
b=json.loads(bp.read_text()); ds=json.loads(dp.read_text())
def topic(m,t,**changes):b['modules'][m-1]['topics'][t-1].update(changes)

topic(1,3,practice='Escolha fotos próprias ou autorizadas. Nomeie cada uma pela função: produto, composição ou luz. Se não tiver uma foto, fotografe agora um objeto inteiro sobre fundo simples. Escreva o que aproveitar e o que ignorar em cada imagem.')
topic(1,5,concept='Guarde a imagem, o pedido e as referências no mesmo lugar. Registre o nome da ferramenta e a data. Acrescente configurações somente quando souber quais foram usadas. Isso forma uma receita para revisar o trabalho.',caution='Um número inicial de aleatoriedade não substitui referências. Quando esse controle existir, leia sua explicação na própria ferramenta.')
topic(2,2,practice='Abra uma foto própria na galeria. Observe o objeto inteiro e depois amplie a alça ou outro detalhe com o gesto de pinça. Escreva dois pedidos: produto inteiro e detalhe. Ampliar a visualização não cria informação nova.')
topic(2,3,practice='Ponha um objeto perto de uma janela. Observe a borda da sombra. Compare com a sombra de uma lanterna, se tiver uma. Escreva a origem da luz e se a sombra termina de modo suave ou marcado.',caution='A ilustração é um exemplo para observar. Na sua geração, confira sombra e reflexo: o resultado pode contrariar o pedido.')
topic(2,5,practice='Desenhe um retângulo no papel. Reserve uma parte para o título e outra para o produto. Compare com um desenho centralizado. Na ilustração da aula, cubra a área vazia com o dedo e confira se a caneca continua visível.')
topic(2,6,concept='Estilo é um conjunto de escolhas de cor, luz, textura e organização do quadro. Escreva cada escolha numa linha. A ficha da prática mostra como juntar as decisões num pedido legível.',practice='Troque elegante por escolhas visíveis: fundo simples, luz suave, poucos objetos e acabamento fosco. Reúna as decisões usando a ficha copiável desta aula. Guarde o texto junto da imagem.')
topic(3,1,concept='Proporção é a relação entre largura e altura. Um quadrado tem proporção 1:1. Resolução é a dimensão em pontos da imagem, chamados pixels. Arquivos de 512 por 512 e 1024 por 1024 pontos continuam quadrados.',practice='Observe as molduras quadrada e vertical da ilustração. Escolha o formato exigido pelo destino da peça. No arquivo salvo, abra Informações ou Detalhes para conferir largura e altura.')
topic(3,2,concept='Identidade é a aparência que faz você reconhecer o mesmo produto. Estilo é a linguagem de cor, luz e textura da cena. Uma foto da caneca orienta sua forma. Outra imagem pode orientar só a luz, sem trocar o objeto.',caution='Os recursos de referência variam entre ferramentas. Leia a ajuda da sua interface e use uma foto por vez se houver mistura de objetos.')
topic(3,2,why='Separar essas funções evita trocar a aparência do produto ao pedir uma nova atmosfera. Confira primeiro a identidade e depois a luz e as cores.')
topic(3,3,concept='Algumas ferramentas deixam você ajustar a liberdade de interpretação do estilo. Um valor diferente pode mudar cor, fundo ou acabamento. Observe o efeito numa pequena comparação. O nome e a escala do ajuste dependem da ferramenta.')
topic(3,4,title='Ajustes de processamento, texto e edição',concept='Algumas ferramentas mostram quantidade de etapas de cálculo, influência do texto ou força de edição. Mais etapas não garantem uma imagem melhor. A força de edição pode mudar quanto da imagem original é preservado. Leia a descrição de um controle e teste só ele.',caution='Na interface, esses controles podem aparecer como steps, guidance ou força de edição. São nomes de ajustes diferentes. Não copie valores entre ferramentas esperando o mesmo resultado.')
topic(3,5,caution='O número inicial ajuda em certos testes, mas não guarda uma pessoa ou estilo. Mantenha a referência do produto e confira o resultado.')
topic(3,6,practice='Preencha a ficha copiável da prática desta aula. Inclua pedido, referência, formato, ferramenta e controles disponíveis. Marque como a testar quando ainda não tiver executado a receita.')
topic(4,2,practice='Escolha uma foto própria de objeto inteiro e confira contorno, cor e alça ou outra parte importante. Salve a referência aprovada com um nome estável. Se o trabalho incluir pessoa, use referência autorizada e com rosto visível.')
topic(4,4,practice='Use a ficha copiável da prática desta aula seis vezes, uma por cena. Registre função, enquadramento, referência e características fixas. Comece pela peça mais simples quando for executar a produção.')
topic(5,2,practice='Desenhe no papel o contorno da imagem e circule a região com defeito. Escreva preservar nas outras áreas. Se editar numa ferramenta, marque a região com uma pequena margem e confira o resultado inteiro.')
topic(6,4,practice='Observe primeiro a miniatura. Abra depois no tamanho previsto para publicação. Por fim, amplie uma borda ou textura. Anote um problema por escala ou registre que o critério foi atendido.')
topic(6,6,practice='Avalie forma, luz, composição e coerência. Para cada critério: zero significa falha; um, precisa revisar; dois, atende. Anote uma evidência por nota. A aula 20 mostra a ficha completa.')
topic(7,1,practice='Use as cinco linhas que você escreveu na aula 1, na ficha da prática. Se pulou aquela aula, escreva produto, público, uso, intenção e três características obrigatórias. Defina a função das três peças antes de gerar.')
topic(7,3,concept='Uma rubrica é uma lista de critérios para avaliar o trabalho. Neste projeto usamos forma, luz, composição e coerência. Zero indica falha; um, precisa revisar; dois, atende. Escreva uma evidência por nota e destaque problemas que impedem o uso.')
topic(7,5,practice='Separe três pastas: finais, referencias e registro. Use nomes que indiquem função e versão. Inclua um arquivo de texto com as instruções de uso e as limitações. Guarde as imagens separadamente da exportação de progresso do curso.',caution='O progresso fica no navegador. A cópia de segurança da jornada não inclui suas imagens externas. Guarde os dois conjuntos de arquivos.')

for m in b['modules']:
    m['prompt']=m['prompt'].replace('alça oval à direita','alça oval visível e inteira').replace('janela à esquerda','janela lateral').replace('janela grande à esquerda','janela grande lateral')
b['modules'][2]['prompt']='Use uma foto própria da caneca como referência. Se não tiver, fotografe um objeto inteiro agora. Preserve forma, cor e alça. Crie uma imagem quadrada com fundo creme e luz suave lateral. Deixe o produto inteiro. Sem texto.'
b['modules'][1]['prompt']='Fotografia de uma caneca artesanal terracota com uma única alça oval visível e inteira. Mesa clara, caneca inteira e margem ao redor. Câmera na altura da borda. Luz de janela lateral e sombra suave no lado oposto à fonte. Esmalte fosco com pequenas irregularidades, sem rachaduras. Fundo creme simples. Produto na metade inferior e espaço livre acima para um título posterior. Formato horizontal 4:3. Sem texto.'
b['modules'][4]['prompt']='Edite uma cópia da imagem fornecida. Preserve o produto, sua escala e sua cor. Amplie apenas o ambiente para um quadro horizontal. Continue o fundo e a mesa sem acrescentar objetos. Mantenha uma sombra coerente junto da base.'

ds[0]['campos']=['Produto: caneca terracota com uma alça','Público: compradores de cerâmica','Uso: catálogo quadrado','Intenção: mostrar a forma com clareza','Obrigatório: contorno inteiro, fundo creme e uma alça']
ds[0]['confira']='Agora confira as cinco linhas do pedido. Quando gerar a imagem, compare o resultado com elas. Uma alça cortada reprova uma peça que deveria mostrá-la inteira.'
ds[1]['passos'][2]='Observe a caneca da ilustração desta aula ou uma imagem sua. Nas Notas, marque forma, luz e espaço livre como atende ou precisa revisar. Justifique uma decisão.'
ds[1]['pronto']='cada referência tem uma função e uma imagem foi avaliada pelos três critérios'
ds[1]['molde']='Referência A: aproveitar <característica>; ignorar <restante>.\nReferência B: aproveitar <característica>; ignorar <restante>.\nImagem observada: <qual>.\nForma: <atende ou revisar + motivo>.\nLuz: <atende ou revisar + motivo>.\nEspaço livre: <atende ou revisar + motivo>.'
ds[2]['molde']='Data: <dia>\nArquivo: <nome>\nFerramenta e versão: <nome ou desconhecido>\nPedido usado: <texto>\nDefeito: <um problema>\nAlterar: <uma decisão>\nPreservar: <duas características>'
ds[2]['passos'][0]='Escolha uma imagem sua. Sem imagem, observe as duas fotos nas mãos de Mauro na ilustração: uma não mostra a alça inteira.'
ds[4]['ex2']='Mauro coloca a caneca perto da janela para fotografar. Ele observa a sombra suave e as pequenas variações da superfície fosca.'
ds[4]['passos'][2]='Escreva um pedido com fonte, sombra e dois sinais da superfície. Exemplo: janela lateral, sombra suave, esmalte fosco e pequenas irregularidades.'
ds[4]['confira']='Confira se o acabamento pedido permaneceu. Cerâmica pode ser brilhante, mas uma peça definida como fosca não deve virar uma superfície espelhada.'
ds[5]['passos'][2]='Confira no pedido o lugar previsto para produto e título. Na ilustração desta aula, cubra a área vazia com o dedo. A caneca deve continuar visível.'
ds[6]['campos'][0]='Formato: 512 × 512 e 1024 × 1024 continuam quadrados (1:1)'
ds[6]['passos'][0]='Escolha onde a imagem será usada. Anote o formato exigido: por exemplo quadrado 1:1, horizontal 4:3 ou vertical 9:16.'
ds[6]['opcoes']=['O formato virou vertical','O detalhe virou garantido','A dimensão em pixels']
ds[8]['molde']='Nome: catálogo suave. Estado: a testar.\nPedido: caneca terracota inteira, fundo creme, janela lateral suave, sem texto.\nFormato: quadrado 1:1.\nReferência: minha-foto-da-caneca.\nModelo: <nome observado ou desconhecido>.\nControles: <valores disponíveis ou não disponíveis>.\nCritérios: uma alça inteira, fundo simples e sombra suave.'
ds[11]['passos'][1]='Anote diferenças intencionais e problemas de identidade. Se suas três fotos estiverem corretas, registre isso e observe a foto da caneca azul na ilustração da aula.'
ds[11]['passos'][2]='Escreva uma correção para a peça problemática. Sem defeitos na sua série, use o caso da caneca azul e peça para restaurar terracota, mantendo a forma.'
ds[14]['entrega']='planejar texto em camada separada e registrar o plano de uma comparação'
ds[14]['resumo'][2]='Planeje uma comparação com recorte semelhante.'
ds[15]['passos'][0]='Escolha uma imagem e anote seu destino. Na galeria, procure o símbolo i ou as opções Informações e Detalhes. Veja largura e altura.'
ds[15]['molde']=ds[15]['molde'].replace('<exigência do destino>','<exigência conhecida ou a confirmar>')
ds[17]['passos'][0]='Abra uma foto própria na galeria. Use Editar e depois Salvar cópia, se disponível. Se só houver Salvar, duplique a foto antes para proteger a original.'
ds[17]['passos'][1]='Abra a cópia. Procure i, Informações ou Detalhes para ver dimensões e formato. Se não souber a exigência do destino, marque como a confirmar.'
ds[18]['passos'][0]='Use a ficha que escreveu na prática da aula 1. Se pulou, escolha agora um produto próprio ou a caneca Aurora. Anote produto, público, uso, intenção e limites.'
ds[19]['tarefa']='Faça e documente uma correção de enquadramento'
ds[19]['passos']=['Escolha uma foto própria com área sobrando. Abra na galeria, duplique ou escolha Salvar cópia antes de editar. Guarde o original.', 'Em Editar, procure Cortar ou Recortar. Reduza apenas o espaço que distrai, sem cortar partes necessárias do objeto. Salve uma nova cópia.', 'Compare original e cópia na galeria. Dê notas de zero a dois para forma, luz, composição e coerência. Registre a mudança e uma evidência. Se piorou, mantenha o original.']
ds[19]['pronto']='uma edição real foi comparada ao original e tem uma decisão justificada'
ds[19]['molde']=ds[19]['molde'].replace('Revisão proposta: <mudança>','Revisão realizada: <mudança ou tentativa desfeita>').replace('Conferência: <o que deve melhorar>','Conferência: <o que melhorou ou piorou>')
ds[19]['calma']='Não encontrou recortar? Procure em Editar na galeria. Se a opção não existir, deixe a prática pendente até usar um editor disponível. Não registre uma edição que não fez.'
ds[20]['passos'][0]='Abra Arquivos no celular e procure Nova pasta. No computador, use o botão Nova pasta. Crie finais, referencias e registro dentro da pasta do projeto.'

captions=[
'A caneca é o assunto; o papel claro é o fundo; a placa branca devolve luz. São decisões separadas.',
'As fotos da mesa mostram forma, ambiente e luz. Uma referência de ambiente não precisa trocar o objeto.',
'Nas fotos que Mauro segura, uma alça não aparece inteira. A comparação ajuda a nomear um defeito específico.',
'A moldura recorta o produto. Observe quanto do objeto e do ambiente permanece dentro dela.',
'Compare a superfície que Joana aponta com os reflexos da outra peça. Acabamento fosco e brilho são sinais observáveis.',
'A área clara acima do produto pode receber um título. Cubra esse espaço com o dedo: o produto continua visível.',
'A moldura quadrada e a vertical mostram formatos diferentes. Mais pixels não transformam um quadrado em retângulo.',
'Duas imagens com acabamento diferente ajudam a escolher um critério. A ilustração não mostra controles de uma ferramenta real.',
'Foto aprovada e amostras de cor ficam juntas. A referência faz parte da receita, junto do texto do pedido.',
'Compare o objeto e a referência. Forma, cor e alça precisam ser visíveis para orientar a série.',
'Cada quadro tem uma função: ambiente, escolha, uso, detalhe, conjunto e encerramento. Planejar não equivale a gerar as peças finais.',
'A peça azul destoa das duas terracota. Aqui a cor é o problema; variar o enquadramento seria uma escolha possível.',
'A pequena marcação cobre a mancha do fundo. O restante do objeto deve ser protegido durante a correção.',
'O fundo cresce ao redor do quadro original. O objeto não precisa ser esticado para caber num formato horizontal.',
'A folha transparente representa uma camada separada. A imagem limpa continua guardada para outra composição.',
'A lupa ajuda a comparar a textura da referência. Uma ampliação pode criar detalhes que não existiam na imagem original.',
'Miniatura, imagem normal e detalhe ampliado respondem a perguntas diferentes sobre a mesma peça.',
'A imagem é conferida no celular, no tamanho de uso. A cópia original permanece separada para futuras edições.',
'Três peças com funções diferentes: produto inteiro, detalhe e uso. As características principais devem permanecer.',
'As duas versões mostram o problema de recorte e a revisão. Julgue também se o produto mudou além do que foi pedido.',
'As três peças finais ficam separadas das referências. A organização ajuda quem recebe a entender o conjunto.'
]
for d,caption in zip(ds,captions):d['observacao']=caption
bp.write_text(json.dumps(b,ensure_ascii=False,indent=2)+'\n');dp.write_text(json.dumps(ds,ensure_ascii=False,indent=2)+'\n')
print('Revisão editorial aplicada às 21 aulas.')
# Rodada 3: coerência entre prática, exemplo e conferência.
b['modules'][2]['verify']='Antes de gerar, anexe uma foto própria do objeto. Depois compare forma e posição. Registre qualquer outra diferença que apareceu.'
topic(3,4,why='Cada ferramenta define seus próprios ajustes. Um valor que funciona numa pode falhar em outra. Comece no padrão e observe uma mudança de cada vez.')
ds[1]['confira']='A encomenda deste exercício é uma caneca com alça inteira, luz suave e área livre acima. Compare a imagem com esses três requisitos. Uma referência de luz não deve trocar o produto.'
ds[1]['passos'][2]='Avalie a caneca da ilustração ou uma imagem sua: a alça está inteira, a luz é suave e há área livre acima? Marque atende ou precisa revisar para cada requisito e justifique uma decisão.'
ds[7]['molde']='Exemplo sem controle na interface:\nA: caneca terracota inteira, fundo creme, luz suave, aparência de fotografia.\nB: caneca terracota inteira, fundo creme, luz suave, aparência de aquarela.\nVariável: apenas a instrução de estilo.\nManter: produto, referência, formato e luz.\nComparar: contorno da alça e textura.\nLimite: duas tentativas. Estado: planejado.\n\nSe houver um controle de estilo:\nNome e função: <leia na ferramenta>.\nValor A: <padrão>. Valor B: <pequena mudança>.\nManter: <pedido, referência e formato>.\nComparar: <característica visível>.'
ds[10]['campos']=['Ambiente: caneca inteira no ateliê; mostra onde a peça nasce','Escolha: mão entre duas peças; mostra a decisão do comprador','Uso: mão segurando a alça; permite observar a escala','Detalhe: aproximação do esmalte; mostra o acabamento','Conjunto: caneca com pires na mesa; mostra o que acompanha','Encerramento: caneca inteira com espaço acima; recebe a mensagem depois']
ds[12]['pedido_complementar']='Edite uma cópia da imagem. Remova apenas a mancha indicada no fundo e reconstrua o fundo creme nessa região. Preserve caneca, contorno, cor, enquadramento e sombra. Não amplie o quadro.'
ds[12]['conferencia_complementar']='Compare a região corrigida e sua borda. Confira se a mancha sumiu, se há emenda e se o produto e a sombra permaneceram iguais.'
b['modules'][4]['verify']='Compare a cópia expandida com o original. Confira escala do produto, continuidade da mesa, direção da luz e sombra junto da base. O objeto não deve ser esticado.'
ds[14]['passos'][1]='Indique onde haverá área livre e qual editor conhecido poderá manter o texto separado. Se não conhece um, escreva editor a escolher: esta prática é um plano.'
bp.write_text(json.dumps(b,ensure_ascii=False,indent=2)+'\n');dp.write_text(json.dumps(ds,ensure_ascii=False,indent=2)+'\n')
