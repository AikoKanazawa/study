class Car extends Vehicle {
  // インスタンスフィールドfuelを定義してください
  private int fuel = 50;
  
  // fuelフィールドのゲッターを定義してください
  public int getFuel(){
    return this.fuel;
  }
  
  // インスタンスメソッドchargeを定義してください
  public void charge(int litre) {
    System.out.println(litre + "L給油します");
    if (litre <= 0) {
      System.out.println("給油できません");
    } else if (litre + this.fuel >= 100) {
      System.out.println("満タンまで給油します");
      this.fuel = 100;
    } else {
      this.fuel += litre;
    }
    System.out.println("ガソリン量：" + this.fuel + "L");
  }
  
}
