use proconio::{input, marker::Chars};

fn main() {
    input!{ mut s: Chars};
    s.reverse();
    let mut cnt = 0;
    let mut index = 0;
    while index < s.len() {
        if s[index] == '0' && s[index + 1] == '0' {
            cnt += 1;
            index += 2;
            continue;
        }
        cnt += 1;
        index += 1;
    }
    println!("{}", cnt);
}
