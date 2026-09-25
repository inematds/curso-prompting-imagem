# Leitor simulado — aulas 8–14

Data: 2026-09-25. Persona: **Mauro, lojista de 56 anos**, usa WhatsApp e ocasionalmente chat de IA, não programa; dispõe de 15 minutos no celular. Esta é uma simulação, não um teste com participante humano real.

Li `AGENTS.md`, `TESTE-HUMANO.md` da skill v6 e os HTML completos. Revisão em grupos de 2–3: 8–9, 10–12, 13–14. Inspecionei com `view_image` as capturas móveis `03.png`, `04.png`, `05.png`, `06.png` e `08.png` de cada aula (35 telas), em `/home/nmaldaner/projetos/output/curso-prompting-imagem/validacao/mobile/aula-N/`. Conferi materiais no inventário do projeto, `curso.html`, `curso.json` e aula 1. Não testei interações no navegador; nas comparações com abas, vi a aba inicial na captura e li ambos os textos no HTML.

## Resultado por aula

| Aula | Entendi e consigo usar | Principal correção mínima |
|---|---:|---|
| 8 | 7,5/10 | Preencher um exemplo A/B sem controles e retirar o jargão de implementação do caminho principal. |
| 9 | 8,5/10 | Mostrar uma receita completa preenchida, incluindo “modelo não informado” e estado “a testar”. |
| 10 | 9/10 | Explicitar no exemplo “produto legível = dá para ver alça, borda e cor”. |
| 11 | 8/10 | Preencher as seis linhas e trocar a referência ao storyboard ausente por essa ficha. |
| 12 | 8/10 | Acrescentar a saída “nenhuma diferença problemática” quando as fotos estiverem corretas. |
| 13 | 8/10 | Remover a referência a um esquema inexistente e tornar concreto o que marcar e preservar. |
| 14 | 8/10 | Usar um pedido completo de expansão e conferir os quatro sinais com exemplos observáveis. |

Notas abaixo de 9 pedem ajuste e nova leitura, conforme TESTE-HUMANO. A aula 10 passa para esta persona; a sugestão indicada é refinamento. Nas demais, as travas não devem ser escondidas por uma média do curso.

## Grupo 8–9

### Aula 8 — Teste os controles que sua ferramenta oferece

| Step | Figura e rótulo em 5 segundos | Onde eu travo | O que eu pularia |
|---|---|---|---|
| 1 — Intensidade de estilo e exploração | Entendo “não mexer em tudo”; acertou parcialmente. A caixa certa é longa e não mostra dois resultados. | “Interpretação estética” e “diversidade de resultados” não me dizem qual botão ou frase mudar. Entendo melhor o exemplo da textura da cerâmica. | A frase sobre explorar versus refinar; iria direto a Joana. |
| 2 — Steps, guidance e força de edição | A ficha deixa claro “fixo / variável / critério”. Acerta o plano de teste, mas não explica visualmente os três controles do título. | “Parâmetros pertencem à implementação” e “modelos destilados” não têm explicação útil para mim. A escala precisa ser conferida, mas Mauro já testa valor menor para preservar: parece uma regra, apesar da ressalva. | A parte de modelos rápidos/destilados e recursos de processamento. |
| 3 — Confira a decisão pelo uso | “Uma variável, um critério e limite” dá a ideia. O quadro “Como conferir” repete uma advertência, sem me mostrar uma conferência feita. | Como registrar o efeito? Eu precisaria ver algo como “A deixou a alça inteira; B mudou a alça”. | O exemplo genérico “No trabalho de Mauro...” e a repetição da advertência. |

**Prática agora:** consigo planejar, mas no chat sem controles a ficha ainda pede “Valor A/Valor B”. A alternativa em prosa ajuda, porém faltam as duas frases concretas e como preencher os campos. Correção: “Sem controle: A = fotografia; B = ilustração em aquarela; mantenho objeto, luz e posição; comparo contorno da alça; duas tentativas”. Não é preciso gerar para cumprir a promessa, que é apenas planejar.

**Promessa:** parcialmente cumprida para mim; compreensão do método é boa, execução do planejamento depende de traduzir termos. **Materiais:** ficha e pedido do módulo presentes. Referência própria é uma produção anterior, não um arquivo fornecido; isso deve continuar explícito. **Termos:** steps e guidance recebem definições curtas; “implementação”, “destilados” e “direção da escala” ficam técnicos demais. **Uma mudança de maior impacto:** exemplo A/B preenchido para quem usa apenas chat, com o parágrafo técnico deslocado ao complementar. **Nota: 7,5/10.**

