use proconio::{input};
fn main() {
    input! {
        num: usize,
    }
    if num%4 == 2 {
        println!("{}", num)
    } if num%4 == 1 {
        println!("{}", num+1)
    } if num%4 == 3 {
        println!("{}", num+3)
    } if num%4 == 0 {
        println!("{}", num+2)
    }
}
