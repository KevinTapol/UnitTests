import sum from "./sum"
import { describe, expect, it } from "vitest"

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