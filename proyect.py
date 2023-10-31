"""Juego \"Piedra, Papel o Tijera\""""


import random


def jugar():
    """Código del juego"""

    usuario = input(
        "Elige 'p' para piedra, 'pa' para papel y 't' para tijera: ")
    usuario = usuario.lower()

    elementos = ['p', 'pa', 't']
    computadora = random.choice(elementos)

    if usuario == computadora:
        return f"Han quedado en empate {computadora}"

    if is_ganador(usuario, computadora):
        return f"Tu: {usuario} y la computadora: {computadora}. Has ganado 💯🔱"
    return f"Tu: {usuario} y la computadora: {computadora}. Has perdido 😥"


def is_ganador(jugador, oponente):
    # Condiciones para ganar: p > t, t > pa, pa > p
    """Función del ganador"""

    if (jugador == 'p' and oponente == 't') or (jugador == 't' and oponente == 'pa') or (jugador == 'pa' and oponente == 'p'):
        return True
    return False


if __name__ == "__main__":
    print(jugar())
