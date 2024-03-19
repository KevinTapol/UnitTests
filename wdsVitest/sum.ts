export default function sum(...numnbers: number[]) {
    return numnbers.reduce((total, number) => total + number, 0)
}