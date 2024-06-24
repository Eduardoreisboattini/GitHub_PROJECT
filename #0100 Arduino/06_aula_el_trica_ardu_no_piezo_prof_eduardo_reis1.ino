/*
  Melodia do Super Mario Bros

  Reproduz a melodia do tema principal do jogo "Super Mario Bros"
  utilizando a função tone() em quatro pinos diferentes.

  Circuito:
  * Quatro alto-falantes ou buzzers conectados aos pinos digitais 8, 7, 6, 5

  Criado com base no tema principal do jogo "Super Mario Bros"
  Este código de exemplo está em domínio público.
*/

void setup()
{
  pinMode(8, OUTPUT); // Configura o pino 8 como saída para o Piezo 1
  pinMode(7, OUTPUT); // Configura o pino 7 como saída para o Piezo 2
  pinMode(6, OUTPUT); // Configura o pino 6 como saída para o Piezo 3
  pinMode(5, OUTPUT); // Configura o pino 5 como saída para o Piezo 4
}

void loop()
{
  // Reproduz a melodia do tema principal do Super Mario Bros
  // Utiliza a função tone() para tocar notas musicais nos respectivos pinos

  // Primeira parte da melodia
  tone(8, 659, 200); // E5 no pino 8 (Piezo 1)
  tone(7, 0, 200);   // Pausa no pino 7 (Piezo 2)
  tone(6, 659, 200); // E5 no pino 6 (Piezo 3)
  tone(5, 0, 200);   // Pausa no pino 5 (Piezo 4)
  delay(200);

  tone(8, 659, 200); // E5 no pino 8 (Piezo 1)
  tone(7, 0, 200);   // Pausa no pino 7 (Piezo 2)
  tone(6, 659, 200); // E5 no pino 6 (Piezo 3)
  tone(5, 0, 200);   // Pausa no pino 5 (Piezo 4)
  delay(200);

  tone(8, 0, 50);    // Pausa no pino 8 (Piezo 1)
  tone(7, 0, 50);    // Pausa no pino 7 (Piezo 2)
  tone(6, 0, 50);    // Pausa no pino 6 (Piezo 3)
  tone(5, 0, 50);    // Pausa no pino 5 (Piezo 4)
  delay(50);

  tone(8, 659, 200); // E5 no pino 8 (Piezo 1)
  tone(7, 0, 200);   // Pausa no pino 7 (Piezo 2)
  tone(6, 0, 200);   // Pausa no pino 6 (Piezo 3)
  tone(5, 0, 200);   // Pausa no pino 5 (Piezo 4)
  delay(200);

  tone(8, 0, 50);    // Pausa no pino 8 (Piezo 1)
  tone(7, 0, 50);    // Pausa no pino 7 (Piezo 2)
  tone(6, 0, 50);    // Pausa no pino 6 (Piezo 3)
  tone(5, 0, 50);    // Pausa no pino 5 (Piezo 4)
  delay(50);

  tone(8, 784, 200); // G5 no pino 8 (Piezo 1)
  tone(7, 0, 200);   // Pausa no pino 7 (Piezo 2)
  tone(6, 0, 200);   // Pausa no pino 6 (Piezo 3)
  tone(5, 0, 200);   // Pausa no pino 5 (Piezo 4)
  delay(200);

  tone(8, 0, 50);    // Pausa no pino 8 (Piezo 1)
  tone(7, 0, 50);    // Pausa no pino 7 (Piezo 2)
  tone(6, 0, 50);    // Pausa no pino 6 (Piezo 3)
  tone(5, 0, 50);    // Pausa no pino 5 (Piezo 4)
  delay(50);

  tone(8, 523, 200); // C5 no pino 8 (Piezo 1)
  tone(7, 0, 200);   // Pausa no pino 7 (Piezo 2)
  tone(6, 0, 200);   // Pausa no pino 6 (Piezo 3)
  tone(5, 0, 200);   // Pausa no pino 5 (Piezo 4)
  delay(200);

  // Segunda parte da melodia
  tone(8, 0, 50);    // Pausa no pino 8 (Piezo 1)
  tone(7, 0, 50);    // Pausa no pino 7 (Piezo 2)
  tone(6, 0, 50);    // Pausa no pino 6 (Piezo 3)
  tone(5, 0, 50);    // Pausa no pino 5 (Piezo 4)
  delay(50);

  tone(8, 659, 200); // E5 no pino 8 (Piezo 1)
  tone(7, 0, 200);   // Pausa no pino 7 (Piezo 2)
  tone(6, 659, 200); // E5 no pino 6 (Piezo 3)
  tone(5, 0, 200);   // Pausa no pino 5 (Piezo 4)
  delay(200);

  tone(8, 0, 50);    // Pausa no pino 8 (Piezo 1)
  tone(7, 0, 50);    // Pausa no pino 7 (Piezo 2)
  tone(6, 0, 50);    // Pausa no pino 6 (Piezo 3)
  tone(5, 0, 50);    // Pausa no pino 5 (Piezo 4)
  delay(50);

  tone(8, 659, 200); // E5 no pino 8 (Piezo 1)
  tone(7, 0, 200);   // Pausa no pino 7 (Piezo 2)
  tone(6, 659, 200); // E5 no pino 6 (Piezo 3)
  tone(5, 0, 200);   // Pausa no pino 5 (Piezo 4)
  delay(200);

  tone(8, 0, 50);    // Pausa no pino 8 (Piezo 1)
  tone(7, 0, 50);    // Pausa no pino 7 (Piezo 2)
  tone(6, 0, 50);    // Pausa no pino 6 (Piezo 3)
  tone(5, 0, 50);    // Pausa no pino 5 (Piezo 4)
  delay(50);

  tone(8, 659, 200); // E5 no pino 8 (Piezo 1)
  tone(7, 0, 200);   // Pausa no pino 7 (Piezo 2)
  tone(6, 659, 200); // E5 no pino 6 (Piezo 3)
  tone(5, 0, 200);   // Pausa no pino 5 (Piezo 4)
  delay(200);

  tone(8, 0, 50);    // Pausa no pino 8 (Piezo 1)
  tone(7, 0, 50);    // Pausa no pino 7 (Piezo 2)
  tone(6, 0, 50);    // Pausa no pino 6 (Piezo 3)
  tone(5, 0, 50);    // Pausa no pino 5 (Piezo 4)
  delay(50);

  tone(8, 784, 200); // G5 no pino 8 (Piezo 1)
  tone(7, 0, 200);   // Pausa no pino 7 (Piezo 2)
  tone(6, 0, 200);   // Pausa no pino 6 (Piezo 3)
  tone(5, 0, 200);   // Pausa no pino 5 (Piezo 4)
  delay(200);

  // Terceira parte da melodia
  tone(8, 0, 50);    // Pausa no pino 8 (Piezo 1)
  tone(7, 0, 50);    // Pausa no pino 7 (Piezo 2)
  tone(6, 0, 50);    // Pausa no pino 6 (Piezo 3)
  tone(5, 0, 50);    // Pausa no pino 5 (Piezo 4)
  delay(50);

  tone(8, 0, 200);   // Silence no pino 8 (Piezo 1)
  tone(7, 0, 200);   // Silence no pino 7 (Piezo 2)
  tone(6, 0, 200);   // Silence no pino 6 (Piezo 3)
  tone(5, 0, 200);   // Silence no pino 5 (Piezo 4)
  delay(200);

  tone(8, 0, 50);    // Pausa no pino 8 (Piezo 1)
  tone(7, 0, 50);    // Pausa no pino 7 (Piezo 2)
  tone(6, 0, 50);    // Pausa no pino 6 (Piezo 3)
  tone(5, 0, 50);    // Pausa no pino 5 (Piezo 4)
  delay(50);

  tone(8, 0, 200);   // Silence no pino 8 (Piezo 1)
  tone(7, 0, 200);   // Silence no pino 7 (Piezo 2)
  tone(6, 0, 200);   // Silence no pino 6 (Piezo 3)
  tone(5, 0, 200);   // Silence no pino 5 (Piezo 4)
  delay(200);

  tone(8, 0, 50);    // Pausa no pino 8 (Piezo 1)
  tone(7, 0, 50);    // Pausa no pino 7 (Piezo 2)
  tone(6, 0, 50);    // Pausa no pino 6 (Piezo 3)
  tone(5, 0, 50);    // Pausa no pino 5 (Piezo 4)
  delay(50);

  tone(8, 659, 200); // E5 no pino 8 (Piezo 1)
  tone(7, 0, 200);   // Pausa no pino 7 (Piezo 2)
  tone(6, 0, 200);   // Pausa no pino 6 (Piezo 3)
  tone(5, 0, 200);   // Pausa no pino 5 (Piezo 4)
  delay(200);

  tone(8, 0, 50);    // Pausa no pino 8 (Piezo 1)
  tone(7, 0, 50);    // Pausa no pino 7 (Piezo 2)
  tone(6, 0, 50);    // Pausa no pino 6 (Piezo 3)
  tone(5, 0, 50);    // Pausa no pino 5 (Piezo 4)
  delay(50);

  tone(8, 0, 200);   // Silence no pino 8 (Piezo 1)
  tone(7, 0, 200);   // Silence no pino 7 (Piezo 2)
  tone(6, 0, 200);   // Silence no pino 6 (Piezo 3)
  tone(5, 0, 200);   // Silence no pino 5 (Piezo 4)
  delay(200);

  tone(8, 0, 50);    // Pausa no pino 8 (Piezo 1)
  tone(7, 0, 50);    // Pausa no pino 7 (Piezo 2)
  tone(6, 0, 50);    // Pausa no pino 6 (Piezo 3)
  tone(5, 0, 50);    // Pausa no pino 5 (Piezo 4)
  delay(50);

  tone(8, 784, 200); // G5 no pino 8 (Piezo 1)
  tone(7, 0, 200);   // Pausa no pino 7 (Piezo 2)
  tone(6, 0, 200);   // Pausa no pino 6 (Piezo 3)
  tone(5, 0, 200);   // Pausa no pino 5 (Piezo 4)
  delay(200);

  // Quarta parte da melodia
  tone(8, 0, 50);    // Pausa no pino 8 (Piezo 1)
  tone(7, 0, 50);    // Pausa no pino 7 (Piezo 2)
  tone(6, 0, 50);    // Pausa no pino 6 (Piezo 3)
  tone(5, 0, 50);    // Pausa no pino 5 (Piezo 4)
  delay(50);

  tone(8, 0, 200);   // Silence no pino 8 (Piezo 1)
  tone(7, 0, 200);   // Silence no pino 7 (Piezo 2)
  tone(6, 392, 200); // G4 no pino 6 (Piezo 3)
  tone(5, 0, 200);   // Pausa no pino 5 (Piezo 4)
  delay(200);

  tone(8, 0, 50);    // Pausa no pino 8 (Piezo 1)
  tone(7, 0, 50);    // Pausa no pino 7 (Piezo 2)
  tone(6, 0, 50);    // Pausa no pino 6 (Piezo 3)
  tone(5, 0, 50);    // Pausa no pino 5 (Piezo 4)
  delay(50);

  tone(8, 0, 200);   // Silence no pino 8 (Piezo 1)
  tone(7, 0, 200);   // Silence no pino 7 (Piezo 2)
  tone(6, 0, 50);    // Pausa no pino 6 (Piezo 3)
  tone(5, 0, 50);    // Pausa no pino 5 (Piezo 4)
  delay(50);

  tone(8, 0, 200);   // Silence no pino 8 (Piezo 1)
  tone(7, 0, 200);   // Silence no pino 7 (Piezo 2)
  tone(6, 0, 50);    // Pausa no pino 6 (Piezo 3)
  tone(5, 0, 50);    // Pausa no pino 5 (Piezo 4)
  delay(50);

  tone(8, 0, 200);   // Silence no pino 8 (Piezo 1)
  tone(7, 0, 200);   // Silence no pino 7 (Piezo 2)
  tone(6, 440, 200); // A4 no pino 6 (Piezo 3)
  tone(5, 0, 200);   // Pausa no pino 5 (Piezo 4)
  delay(200);

  tone(8, 0, 50);    // Pausa no pino 8 (Piezo 1)
  tone(7, 0, 50);    // Pausa no pino 7 (Piezo 2)
  tone(6, 0, 50);    // Pausa no pino 6 (Piezo 3)
  tone(5, 0, 50);    // Pausa no pino 5 (Piezo 4)
  delay(50);

  tone(8, 0, 200);   // Silence no pino 8 (Piezo 1)
  tone(7,

 0, 200);   // Silence no pino 7 (Piezo 2)
  tone(6, 0, 50);    // Pausa no pino 6 (Piezo 3)
  tone(5, 0, 50);    // Pausa no pino 5 (Piezo 4)
  delay(50);

  tone(8, 0, 200);   // Silence no pino 8 (Piezo 1)
  tone(7, 0, 200);   // Silence no pino 7 (Piezo 2)
  tone(6, 0, 50);    // Pausa no pino 6 (Piezo 3)
  tone(5, 0, 50);    // Pausa no pino 5 (Piezo 4)
  delay(50);

  tone(8, 523, 200); // C5 no pino 8 (Piezo 1)
  tone(7, 0, 200);   // Pausa no pino 7 (Piezo 2)
  tone(6, 0, 200);   // Pausa no pino 6 (Piezo 3)
  tone(5, 0, 200);   // Pausa no pino 5 (Piezo 4)
  delay(200);
}