### Aula 9 — Guarde uma configuração que você consegue explicar

| Step | Figura e rótulo em 5 segundos | Onde eu travo | O que eu pularia |
|---|---|---|---|
| 1 — Seed e comparação honesta | Entendo que guardar só um número não basta. A caixa verde exige leitura, mas a oposição é clara. | “Modelo informado” me deixa na dúvida se o nome do aplicativo serve; nem todo chat mostra o modelo. | Detalhes da experiência perfeitamente controlada, depois de entender que devo registrar o conjunto. |
| 2 — Um preset verificável | “Catálogo suave / caneca aprovada / alça inteira” é uma ficha curta e útil. Acertou. | Ela é chamada receita, mas não mostra pedido, ferramenta nem valores. Ao copiar para trabalhar, faltam os campos prometidos. | A frase abstrata “preset sem contexto só repete números”. |
| 3 — Confira a decisão pelo uso | Entendo “testada ou a testar”. O quadro “Como conferir” fala de atualizações, em vez de conferir esse estado. | Se nunca gerei, não sei o que pôr em “nome da imagem aprovada”. A instrução posterior permite “a testar”, mas não diz deixar imagem em branco/pendente. | O exemplo genérico de aprovação e a advertência repetida. |

**Prática agora:** consigo usar Notas e copiar o pedido da aula 1, que existe. Preciso de “modelo: não informado”, “imagem aprovada: pendente”, e campos de ferramenta/proporção na própria ficha (pedidos nos passos, ausentes na ficha). **Promessa:** cumprida conceitualmente; a receita ainda exige completar lacunas sozinho. **Materiais:** ficha existe na prática; “ficha de geração no aprofundamento desta aula” aponta para o lugar errado. Trocar por “copie a ficha de Pratique agora”. A menção à documentação Midjourney não oferece link; não foi verificada externamente nesta leitura. **Termos:** seed e preset são definidos; “reprodutibilidade” também é explicado no complementar. **Uma mudança de maior impacto:** receita completa preenchida, inclusive alternativa sem modelo/geração. **Nota: 8,5/10.**

## Grupo 10–12

### Aula 10 — Aprove a imagem que vai orientar a série

| Step | Figura e rótulo em 5 segundos | Onde eu travo | O que eu pularia |
|---|---|---|---|
| 1 — Defina o que não pode mudar | A aba inicial mostra “não começar com a alça escondida”. Acerto esse problema; o pedido bom requer tocar outra aba. | Nenhuma trava impeditiva. “Invariantes” é explicado imediatamente com cor, alças e formato. | “Mesmo universo” e “diversidade com controle”; as características concretas já resolvem. |
| 2 — Crie e aprove uma imagem-base | Fixo / variável / base aprovada é simples. Acerto a ideia. | “Produto legível” pode parecer que o rótulo precisa dar para ler. O exemplo acima esclarece, mas a ficha isolada perde precisão. | Exemplos de rosto e cabelo, porque trabalho com produto. |
| 3 — Confira a decisão pelo uso | Entendo “as três características precisam aparecer”. Acerta. | Nenhuma trava para escolher outra foto. Seria mais direto listar alça, borda e cor no quadro. | A frase de Mauro que não apresenta uma decisão nova. |

**Prática agora:** sim. Posso fotografar um objeto, conferir três características e anotar aprovação. A alternativa não exige saldo nem geração. **Promessa:** cumprida. **Materiais:** ficha e prompt complementar presentes; a foto-base é minha, e o passo explica como obtê-la. **Termos:** invariantes e imagem-base são definidos. “Legível” merece a substituição local por “alça, borda e cor visíveis”. **Uma mudança de maior impacto:** essa troca de frase na ficha; não impede o uso atual. **Nota: 9/10.**

### Aula 11 — Planeje cenas diferentes sem trocar o produto

