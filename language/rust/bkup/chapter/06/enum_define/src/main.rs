fn main() {

}

struct IpAddr {
    kind: IpAddrKind,
    Address: String,
}
enum IpAddrKind {
    V4,
    V6,
}

//let home = IpAddr {
//  kind: IpAddrKind::V4,
//  address: String::from("1.1.1.1"),
//};
//
//let loopback = IpAddr {
//  kind: IpAddKind::V6,
//  address: String::from("::1"),
//};