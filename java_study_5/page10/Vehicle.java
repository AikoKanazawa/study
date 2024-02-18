abstract class Vehicle {
  private String name;
  private String color;
  protected int distance = 0;
  // インスタンスフィールドownerを定義してください
  private Person owner;

  Vehicle(String name, String color) {
    this.name = name;
    this.color = color;
  }

  public String getName() {
    return this.name;
  }
  public String getColor() {
    return this.color;
  }
  public int getDistance() {
    return this.distance;
  }
  
  // ownerフィールドのゲッターを定義してください
  public Person getOwner(){
    return this.owner;
  }
  
  public void setName(String name) {
    this.name = name;
  }
  public void setColor(String color) {
    this.color = color;
  }
  
  // ownerフィールドのセッターを定義してください
  public void setOwner(Person person){
    this.owner = person;
  }

  public void printData() {
    System.out.println("名前：" + this.name);
    System.out.println("色：" + this.color);
    System.out.println("走行距離：" + this.distance + "km");
  }

  public abstract void run(int distance);
}
