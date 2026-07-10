Projeto base bem simples de selenium e cypress, onde possui uma simples estruturação de pastas e arquivos afim de manter a legibilidade do código. O projeto possui a capacidade de rodar apenas testes do cypress e/ou testes do selenium assim como ambos podem ser executados ao mesmo tempo. A critério da necessidade

1° etapa: Após clonar com sucesso o projeto, execute o comando 'npm i' para instalar todas as dependências necessárias para que o projeto seja executado corretamente. (caso apareça alguma depreciação, apenas execute o comando npx audit fix conforme sugerido no terminal para corrigir)

2° etapa: certifiquisse que de após executar, as pastas 'node_modules', 'package.json' e 'package-lock.json' esteja no projeto

3° etapa: preencha o arquivo cypress.env.json com suas informações de acesso ao SISPREV, assim como as informações de acesso ao banco. Como esses dados são sensíveis, esse arquivo nunca será compartilhado com ninguém, será único para cada um.