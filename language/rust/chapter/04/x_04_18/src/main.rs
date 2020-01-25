fn main() {
    println!("Hello, world!");

    let x: Option<i32> = Some(5);
}

enum Opton<T> {
    Some(T),
    None,
}
