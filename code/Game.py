import sys
import pygame
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Menu import Menu
class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH,WIN_HEIGHT ))


    def run(self, ):
        # Loop principal do jogo
        rodando = True
        while rodando:
            menu =  Menu(self.window)
            menu.run()
            pass






            # Verificação de eventos
            """for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    rodando = False  # Sai do loop se o evento for de fechamento
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_w:
                        # Lógica para tecla W pressionada
                        print("Tecla W pressionada")
                    elif evento.key == pygame.K_s:
                        # Lógica para tecla S pressionada
                        print("Tecla S pressionada")
                    elif evento.key == pygame.K_a:
                        # Lógica para tecla A pressionada
                        print("Tecla A pressionada")
                    elif evento.key == pygame.K_d:
                        # Lógica para tecla D pressionada
                        print("Tecla D pressionada")
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    if evento.button == 1:
                        # Lógica para clique do botão esquerdo do mouse
                        print("Botão esquerdo do mouse pressionado:", evento.pos)
                    elif evento.button == 3:
                        # Lógica para clique do botão direito do mouse
                        print("Botão direito do mouse pressionado:", evento.pos)

            # Lógica de atualização (aqui você desenharia e atualizaria o jogo)
            # Adicione aqui o código para desenhar seus objetos
            pygame.display.flip()  # Atualiza a tela

        # Encerramento do Pygame
        pygame.quit()
        sys.exit()
        """

