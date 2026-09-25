# Leitor simulado — aulas 1–7

Data: 2026-09-25. Persona: Joana, artesã, 38 anos; celular, WhatsApp e chat de IA; não programa; intervalo de 15 minutos. Simulação de leitura, não teste com pessoa real.

Procedimento: leitura de AGENTS.md e TESTE-HUMANO.md; HTML integral das sete aulas, em grupos 1–3, 4–5 e 6–7; inspeção visual direta das capturas mobile 01, 03, 04, 05, 06, 07 e 08 de cada aula em `/home/nmaldaner/projetos/output/curso-prompting-imagem/validacao/mobile/aula-N/`. As capturas mostram steps, quiz e prática; não comprovam funcionamento dos botões. Não executei geração, não alterei aulas nem publiquei. Verifiquei as referências locais também em curso.html e curso.json.

## Resultado de liberação

| Aula | Entendi e consigo usar | Correção de maior impacto |
|---|---:|---|
| 1 | 8,5/10 | Exibir um exemplo preenchido com as cinco linhas prometidas, em vez de três. |
| 2 | 7/10 | Fazer a prática avaliar efetivamente uma imagem, ou limitar a promessa a preparar os critérios. |
| 3 | 8/10 | Dar uma imagem específica e um defeito marcado para quem não possui geração anterior. |
| 4 | 8,5/10 | Comparar visualmente produto inteiro e detalhe na mesma caneca. |
| 5 | 7,5/10 | Mostrar dois sinais de material e a diferença visível entre sombra dura e suave. |
| 6 | 8/10 | Fazer o teste de área livre sobre a cena disponível, com instrução explícita para o celular. |
| 7 | 7,5/10 | Retirar do caminho principal a digressão de versões de ferramenta e esclarecer proporção com exemplos numéricos simples. |

Todas ficam abaixo de 9 nesta rodada. Isso não é uma reprovação de layout: os impedimentos são ligações entre exemplo, decisão e exercício, além de materiais citados que não existem na entrega examinada.

## Grupo 1 — aulas 1–3

### Aula 1 — Decida o trabalho antes de pedir a imagem

| Step | Em 5 segundos: figura e rótulo | Onde travei | O que pularia |
|---|---|---|---|
| 1 — Modelo, plataforma e editor | Vejo pedidos vago/verificável. Entendo que tenho de pedir melhor, mas a figura não esclarece modelo, plataforma e editor. | Preciso distinguir três funções, porém não há exemplo concreto de quem faz o quê no meu chat. O trecho sobre versão parece exigência técnica antes da primeira tarefa. | Explicação de comparação entre versões, porque ainda vou apenas escrever uma encomenda. |
| 2 — Briefing em cinco linhas | Vejo uma ficha de produto, uso e obrigatório. Parece que bastam três linhas. | A promessa diz cinco e a figura omite público e intenção; não tenho exemplo preenchido justamente dos campos menos óbvios. | Frases sobre catálogo versus ambientação após já ter entendido a distinção. |
| 3 — Confira a decisão | Leio que alça cortada reprova. Acerto a regra lendo os cartões, sem ver uma comparação. | O texto pede comparar com a imagem, mas a prática ainda não produz imagem. Falta distinguir conferência da ficha e conferência futura da geração. | O cartão de Mauro e a repetição literal de “Compare a encomenda...” em seguida. |

**Prática agora:** consigo preencher as Notas com meu objeto, sem outra ferramenta. A promessa central é cumprida, mas público e intenção exigem mais inferência do que produto/cor/formato. Correção mínima: completar a ficha ilustrada com “Público: compradores de cerâmica” e “Intenção: mostrar a forma com clareza”; no step 3, dizer que agora confiro o texto e, quando gerar, confiro a imagem.

**Cena de produto:** a foto inicial mostra escolha de cenário e fotografias na mesa; não mostra as cinco decisões nem uma alça cortada. Serve como contexto, não como demonstração do briefing. A fotografia não substitui a ficha completa.

**Material:** o pedido complementar contém “alça oval no lado da alça” e “janela pelo lado da janela”. São instruções circulares para um pedido sem referência anexada. Usar um lado definido visto por quem olha, ou simplesmente “alça visível e inteira; luz lateral suave”.

