# Prompting de Imagem v6.2

Curso aberto e gratuito, com 7 módulos e 21 aulas de aproximadamente 15 minutos.
Enquadramento, luz, composição, referências, edição e organização de imagens de produto.

[Abra o curso](https://inematds.github.io/curso-prompting-imagem/).

## Estrutura

- `landing.html`: apresentação e módulos. `index.html`: entrada pública.
- `aulas/`: aulas montadas a partir das fontes editoriais em `context/`.
- `curso.html`: página única com progresso local, práticas e revisão espaçada.
- `assets/`: motor oficial INEMA v6 e 21 ilustrações geradas com Codex image_gen.
- `context/curriculo.md`: público e objetivos; `context/leitor-*.md`: revisões simuladas.

A referência visual é OSWork v6.2: tema papel, leitura em uma coluna e aprendizagem discreta.
A identificação v6.2 indica o formato educacional; a versão deste conteúdo é 1.0.0.
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
