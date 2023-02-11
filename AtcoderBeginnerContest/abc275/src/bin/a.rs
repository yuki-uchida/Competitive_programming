use proconio::{input};
fn main() {
    input! {
        n: usize,
        mut heights: [usize; n],
    }
    let mut ans_index = 0;
    let mut ans_height = heights[0];
    for i in 1..n {
        if ans_height < heights[i] {
            ans_index = i;
            ans_height = heights[i];
        }
    }
    println!("{}", ans_index + 1);
}
