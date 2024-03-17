function cloneArray(array){
    // keep in mind this creates a clone of the array so they are not the same reference but are the same value
    return [...array]
}

module.exports = cloneArray