**Nota:** 8,5/10. Uma mudança prioritária: ficha visual realmente preenchida nas cinco linhas.

### Aula 2 — Dê uma função a cada referência

| Step | Em 5 segundos: figura e rótulo | Onde travei | O que pularia |
|---|---|---|---|
| 1 — Referências com função | “A forma da caneca; B luz”: acerto que cada foto tem um papel. | Não vejo as duas fotos ao lado dos rótulos. Preciso imaginar a diferença entre usar a luz e copiar os objetos. | Parte sobre composição, estilo e paleta antes de resolver duas fotos simples. |
| 2 — Compare pelo trabalho | A ficha repete A/B/teste. Parece seleção de referências, não comparação de resultados. | “Aderência ao briefing” é mais difícil que “cumpriu o pedido”. Não há duas tentativas visíveis nem avaliação preenchida. | Ranking/modelo impressionante: não me ajuda a comparar minha caneca agora. |
| 3 — Confira a decisão | Entendo que a alça deve permanecer igual. | A pergunta já diz que a alça mudou. Responder o quiz não comprova que eu reconheceria essa mudança numa imagem. | Repetição do cartão de Mauro e do critério imediatamente abaixo. |

**Prática agora:** consigo selecionar duas fotos e escrever papéis. Não comparo uma geração: nenhum passo manda observar resultado ou marcar aprovação por critério. A frase final afirma uma habilidade que o exercício não praticou. Correção mínima: acrescentar a observação de uma imagem própria com “forma/luz/espaço livre: atende/não atende + evidência”; para quem não tem imagem, oferecer um caso estático com resultado visível. Se mantiver só planejamento, mudar a promessa para “selecionar referências e preparar critérios de comparação”.

**Cena de produto:** as três fotos da abertura sugerem produto/cena/luz, porém faltam rótulos que conectem cada foto à função. A cena é aproveitável com legenda concreta; os cartões dos steps são texto diagramado, não evidência visual.

**Material inexistente:** complementar manda usar “ficha SVG do produto disponível no aprofundamento”. Não há link nessa aula, nem SVG no inventário local examinado. Para iniciante sem fotos esse é um caminho interrompido. Correção mínima: indicar uma foto própria tirada agora ou apontar um arquivo realmente fornecido. A alternativa da prática “descreva duas imagens” existe, mas não corrige a referência falsa no complementar.

**Nota:** 7/10. Uma mudança prioritária: alinhar promessa e prática com uma comparação observável.

### Aula 3 — Guarde a receita e corrija uma coisa

| Step | Em 5 segundos: figura e rótulo | Onde travei | O que pularia |
|---|---|---|---|
| 1 — Organize para repetir | O cartão mostra “melhore tudo” versus corrigir alça. Entendo correção, não organização de arquivos. | “Seed” e lista de controles aparecem antes de eu saber guardar imagem e pedido juntos no celular. | Seed e configurações desconhecidas; eu registraria nome do chat e texto. |
| 2 — Ciclo de revisão | V01 cortada → V02 abrir → aprovar: entendo sequência. | Não há exemplo do registro completo com imagem, pedido e ferramenta. A ficha visual só registra decisão. | “Ajustar uma hipótese” e “diagnóstico”: descrever um defeito já resolve. |
| 3 — Confira a decisão | Entendo que corrigir alça e mudar cor não serve. | Consigo acertar a resposta sem ter visto a cor alterada. Falta uma comparação para treinar o olhar. | Cartão genérico de aprovação e repetição do mesmo critério. |

**Prática agora:** consigo usar uma imagem minha. Sem imagem, a alternativa manda observar a cena inteira da aula; nela há duas fotografias pequenas na mão de Mauro e uma parece cortar/esconder a alça. Não fica explícito que devo avaliar essas miniaturas, em vez da foto de Mauro. Correção mínima: “Observe a foto que Mauro segura à esquerda de quem olha: a alça não aparece. Registre esse problema; preserve cor terracota e fundo claro.” Melhor ainda, oferecer essa foto isolada em tamanho legível. A ficha copiável pede arquivo/ferramenta/pedido, mas não tem data apesar de o passo 2 pedi-la: acrescentar campo Data.

