import  time

# Função para verificar se o corpo do e-mail contém palavras suspeitas de phishing
def verificar_phishing(mensagem):
    # Lista de palavras que indicam possíveis e-mails de phishing
    palavras_suspeitas = ["Ganhe", "Prêmio", "Urgente", "Desconto", "Click", "Promoção", "Ganhe",
"Prêmio",
"Urgente",
"Desconto",
"Promoção",
"Exclusivo",
"Rápido",
"Imediato",
"Alerta",
"Aviso",
"Não perca",
"Oportunidade",
"Grátis",
"Atualização",
"Confirmação",
"Reclamação",
"Ação necessária",
"Suspensão",
"Bloqueio",
"Rede social"
"Atualize agora",
"Verifique",
"Clique aqui",
"Acione",
"Oferta",
"Pagamento",
"Fatura",
"Registro",
"Credenciamento",
"Conta bancária",
"Transferência",
"Seguro",
"Prontidão",
"Acabou de ser escolhido",
"Ativar",
"Instruções",
"Suporte técnico",
"Boa sorte",
"Reembolsar",
"Urgência",
"Limite de tempo",
"Ativação",
"Vencimento",
"Recuperação de conta",
"Acesso restrito",
"Reconhecimento"
"Promessa",
"Jogo",
"Crédito",
"Segurança",
"Atualização de dados",
"Confirmação de identidade",
"Transferência urgente",
"Bônus",
"Convite",
"Cartão de crédito",
"Parabéns",
"Recompensa",
"Seu prêmio",
"Ganho imediato",
"Clique agora",
"Oferta exclusiva",
"Vaga limitada",
"Benefícios exclusivos",
"Confirmar agora",
"Ganhe dinheiro",
"Enviar agora",
    ]


    # TODO: Verifique se alguma palavra suspeita está presente no corpo do e-mail:
    mensagem = mensagem.lower()

    # Verificando se alguma palavra suspeita está presente no corpo do e-mail
    for palavra in palavras_suspeitas:
        if palavra in mensagem:
            return "Phishing"

    # Caso não encontre nenhuma palavra suspeita
    return "Seguro"


email_usuario = input("Cole aqui a mensagem que voce recebeu: ")

email_usuario = email_usuario.strip()

resultado = verificar_phishing(email_usuario)
time.sleep(5)
print("Analisando...")
time.sleep(2)
print(f"Classificação: {resultado}")