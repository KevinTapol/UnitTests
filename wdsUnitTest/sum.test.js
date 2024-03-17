const sum = require("./sum")

/*
test("adds two numbers", () => {

    if (sum(1,2) === 3){
        console.log("pass")
    } else {
        console.log("fail")
    }
})
*/

test("adds two numbers", () => {
    expect(
        sum(1,2)
        ).toBe(3)
})