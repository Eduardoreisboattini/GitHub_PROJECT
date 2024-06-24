#include <LiquidCrystal.h>

int seconds = 0;

LiquidCrystal lcd_1(12, 11, 5, 4, 3, 2);

void setup()
{
  lcd_1.begin(16, 2); // Set up the number of columns and rows on the LCD.

  // Print a static message to the LCD.
  lcd_1.print("Voce eh o melhor,");
  lcd_1.setCursor(0, 1); // Move cursor to the beginning of the second line
  lcd_1.print("voce eh JUMPER!");
}

void loop()
{
  // In this example, we're not changing the displayed content in the loop.
  // You could add functionality here if needed, but for a static message,
  // it's not necessary.
}
