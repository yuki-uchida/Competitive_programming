use proconio::{input, marker::Chars};
fn main() {
    input! {
        n: usize,
        s: Chars,
    }
    // 1から7
    for i in 1..n{
        let mut l = 0;
        while i+l < n{
            if s[l] == s[i+l]{
                break;
            }
            l += 1;
        }
        println!("{}", l);
    }
}
