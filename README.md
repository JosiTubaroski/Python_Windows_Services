# Python | Como instalar um script Python no Windows Services

Estudo sobre como instalar um script python no windows services ou seja um agendador de tarefas em Python.

## Estrutura do projeto no Visual Code

![Estrutura Projeto](https://github.com/JosiTubaroski/Python_Windows_Services/blob/main/img/Estrutura_Projeto.GIF)

## Instando bibliotecas

No exemplo abaixo foi instalada a biblioteca schedule pelo próprio terminal do Visual Code

![Biblioteca Schedule](https://github.com/JosiTubaroski/Python_Windows_Services/blob/main/img/02_Biblioteca_Schedule.GIF)

## Importando as bibliotecas

![Importando Bibliotecas](https://github.com/JosiTubaroski/Python_Windows_Services/blob/main/img/03_ImportandoBibliotecas.GIF)

## Definindo funções


![image](https://github.com/JosiTubaroski/Python_Windows_Services/blob/main/img/04_Definindo_Funcoes.GIF)

## Montando os schedulers

![image](https://github.com/JosiTubaroski/Python_Windows_Services/blob/main/img/05_Schedulando.GIF)

## Determinando a condição de execução

![image](https://github.com/JosiTubaroski/Python_Windows_Services/blob/main/img/06_Determina_Cond_Exec.GIF)

## Execução automatica de atividades

![image](https://github.com/JosiTubaroski/Python_Windows_Services/blob/main/img/08_Executando_Jobs.GIF)

Para interromper uma execução, utilizar Ctrl + C.

## Criando o ambiente virtualenv

![image](https://github.com/JosiTubaroski/Python_Windows_Services/blob/main/img/07_Criando_VirtualEnv.GIF)

## Ativando JobScheduler1

![image](https://github.com/JosiTubaroski/Python_Windows_Services/blob/main/img/09_Ativar_JobScheduler.GIF)

## JobScheduler1 Ativado

![image](https://github.com/JosiTubaroski/Python_Windows_Services/blob/main/img/10_Job_Ativado.GIF)

Para ativação do jobscheduler1 foi necessário executar o script abaixo no PowerShell

![image](https://github.com/JosiTubaroski/Python_Windows_Services/blob/main/img/11_Comando_Shell.GIF)

## Baixar o programa que se chama NSSM

![image](https://github.com/JosiTubaroski/Python_Windows_Services/blob/main/img/12_Download_NSSM.GIF)

Sobre o NSSM: O "NSSM.exe" refere-se ao "Non-Sucking Service Manager", que é uma ferramenta de código aberto para Windows usada para criar e gerenciar serviços do Windows. Um serviço no Windows é um programa ou processo que é executado em segundo plano, geralmente sem uma interface de usuário visível, e pode ser configurado para iniciar automaticamente quando o sistema é iniciado.

O NSSM permite que você converta um aplicativo ou script em um serviço do Windows, o que pode ser útil em várias situações. Por exemplo, você pode usá-lo para executar uma tarefa em segundo plano, como um servidor web, um serviço de banco de dados, ou qualquer outro aplicativo que precise ser executado como um serviço.

## Em seguida executar o DOS como ADMINISTRADOR, e realizar a instalação do serviço

![image](https://github.com/JosiTubaroski/Python_Windows_Services/blob/main/img/13_Instalacao_Servi%C3%A7o.GIF)

## Acessar serviços e verificar o serviço Jobscheduler1

![image](https://github.com/JosiTubaroski/Python_Windows_Services/blob/main/img/14_Servico_Job_Scheduler.GIF)

## Iniciar Serviço

![image](https://github.com/JosiTubaroski/Python_Windows_Services/blob/main/img/15_Iniciar_Servico.GIF)

![image](https://github.com/JosiTubaroski/Python_Windows_Services/blob/main/img/16_Servico_EmExecucao.GIF)

## Logs do Serviço

![image](https://github.com/JosiTubaroski/Python_Windows_Services/assets/66569714/b8bea5db-0b09-4b96-8570-8750df9b634e)

