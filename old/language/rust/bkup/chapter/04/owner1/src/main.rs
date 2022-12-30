// fn main() {
//     let s = "hello";
//     let mut sx = String::from("hello");

//     sx.push_str(", world");

//     println!("{}", sx);

//     // ! error s1 is move to s2, drop s1
//     // let s1 = String::from("hello");
//     // let s2 = s1;
//     // println!("s1 is {}", s1);

//     let s3 = String::from("hello");
//     let s4 = s3.clone();


//     println!("s1 is {}", s3);

// }
// fn main() {
//     let s1 = gives_ownership();         // gives_ownershipは、戻り値をs1に
//                                         // ムーブする

//     let s2 = String::from("hello");     // s2がスコープに入る

//     let s3 = takes_and_gives_back(s2);  // s2はtakes_and_gives_backにムーブされ
//                                         // 戻り値もs3にムーブされる
// } // ここで、s3はスコープを抜け、ドロップされる。s2もスコープを抜けるが、ムーブされているので、
//   // 何も起きない。s1もスコープを抜け、ドロップされる。

// fn gives_ownership() -> String {             // gives_ownershipは、戻り値を
//                                              // 呼び出した関数にムーブする

//     let some_string = String::from("hello"); // some_stringがスコープに入る

//     some_string                              // some_stringが返され、呼び出し元関数に
//                                              // ムーブされる
// }

// // takes_and_gives_backは、Stringを一つ受け取り、返す。
// fn takes_and_gives_back(a_string: String) -> String { // a_stringがスコープに入る。

//     a_string  // a_stringが返され、呼び出し元関数にムーブされる
// }

fn main() {
    let s1 = String::from("hello");
    let (s2, len) = calculate_length(s1);
    println!("The length of '{}' is {}.", s2, len);

}
fn calculate_length(s: String) -> (String, usize) {
    let length: usize = s.len(); // len()メソッドは、Stringの長さを返します

    (s, length)
}