use proconio::{input};
fn main() {
    input! {
        n: usize,
        pairs: [[i32; 2]; n],
    }
    // println!("{:?}", pairs);
    for i in 0..n {
        println!("{}", pairs[i][0] + pairs[i][1]);
    }
}
