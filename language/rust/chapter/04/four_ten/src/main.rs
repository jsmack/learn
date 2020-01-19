fn main() {
    println!("Hello, world!");

    let y = &5;
    let f = Foo {x: y};
 //   let x: &'static str = "Hello, world";

    static FOO: i32 = 5;
    let x: &'static i32 = &FOO;

    println!("{}", f.x())
}

fn foo(x: &i32) {
}

// 'a call liftime a
fn bar<'a>(x: &'a i32) {

}

struct Foo<'a> {
    x: &'a i32,
}

impl <'a> Foo<'a> {
    fn x(&self) -> &'a i32 { self.x }
}
