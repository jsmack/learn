fn main() {
    println!("Hello, world!");

    another_function(5, 33);
    another_function2();
    println!("The five func return value is {}", five());
    let z  = plus_one(100);
    println!("The five func return value is {}", z);
}

fn another_function(x: u32, y: u32) {
    println!("func test");
    println!("The value of x is {}",x);
    println!("The value of y is {}",y);

}

fn another_function2() {
    let _x = 5;

    let y = {
        let x = 3;
        //unnessesary ;(semicommon)
        x + 1
    };

    println!("The value of y is: {}", y);
}

fn five() -> u32 {
    5
}

fn plus_one(z: i32) -> i32 {
    z + 1
}