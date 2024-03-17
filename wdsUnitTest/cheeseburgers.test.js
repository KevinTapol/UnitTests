const fries = require('./cheeseburgers')

test('returns the product of 2 numbers', () => {
    expect(fries(2, 3)).toBe(6)
})