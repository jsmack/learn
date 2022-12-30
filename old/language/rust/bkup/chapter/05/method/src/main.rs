fn main() {
    let rect1 = Rectangle{ width: 30, height: 50};

    println!(
        "The area of the rectangle is {} square pixels.",
        rect1.area()
    );

    let rect2 = Rectangle{ width: 10, height: 30};
    println!(
        "Can rect1 hold rect2? {}",
        rect1.can_hold(&rect2)
    );

    // print 1600
    let rect3 =  Rectangle::square(40);
    println!("{}",rect3.width * rect3.height);

    // print 300
    let rect4 = Rectangle::area(&rect2);
    println!("{}", rect4);
}

#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

// when define function in struct, need impl
impl Rectangle {
    // Rectangle: &Rectangle == &self
    fn area(&self) -> u32 {
        self.width * self.height
    }

    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }

}

// duplicate impl OK
impl Rectangle {
    fn square(size: u32) -> Rectangle {
        Rectangle { width: size, height: size}
    }
}
