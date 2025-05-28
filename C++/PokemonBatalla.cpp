#include <iostream>
#include <string>
using namespace std;

class Ataque {
public:
    string nombre;
    int dano;

    Ataque(string n, int d) {
        nombre = n;
        dano = d;
    }
};

class Pokemon {
public:
    string nombre;
    int vida;
    Ataque ataque1;
    Ataque ataque2;
    Ataque ataque3;
    Ataque ataque4;

    Pokemon(string n, int v, Ataque a1, Ataque a2, Ataque a3, Ataque a4)
        : nombre(n), vida(v), ataque1(a1), ataque2(a2), ataque3(a3), ataque4(a4) {}

    void atacar(Pokemon &enemigo, Ataque ataque) {
        cout << nombre << " usa " << ataque.nombre << endl;
        enemigo.vida = enemigo.vida - ataque.dano;
        if (enemigo.vida < 0) enemigo.vida = 0;
        cout << enemigo.nombre << " le quedan " << enemigo.vida << " puntos de vida." << endl << endl;
    }

    void mostrarAtaques() {
        cout << "1. " << ataque1.nombre << " (" << ataque1.dano << " daño)" << endl;
        cout << "2. " << ataque2.nombre << " (" << ataque2.dano << " daño)" << endl;
        cout << "3. " << ataque3.nombre << " (" << ataque3.dano << " daño)" << endl;
        cout << "4. " << ataque4.nombre << " (" << ataque4.dano << " daño)" << endl;
    }

    Ataque elegirAtaque(int opcion) {
        if (opcion == 1) return ataque1;
        else if (opcion == 2) return ataque2;
        else if (opcion == 3) return ataque3;
        else return ataque4;
    }
};

Pokemon elegirPokemon(int jugador) {
    cout << "Jugador " << jugador << ", elige tu Pokemon:" << endl;
    cout << "1. Pikachu\n2. Charmander\n3. Bulbasaur\n4. Squirtle" << endl;
    int eleccion;
    cin >> eleccion;

    if (eleccion == 1) {
        return Pokemon("Pikachu", 100,
            Ataque("Impactrueno", 20),
            Ataque("Placaje", 10),
            Ataque("Ataque Rapido", 15),
            Ataque("Rayo", 30));
    } else if (eleccion == 2) {
        return Pokemon("Charmander", 100,
            Ataque("Lanzallamas", 25),
            Ataque("Aranazo", 15),
            Ataque("Bola de Fuego", 15),
            Ataque("Placaje", 10));
    } else if (eleccion == 3) {
        return Pokemon("Bulbasaur", 100,
            Ataque("Latigazo", 20),
            Ataque("Hoja Afilada", 25),
            Ataque("Placaje", 10),
            Ataque("Drenadoras", 15));
    } else {
        return Pokemon("Squirtle", 100,
            Ataque("Pistola Agua", 20),
            Ataque("Burbuja", 15),
            Ataque("Placaje", 10),
            Ataque("Hidro Pulso", 25));
    }
}

int main() {
    cout << "Batalla Pokemon" << endl;

    Pokemon jugador1 = elegirPokemon(1);
    Pokemon jugador2 = elegirPokemon(2);

    while (jugador1.vida > 0 && jugador2.vida > 0) {
        int opcion;

        cout << jugador1.nombre << ", escoge ataque:" << endl;
        jugador1.mostrarAtaques();
        cin >> opcion;
        jugador1.atacar(jugador2, jugador1.elegirAtaque(opcion));

        if (jugador2.vida == 0) break;

        cout << jugador2.nombre << ", escoge ataque:" << endl;
        jugador2.mostrarAtaques();
        cin >> opcion;
        jugador2.atacar(jugador1, jugador2.elegirAtaque(opcion));
    }

    if (jugador1.vida == 0 && jugador2.vida == 0) {
        cout << "Empate" << endl;
    } else if (jugador1.vida == 0) {
        cout << jugador2.nombre << " gana" << endl;
    } else {
        cout << jugador1.nombre << " gana" << endl;
    }

    return 0;
}