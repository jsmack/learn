fn main() {
    //vector
    let v1 = vec![1,2,3,4,5];
    let v2 = vec![0; 10];  // 0 10個

    println!("{}", v1[2]);  // 3

    let i: usize = 1;
    let j: i32 = 2;

    v1[i];
    //v1[j];   // error j is not usize
    
    let mut v3 = vec![1,2,3,4,5];

    for i in &v3 {
        println!("A reference to {}", i);
    }

    for i in &mut v3 {
        println!("A mutable reference to {}", i);
    }
    
    for i in v3 {
        println!("Take ownership of the vector and its element {}", i);
    }
}
