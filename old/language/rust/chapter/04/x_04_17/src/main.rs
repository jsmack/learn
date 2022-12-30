fn main() {
    // let greeting = "Hello there";

    // //multi line
    // let s = "foo
    //          bar";
    
    // assert_eq!("foo\n             bar", s);

    // assert_eq!("foobar", s);

    let mut s1 = "Hello".to_string(); // mut s: String


    println!("{}", s1);
    s1.push_str(",world");
    println!("{}", s1);

    let s = "hello".to_string();
    takes_slice(&s);

    let hachiko = "忠犬ハチ公";

    for b in hachiko.as_bytes() {
        print!("{}, ", b);
    }

    println!("");

    for c in hachiko.chars() {
        print!("{}, ", c);
    }

    println!("");
    let dog = hachiko.chars().nth(1); // hachiko[1]のような感じで

    // slice 
    println!("{}", &s1[0..2]);
}

fn takes_slice(slice: &str) {
    println!("{}", slice);
}
