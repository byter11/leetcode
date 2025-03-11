/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var luckyNumbers  = function(matrix) {
    const colSum = Array(matrix[0].length).fill(0)
    const rowSum = Array(matrix.length).fill(10000000)
    
    
    matrix.forEach((row, i) => {
      row.forEach((col, j) => {
        colSum[j] = Math.max(colSum[j], col)
                             
        rowSum[i] = Math.min(rowSum[i], col)
      })
    })
                                             
                                       return colSum.filter(c => rowSum.includes(c))




                                             

};