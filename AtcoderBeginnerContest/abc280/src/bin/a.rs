use proconio::{input, marker::Chars};
fn main() {
    input! {
        h: usize,
        w: usize,
        maths: [Chars; h], 
    }
    let mut ans = 0;
    for i in 0..h {
        ans += maths[i].iter().filter(|&c| *c == '#').count();
    }
    println!("{}", ans);
}
