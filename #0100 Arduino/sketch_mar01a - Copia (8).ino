// Incluindo a biblioteca do módulo relé
#include <Arduino.h>

// Definindo os pinos do Arduino conectados ao módulo relé
const int relay1Pin = 2; // Pino para controlar o primeiro canal do relé
const int relay2Pin = 3; // Pino para controlar o segundo canal do relé

void setup() {
  // Inicializa os pinos como saídas
  pinMode(relay1Pin, OUTPUT);
  pinMode(relay2Pin, OUTPUT);

  // Desliga as lâmpadas no início (por segurança)
  digitalWrite(relay1Pin, LOW);
  digitalWrite(relay2Pin, LOW);
}

void loop() {
  // Acende a primeira lâmpada
  digitalWrite(relay1Pin, HIGH);
  delay(1000); // Aguarda 1 segundo

  // Apaga a primeira lâmpada
  digitalWrite(relay1Pin, LOW);
  delay(1000); // Aguarda 1 segundo

  // Acende a segunda lâmpada
  digitalWrite(relay2Pin, HIGH);
  delay(1000); // Aguarda 1 segundo

  // Apaga a segunda lâmpada
  digitalWrite(relay2Pin, LOW);
  delay(1000); // Aguarda 1 segundo
}

#include <Arduino.h> 
//Esta linha inclui a biblioteca do Arduino, necessária para usar suas funções.

const int relay1Pin = 2; 
const int relay2Pin = 3; 
//Estas linhas definem os pinos do Arduino aos quais estão conectados os canais do relé.

void setup() {
  pinMode(relay1Pin, OUTPUT); 
  pinMode(relay2Pin, OUTPUT); 
  //Estas linhas definem os pinos do Arduino como saídas.

  digitalWrite(relay1Pin, LOW); 
  digitalWrite(relay2Pin, LOW); 
  //Estas linhas desligam as lâmpadas no início para garantir que elas não estejam acesas acidentalmente.
}

void loop() {
  digitalWrite(relay1Pin, HIGH); 
  delay(1000); 
  digitalWrite(relay1Pin, LOW); 
  delay(1000); 
  //Estas linhas acendem e apagam a primeira lâmpada com intervalos de 1 segundo.

  digitalWrite(relay2Pin, HIGH); 
  delay(1000); 
  digitalWrite(relay2Pin, LOW); 
  delay(1000); 
  //Estas linhas acendem e apagam a segunda lâmpada com intervalos de 1 segundo.
}
