fn main() {
    let x: Message = Message::Move { x: 3, y: 4};
    println!("Hello, world!");
}

enum Message {
    Quit,
    ChangeColor(i32,i32,i32),
    Move { x: i32, y: i32},
    Write(String).
}