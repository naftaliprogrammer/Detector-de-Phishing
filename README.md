# Detector-de-Phishing
Este repositório contém um script simples em Python para detectar e-mails suspeitos de phishing com base em palavras-chave comuns encontradas em mensagens fraudulentas. A função verificar_phishing verifica o corpo do e-mail em busca de termos associados a esquemas de phishing, como "Ganhe", "Prêmio", "Urgente", "Promoção", entre outros. Se alguma dessas palavras for encontrada, o e-mail é classificado como "Phishing"; caso contrário, é classificado como "Seguro".

Funcionalidades:

Análise de mensagens de e-mail em busca de palavras-chave suspeitas.
Classificação do e-mail como "Phishing" ou "Seguro".
Interface simples para o usuário inserir a mensagem a ser analisada.
Simulação de tempo de processamento para análise.
Como usar:

Cole o conteúdo do e-mail recebido quando solicitado.
O script analisará a mensagem e informará se o e-mail é suspeito de phishing ou não.
Tecnologias utilizadas:

Python 3.x
Biblioteca time para simulação de pausa no processo
Este script pode ser útil para detectar e alertar sobre e-mails fraudulentos e prevenir ataques de phishing.
