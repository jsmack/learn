fn main() {
    let x = 5;

    if x == 5 {
        println!("x は 5 です!");
    } else if x == 6 {
        println!("x は 6 です!");
    } else {
        println!("x は 5 でも 6 でもありません :(");
    }

    let y = if x == 5 {
        10
    } else {
        15
    }; // y: i32

    println!("{}", y);

    let z = if x == 5 { 10 } else { 15 };

}
