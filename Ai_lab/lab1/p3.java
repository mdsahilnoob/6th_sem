// write a program to implement gates without truth table

import java.util.Scanner;

public class p3 {
    public static boolean andGate(boolean a, boolean b) {
        return a && b;
    }
    public static boolean orGate(boolean a, boolean b) {
        return a || b;
    }
    public static boolean notGate(boolean a) {
        return !a;
    }
    public static boolean nandGate(boolean a, boolean b) {
        return !(a && b);
    }
    public static boolean norGate(boolean a, boolean b) {
        return !(a || b);
    }
    public static boolean xorGate(boolean a, boolean b) {
        return a ^ b;
    }
    public static boolean xnorGate(boolean a, boolean b) {
        return !(a ^ b);
    }
    public static boolean toBool(int value) {
        return value != 0;
    }
    public static int toInt(boolean value) {
        return value ? 1 : 0;
    }
    public static void displayResult(String gateName, boolean a, boolean b, boolean result) {
        System.out.printf("%s(%d, %d) = %d%n", gateName, toInt(a), toInt(b), toInt(result));
    }

    public static void displayResult(String gateName, boolean a, boolean result) {
        System.out.printf("%s(%d) = %d%n", gateName, toInt(a), toInt(result));
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("\n===== Logic Gates Implementation =====");
            System.out.println("1. AND Gate");
            System.out.println("2. OR Gate");
            System.out.println("3. NOT Gate");
            System.out.println("4. NAND Gate");
            System.out.println("5. NOR Gate");
            System.out.println("6. XOR Gate");
            System.out.println("7. XNOR Gate");
            System.out.println("8. Test All Gates");
            System.out.println("0. Exit");
            System.out.print("\nEnter your choice: ");

            int choice = scanner.nextInt();

            if (choice == 0) {
                System.out.println("Exiting...");
                break;
            }

            if (choice == 8) {
                System.out.print("Enter first input (0 or 1): ");
                int input1 = scanner.nextInt();
                System.out.print("Enter second input (0 or 1): ");
                int input2 = scanner.nextInt();

                boolean a = toBool(input1);
                boolean b = toBool(input2);

                System.out.println("\n----- Results -----");
                displayResult("AND  ", a, b, andGate(a, b));
                displayResult("OR   ", a, b, orGate(a, b));
                displayResult("NOT A", a, notGate(a));
                displayResult("NOT B", b, notGate(b));
                displayResult("NAND ", a, b, nandGate(a, b));
                displayResult("NOR  ", a, b, norGate(a, b));
                displayResult("XOR  ", a, b, xorGate(a, b));
                displayResult("XNOR ", a, b, xnorGate(a, b));

            } else if (choice == 3) {
                System.out.print("Enter input (0 or 1): ");
                int input = scanner.nextInt();
                boolean a = toBool(input);
                boolean result = notGate(a);
                System.out.println("\nResult: NOT(" + input + ") = " + toInt(result));

            } else if (choice >= 1 && choice <= 7) {
                System.out.print("Enter first input (0 or 1): ");
                int input1 = scanner.nextInt();
                System.out.print("Enter second input (0 or 1): ");
                int input2 = scanner.nextInt();

                boolean a = toBool(input1);
                boolean b = toBool(input2);
                boolean result = false;
                String gateName = "";

                switch (choice) {
                    case 1:
                        result = andGate(a, b);
                        gateName = "AND";
                        break;
                    case 2:
                        result = orGate(a, b);
                        gateName = "OR";
                        break;
                    case 4:
                        result = nandGate(a, b);
                        gateName = "NAND";
                        break;
                    case 5:
                        result = norGate(a, b);
                        gateName = "NOR";
                        break;
                    case 6:
                        result = xorGate(a, b);
                        gateName = "XOR";
                        break;
                    case 7:
                        result = xnorGate(a, b);
                        gateName = "XNOR";
                        break;
                }

                System.out.println("\nResult: " + gateName + "(" + input1 + ", " + input2 + ") = " + toInt(result));

            } else {
                System.out.println("Invalid choice! Please try again.");
            }
        }

        scanner.close();
    }
}