**Promessa:** registrar tentativa e planejar correção é compatível com a prática; não se promete executar edição. A ajuda “desconhecido” evita travar com ferramenta/versão.

**Material inexistente:** “documentação de Seeds no aprofundamento” não tem link na aula examinada. Remover a remissão ou fornecer link explícito em complemento opcional. “Seed” pode ficar exclusivamente nesse complemento.

**Nota:** 8/10. Uma mudança prioritária: exercício alternativo com defeito e imagem inequívocos.

## Grupo 2 — aulas 4–5

### Aula 4 — Escolha o assunto e o tamanho do plano

| Step | Em 5 segundos: figura e rótulo | Onde travei | O que pularia |
|---|---|---|---|
| 1 — Sujeito e ação | O pedido cheio de objetos parece confuso; a comparação textual permite entender a prioridade. | “Faltam limites observáveis” é genérico; nesse caso o problema concreto é não escolher o assunto principal. | A palavra “sujeito” após entender que significa minha caneca. |
| 2 — Enquadramento e ponto de vista | A ficha diz ambiente/produto/detalhe. Reconheço três usos, mas não vejo os três recortes. | Plano aberto, médio e detalhe são apresentados sem a diferença visual correspondente. | Frase “o aluno e o público conseguem inspecionar”, que soa explicação ao professor. |
| 3 — Confira a decisão | Entendo que acabamento pede aproximação. | O quiz contrasta borda com prédio/cozinha: alternativas muito distantes não treinam a decisão entre dois recortes plausíveis. | Cartão repetido de Mauro. |

**Prática agora:** consigo escrever objeto inteiro e detalhe; promessa cumprida no nível de escrita. Para saber se pedi o detalhe suficiente, falta vê-lo. A cena inicial com moldura demonstra selecionar o quadro, mas só traz um enquadramento do produto inteiro. Correção mínima: usar dois recortes da mesma imagem, marcados “produto inteiro” e “detalhe da alça”; não é necessário gerar nova cena.

**Material inexistente:** “Use o laboratório de enquadramento” não aponta a um controle ou link disponível na aula. Substituir por “Abra uma foto sua na galeria e compare o produto inteiro com uma ampliação da alça”, sem sugerir que ampliar recupera detalhe inexistente; ou fornecer o laboratório real.

**Nota:** 8,5/10. Uma mudança prioritária: comparação visível entre os dois enquadramentos exigidos na prática.

### Aula 5 — Descreva a luz e a superfície

| Step | Em 5 segundos: figura e rótulo | Onde travei | O que pularia |
|---|---|---|---|
| 1 — Luz | O cartão manda trocar adjetivos por janela/sombra/reflexos. Sei escrever o pedido. | Para reconhecer “transição gradual” preciso enxergar uma sombra suave e uma dura; os cartões só as nomeiam. | Discussão de “iluminação cinematográfica”, se não houver exemplo visual. |
| 2 — Textura | Ficha separa fonte, sombra e material. Acerto a distinção pelas palavras. | “Mauro aproxima a referência da janela”: ele move a foto ou o objeto? Aproximar a fotografia não muda a luz retratada. | Essa ação ambígua; não saberia reproduzi-la. |
| 3 — Confira a decisão | Entendo “plástico brilhante” como erro pretendido. | Cerâmica pode ser brilhante. O erro deve ser mudar o acabamento fosco escolhido, não ter brilho por si só. | Repetições de “coerência” sem indicar onde olhar. |

**Prática agora:** observar objeto/foto e escrever a fonte é viável. A ficha exige dois sinais de superfície, mas o exemplo final fornece apenas “cerâmica fosca” junto de janela/sombra; falta um segundo sinal, como variações discretas do esmalte. Correção mínima: fornecer o exemplo completo “superfície fosca, com pequenas irregularidades; janela lateral e sombra de borda difusa”. Trocar “aproxima a referência” por “coloca a caneca perto da janela para fotografar”.

**Cena de produto:** mostra Joana apontando para caneca fosca e outra peça de acabamento diferente; sem legenda, não separo o que mudou por material e por iluminação. Pode ensinar mais ao identificar explicitamente a superfície fosca e a área de brilho da outra peça. Não demonstra a comparação dura/suave pedida no texto.

