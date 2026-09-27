# Validação EN/ES — 26/09/2026

- 21/21 aulas em cada idioma, auditoria final 10/10 por aula (auditoria-en.json e auditoria-es.json).
- Motor: 26/26 comportamentos aprovados em PT, EN e ES.
- Navegador: 21 aulas por idioma sem transbordamento a 390px; imagens carregadas, nenhum erro JavaScript; links de idioma preservam a aula.
- Exportação/importação: identifica a edição, restaura a edição correta e rejeita outra edição sem mudar o estado.
- Estrutura: mesmos IDs, respostas de quiz, contagem de aulas, links/arquivos locais válidos e JS sintaticamente válido.
- Desktop: EN/ES a 1440px, nos temas papel/escuro/sépia, sem transbordamento; capturas inspecionadas de EN aula1, ES aula21 e ES desktop escuro aula11.
- Revisão textual simulada pelo GPT-6 Luna: relatórios revisao-i18n-*.md. Não houve teste com alunos externos.
- 1.523 unidades traduzidas por idioma; tags/atributos, números, URLs e placeholders preservados. Nenhuma unidade longa ficou idêntica ao PT.
- Testes executados offline: requisições HTTP bloqueadas no navegador; fontes de fallback locais. Nenhuma API de modelo utilizada.

Capturas locais: /home/nmaldaner/projetos/output/cursos-v62-traducao/curso-prompting-imagem/.
