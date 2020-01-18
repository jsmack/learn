//fn main() {
//    let v1 = vec![1,2,3];
//    let v2 = vec![1,2,3];
//
//    println!("{}", foo(v1,v2).2)
//}
//
//
//fn foo(v1: Vec<i32>, v2: Vec<i32>) -> (Vec<i32>,Vec<i32>,i32) {
//    (v1,v2,44)
//}

fn foo(v1: &Vec<i32>,v2: &Vec<i32>)  -> i32 {
    42
}

//fn foo2(v: &Vec<i32>) {
//    v.push(5);
//}

fn main() {
    let v1 = vec![1,2,3];
    let v2 = vec![1,2,3];
 //   let v3 = vec![];

    println!("{}", foo(&v1,&v2));
 //   foo2(&v3);
 //   println!("{}", v3[0]);
    let mut x = 5;
    {
        let y = &mut x;
        *y  += 1;
    }
    println!("The x value is {}", x); //The x value is 6

    let mut v = vec![1,2,3];

    for i in &v {
        println!("{}", i);
    }

    for i in &v {
        println!("{}", i);
       // v.push(34); //mutable borrow occurs here
    }
}