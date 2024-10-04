+import java.util.Scanner
+
+fun main() {
+    val scanner = Scanner(System.`in`)
+    val data = mutableListOf<Int>()
+
+    println("Enter some integers (type 'done' to finish):")
+    while (true) {
+        val input = scanner.nextLine()
+        if (input == "done") {
+            break
+        }
+        data.add(input.toInt())
+    }
+
+    println("Enter the target integer:")
+    val target = scanner.nextInt()
+
+    val result = findOccurrences(data, target)
+    println("The number of occurrences of $target in the entered integers is: $result")
+}
+
+fun findOccurrences(data: List<Int>, target: Int): Int {
+    return data.count { it == target }
+}

