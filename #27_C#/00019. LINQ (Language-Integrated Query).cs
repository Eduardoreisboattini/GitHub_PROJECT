int[] numbers = { 1, 2, 3, 4, 5 };

var evenNumbers = from num in numbers
                  where num % 2 == 0
                  select num;

foreach (int num in evenNumbers)
{
    Console.WriteLine(num);
}
