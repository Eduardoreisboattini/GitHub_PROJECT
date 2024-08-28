// #68 Kotlin\File_00001.cs
// This code is a simple example of a program that analyzes a dataset.

// Importing the necessary libraries
import java.io.*;
import java.util.*;

class File_00001 {
    public static void main(String[] args) {
        
        // Data set path
        String filePath = "C:\\Users\\edu_b\\GitHub_PROJECT\\#00 Programming Languages\\#00308.Kotlin\\data_set.txt";
        
        // Reading data from the file
        ArrayList<Double> dataSet = new ArrayList<Double>();
        try {
            FileReader fileReader = new FileReader(filePath);
            BufferedReader bufferedReader = new BufferedReader(fileReader);
            String line;
            while ((line = bufferedReader.readLine()) != null) {
                double value = Double.parseDouble(line);
                dataSet.add(value);
            }
            bufferedReader.close();
        } catch (FileNotFoundException e) {
            System.out.println("File not found");
            e.printStackTrace();
        } catch (IOException e) {
            System.out.println("Error reading file");
            e.printStackTrace();
        }
        
        // Analyzing the data
        double sum = 0;
        double max = Double.MIN_VALUE;
        double min = Double.MAX_VALUE;
        for (double value : dataSet) {
            sum += value;
            if (value > max) {
                max = value;
            }
            if (value < min) {
                min = value;
            }
        }
        
        // Printing results
        System.out.println("Number of data points: " + dataSet.size());
        System.out.println("Sum of the data points: " + sum);
        System.out.println("Maximum value: " + max);
        System.out.println("Minimum value: " + min);
        
    }
}

