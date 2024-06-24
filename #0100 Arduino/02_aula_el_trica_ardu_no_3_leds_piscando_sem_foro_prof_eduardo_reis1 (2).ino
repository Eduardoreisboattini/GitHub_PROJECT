// Definindo os pinos dos LEDs
const int pinVermelho = 2;
const int pinAmarelo = 3;
const int pinVerde = 4;

void setup() {
  // Configura os pinos dos LEDs como saídas
  pinMode(pinVermelho, OUTPUT);
  pinMode(pinAmarelo, OUTPUT);
  pinMode(pinVerde, OUTPUT);
}

void loop() {
  // Verde aceso por 7 segundos
  digitalWrite(pinVerde, HIGH);
  digitalWrite(pinAmarelo, LOW);
  digitalWrite(pinVermelho, LOW);
  delay(7000); // 7 segundos

  // Amarelo aceso por 3 segundos
  digitalWrite(pinVerde, LOW);
  digitalWrite(pinAmarelo, HIGH);
  digitalWrite(pinVermelho, LOW);
  delay(3000); // 3 segundos

  // Vermelho aceso por 7 segundos
  digitalWrite(pinVerde, LOW);
  digitalWrite(pinAmarelo, LOW);
  digitalWrite(pinVermelho, HIGH);
  delay(7000); // 7 segundos

  // Amarelo piscando rápido antes de voltar para o verde
  for (int i = 0; i < 5; i++) {
    digitalWrite(pinVerde, LOW);
    digitalWrite(pinAmarelo, HIGH);
    digitalWrite(pinVermelho, LOW);
    delay(200); // 200ms ligado
    digitalWrite(pinAmarelo, LOW);
    delay(200); // 200ms desligado
  }

  // Reinicia o ciclo com o verde aceso novamente
}

