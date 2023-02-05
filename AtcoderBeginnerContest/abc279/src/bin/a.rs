use proconio::{input, marker::Chars};
fn main() {
    input! {
        s: Chars,
    }
    let mut ans = 0;
    ans += s.iter().filter(|&c| *c == 'v').count();
    ans += s.iter().filter(|&c| *c == 'w').count() * 2;
    println!("{}", ans);
}
