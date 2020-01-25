fn main() {
    let org_x = 1;
    let org_y = 0;
    let mut org = Point{ x:1, y:2};
    org.x = 100;
    println!("{}", org.x);

    let mut point2 = Point3d { x:0, y:1,z:3};
    point2 = Point3d { z:10, .. point2 };
    println!("{},{},{}", point2.x, point2.y, point2.z);
}

struct Point {
    x: i32,
    y: i32,
}


struct Point3d {
    x: i32,
    y: i32,
    z: i32,
}
struct Color(i32, i32, i32);