**Material inexistente:** complementar manda alternar a janela “no esquema” e fala “no desenho”; esse esquema com controles não existe na aula examinada. O pedido “janela pelo lado da janela” tampouco estabelece uma direção. Substituir por observação física de um objeto próprio e lado inequívoco; não mandar procurar controles ausentes.

**Promessa:** parcialmente cumprida. Consigo separar os campos no papel, mas a capacidade de distinguir visualmente depende de apoio que não foi fornecido.

**Nota:** 7,5/10. Uma mudança prioritária: exemplo visual rotulado mostrando sombra e dois sinais da superfície.

## Grupo 3 — aulas 6–7

### Aula 6 — Organize o quadro e a linguagem visual

| Step | Em 5 segundos: figura e rótulo | Onde travei | O que pularia |
|---|---|---|---|
| 1 — Composição | Pedido verificável indica caneca embaixo e título em cima. Entendo o arranjo. | “Terços” aparece sem grade. “Hierarquia confusa” poderia simplesmente dizer título cobrindo o produto. | Terços até ter um exemplo, já que metade superior/inferior é suficiente à prática. |
| 2 — Estilo e estrutura | A ficha organiza assunto, espaço e estilo. Consigo copiar a lógica. | “Prompt em camadas” não mostra camadas, e “representar dados em campos” soa tarefa técnica. | Esse parágrafo; a ficha copiável já demonstra o que preciso. |
| 3 — Confira a decisão | “Cubra a área do título” parece ação útil. | Em que imagem faço isso? Só produzi texto. Posso usar o dedo na cena inicial, mas a aula não manda fazê-lo. | A checagem visual se não estiver claro onde executá-la. |

**Prática agora:** consigo substituir “elegante” por cor/luz/organização, cumprindo a promessa de escrever um pedido. O passo 3 pede conferir “a peça”, que ainda não foi criada. Correção mínima: “Confira no pedido onde ficará o produto e onde ficará o título; na imagem inicial, cubra com o dedo a área vazia para simular um título e veja se a caneca continua visível.” Se quiser avaliar a própria composição, desenhar um retângulo simples no papel antes de gerar.

**Cena de produto:** aqui há evidência aproveitável: caneca embaixo e ampla área clara atrás. Ela ensina reserva de espaço, porém falta a legenda dizendo exatamente o que observar. Vale conectá-la ao step 3.

**Material inexistente e revisão textual:** complementar pede grade do laboratório e construtor de prompt, sem controles/links correspondentes. “Guarde a ficha ficha estruturada” tem duplicação. Correção mínima: trocar os dois comandos pela ficha disponível nas Notas, remover duplicação e usar “A ficha separa assunto, posição, luz, cores e material”.

**Nota:** 8/10. Uma mudança prioritária: conectar a verificação do espaço à imagem existente e à ação com o dedo no celular.

### Aula 7 — Separe formato, identidade e estilo

| Step | Em 5 segundos: figura e rótulo | Onde travei | O que pularia |
|---|---|---|---|
| 1 — Proporção e resolução | A figura compara papéis de referências, não proporção/resolução. Entendo a regra da aula 2 outra vez. | “Pixels” vira “pontos” depois; faltam dois quadrados de tamanhos diferentes para mostrar o que permanece igual. | Repetição de referência A/B antes de resolver formato. |
| 2 — Identidade e estilo | A ficha A forma/B paleta é reconhecível. | “O acervo” não identifica acervo algum. Omni Reference, V7, Edit Model e V8.X interrompem o fluxo de quem usa outro chat; não sei se preciso trocar de ferramenta. | Todo o parágrafo de versões, que deveria ser complementar e condicional. |
| 3 — Confira a decisão | Entendo a separação do formato e objeto. | “Mais pontos” e “dimensão em pontos” são vagos. O quiz pode ser respondido por eliminação sem entender 1:1. | Formulação técnica da resposta, buscando o exemplo prático. |

**Prática agora:** consigo escolher quadrado e atribuir papéis a referências. Porém “horizontal” não escolhe uma proporção específica: 4:3 e 16:9 são horizontais diferentes. Para cumprir a promessa com precisão, a ficha deveria permitir “quadrado 1:1, horizontal 4:3, vertical 9:16” como exemplos e lembrar de usar o formato exigido pelo destino.