| Step | Figura e rótulo em 5 segundos | Onde eu travo | O que eu pularia |
|---|---|---|---|
| 1 — Combine referências sem misturar papéis | Entendo “a mesma caneca em todas”. Acerto parcialmente: o quadro fala das seis funções, não mostra qual foto informa produto e qual informa ambiente. | “Associar cada arquivo ao papel correto” sem uma frase preenchida. A instrução clara “imagem A para personagem; B para caneca” está só no complementar. | A enumeração de seis funções na caixa, pois volta no passo seguinte. |
| 2 — Planeje seis cenas com funções diferentes | A ficha com ambiente, detalhe e uso é clara em cinco segundos. | Só há três linhas de exemplo. Não sei o que fotografar para diferenciar “escolha”, “conjunto” e “encerramento”; a lista no texto ajuda, mas não fecha o planejamento. | Frases sobre ponto de vista com intenção, se ainda estiver tentando preencher seis linhas. |
| 3 — Confira a decisão pelo uso | Entendo que uma cena não deve repetir a informação de outra. Acerta. | Não vejo um par redundante e sua correção. “Função distinta e identidade comum” é mais difícil que “mostra outra coisa, com a mesma caneca”. | A frase genérica de aprovação e o critério repetido. |

**Prática agora:** faria três cenas; completar seis com enquadramento e arquivo em dez minutos exige um modelo completo. Não confundir planejar com gerar: a aula faz essa distinção corretamente. **Promessa:** parcialmente cumprida. **Materiais:** o complementar pede “storyboard dos materiais”; nenhum storyboard/template separado ou seção de materiais correspondente foi encontrado nos arquivos e em `curso.html`. A ficha copiável existe, mas contém apenas um quadro. Trocar por seis linhas preenchidas na própria prática é a menor correção. **Termos:** “storyboard” surge sem definição; usar “roteiro visual de seis cenas”. “Escala” funciona melhor como “tamanho percebido em relação à mão”. **Uma mudança de maior impacto:** ficha de seis cenas preenchida e acessível no lugar citado. **Nota: 8/10.**

### Aula 12 — Veja o conjunto e corrija a peça que destoa

| Step | Figura e rótulo em 5 segundos | Onde eu travo | O que eu pularia |
|---|---|---|---|
| 1 — Faça uma folha de contato | Entendo “corrija só a foto errada”. Acerto essa mensagem, mas não vejo uma folha de contato: vejo caixas de texto. | A galeria geralmente mostra miniaturas, porém “abra três imagens juntas” não explica como limitar às três. Criar um álbum temporário resolveria. | “Paleta, escala, figurino” antes de olhar o exemplo da alça. |
| 2 — Corrija o ponto que quebra a série | A/B/C, com B tendo duas alças, é imediatamente compreensível. Acerta. | O exemplo anterior muda uma camisa; a ficha muda alça. A alternância acrescenta esforço sem ensinar algo novo. | A repetição “correção preserva decisões que já funcionam”. |
| 3 — Confira a decisão pelo uso | Entendo “encontre uma diferença problemática”. Acerta. | E se minhas três fotos do mesmo objeto estiverem corretas? A condição de conclusão exige problema e correção; pode me fazer inventar defeito. | A advertência repetida sobre enquadramento depois do quiz. |

**Prática agora:** consigo comparar, mas talvez não consiga concluir honestamente com fotos corretas. Acrescentar “Se não houver defeito, registre conjunto aprovado e justifique pelas três características fixas”. Sugerir “crie um álbum com as três fotos e veja as miniaturas” torna a operação móvel concreta. **Promessa:** parcialmente cumprida por falta dessa saída. **Materiais:** ficha presente; série de três imagens não é fornecida, mas fotos próprias são alternativa explícita. Não há folha de contato ilustrada nos steps inspecionados. **Termos:** folha de contato é definida; paleta e linguagem visual ficam sem tradução no trecho (“cores predominantes” e “jeito de iluminar e enquadrar”). **Uma mudança de maior impacto:** permitir aprovação sem inventar uma diferença. **Nota: 8/10.**

## Grupo 13–14

### Aula 13 — Escolha o alcance da edição

