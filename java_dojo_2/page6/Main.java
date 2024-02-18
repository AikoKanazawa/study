import java.util.Scanner;

class Main {
  public static void main(String[] args) {
    Bicycle bicycle = new Bicycle("ビアンキ", "緑");
    Scanner scanner = new Scanner(System.in);
    System.out.println("【自転車の情報】");
    bicycle.printData();
    System.out.println("-----------------");
    System.out.print("走る距離を入力してください：");
    int bicycleDistance = scanner.nextInt();
    bicycle.run(bicycleDistance);
    
  }
}