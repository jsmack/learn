```
$ cargo new chap_03 --bin
     Created binary (application) `chap_03` package
$ find ./chap_03 -type f
./chap_03/Cargo.toml
./chap_03/src/main.rs
$
$ cat ./chap_03/Cargo.toml 
[package]
name = "chap_03"
version = "0.1.0"
authors = ["hogehoge <hogehoge@gmail.com>"]
edition = "2018"

# See more keys and their definitions at https://doc.rust-lang.org/cargo/reference/manifest.html

[dependencies]
$ cat ./chap_03/src/main.rs 
fn main() {
    println!("Hello, world!");
}
```
### compile
```
$ cd chap_03/
$ cargo build
   Compiling chap_03 v0.1.0 (/Users/hogehoge/work/git/learn/language/rust/chapter/01/03/chap_03)
    Finished dev [unoptimized + debuginfo] target(s) in 4.23s
$ find ./ -type f
.//Cargo.toml
.//target/.rustc_info.json
.//target/debug/.fingerprint/chap_03-11d35e4685ca1499/bin-chap_03-11d35e4685ca1499
.//target/debug/.fingerprint/chap_03-11d35e4685ca1499/dep-bin-chap_03-11d35e4685ca1499
.//target/debug/.fingerprint/chap_03-11d35e4685ca1499/invoked.timestamp
.//target/debug/.fingerprint/chap_03-11d35e4685ca1499/bin-chap_03-11d35e4685ca1499.json
.//target/debug/chap_03
.//target/debug/incremental/chap_03-17sldkoqk3wgr/s-fja6ub644d-1m6b1ix-10m89kesli594/2g287mg7rxkcjt9x.o
.//target/debug/incremental/chap_03-17sldkoqk3wgr/s-fja6ub644d-1m6b1ix-10m89kesli594/34qp5xqckknesj3r.o
.//target/debug/incremental/chap_03-17sldkoqk3wgr/s-fja6ub644d-1m6b1ix-10m89kesli594/14oh0h5qtjanhdi8.o
.//target/debug/incremental/chap_03-17sldkoqk3wgr/s-fja6ub644d-1m6b1ix-10m89kesli594/query-cache.bin
.//target/debug/incremental/chap_03-17sldkoqk3wgr/s-fja6ub644d-1m6b1ix-10m89kesli594/dep-graph.bin
.//target/debug/incremental/chap_03-17sldkoqk3wgr/s-fja6ub644d-1m6b1ix-10m89kesli594/3e46sxk4ja73coe4.o
.//target/debug/incremental/chap_03-17sldkoqk3wgr/s-fja6ub644d-1m6b1ix-10m89kesli594/3eg6zr7chtx2p431.o
.//target/debug/incremental/chap_03-17sldkoqk3wgr/s-fja6ub644d-1m6b1ix-10m89kesli594/1q10sa5ooe5isqpa.o
.//target/debug/incremental/chap_03-17sldkoqk3wgr/s-fja6ub644d-1m6b1ix-10m89kesli594/work-products.bin
.//target/debug/incremental/chap_03-17sldkoqk3wgr/s-fja6ub644d-1m6b1ix.lock
.//target/debug/.cargo-lock
.//target/debug/chap_03.d
.//target/debug/deps/chap_03-11d35e4685ca1499.dSYM/Contents/Resources/DWARF/chap_03-11d35e4685ca1499
.//target/debug/deps/chap_03-11d35e4685ca1499.dSYM/Contents/Info.plist
.//target/debug/deps/chap_03-11d35e4685ca1499.d
.//target/debug/deps/chap_03-11d35e4685ca1499
.//Cargo.lock
.//src/main.rs
```
### execute
```
$ ./target/debug/chap_03 
Hello, world!
```

### compile and execute
```
$ cargo run
    Finished dev [unoptimized + debuginfo] target(s) in 0.01s
     Running `target/debug/chap_03`
Hello, world!
$
```

### check
```
$ cargo check
    Checking chap_03 v0.1.0 (/Users/hogehoge/work/git/learn/language/rust/chapter/01/03/chap_03)
    Finished dev [unoptimized + debuginfo] target(s) in 0.14s
```