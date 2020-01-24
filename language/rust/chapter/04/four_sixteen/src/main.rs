fn main() {
    let c = Circle { x: 0.0, y: 0.0, radius: 2.0};
    println!("{}", c.area());
    println!("{}", c.grow(4.0).area());
}

struct Circle {
    x: f64,
    y: f64,
    radius: f64,
}

impl Circle {
    fn area(&self) -> f64 {
        std::f64::consts::PI * (self.radius * self.radius)
    }
    fn grow(&self, increment: f64) -> Circle {
        Circle { x: self.x, y: self.y, radius: self.radius + increment }
    }
}

// impl Circle {
//     fn reference(&self) {
//        println!("taking self by reference!");
//     }

//     fn mutable_reference(&mut self) {
//        println!("taking self by mutable reference!");
//     }

//     fn takes_ownership(self) {
//        println!("taking ownership of self!");
//     }
// }