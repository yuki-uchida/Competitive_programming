use proconio::{input, marker::Bytes};
fn main() {
    input! {
        s: Bytes,
    }
    let string_length: usize = s.len();
    if string_length != 8 {
        println!("No");
    }else{
        if s[0].is_ascii_uppercase() && s[1] != b'0' && s[1].is_ascii_digit() && s[2].is_ascii_digit() && s[3].is_ascii_digit() && s[4].is_ascii_digit() && s[5].is_ascii_digit() && s[6].is_ascii_digit() &&  s[7].is_ascii_uppercase() {
            println!("Yes");
        }else{
            println!("No");
        }
    }
}