**Cena de produto:** moldura quadrada e moldura vertical tornam diferença de formato visível; fotos sobre a mesa permitem distinguir produto/atmosfera, mas sem rótulos exigem adivinhação. A legenda pode dizer “moldura quadrada para a ficha; foto da caneca para forma; foto da luz para aparência”. Resolução ainda precisa de exemplo: 512×512 e 1024×1024 mantêm o quadrado.

**Materiais/pré-requisito:** complementar manda alternar formatos no laboratório e consultar documentação vinculada no aprofundamento. Não há laboratório ou links nessa aula. O pedido completo ainda manda anexar “a referência própria criada no módulo anterior”, mas as práticas 4–6 só escreveram fichas; não exigiram produzir uma foto. Correção mínima: “Anexe uma foto própria do objeto; se ainda não tem, fotografe-o inteiro agora”, e substituir laboratório por observação das molduras da cena. Não validei tecnicamente a informação atual de Midjourney; esta revisão avalia compreensão e disponibilidade de materiais.

**Nota:** 7,5/10. Uma mudança prioritária: ensinar formato/resolução com exemplo curto e mover versões de ferramenta ao complemento com link real.

## Ajustes comuns de baixo custo

1. O step 3 das sete aulas repete o mesmo cartão de Mauro (“aprovação precisa de uma observação concreta”) e repete o critério no parágrafo/cartão. Eu passaria direto após a terceira aula. Usar esse espaço para uma decisão específica com evidência visível ou encurtar a repetição.
2. As cenas de abertura variam e retratam o trabalho, mas nenhum step aponta para uma região delas. Transformar decoração em ensino com “olhe a alça da foto à esquerda”, “observe o espaço acima da caneca” ou legenda equivalente. Não alegar que cenas ilustradas são resultados reais de prompts.
3. Os comandos de materiais complementares devem corresponder a arquivos, controles ou links presentes. Nas aulas 1–7, os únicos links do HTML-fonte são trilha/próxima; a busca local não encontrou os materiais específicos citados. Remover remissões antigas é uma correção menor que reconstruir laboratórios.
4. “Se faltar acesso à geração, registre o plano como pendente” aparece em práticas cujo resultado é só uma ficha escrita. Como leitora, perguntaria se minha tarefa está incompleta sem gerar. Nas práticas de escrita, dizer que a ficha já é a entrega; reservar a instrução de pendência para exercícios que de fato geram/editam.
5. A prática aparece por volta da sétima tela mobile. Para um intervalo de 15 minutos com dez minutos de prática, repetição custa tempo de execução. Não medi leitura humana real; a evidência é a sequência das capturas, não uma duração cronometrada.

## Rodada 2 — conferência independente após os ajustes

Data: 2026-09-25. Mesma persona. Releitura do HTML atualizado em grupos 1–3, 4–5 e 6–7; inspeção direta de 46 novas capturas em `validacao/revisao-mobile/`: 04–09 nas aulas 1–3 e 03–09 nas aulas 4–7. Não se presume funcionamento dos botões nem correção posterior à leitura. As observações da rodada 1 são históricas; abaixo consta o estado reavaliado.

