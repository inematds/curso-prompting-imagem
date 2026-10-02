# Prompting de Imagem v6.2

Curso aberto e gratuito, com 7 módulos e 21 aulas de aproximadamente 15 minutos.
Enquadramento, luz, composição, referências, edição e organização de imagens de produto.

[Português](https://inematds.github.io/curso-prompting-imagem/) · [English](https://inematds.github.io/curso-prompting-imagem/en/) · [Español](https://inematds.github.io/curso-prompting-imagem/es/).

## Estrutura

- `landing.html`: apresentação e módulos. `index.html`: entrada pública.
- `aulas/`: aulas montadas a partir das fontes editoriais em `context/`.
- `curso.html`: página única com progresso local, práticas e revisão espaçada.
- `assets/`: motor oficial INEMA v6 e 21 ilustrações geradas com Codex image_gen.
- `context/curriculo.md`: público e objetivos; `context/leitor-*.md`: revisões simuladas.

A referência visual é OSWork v6.2: tema papel, leitura em uma coluna e aprendizagem discreta.
A identificação v6.2 indica o formato educacional; a versão deste conteúdo é 1.1.0.
As imagens são ilustrações didáticas, não comparações experimentais entre geradores.
O conteúdo é autoral; não inclui vídeos nem transcrições do acervo privado que originou o planejamento.

## Montagem e validação

Requer Python 3 e a skill `formato-curso-v6` instalada. `montar.py` usa o caminho local definido em `SKILL`.

```sh
python3 montar.py
node /caminho/formato-curso-v6/scripts/auditar-curso.cjs curso.html --json context/auditoria.json
node /caminho/formato-curso-v6/scripts/testar-motor.cjs curso.html
```

Os scripts de validação precisam de Playwright instalado; `PLAYWRIGHT_PATH` pode apontar para o pacote.
Não editar `curso.html` manualmente. Editar os JSON editoriais e montar novamente.
`revisar_conteudo.py` registra as correções da primeira edição; não é necessário rodá-lo para montar.

Validação desta edição: 21/21 aulas com 10/10 na auditoria automática; 26/26 comportamentos do motor aprovados;
leitura simulada de todas as aulas com nota ≥9. Isso não equivale a um teste com alunos reais.
Detalhes em `context/validacao.md`.

## Mais no INEMA.CLUB

- [Ficha deste curso](https://www.inema.club/cursos/283-prompting-de-imagem-v6-2-pense-como-diretor-de-fotografia/)
- [Guia para aprender inteligência artificial](https://www.inema.club/aprender-inteligencia-artificial/)
- [Catálogo de cursos](https://www.inema.club/cursos/)

## Edições EN/ES

Tradução textual com GPT-6 Luna por subagentes nativos da assinatura Codex, sem API externa.
As 21 aulas, cartões, práticas, glossário e controles estão em cada idioma; imagens são compartilhadas.
Progresso e anotações ficam separados por idioma. Exportações identificam a edição; uma edição rejeita o progresso da outra.
Revisões em `context/revisao-i18n-*.md` são simuladas, não testes com alunos reais.

Após montar o português, reaplique as traduções salvas (Python com BeautifulSoup):

```sh
python3 scripts/i18n_local.py build .
python3 scripts/verify_i18n.py .
node scripts/check_i18n_browser.cjs . /tmp/prompting-i18n-checks
```

A montagem não chama modelos nem redes. Catálogos traduzidos estão em `i18n/`; mudanças no texto português exigem atualizar o catálogo e revisar as novas traduções. Os scripts de JS e navegador usam os pacotes locais Babel/Playwright indicados em seus arquivos. O motor original `assets/curso.js` é preservado; `assets/curso-i18n.js` é a versão gerada com proteção de importação por idioma.

<!-- inema-backlink:v1 -->
## Mais no INEMA.CLUB

- [Ficha completa deste curso](https://www.inema.club/cursos/283-prompting-de-imagem-v6-2-pense-como-diretor-de-fotografia/)
- [Guia: como aprender inteligência artificial](https://www.inema.club/aprender-inteligencia-artificial/)
- [Todos os cursos](https://www.inema.club/cursos/)
<!-- /inema-backlink:v1 -->