| Step | Figura e rótulo em 5 segundos | Onde eu travo | O que eu pularia |
|---|---|---|---|
| 1 — Global ou local: qual é o alcance? | Entendo que mudar tudo por uma mancha é exagero. Acerta; comparação boa está na outra aba. | “Temperatura” pode parecer calor físico; dizer “imagem mais azulada ou amarelada”. Não bloqueia o exemplo da mancha. | “Nova atmosfera” e “intervenção”, pois local/global já está explicado. |
| 2 — Máscara: indique onde mexer | A ficha mostra global/local/conferência. Acerto a classificação, mas não aprendo onde a máscara termina: nenhuma região marcada aparece. | O texto manda conferir se a seleção encostou na caneca, sem dizer o resultado desejado. Para remover mancha no fundo, deve evitar cobrir a caneca. | Branco/preto da máscara, caso minha ferramenta nem tenha esse recurso. |
| 3 — Confira a decisão pelo uso | Entendo que devo olhar a emenda. Acerta. | Gostaria de um exemplo curto de emenda: “linha de cor diferente entre fundo antigo e novo”. | O parágrafo genérico de Mauro e a repetição literal da mesma instrução no quadro. |

**Prática agora:** consigo escrever o plano da mancha sem editor, atendendo a promessa de distinguir alcances. Para desenhar uma marcação corretamente, a figura não ajuda. **Promessa:** núcleo cumprido; a máscara, que ocupa um step, fica sem demonstração. **Materiais:** pedido e ficha presentes. “No esquema, observe a seleção e a área protegida” refere-se a um esquema que não aparece: há apenas ficha textual. Correção mínima textual: “No seu desenho, circule a mancha com pequena margem e escreva fora do círculo: preservar caneca e sombra”. **Termos:** global/local, máscara e inpainting são definidos; “estrutural” e “diagramação” aparecem como novas categorias no complementar sem explicação. **Uma mudança de maior impacto:** substituir a referência ao esquema por instrução espacial preenchida, deixando explícito o que fica fora da seleção. **Nota: 8/10.**

### Aula 14 — Amplie o quadro e confira a integração

| Step | Figura e rótulo em 5 segundos | Onde eu travo | O que eu pularia |
|---|---|---|---|
| 1 — Expandir é criar fora do quadro | Entendo “aumentar o fundo, não esticar a caneca”. Acerta. | Sem desenho do quadrado dentro do retângulo, preciso imaginar o espaço que será criado. A frase ainda é suficiente para planejar. | O nome outpainting depois de entender sua definição. |
| 2 — Integre objeto, luz e fundo | Entendo “mesa contínua e sombra na base”. Acerta parcialmente: escala e perspectiva ficam só em palavras. | Como reconhecer perspectiva errada? A dica da borda da mesa só vem após o quiz. “Mesma escala” precisa virar “a caneca não cresce nem encolhe na parte original”. | “Conjunto de sinais”, pois preciso saber o que comparar. |
| 3 — Confira a decisão pelo uso | O quadro ensina que a área nova foi inventada. Acerto, mas ele não confere o critério anunciado: produto sem deformação. | Posso repetir a regra sobre não documentar o local, mas ainda não conferi largura da caneca, linha da mesa e início da sombra. | A frase genérica de aprovação e sua advertência repetida. |

**Prática agora:** consigo escrever a expansão, mas listar “escala, perspectiva, luz e contato” pode ser só copiar palavras sem saber conferir. Trocar por quatro perguntas observáveis: tamanho e forma da caneca permaneceram? A borda da mesa continua? A luz vem do mesmo lado? A sombra começa no apoio? **Promessa:** parcialmente cumprida quanto a conferir integração. **Materiais:** ficha de expansão presente. O “Pedido completo do módulo” manda remover objeto do fundo; é um pedido de edição local, não de expansão. Para quem copia esse bloco esperando praticar a aula 14, produz a operação errada. Usar pedido completo específico: ampliar laterais para quadro horizontal, preservar objeto e continuar mesa. **Termos:** outpainting e sombra de contato são definidos; perspectiva recebe uma dica tardia, escala não tem definição operacional no corpo. **Uma mudança de maior impacto:** alinhar o pedido completo e o quadro “Como conferir” à expansão desta aula. **Nota: 8/10.**

## Observação transversal das telas

As capturas em 390 px mostram texto e botões legíveis, boa separação das caixas e ausência de corte horizontal nas áreas inspecionadas. Entretanto, as “figuras” dos steps são quase todas texto dentro de caixas. Em cinco segundos entendo a regra geral, mas não vejo visualmente máscara, sombra de contato, diferença entre duas gerações ou série de miniaturas. Uma ilustração na abertura não substitui a demonstração do step.

