fn main() {
    println!("Hello, world!");

    let x = 2;

    match x {
        1 => println!("one"),
        2 => println!("two"),
        3 => println!("three"),
        _ => println!("anything"),
    }

    let c = 'c';

    // output c,c
    match c {
        x => println!("{},{}", x, c),
    }
    match x {
        1 | 2 => println!("one or two"),
        3 => println!("three"),
        _ => println!("anything"),
    }

    let origin = Point {x: 10, y: 20};
    match origin {
        Point {x , y} => println!("{},{}",x,y),
    }
    match origin {
        Point { x: x1, y: y1 } => println!("({},{})", x1, y1),
    }
    match origin {
        Point { y, .. } => println!("{}", y),
    }

    let tuple: (u32, String) = (5, String::from("hoge"));
    // let (x, _s) = tuple;
    // println!("{}", x);
    let (y, _) = tuple;
    println!("{}", y);
    println!("{:#?}", tuple);

    let x2 = 1;

    match x2 {
        1 ... 5 => println!("one through five"),
        _ => println!("anything"),
    }

    let name = "Steve".to_string();
    let xx: Option<Person> = Some(Person { name: Some(name) });
}


struct Point {
    x: i32,
    y: i32,
}

#[derive(Debug)]
struct Person {
    name: Option<String>,
}
