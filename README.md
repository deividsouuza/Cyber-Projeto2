## Objetivos

- Explicar, em alto nível, como ransomware e keyloggers ameaçam a confidencialidade e a disponibilidade.
- Observar um fluxo simulado de impacto sem afetar o computador.
- Relacionar sinais de alerta a controles defensivos.
- Manter um projeto reproduzível e seguro para fins educacionais.

## O que o programa faz

O arquivo `simulacao.py` imprime dois roteiros com dados inventados:

1. **Ransomware:** mostra nomes fictícios de arquivos, um estado “antes/depois” conceitual e uma mensagem de resgate fictícia. Nenhum arquivo é lido, criado, sobrescrito ou criptografado.
2. **Keylogger:** mostra eventos de teclas previamente escritos no próprio exemplo. Não há captura do teclado ou gravação em arquivo. A etapa de exfiltração é apenas identificada como bloqueada, sem rede ou e-mail.

A simulação não usa `pynput`, `cryptography`, `smtplib`, permissões elevadas, persistência ou técnicas de furtividade.

## Como executar

Requer Python 3:

~~~bash
python simulacao.py
~~~

O programa não recebe argumentos nem acessa a rede ou o sistema de arquivos. Toda a demonstração acontece em memória e a saída aparece no terminal.

## Saída ilustrativa

~~~text
SIMULAÇÃO EDUCATIVA — sem captura, criptografia ou rede

[RANSOMWARE] arquivos fictícios: relatorio.txt, foto.jpg
[RANSOMWARE] estado simulado: acessíveis -> indisponíveis (apenas modelo)
[RANSOMWARE] nota fictícia: "Seus arquivos foram bloqueados." (não há resgate real)
[KEYLOGGER] eventos sintéticos: [tecla A], [tecla B], [ENTER]
[KEYLOGGER] captura real: não realizada
[EXFILTRAÇÃO] envio de dados: bloqueado/não implementado

Defesas: backups offline testados, princípio do menor privilégio, EDR/antivírus, atualizações, MFA e conscientização.
~~~

Essa saída descreve estados inventados, não uma infecção, captura ou criptografia real.

## Como essas ameaças funcionam (visão conceitual)

### Ransomware

Um ransomware malicioso pode obter execução, localizar dados acessíveis ao usuário, impedir seu uso e tentar extorquir a vítima. O impacto pode incluir indisponibilidade, exposição de dados e interrupção operacional. Pagar resgate não garante recuperação nem exclusão de cópias roubadas.

**Sinais que podem merecer investigação:** alterações incomuns em muitos arquivos, extensões inesperadas, alertas de proteção, processos desconhecidos acessando grande volume de dados e notas de resgate inesperadas.

### Keylogger

Um keylogger pode tentar registrar entradas do usuário para roubar credenciais ou outras informações. Uma implementação maliciosa pode esconder sua presença ou enviar registros a terceiros; este projeto não implementa nenhuma dessas capacidades.

**Sinais que podem merecer investigação:** aplicativos desconhecidos com permissões de acessibilidade/entrada, alertas do endpoint, conexões inesperadas e solicitações de credenciais fora do fluxo normal.

## Medidas de prevenção e resposta

- **Backups:** manter cópias offline ou imutáveis, separar credenciais do ambiente de produção e testar a restauração.
- **Atualizações:** corrigir sistema operacional, navegador, aplicativos e ferramentas de proteção.
- **Menor privilégio:** usar conta padrão no dia a dia, limitar permissões e restringir execução de aplicações quando possível.
- **Proteção de endpoint:** manter antivírus/EDR ativo e atualizado; investigar alertas em vez de ignorá-los.
- **E-mail e navegação:** desconfiar de anexos e links inesperados, validar remetentes e baixar software somente de fontes confiáveis.
- **Autenticação:** usar MFA e senhas únicas; evitar inserir credenciais após alertas ou em páginas suspeitas.
- **Rede:** aplicar firewall, segmentação e monitoramento de tráfego conforme o ambiente.
- **Resposta a incidente:** isolar o dispositivo suspeito da rede, preservar evidências e acionar a equipe responsável. Evitar apagar arquivos ou reinstalar antes de seguir o procedimento de resposta da organização.
- **Conscientização:** treinar usuários para reconhecer engenharia social e reportar eventos rapidamente.

## Reflexão

A simulação ajuda a distinguir o impacto conceitual de cada ameaça: ransomware afeta principalmente a disponibilidade e pode envolver roubo de dados; keyloggers ameaçam a confidencialidade de entradas do usuário. Defesas em camadas reduzem a chance de execução e ajudam a limitar o impacto. Backups testados e resposta rápida são importantes quando a prevenção falha.

Este material documenta apenas uma simulação segura. Não afirma que as aulas foram assistidas, que malware foi executado ou que houve testes em um ambiente real. Para completar o relato pessoal, acrescente suas próprias observações depois de assistir ao conteúdo do curso.

## Referências

- [Python — documentação oficial](https://docs.python.org/3/)
- [Cryptography — documentação](https://cryptography.io/)
- [pynput — página do projeto](https://pypi.org/project/pynput/)
- [smtplib — documentação oficial](https://docs.python.org/3/library/smtplib.html)
- [CISA — StopRansomware](https://www.cisa.gov/stopransomware)

## Arquivos

- `README.md` — escopo, explicações e recomendações defensivas.
- `simulacao.py` — roteiro fictício em memória, sem ações no sistema.
