use proconio::input;
use proconio::marker::Usize1;

fn main() {
    input! {
        n: usize,
        p: Usize1,
        q: Usize1,
        r: Usize1,
        s: Usize1,
        nums: [usize; n],
    }
    for i in  0..n {
      if p <= i && i <= q {
        print!("{} ", nums[r + i - p]);
      } else if r <= i && i <= s {
        print!("{} ", nums[p + i -r]);
      } else {
        print!("{} ", nums[i]);
      }
    }
}