O mesmo parágrafo “No trabalho de Mauro, a aprovação precisa de uma observação concreta...” aparece no step 3 de todas as sete aulas. Eu o pularia depois da segunda ocorrência. A menor correção é substituí-lo por uma decisão real de uma linha: objeto, diferença observada e próxima ação. O quadro “Como conferir” também costuma repetir o parágrafo imediatamente anterior; em especial aulas 8, 9 e 14, trocar pela pergunta de verificação concreta melhora o uso em 15 minutos.

O tempo não foi medido com usuário humano. As práticas de planejamento são plausíveis para dez minutos, mas procurar termos, localizar materiais vagamente citados e voltar à aula 1 aumenta o esforço no celular. Não atesto execução de edição nem funcionamento de botões a partir de screenshots.

## Rodada 2 — após as primeiras correções

Releitura independente em 2026-09-25, mesma persona. Li novamente os sete HTML e inspecionei 20 capturas em `validacao/revisao-mobile/`: `05` e `06` de todas as sete aulas; adicionalmente 8/04, 8/08, 9/07, 11/07, 12/08 e 14/07. Os steps 1 e 2 foram reavaliados pelo texto; os novos steps 3, pelas telas. O feedback abaixo descreve o estado efetivamente encontrado, não presume que todas as alterações anunciadas foram concluídas.

| Aula | Nota anterior → atual | Resultado |
|---|---:|---|
| 8 | 7,5 → 8 | Melhoria parcial; jargão antigo permanece e falta par A/B para chat. |
| 9 | 8,5 → 9 | Ficha preenchida e localização corrigida destravam a prática. |
| 10 | 9 → 9,2 | Figura e legenda tornam a referência concreta. |
| 11 | 8 → 8,5 | Material agora localizável; seis funções ainda precisam de exemplos preenchidos. |
| 12 | 8 → 9 | Caneca azul e alternativa para fotos corretas resolvem a trava principal. |
| 13 | 8 → 8,5 | Máscara entendível; surgiu pedido de expansão no complementar de edição local. |
| 14 | 8 → 8,5 | Pedido de expansão corrigido, mas conferência ainda manda remover elemento. |

### Aula 8 — revisão dos três steps

- **Step 1:** em cinco segundos continuo entendendo “uma coisa por vez”. As frases novas sobre cor/fundo/acabamento são mais concretas. Pularia a duplicação “nome e escala dependem da ferramenta” / “nome e escala variam entre ferramentas”.
- **Step 2:** a abertura foi simplificada, mas na captura `04.png` continuam literalmente “Esses parâmetros pertencem à implementação” e “Modelos rápidos ou destilados podem ter faixas específicas”. Ainda travo nesses termos; pularia ambos. O exemplo de valor menor preservar mais ainda soa universal, sem dizer “se a descrição desse controle indicar isso”.
- **Step 3:** em cinco segundos vejo duas versões de caneca com acabamento diferente. A legenda deixa claro que não é tela real de ferramenta: melhora válida. Ainda não descubro qual A/B devo escrever se meu chat não tem controle. Pularia a frase “critério → forma preservada e textura coerente” por repetir a ficha.

**Prática/promessa:** ainda parcial para Mauro no chat: ficha continua com valores vazios, alternativa sem controle continua só em prosa. **Material:** presente. **Correção mínima pendente:** apagar os dois parágrafos técnicos remanescentes e preencher a alternativa: “A = fotografia; B = aquarela; manter objeto, posição e luz; comparar contorno da alça”. **Nota: 8.**

### Aula 9 — revisão dos três steps

- **Step 1:** entendo guardar o conjunto e não só seed; sem nova trava impeditiva. Pularia a explicação da experiência controlada.
- **Step 2:** receita/referência/critério segue clara. A nova ficha de prática resolve a falta de conteúdo que eu encontrava aqui.
- **Step 3:** foto e amostras entrando na mesma pasta comunicam em cinco segundos que devo guardar referências juntas. A legenda é aderente à figura. Pularia a frase “critério →...” redundante.

**Prática/promessa:** agora consigo copiar uma receita útil, inclusive modelo desconhecido e estado a testar. A figura não demonstra repetição perfeita, coerente com a promessa. **Material:** referência ao aprofundamento substituída pela prática existente; citação externa imprecisa removida. **Resíduo não impeditivo:** ficha não tem campo “ferramenta”, embora o passo peça acrescentá-lo; incluir uma linha poupa edição no celular. Pode também explicitar “imagem aprovada: pendente” quando não gerou. **Nota: 9.**

### Aula 10 — revisão dos três steps

