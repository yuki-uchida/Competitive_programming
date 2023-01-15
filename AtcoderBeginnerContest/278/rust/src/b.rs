use proconio::input;
fn main() {
    input! {
        mut h: usize,
        mut m: usize,
    }
    loop {
        let (convert_h, convert_m) = (h / 10 * 10 + m / 10, h % 10 * 10 + m % 10);
        if convert_h < 24 && convert_m < 60 {
            println!("{} {}", h, m);
            break;
        }
        m += 1;
        if m == 60 {
            h += 1;
            m = 0;
        }
        if h == 24 {
            h = 0;
        }
    }
}
