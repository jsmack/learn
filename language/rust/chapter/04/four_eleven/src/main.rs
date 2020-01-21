fn main() {
    let x1 = 6;
    //x1 = 5; // error imutable

    let mut x2 =6;
    x2 = 5; // OK

    let mut x3 = 5;
    let y3 = &mut x3;

    let x4 =  Arc::new(5);
    let y4 = x4.clone();

    let point = Point { x: 5, y: Cell::new(6)};
    point.y.set(7);

    println!("{:?}", point.y);
}


use std::sync::Arc;

use std::cell::Cell;

struct Point {
    x: i32,
    y: Cell<i32>,
}