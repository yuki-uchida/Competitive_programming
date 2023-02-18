use proconio::{input};
fn main() {
    input! {
        n: usize, // n歳の時
        m: usize, // m歳の時の身長が知りたい
        x: usize, // x歳からは身長が伸びない
        t: usize, // n歳の時の身長はt
        d: usize, // 毎年身長がd伸びる
    }
    // n => t
    // x => 
    let tall_n: usize = t;
    let tall_x = if n >= x {
        t
    } else {
        t + (d*(n-x))
    };
    if m >= x {
        println!("{}",tall_x);
    } else {
        println!("{}",tall_x - (d*(x-m)));
    }
}
