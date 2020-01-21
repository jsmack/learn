fn main() {
    println!("Hello, world!");

    let x = 10;

    match x {
        1 => println!("{}", x),
        2 => println!("{}", x),
        3 => println!("{}", x),
        4 => println!("{}", x),
        5 => println!("{}", x),
        _ => println!("something else"),
    }
}


enum Message {
    Quit,
    ChangeColor(i32,i32,i32),
    Move { x: i32, y: i32},
    Write(String).
}

fn quit() { /* ... */ }
fn change_color(r: i32, g: i32, b: i32) { /* ... */ }
fn move_cursor(x: i32, y: i32) { /* ... */ }

fn process_message(msg: Message) {
    match msg {
        Message::Quit -> quit()
        Message::ChangeColor(r, g, b) => change_color(r, g, b),
        Message::Move { x: x, y: y } => move_cursor(x, y),
        Message::Write(s) => println!("{}", s),
    };
}