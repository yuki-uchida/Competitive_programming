use proconio::{input};
fn main() {
    input! {
        n: usize, 
        x: usize,
    }
    let index = (x - 1) / n;
    // println!("{}", index);
    println!("{}", (b'A' + (index as u8)) as char);
}
