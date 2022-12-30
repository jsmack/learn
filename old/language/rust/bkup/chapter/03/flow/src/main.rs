fn main() {
    let number = 3;
    if number < 2 {
        println!("true");
    }
    else {
        println!("false");
    }
    let _number2 = 0;
    /*
       = note: expected type `bool`
              found type `{integer}`
    */
    //if number2 {
    //    println!("zero");
    //}
    
    let condition :bool = true;
    let number3 = if condition {
        5
    }else {
        6
    };

    println!("{}", number3);

    //loop {
    //    println!("loop");
    //}

    let mut number4 = 3;
    while number4 != 0 {
        println!("{}", number4);
        number4 = number4 - 1;
    }

    let ary = [10, 20, 30, 40, 50];
    let mut index = 0;

    while index < 5 {
        println!("{}", ary[index]);
        index = index + 1;
    }

    for element in ary.iter() {
        println!("{}",element);
    }

    for number5 in 1..4 {
        println!("{}", number5);
    }
    for number6 in (1..4).rev() {
        println!("{}", number6);
    }


}
