import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

LocalDate currentDate = LocalDate.now();
System.out.println("Current date: " + currentDate);

LocalDateTime currentDateTime = LocalDateTime.now();
DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
String formattedDateTime = currentDateTime.format(formatter);
System.out.println("Formatted date and time: " + formattedDateTime);