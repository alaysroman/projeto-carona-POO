from typing import List, Dict

# Classe para gerenciamento de caronas
class Carona:
    def __init__(self, origem: str, destino: str, horario: str, vagas: int):
        self.origem = origem
        self.destino = destino
        self.horario = horario
        self.vagas = vagas

    def reservar_vaga(self) -> bool:
        if self.vagas > 0:
            self.vagas -= 1
            return True
        return False

    def exibir_detalhes(self):
        return {
            "origem": self.origem,
            "destino": self.destino,
            "horario": self.horario,
            "vagas": self.vagas,
        }

# Classe para gerenciar os usuários
class Usuario:
    def __init__(self, nome: str, email: str):
        self.nome = nome
        self.email = email
        self.historico_reservas = []

    def reservar_carona(self, carona: Carona):
        if carona.reservar_vaga():
            self.historico_reservas.append(carona)
            print(f"Reserva feita com sucesso para {carona.origem} -> {carona.destino}.")
        else:
            print("Reserva não disponível: carona sem vagas.")

    def visualizar_historico(self):
        print(f"Histórico de reservas para {self.nome}:")
        for carona in self.historico_reservas:
            detalhes = carona.exibir_detalhes()
            print(f"- {detalhes['origem']} -> {detalhes['destino']} às {detalhes['horario']}")

# Classe para a interface de interação
class InterfaceCarona:
    def __init__(self):
        self.caronas = []

    def adicionar_carona(self, origem: str, destino: str, horario: str, vagas: int):
        nova_carona = Carona(origem, destino, horario, vagas)
        self.caronas.append(nova_carona)
        print(f"Carona de {origem} para {destino} adicionada com sucesso!")

    def listar_caronas(self):
        print("Lista de caronas disponíveis:")
        for idx, carona in enumerate(self.caronas, start=1):
            detalhes = carona.exibir_detalhes()
            print(f"{idx}. {detalhes['origem']} -> {detalhes['destino']} às {detalhes['horario']} | Vagas: {detalhes['vagas']}")

    def selecionar_carona(self, indice: int) -> Carona:
        if 0 < indice <= len(self.caronas):
            return self.caronas[indice - 1]
        else:
            print("Índice inválido.")
            return None

# Classe para notificações
class Notificacao:
    @staticmethod
    def enviar_email(destinatario: str, mensagem: str):
        print(f"Email enviado para {destinatario}: {mensagem}")

    @staticmethod
    def exibir_notificacao(mensagem: str):
        print(f"Notificação: {mensagem}")

# Função principal
def main():
    interface = InterfaceCarona()

    # Adicionando algumas caronas
    interface.adicionar_carona("São Paulo", "Rio de Janeiro", "10:00", 3)
    interface.adicionar_carona("Curitiba", "Florianópolis", "15:00", 2)

    # Listando caronas
    interface.listar_caronas()

    # Criando um usuário
    usuario = Usuario(nome="Ana", email="ana@email.com")

    # Reservando uma carona
    carona_selecionada = interface.selecionar_carona(1)
    if carona_selecionada:
        usuario.reservar_carona(carona_selecionada)

    # Visualizando o histórico de reservas
    usuario.visualizar_historico()

    # Enviando uma notificação
    Notificacao.enviar_email(usuario.email, "Sua reserva foi confirmada!")
    Notificacao.exibir_notificacao("Reserva realizada com sucesso!")

    # Listar caronas novamente para ver atualização de vagas
    interface.listar_caronas()

if __name__ == "__main__":
    main()

