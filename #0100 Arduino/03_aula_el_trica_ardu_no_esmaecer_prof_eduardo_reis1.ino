// Código C++
//
/*
  Fade
  Este exemplo mostra como fazer um LED no pino 9
  diminuir e aumentar de intensidade usando a função
  analogWrite().

  A função analogWrite() utiliza PWM, então se você
  quiser mudar o pino que está usando, certifique-se de
  escolher outro pino que suporte PWM. Na maioria dos
  Arduinos, os pinos PWM são identificados pelo símbolo
  "~", como ~3, ~5, ~6, ~9, ~10 e ~11.
*/

int brightness = 0; // variável para controlar a intensidade do LED

void setup()
{
  pinMode(9, OUTPUT); // Configura o pino 9 como saída
}

void loop()
{
  // Aumenta a intensidade do LED
  for (brightness = 0; brightness <= 255; brightness += 5) {
    analogWrite(9, brightness); // Define a intensidade do LED
    delay(30); // Aguarda 30 milissegundos
  }

  // Diminui a intensidade do LED
  for (brightness = 255; brightness >= 0; brightness -= 5) {
    analogWrite(9, brightness); // Define a intensidade do LED
    delay(30); // Aguarda 30 milissegundos
  }
}
