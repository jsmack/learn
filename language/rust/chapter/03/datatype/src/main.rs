fn main() {
    let guess: usize = "42".parse().expect("Not a number!");
    // thread 'main' panicked at 'Not a number!: ParseIntError
    // let guess: usize = "hoge".parse().expect("Not a number!");

    let x = 2.3;
    println!("{}", x);
    let y: f32 = 4.0;
    println!("{}", y);  

    // 足し算
    let sum = 5 + 10;   

    // 引き算
    let difference = 95.5 - 4.3;
    
    // 掛け算
    let product = 4 * 30;
    
    // 割り算
    let quotient = 56.7 / 32.2;
    
    // 余り
    let remainder = 43 % 5;

    let t = true;
    let f: bool = false;
    println!("The  value of {}", t);
    println!("The  value of {}", f);

    let c = 'z';
    let z = 'ℤ';
    let heart_eyed_cat = '😻';    //ハート目の猫
    println!("{}", heart_eyed_cat);

    //tuple
    let tup: (i32, f64, u8) = (500,6.4, 1);
    let (x, y, z) = tup;

    println!("The value of y is: {}", y);
    println!("{}", tup.2);

    
    let x: (i32, f64, u8) = (500, 6.4, 1);
    let five_hundred = x.0;
    let six_point_four = x.1;
    let one = x.2;
    println!("{}", five_hundred)

    // array
    let a = [1, 2, 3, 4, 5];

    let first = a[0];
    let second = a[1];
    
    let index = 10;
    let element = a[index];
}
