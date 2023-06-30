 program Calculator;
var
  num1, num2, result: real;
  operator: char;
begin
  writeln('Enter the first number: ');
  readln(num1);
  writeln('Enter an operator (+, -, *, /): ');
  readln(operator);
  writeln('Enter the second number: ');
  readln(num2);

  case operator of
    '+': result := num1 + num2;
    '-': result := num1 - num2;
    '*': result := num1 * num2;
    '/': result := num1 / num2;
  end;

  writeln('Result: ', result:0:2);
end.