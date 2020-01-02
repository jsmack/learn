use std::io;
use rand::Rng;
use std::cmp::Ordering;

fn main() {
    println!("Guess the number");



    let secret_number = rand::thread_rng().gen_range(1,101);

    println!("The secret number is : {}", secret_number);

    println!("Please input your guess.");
    // mut == mutable, If do not define the "mut", it is a immutable
    // String::new return string type object
    let mut guess = String::new();

    // io type stdin
    io::stdin().read_line(&mut guess)
        .expect("Failed to read line");

    // exchange str to numeric
    // trim = remove white space
    // parse = str to numeric and remove line feed(\n)
    let guess: u32 = guess.trim().parse()
        .expect("Plese input number");

    println!("You guess: {}", guess);

    match guess.cmp(&secret_number) {
        Ordering::Less => println!("Too small"),
        Ordering::Greater => println!("Too big"),
        Ordering::Equal => println!("just do it"),

    }
}
// cargo doc --open
// cargo build --release