- **Step 1:** a comparação continua clara; nenhuma trava nova. Pularia as frases mais abstratas sobre universo e diversidade.
- **Step 2:** “produto legível” permanece na ficha; o restante explica o que deve estar visível, portanto não impede a prática.
- **Step 3:** agora vejo uma pessoa confrontando caneca e fotografia. Em cinco segundos entendo “conferir se é a mesma peça”; a legenda nomeia forma, cor e alça. Acerta. Não preciso pular a figura.

**Prática/promessa:** executável com foto própria. **Material:** presente; complementar agora oferece objeto próprio, sem exigir geração de personagem para fazer a atividade de produto. **Ajuste opcional:** trocar “legível” por “forma, cor e alça visíveis” na ficha. **Nota: 9,2.**

### Aula 11 — revisão dos três steps

- **Step 1:** continuo entendendo a identidade fixa, mas falta no caminho principal uma frase “foto A = produto; foto B = ambiente”. Eu buscaria ajuda para associar arquivos no pedido; o complementar tem o exemplo.
- **Step 2:** ambiente/detalhe/uso são claros. Ainda travo para preencher escolha/conjunto/encerramento com enquadramento e referência. A ficha continua com apenas uma cena vazia.
- **Step 3:** agora há seis imagens sobre a mesa; em cinco segundos entendo sequência variada. A legenda lista as funções, porém não identifica cada quadro e a cena de “conjunto” não fica inequívoca na miniatura. Pularia o texto redundante antes da imagem.

**Prática/promessa:** melhor, mas preencher seis cenas sozinho em dez minutos ainda exige inferir três delas. **Material:** resolvido o storyboard ausente: complementar manda copiar a ficha da própria aula seis vezes. **Correção mínima pendente:** acrescentar seis linhas preenchidas, por exemplo “1 ambiente: plano aberto do ateliê; 2 escolha: mão junto à caneca; 3 uso: mão segurando; 4 detalhe: aproximação do esmalte; 5 conjunto: caneca e pires na mesa; 6 encerramento: caneca lateral e espaço para mensagem”, indicando mesma referência do produto. **Nota: 8,5.**

### Aula 12 — revisão dos três steps

- **Step 1:** continuo entendendo corrigir só a peça errada. Pularia a passagem sobre figurino, pois a prática trata de produto.
- **Step 2:** ficha A/B/C é fácil. Há alternância entre defeito da camisa, duas alças e agora cor azul; não bloqueia, mas unificar pela cor reduziria esforço.
- **Step 3:** em cinco segundos identifico a foto azul entre duas terracota. A figura agora demonstra o critério e a legenda explica o problema sem me mandar adivinhá-lo.

**Prática/promessa:** consigo concluir mesmo com fotos próprias corretas: registro isso e redijo a correção do caso azul. Solução honesta e suficiente. **Material:** caso necessário está visível na própria aula. **Resíduo opcional:** instruir criar álbum temporário para ver três miniaturas e unificar exemplos pela cor. **Nota: 9.**

### Aula 13 — revisão dos três steps

- **Step 1:** global/local continua compreensível. “Temperatura” ainda seria melhor como “cor mais azulada ou amarelada”, mas não bloqueia a mancha.
- **Step 2:** definições de máscara e preenchimento permanecem úteis. A frase “confere se a seleção encostou na borda” ainda não explicita que, neste caso, deve evitar cobrir a caneca.
- **Step 3:** a nova ilustração mostra um pequeno remendo sobre o fundo, fora do objeto; em cinco segundos entendo limitar a correção. Legenda e desenho próprio no complementar substituem o esquema ausente. Acertou.

**Prática/promessa:** planejamento local executável. **Regressão no material:** o “Pedido completo do módulo” foi trocado por “Amplie apenas o ambiente para um quadro horizontal”, embora esta aula e a conferência seguinte tratem de remover elemento. Quem copia esse bloco faz outra operação. **Correção mínima pendente:** restaurar na aula 13 um pedido completo específico de remoção da mancha, preservando caneca, mesa e sombra; manter expansão só na 14. Não precisa mudar imagem. **Termos residuais:** estrutural/diagramação sem explicação no complementar. **Nota: 8,5.**

### Aula 14 — revisão dos três steps

