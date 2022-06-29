import os

def respondendo(perguntas, nome):
    if perguntas == '1':
        print(f'{os.linesep}{nome}, o Meta Marcha é um projeto de ERP social desenvolvido por estudantes do Instituto PROA, tendo como objetivo ajudar empreendedores na gestão de sua empresa e somando também conhecimentos através de cursos.{os.linesep}')
    elif perguntas == '2':
        print(f'{os.linesep}{nome}, nossos planos têm um valor social que consideramos custo benefício, visando te ajudar por um baixo preço e ao mesmo tempo manter nossa plataforma online. A partir de R$ 19,90 você tem acesso à diversas ferramentas que auxiliarão na manutenção de sua empresa, incluindo controle de estoque e de caixa.{os.linesep}')
    elif perguntas == '3':
        print(f'{os.linesep}{nome}, você pode escolher o plano que melhor te agrade e assassinar com cartão de crédito ou débito. Todos os nossos planos têm teste grátis de 30 dias, com cobrança normal após esse prazo.{os.linesep}')
    elif perguntas == '4':
        print(f'{os.linesep}{nome}, mantemos um código de ética fortemente baseado na LGPD (Lei Geral de Proteção de Dados Pessoais), em vigor desde 2020. Nela, temos o dever de proteger seus dados com o mais extremo sigilo, além de atualizar constantemente sobre o modo como trabalhamos. Você pode ler os nossos Termos de Uso para saber mais sobre a equipe e o tratamento de dados.{os.linesep}')
    elif perguntas == '5':
        print(f'{os.linesep}{nome}, o Meta Marcha planeja não apenas engrandecer a gestão de sua empresa, mas também quem a dirige. Oferecemos blogs gratuitos para que você se profissionalize, sendo não só um bom empreendedor, mas uma ótima pessoa em todos os âmbitos.{os.linesep}')
    elif perguntas == '6':
        print(f'{os.linesep}{nome}, o Meta Marcha foi desenvolvido por sete programadores com a missão de ajudar micro e pequenos empreendedores na gestão de sua empresa. Somos: Amanda Valentim (front-end), Camila Soares (front-end), Beatriz Miranda (back-end e design), João Pedro (full stack), Michelly Nonato (full stack) e Samara Moura (back-end, design e documentação). Você pode encontrar nossos contatos na aba Devs.{os.linesep}')
    else:
        print('Selecione uma opcao valida!')


def start():
    # informacoes
    print('Salve! Eu sou a Melissa e vou te ajudar hoje.')
    nome = input(f'{os.linesep}Qual é o seu nome?  ')


    while True:

        # terminal opções
        perguntas = input(f'{os.linesep}{nome}, selecione sua dúvida:{os.linesep}1. O que é o Meta Marcha?{os.linesep}2. Preço dos planos{os.linesep}3. Como posso assinar?{os.linesep}4. Proteção de dados{os.linesep}5. Blogs e cursos{os.linesep}6. A equipe{os.linesep}')

        # resposdendo
        respondendo(perguntas, nome)


if __name__ == '__main__':
    start()