/*
  Calibração

  Demonstração de uma técnica para calibrar entrada de sensor. As leituras
  do sensor nos primeiros cinco segundos da execução do sketch definem o mínimo
  e máximo dos valores esperados no pino do sensor.

  Os valores mínimos e máximos iniciais do sensor podem parecer invertidos.
  Inicialmente, você define o mínimo como alto e espera por algo menor,
  salvando isso como novo mínimo. Da mesma forma, você define o máximo como
  baixo e espera por algo maior para salvar como novo máximo.

  Circuito:
  * Sensor analógico (um potenciômetro pode ser usado) conectado ao pino analógico 0
  * LED conectado do pino digital 9 para o terra

*/

// Constantes que não serão alteradas:
const int sensorPin = A0;    // pino ao qual o sensor está conectado
const int ledPin = 9;        // pino ao qual o LED está conectado

// Variáveis:
int sensorValue = 0;         // valor do sensor
int sensorMin = 1023;        // valor mínimo do sensor
int sensorMax = 0;           // valor máximo do sensor

void setup() {
  // Liga o LED para sinalizar o início do período de calibração:
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, HIGH);

  // Calibração durante os primeiros cinco segundos
  while (millis() < 5000) {
    sensorValue = analogRead(sensorPin);

    // Registra o valor máximo do sensor
    if (sensorValue > sensorMax) {
      sensorMax = sensorValue;
    }

    // Registra o valor mínimo do sensor
    if (sensorValue < sensorMin) {
      sensorMin = sensorValue;
    }
    
    // Aguarda um pouco
    delay(50);
  }

  // Sinaliza o fim do período de calibração
  digitalWrite(LED_BUILTIN, LOW);
}

void loop() {
  // Lê o sensor:
  sensorValue = analogRead(sensorPin);

  // Aplica a calibração para a leitura do sensor
  sensorValue = map(sensorValue, sensorMin, sensorMax, 0, 255);

  // Caso o valor do sensor esteja fora da faixa observada durante a calibração
  sensorValue = constrain(sensorValue, 0, 255);

  // Ajusta a intensidade do LED usando o valor calibrado:
  analogWrite(ledPin, sensorValue);
  
  // Aguarda um pouco
  delay(50);
}
