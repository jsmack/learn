fn main() {
    let mut x: i32 = 5;
    let mut done: bool = false;

    while !done {
        x += x - 3;
        println!("{}", x);

        if x % 5 == 0 { done = true };
    }

    for x in 0..10 {
        println!("{}", x);
    }

    for (i,j) in (5..10).enumerate() {
        println!("i = {}, j = {}", i, j);
    }

    let lines = "hello\nworld".lines();

    for (linenumber, line) in lines.enumerate() {
        println!("{}: {}", linenumber, line);
    }
    x = 5;
    loop {
        x += x - 3;
        println!("{}", x);
        if x % 5 == 0 { break };
    }

    for x in 0..10 {
        if x % 2 == 0 { continue;}
        else { println!("{}", x);}
    }

    'outer: for x in 0..10 {
        'inner: for y in 0..10 {
            if x % 2 == 0 { continue 'outer; } // x のループを継続
            if y % 2 == 0 { continue 'inner; } // y のループを継続
            println!("x: {}, y: {}", x, y);
        }
    }

}
