import java.util.Scanner;

class Main {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    Car car = new Car();
    car.setName("フェラーリ");
    car.setColor("赤");
    Bicycle bicycle = new Bicycle();
    bicycle.setName("ビアンキ");
    bicycle.setColor("緑");

    System.out.println("【車の情報】");
    car.printData();
    // getFuelメソッドを用いて「ガソリン量：◯◯L」と出力してください
    System.out.println("ガソリン量：" + car.getFuel() + "L");
    
    
    System.out.println("-----------------");
    System.out.print("給油する量を入力してください：");
    int litre = scanner.nextInt();
    // chargeメソッドを呼び出して、引数にlitreを渡してください
    car.charge(litre);

    System.out.println("=================");
    System.out.println("【自転車の情報】");
    bicycle.printData();
  }
}