| Aula | Nota atual | Evidência observada | Trava restante e correção mínima |
|---|---:|---|---|
| 1 | 9/10 | Capturas 04–06 mostram funções modelo/plataforma/editor e ficha com cinco linhas, incluindo público e intenção. Step 3 separa conferir o pedido agora e a imagem depois. Consigo preencher e terminar a ficha. | O aviso da prática ainda manda registrar como pendente se não houver geração, apesar de a entrega ser escrita. Trocar por “A entrega desta aula é a ficha preenchida; você pode gerar depois”. Não preciso gerar para cumprir a promessa. |
| 2 | 8,5/10 | Capturas 07–08 agora exigem observar uma imagem e registrar atende/revisar em forma, luz e espaço, com justificativa. A referência inexistente a SVG foi removida. | Falta definir **o que deve ser atendido** no caso oferecido: forma/luz/espaço são dimensões, não critérios de aprovação. “Observe a caneca da ilustração” também pode ser a peça real ou uma das três fotografias. Correção mínima: “Avalie a foto da esquerda da mesa. Para este exercício, o pedido exige alça inteira, luz suave e área livre acima da caneca. Marque o que atende e o que precisa revisar”. Com essa referência explícita, a prática permite decisão reproduzível. |
| 3 | 9/10 | Captura 05 mostra duas fotos, uma sem alça visível; 07 aponta diretamente para as fotografias nas mãos de Mauro. A ficha ganhou data; a receita principal ficou sem seed e aceita desconhecido. Consigo registrar problema, alteração e duas preservações. | O aviso genérico de pendência permanece. As fotos são pequenas: identificar “foto à esquerda de quem olha” reduziria busca, mas a diferença já pode ser encontrada com a instrução atual. |
| 4 | 9/10 | Captura 04 traz a série produto inteiro/detalhe da alça/uso. Consigo relacionar pedido de detalhe à fotografia central; captura 06 conecta moldura e recorte. O complemento substitui laboratório por galeria e gesto de pinça, com limite explicitado. | Eu pularia a frase sobre “aluno e público inspecionar”; não bloqueia a tarefa. Resta remover o aviso de geração pendente da prática de escrita. |
| 5 | 9/10 | Captura 03 mostra sombra de borda nítida e difusa. Captura 06 aponta comparação entre fosco/brilho; 08 fornece fonte, sombra e dois sinais da superfície. Mauro agora move a caneca, não “a referência”. Consigo observar meu objeto e preencher a ficha. | Os textos dentro do diagrama são muito menores que o corpo no celular. A forma das sombras e legenda externa ainda permitem entender, mas aumentar os rótulos ou empilhar os dois casos melhora leitura. Remover aviso genérico de geração pendente. |
| 6 | 9/10 | Texto do step 2 explica uma escolha por linha; captura 05 tem área livre visível; 06 e 07–08 mandam cobrir a área com o dedo. Consigo escrever pedido e executar a verificação visual. Laboratório/construtor fictícios foram retirados. | O cartão de Mauro escolhe “estilo → creme, terracota, luz suave”, enquanto a figura/ação verifica espaço livre. Trocar essa frase por “área livre acima da caneca → título sem cobrir o produto”. É desvio leve porque a legenda seguinte dá a ação correta. Resta aviso genérico de pendência. |
| 7 | 9/10 no caminho principal | Captura 04 mostra dois quadrados com dimensões diferentes e explica que estão representados no mesmo tamanho de tela. Step 2 perdeu a digressão sobre versões. Captura 08 pede proporção numérica e papéis distintos das referências. Consigo escolher 1:1 e escrever o pedido. | No **complemento**, ainda consta “anexe a referência própria criada no módulo anterior”. As práticas 4–6 não criaram obrigatoriamente arquivo de imagem. Trocar por “anexe uma foto própria do objeto”, como o pedido logo acima já permite. A ficha copiável ainda só mostra horizontal/vertical/quadrado; incluir os exemplos 4:3/9:16/1:1 ali alinha ficha e passo 1. |

### Resposta por step, após as correções

