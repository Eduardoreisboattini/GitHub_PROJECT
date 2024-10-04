(23-50)
<!DOCTYPE html>
<html>
<head>
    <title>TypeScript</title>
</head>
<body>
    <h1>TypeScript</h1>
    <p>TypeScript is a statically typed superset of JavaScript that adds optional static typing and other features to plain JavaScript.</p>
    <p>Here are some of the key characteristics and uses of TypeScript:</p>
    <ul>
        <li>TypeScript code is compiled into JavaScript code that can run in any browser or environment.</li>
        <li>TypeScript supports optional static typing, which means you can add type annotations to variable declarations to make your code more robust and easier to understand.</li>
        <li>TypeScript also supports classes, interfaces, and modules, which are features that are not part of JavaScript but are commonly used in object-oriented programming.</li>
        <li>TypeScript includes a rich set of tools for building web applications, including a task runner, a module loader, and a development server.</li>
        <li>TypeScript is a popular choice for building large-scale applications, including web applications, mobile applications, and desktop applications.</li>
        <li>TypeScript code can be compiled into JavaScript code that runs in any browser or environment, making it a versatile choice for web development.</li>
    </ul>
    <h2>Example</h2>
    <p>Here is an example of a TypeScript code that defines a class with a constructor and a method:</p>
    <pre><code>
class Greeter {
    greeting: string;
    constructor(message: string) {
        this.greeting = message;
    }
    greet() {
        return "Hello, " + this.greeting;
    }
}

let greeter = new Greeter("world");
console.log(greeter.greet());
    </code></pre>
    <p>This code defines a class called Greeter with a constructor that takes a message parameter and a greet method that returns a greeting message. The code creates an instance of the Greeter class and logs a greeting message to the console.</p>
    <p>Note that the code above is written in TypeScript, but it can be compiled into JavaScript code that can run in any browser or environment.</p>
</body>
</html>
(51-52)
