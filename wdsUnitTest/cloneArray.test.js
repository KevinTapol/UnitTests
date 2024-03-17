const cloneArray = require('./cloneArray')

// checking to see if clone array is making a copy referencing the different memory locations

test('clones array to be equal by value but not reference', () => {
    const array = [1, 2, 3]
    expect(cloneArray(array)).toEqual(array)
    expect(cloneArray(array)).not.toBe(array)
})