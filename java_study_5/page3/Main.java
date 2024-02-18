class Main {
  public static void main(String[] args) {
    Car car = new Car();
    // setNameメソッドを用いて、carの名前を「フェラーリ」にしてください
    car.setName("フェラーリ");
    
    // setColorメソッドを用いて、carの色を「赤」にしてください
    car.setColor("赤");
    
    Bicycle bicycle = new Bicycle();
    // setNameメソッドを用いて、bicycleの名前を「ビアンキ」にしてください
    bicycle.setName("ビアンキ");
    
    // setColorメソッドを用いて、bicycleの色を「緑」にしてください
    bicycle.setColor("緑");
    
    System.out.println("【車の情報】");
    car.printData();

    System.out.println("=================");
    System.out.println("【自転車の情報】");
    bicycle.printData();
  }
}
