import openai


##Obtem a chave da API do modelo de linguagem
openai.api_key = "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"

def gera_texto(texto):
    ##Cria a resposta do modelo de linguagem
    response = openai.Completion.create(
        
        engine = "text-davinci-003", #Modelo usado
        prompt = texto, #Texto inicial com o chatbot
        max_tokens = 150, #Tamanho da resposta gerada do modelo
        n = 5, #Quantas conclusões serao geradas a cada prompt
        stop = None, #O texto retornado nao conterá a sequência de parada
        temperature = 0.8, #Medida aleatoria de um texto gerado pelo menos onde o valor vai de 0 a 1.
                           #Quanto mais proximo de 1 - mais aleatória.
                           #Mais proximo de 0 - saída muito identificavel.
        
    )
    
    return response.choices[0].text.strip()

def main():
    
    print("\nBem vindo ao GPT-4 Chabot!")
    print("(Digite 'sair' a qualquer momento para encerrar o chat)")
    
    while True:
        user_message = input("\nVocê: ") #Pega a pergunta digitada pelo usuario
        
        if user_message.lower() == "sair": #Finaliza o programa caso o usuario escreva sair
            break
    
        gpt4_prompt = f"\nUsuário: {user_message}\nChatbot:" #Insere a mensagem digitada na variavel criada 
        chatbot_response = gera_texto(gpt4_prompt) #Gera a resposta do chatbot pela funcao gera_texto
        print(f"\nChatbot: {chatbot_response}\n\n") #Imprime a resposta
    
if __name__ == "__main__":
    main()