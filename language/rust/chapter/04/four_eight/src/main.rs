fn main() {
    let v = vec![1, 2, 3];
//    take(v);
//    println!("{}", v[0]);
    let mut v2 = v;
    println!("{}", v2[1]);
    v2.truncate(2);
    println!("{}", v2[1]);

    let v3 = vec![1,2,3];
    let v4 = vec![1,2,3];
    println!("{}", bar(v3,v4).2);

}

fn take(v: Vec<i32>) {

}
fn foo() {
    let v = vec![1, 2, 3];
}

fn bar(v1: Vec<i32>, v2: Vec<i32>) -> (Vec<i32>, Vec<i32>, i32) {
    (v1, v2, 999)
}