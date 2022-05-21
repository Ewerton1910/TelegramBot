import requests
import time
import json
import os
import webbrowser


class TelegramBot:
    def __init__(self):
        token = ''
        self.url_base = f'https://api.telegram.org/bot{token}/'

    def Iniciar(self):
        update_id = None
        while True:
            atualizacao = self.obter_novas_mensagens(update_id)
            dados = atualizacao["result"]
            if dados:
                for dado in dados:
                    update_id = dado['update_id']
                    mensagem = str(dado["message"]["text"])
                    chat_id = dado["message"]["from"]["id"]
                    eh_primeira_mensagem = int(
                        dado["message"]["message_id"]) == 1
                    resposta = self.criar_resposta(
                        mensagem, eh_primeira_mensagem)
                    self.responder(resposta, chat_id)

    # Obter mensagens
    def obter_novas_mensagens(self, update_id):
        link_requisicao = f'{self.url_base}getUpdates?timeout=100'
        if update_id:
            link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
        resultado = requests.get(link_requisicao)
        return json.loads(resultado.content)

    # Criar uma resposta
    def criar_resposta(self, mensagem, eh_primeira_mensagem):
        if eh_primeira_mensagem == True or mensagem in ('menu', 'Menu'):
            return f'''Digite o número do Assunto Para o atendimento :{os.linesep}1 - Conhecer a TestBet{os.linesep}2 - Conhecer Valores dos Planos{os.linesep}3 - Link para a Hotmart{os.linesep}4 - Saber mais'''
        if mensagem == '1':
            return f'''A TestBet é um Grupo no qual você recebe dicas de entradas no esporte virtual, sendo um total de 19 entradas diarias.{os.linesep}Gostaria de Conhecer nossos planos?(s/n)
            '''
        elif mensagem == '2':
            return f'''Plano Mensal - R$75,00 \nPlano Anual - R$ 199,00{os.linesep}Confirmar pedido?(s/n)
            '''
        elif mensagem == '3':
            return f'''Click no link para ser redirecionado para a Hotmart('https://hotmart.com/pt-br/marketplace/produtos/bet-milhao-vip/I68095613P'){os.linesep}Confirmar pedido?(s/n)'''
        elif mensagem == '4':
            return f'''Lucrar com futebol virtual sem precisar entender nada, é sério isso?

É exatamente assim que o Robô BET MILHÃO funciona...

➡️Ele análisa os jogos do futebol VIRTUAL DA BETANO em tempo real que estão acontecendo. E após selecionar as melhores oportunidades ele envia no Grupo VIP.🤖🤑

✅Você não precisa análisar
✅Não precisa entender de futebol
✅Não precisa dispor de seu tempo
✅Não precisa ter experiência
✅Não atrapalha em nada no seu dia

É simples! Basta clicar no LINK e seguir a dica do Robô!

Já são mais de 300 alunos lucrando diáriamente com o Robô mais assertivo do Brasil! 🤑

➡️Quer falar diretamente comigo e tirar suas dúvidas?
Clique no LINK abaixo ⤵️


@SUPORTEBETMILHAO{os.linesep}Confirmar pedido?(s/n)'''  

        elif mensagem.lower() in ('s', 'sim'):
            return ''' Acesse o Site para realizar sua compra: https://hotmart.com/pt-br/marketplace/produtos/bet-milhao-vip/I68095613P '''
        elif mensagem.lower() in ('n', 'não'):
            return ''' Pedido Confirmado! '''
        else:
            return 'Bem vindo a TestBet Gostaria de acessar o menu? Digite "menu"'

    # Responder
    def responder(self, resposta, chat_id):
        link_requisicao = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(link_requisicao)


bot = TelegramBot()
bot.Iniciar()