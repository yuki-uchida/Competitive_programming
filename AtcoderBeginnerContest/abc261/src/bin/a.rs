use proconio::{input};
fn main() {
    input! {
        left1: usize,
        right1: usize,
        left2: usize,
        right2: usize,
    }
    let range1 = left1..=right1;
    let range2 = left2..=right2;
    let start = std::cmp::max(range1.start(), range2.start());
    let end = std::cmp::min(range1.end(), range2.end());
    if start <= end {
        println!("{}", end-start);
    } else {
        println!("0");
    }
}