- **Aula 1:** step 1 — identifico funções pela nova ficha em cinco segundos; pularia a comparação de versões, sem travar. Step 2 — identifico cinco campos e consigo completar público/intenção; não falta exemplo. Step 3 — entendo que verifico texto antes da imagem; a legenda ensina decisões separadas, embora não mostre alça cortada.
- **Aula 2:** step 1 — identifico função A/B, mas ainda tenho de imaginar as referências concretas. Step 2 — entendo manter critérios; “aderência ao briefing” continua vocabulário dispensável, eu leria como “cumpriu o pedido”. Step 3 — vejo fotografias úteis e regra de preservar a alça; na prática ainda travo em decidir “atende a quê?” sem um alvo explícito para cada critério.
- **Aula 3:** step 1 — entendo guardar imagem/pedido/referências, sem obrigação de achar configurações. Step 2 — a sequência defeito → correção → aprovação é legível; pularia “hipótese/diagnóstico”. Step 3 — agora reconheço que devo olhar as fotos pequenas de Mauro. A legenda resolve a ambiguidade principal do exercício, ainda que uma seta ou indicação de lado o torne mais rápido.
- **Aula 4:** step 1 — a série permite perceber o efeito do recorte; não fica só no pedido escrito. Step 2 — relaciono inteiro/detalhe à série imediatamente anterior. Step 3 — a moldura mostra como escolher o que entra no quadro. Pularia o quiz muito óbvio, mas consigo fazer a prática prometida.
- **Aula 5:** step 1 — as bordas dura/suave ficam diferentes em cinco segundos mesmo com rótulos pequenos. Step 2 — fonte/sombra/material estão separados e a ação de fotografar o objeto é executável. Step 3 — entendo comparar o acabamento escolhido, sem concluir que toda cerâmica brilhante é erro. Consigo escrever dois sinais; não persiste a falta do segundo atributo.
- **Aula 6:** step 1 — identifico produto embaixo e título em cima pelo pedido. Step 2 — consigo transformar estilo em linhas de escolhas. Step 3 — área clara da imagem e gesto do dedo dão verificação concreta. Pularia o cartão de estilo imediatamente antes dessa imagem, porque o assunto ali deveria ser posição/área livre.
- **Aula 7:** step 1 — quadrados e números mostram que o formato se mantém; acertaria a pergunta sem depender de eliminação. Step 2 — objeto versus atmosfera agora é explicado em linguagem utilizável no meu chat. Step 3 — molduras mostram formatos diferentes. Consigo a prática principal; a frase do complemento que exige arquivo “criado no módulo anterior” ainda me faz procurar algo que não produzi.

### Decisão desta rodada

A mudança visual/operacional é comprovada pelas capturas; seis aulas chegam a 9 no caminho principal. A aula 2 ainda requer **uma encomenda concreta e uma imagem inequivocamente identificada** antes de eu considerar a avaliação utilizável sem ajuda. As pequenas correções remanescentes foram identificadas no texto atual, sem aprovar sua realização futura. O aviso comum de geração pendente deve ser ajustado nas práticas cuja entrega já é uma ficha escrita. A frase residual do complemento da aula 7 deve ser corrigida. Não foram medidos tempo humano real nem funcionamento interativo.

## Julgamento final — conferência pontual do HTML corrigido

Data: 2026-09-25. Releitura das frases modificadas no HTML atual; esta etapa não recapturou telas e se apoia na inspeção visual da rodada 2 para os elementos gráficos.

- **Aula 2: 9/10.** O step 3 agora declara a encomenda: alça inteira, luz suave e área livre acima. O último passo da prática repete os três requisitos como perguntas e pede atende/revisar com justificativa. Como Joana, consigo preencher a avaliação sem inventar o padrão de aprovação. A ficha registra “Imagem observada”, portanto posso escolher uma imagem própria ou uma das vistas da ilustração e identificar qual avaliei. Especificar uma das fotografias da mesa ainda reduziria a busca no exercício guiado, mas a seleção já pode ser registrada e não impede aplicar os critérios. Não interpreto esse exercício como teste real de geração ou comparação entre ferramentas: ele treina avaliação visual por requisitos.
- **Aulas 1–7: aviso de prática corrigido.** Conferi `.psafe` nas sete fontes. Agora diz que a ficha pode ser preenchida no papel ou nas Notas; preservar original só se a prática pedir edição. Não exige geração nem manda marcar pendência numa entrega escrita. A trava comum foi removida.
- **Aula 7: complemento coerente.** A conferência agora pede “anexe uma foto própria do objeto”; o pedido imediatamente anterior explica fotografar um objeto inteiro se faltar foto. Não depende mais de um arquivo supostamente produzido no módulo anterior.

**Notas finais:** aula 1 = 9; aula 2 = 9; aula 3 = 9; aula 4 = 9; aula 5 = 9; aula 6 = 9; aula 7 = 9. As sete passam no critério desta simulação para compreender e executar a prática proposta. Permanecem sugestões de refinamento já registradas — rótulos maiores no esquema de sombra e cartão de Mauro da aula 6 alinhado à área livre — sem bloqueio da execução. Isso não substitui teste com pessoas nem verifica botões, geração real ou tempo de conclusão.
