use std::io;
use rand::Rng;
use std::cmp::Ordering;

fn main() {
    println!("Guess the number");

    let secret_number = rand::thread_rng().gen_range(1, 101);

    println!("The secret number is : {}", secret_number);

    loop {
        // mut == mutable, If do not define the "mut", it is a immutable
        // String::new return string type object

        println!("Please input your guess.");
        let mut guess = String::new();
        io::stdin().read_line(&mut guess)
            .expect("Failed to read line");

        // check digit  success -> return num, failed -> loop
        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };

        println!("You guess: {}", guess);

        match guess.cmp(&secret_number) {
            Ordering::Less => println!("Too small"),
            Ordering::Greater => println!("T\
            oo big"),
            Ordering::Equal => {
                println!("You win");
                break;
            }
        }
    }
}