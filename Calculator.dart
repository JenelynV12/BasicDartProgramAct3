import 'dart:io';

void main() {
  while (true) {
    print('Enter first number:');
    double num1 = double.parse(stdin.readLineSync()!);

    print('Enter second number:');
    double num2 = double.parse(stdin.readLineSync()!);

    print('Choose an operation:');
    print('A: Add');
    print('B: Subtract');
    print('C: Multiply');
    print('D: Divide');

    String? choice = stdin.readLineSync();

    if (choice == 'A') {
      print('$num1 + $num2 = ${num1 + num2}');
    } else if (choice == 'B') {
      print('$num1 - $num2 = ${num1 - num2}');
    } else if (choice == 'C') {
      print('$num1 * $num2 = ${num1 * num2}');
    } else if (choice == 'D') {
      if (num2 != 0) {
        print('$num1 / $num2 = ${num1 / num2}');
      } else {
        print('Error: Cannot divide by zero.');
      }
    } else {
      print('Invalid choice.');
    }

    print('\nDo you want to perform another operation? (yes/no)');
    String? again = stdin.readLineSync();
    if (again?.toLowerCase() != 'yes') {
      break;
    }
  }
}              