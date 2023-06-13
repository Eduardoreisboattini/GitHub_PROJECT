delegate void Operation(int a, int b);

void Add(int a, int b)
{
    Console.WriteLine(a + b);
}

void Subtract(int a, int b)
{
    Console.WriteLine(a - b);
}

Operation operation = Add;
operation += Subtract;
operation(5, 3);
