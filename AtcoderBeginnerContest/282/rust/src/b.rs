use proconio::input;
use proconio::marker::Bytes;
fn main() {
    input! {
        people: usize,
        question_count: usize,
        is_able_to_answer_question: [Bytes; people],
    };
    // println!("{:?}",is_able_to_answer_question);
    // 二人ペアにして、全ての問題が解ける数を数える
    // 二人ペアなのでmC2通りある
    let mut is_able_to_answer_question_count: usize = 0; 
    for i in 0..(people) {
        for j in (i+1)..(people) {
            // println!("{:?}, {:?}", i, j);
            let i_person_is_able_to_answer = &is_able_to_answer_question[i];
            let j_person_is_able_to_answer = &is_able_to_answer_question[j];
            let mut or_is_able_to_answer = true;
            for k in 0..question_count {
                if i_person_is_able_to_answer[k] != b'o' && j_person_is_able_to_answer[k] != b'o' {
                    or_is_able_to_answer = false;
                    break;
                }
            }
            if or_is_able_to_answer {
                is_able_to_answer_question_count += 1;
            }
        }
    }
    println!("{:?}", is_able_to_answer_question_count);
}
