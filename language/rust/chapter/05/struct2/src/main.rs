fn main() {
    // This code is normal
    let width1 = 30;
    let heigth1  = 50;
    println!(
        "The area of the rectangle is {} square pixels",
        area(width1, heigth1)
    );

    // This code used tuple
    let rect1 = (30, 50);
    println!(
        "The area of the rectangle is {} square pixels.",
        area_tuple(rect1)
    );

    // This code used struct
    let rect2 = Rectangle { width: 30, height: 50, };
    println!(
        "The area of the rectangle is {} square pixels.",
        area_struct(&rect2)
    );



    // The code extend trait ?
    let rect3 = Rectangle3 { width: 30, height: 50};
    println!("rect3 is {:?}", rect3 );

}

fn area(width: u32, heigth: u32) -> u32 {
    width * heigth
}

fn area_tuple(dimensions: (u32,u32)) -> u32 {
    dimensions.0 * dimensions.1
}
struct Rectangle {
    width: u32,
    height: u32,
}

fn area_struct(rectangle: &Rectangle) -> u32 {
    rectangle.width * rectangle.height
}

#[derive(Debug)]
struct Rectangle3 {
    width: u32,
    height: u32,
}