- **Step 1:** regra de expandir fundo em vez de esticar é clara. Nenhuma nova trava.
- **Step 2:** sombra junto da base é entendível; escala/perspectiva ainda pedem exemplos observáveis. Eu pularia “conjunto de sinais” e procuraria a dica da borda da mesa.
- **Step 3:** ilustração mostra um quadro pequeno dentro de área maior desenhada. Em cinco segundos entendo ampliar ao redor sem deformar. Legenda adequada; ajuda mais que a advertência textual anterior. Não mostra comparação de sombra correta/incorreta, portanto não resolve sozinha todos os critérios da integração.

**Prática/promessa:** consigo planejar expansão, mas a lista de quatro termos ainda se beneficia de perguntas concretas. **Material:** pedido completo agora é de expansão, correto. Entretanto a seção seguinte “Conferência do módulo” continua: “Use uma cópia de uma imagem sua que contenha um elemento a remover... escolha outra correção localizada”. Isso contradiz a atividade. **Correção mínima pendente:** trocar essa conferência por “Compare com o original: a caneca manteve tamanho e forma? A borda da mesa continua? A luz vem do mesmo lado? A sombra começa no apoio?”. **Nota: 8,5.**

**Conclusão da rodada 2:** melhorias reais nas sete aulas; aulas 9, 10 e 12 atingem o corte desta persona. Aulas 8, 11, 13 e 14 ainda requerem as pequenas correções identificadas, sem necessidade de refazer imagens. A substituição global do pedido do módulo 5 precisa ser revista por aula para não trocar uma incoerência por outra. Não houve teste de interação nem participante humano real nesta rodada.

## Rodada 3 — julgamento final após correções pontuais

Em 2026-09-25 reli integralmente os HTML das aulas 8, 11, 13 e 14. Confirmei também em `curso.html` montado a presença das correções e a ausência dos dois parágrafos técnicos da aula 8. Não gerei nem inspecionei novas capturas nesta rodada: a avaliação visual continua apoiada nas telas da rodada 2; o novo julgamento é do conteúdo e da possibilidade de realizar a prática.

| Aula | Nota final | Evidência e julgamento como Mauro |
|---|---:|---|
| 8 | 9/10 | Os parágrafos sobre implementação/modelos destilados foram substituídos por frases simples. A ficha fornece A fotografia e B aquarela, condições mantidas, contorno/textura como critérios, duas tentativas e estado planejado. Agora consigo copiar e preparar o teste mesmo sem controles. |
| 9 | 9/10 | Mantém aprovação da rodada 2: receita preenchida, modelo desconhecido permitido e material corretamente localizado. |
| 10 | 9,2/10 | Mantém aprovação da rodada 2: escolha da foto-base executável, características concretas e ilustração adequada. |
| 11 | 9/10 | O step 2 agora contém as seis cenas completas. “Conjunto = caneca com pires” e “encerramento = caneca inteira com espaço acima” resolvem as funções que eu não conseguia imaginar. Posso usar essas seis linhas como exemplo e adaptar a ficha. |
| 12 | 9/10 | Mantém aprovação da rodada 2: posso registrar série correta e usar o caso visível da caneca azul para exercitar uma correção. |
| 13 | 9/10 | Pedido próprio agora remove só a mancha e preserva objeto/quadro/sombra. Conferência específica pede mancha ausente, emenda e preservação. O complementar deixou de mandar executar expansão. Consigo planejar a mudança por escrito ou desenho. |
| 14 | 9/10 | Pedido e conferência tratam ambos de expansão. A conferência agora nomeia continuidade da mesa, luz, sombra e objeto sem esticar, dando sentido prático aos termos da ficha. Consigo planejar e dizer o que conferir. |

**Estado final:** as sete aulas atingem pelo menos 9/10 para esta persona simulada. As travas que impediam cumprir as práticas foram resolvidas. Permanecem refinamentos não impeditivos: a aula 8 repete a dependência de nome/escala e seu exemplo poderia condicionar “valor menor preserva” à descrição da ferramenta; a aula 9 poderia trazer campo explícito de ferramenta; a aula 13 poderia traduzir temperatura e as categorias opcionais estrutural/diagramação. Esses pontos não impedem Mauro de realizar o planejamento pedido usando os exemplos atuais.

Esta aprovação cobre entendimento e práticas de planejamento descritas, não comprova resultado de geração/edição em uma ferramenta, tempo medido com pessoa real nem a nova quebra de linhas móvel da ficha de seis cenas. Os cinco checks textuais realizados no HTML montado passaram.
