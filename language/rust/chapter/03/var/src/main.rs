fn main() {
    // error , because Rust defaut variable is immutable 
    // let x = 5;
    let mut x = 5;
    println!("The value of x is {}", x);

    x = 6;
    println!("The value of x is {}", x);

    let spaces = "   ";
    let spaces = spaces.len();
    println!("The space length is {}", spaces);

    let space2 = "    ";
    println!("The space length is {}", space2.len());

    let mut space3 = "     ";

    // error because str type to usize type
    space3  = space3.len();
    println!("The space length is {}", space3);
}
