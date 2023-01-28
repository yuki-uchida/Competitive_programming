use proconio::input;
fn main() {
    input! {
        nums: [u128;6],
    }
    let a = &nums[0];
    let b = &nums[1];
    let c = &nums[2];
    let d = &nums[3];
    let e = &nums[4];
    let f = &nums[5];
    let num = 998244353;
    let left = ((a%num) * (b%num) * (c%num))%num;
    let right = ((d%num) * (e%num) * (f%num))%num;
    println!("{}", (left + num -right)%num);
}
