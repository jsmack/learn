fn main() {
    println!("Hello, world!");
    let mut user1 = User {
        email: String::from("someone@example.com"),
        username: String::from("someusername123"),
        active: true,
        sign_in_count: 1,
    };
    println!("{}", user1.email);
    user1.email = String::from("anotheremail@example.com");

    let mut user2 = User {
        email: String::from("another@example.com"),
        username: String::from("another2username123"),
        ..user1
        //active: user1.active,
        //sign_in_count: user1.sign_in_count,
    };

    struct Color(i32, i32, i32);
    struct Point(i32, i32, i32);

    let black  = Color(0, 0, 0);
    let black  = Color(0, 0, 0);
    let origin = Point(0, 0, 0);

//    let userx = Userx {
//        email: "hoge@hoge",
//        username: "hoge",
//        actibe: true,
//        sign_in_count: 2,
//    };
}


struct User {
    username: String,
    email: String,
    sign_in_count: u64,
    active: bool,
}

// life time error
//struct Userx {
//    username: &str,
//    email: &str,
//    sign_in_count: u64,
//    actibe: bool,
//}

fn build_user(email: String, username: String) -> User {
    User {
        email,
        username,
//        email: email,
//        username: username,
        active: true,
        sign_in_count: 1,
    }
}