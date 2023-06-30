 program Factorial;
var
  num, factorial: integer;
  i: integer;
begin
  writeln('Enter a number: ');
  readln(num);

  factorial := 1;
  for i := 1 to num do
    factorial := factorial * i;

  writeln('Factorial of ', num, ' is ', factorial);
end.