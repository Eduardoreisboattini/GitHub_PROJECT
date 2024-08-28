println "Hello World!"

def name = "Alice"
println "Hello $name!"

def numbers = [1, 2, 3, 4, 5]
println numbers.size()

def numbers2 = [1, 2, 3, 4, 5] as Set
println numbers2

def map = [name: "Alice", age: 30]
println map.name

def people = [
    [name: "Alice", age: 30],
    [name: "Bob", age: 35],
    [name: "Charlie", age: 40]
]

people.each { person ->
    println "${person.name} is ${person.age} years old"
}

def fibonacci = { n ->
    if (n < 2) {
        n
    } else {
        fibonacci(n - 1) + fibonacci(n - 2)
    }
}

println fibonacci(10)

def multiply = { a, b ->
    a * b
}

println multiply(5, 10)

def add = { a, b = 0 ->
    a + b
}

println add(3)

def add2 = add.curry(3)
println add2(5)

def add3 = add.rcurry(5)
println add3(3)

def add4 = add.ncurry(1, 3)
println add4(5)

def add5 = add.rcurry(5).ncurry(1)
println add5(3)

def add6 = add.curry(3).rcurry(5).ncurry(1)
println add6(4)

def add7 = add.rcurry(5).ncurry(1).curry(3)
println add7(4)

def add8 = add.rcurry(5).curry(3).ncurry(1)
println add8(4)

def add9 = add.ncurry(1, 3).curry(5).rcurry(3)
println add9(4)

def add10 = add.ncurry(1, 3).rcurry(3).curry(5)
println add10(4)


def sayHello = { name ->
    println "Hello $name!"
}

sayHello.curry("Alice")()

def sayHello2 = { name ->
    { println "Hello $name!" }
}

sayHello2("Alice")()

def sayHello3 = { name ->
    def greet = { println "Hello $name!" }
    greet()
}

sayHello3("Alice")

def sayHello4 = { name ->
    def greet = { println "Hello $name!" }
    return greet
}

sayHello4("Alice")()


def isOdd = { n -> n % 2 != 0 }
def isEven = { n -> n % 2 == 0 }

def filterOddEven = { numbers ->
<<<<<<<  8cd0a73d-a29c-40b0-966a-85ddd077014f  >>>>>>>
    def odd = numbers.grep(isOdd)
    def even = numbers.grep(isEven)
    [odd, even]
}

def result = filterOddEven([1, 2, 3, 4, 5, 6, 7, 8, 9])
println result[0]
println result[1]

