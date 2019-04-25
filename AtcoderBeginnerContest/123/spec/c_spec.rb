require './c_question'
RSpec.describe C_question do
    context "正しい答えになるか" do 
        let(:c_instance) {C_question.new}
        describe "テストセット" do
            it "test--set" do
                expect(c_instance.calc(
                    5,
                    3,
                    2,
                    4,
                    3,
                    5)).to eq 7
            end
        end
    end
end
