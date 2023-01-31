use proconio::input;


fn main() {
    input! {
        n: usize,
        mut texts: [String; n],
    }
    for text in texts.iter().rev() {
        println!("{}", text);
    }
}
