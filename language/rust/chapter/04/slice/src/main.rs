fn main() {
    let mut s = String::from("hello world");

    let word = first_word(&s);
    println!("{}", word);

    println!("{}", &s[0..5]);
    println!("{}", &s[6..11]);

    println!("{}", &s[..2]);


    println!("{}", first_word2(&s));



    s.clear();
}

fn first_word(s: &String) -> usize {
    // exchange String object to byte
    let bytes = s.as_bytes();

    // 
    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return i;
        }
        else {
            println!("{}", i);
        }
    }

    s.len()
}

fn first_word2(s: &String) -> &str {
    let bytes = s.as_bytes();

    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return &s[1..i];
        }
    }
    &s[..]
}