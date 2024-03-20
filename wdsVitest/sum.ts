export default function sum(...numnbers: number[]) {
    return numnbers.reduce((total, number) => total + number, 0)
}

// inline testing same file
// If the code is small, it is good practice to put your code in line and strip the tests afterwards.

/* 
Error occurs because we need to tell Typescript that we have this import on import.meta.vitest. 
To fix this, go to tsconfig.json and add 
"types": [
    "vitest/importMeta"
]
I am not sure why this doesn't require a comma at the end of the key value pair where the value is an array.
*/
if (import.meta.vitest){
    const { describe, expect, it } = import.meta.vitest
    describe("#sum", () => {
        it("returns 0 with no numbers", () => {
            expect(sum()).toBe(0)
        })
    
        it("returns the same number passed in", () => {
            expect(sum(2)).toBe(2)
        })
    
        it("returns the sum of multiple numbers", () => {
            expect(sum(1,2,3)).toBe(6)
        })
    })
}
