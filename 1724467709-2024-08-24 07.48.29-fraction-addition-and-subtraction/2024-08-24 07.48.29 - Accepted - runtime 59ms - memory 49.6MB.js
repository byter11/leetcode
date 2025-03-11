/**
 * @param {string} expression
 * @return {string}
 */

var gcd = function(a, b) {
    return a == 0 ? b : gcd(b % a, a)
}

var fractionAddition = function(expression) {
    if (expression[0] != '-') expression = "+" + expression
    const tokens = expression.split(/(\+)/g)
    .flatMap(t => t.split(/(\-)/g)).filter(c => c)

    let nom = 0
    let denom = 1
    for(let i = 0; i<tokens.length - 1; i += 2) {
        const sign = tokens[i] == '-' ? -1 : 1
        let [n, d] = tokens[i+1].split('/')
        n = parseInt(n) * sign
        d = parseInt(d)

        nom *= d
        nom += n * denom
        denom *= d
    }

    g = Math.abs(gcd(nom, denom))
    
    return `${Number(nom/g).toFixed(0)}/${Number(denom/g).toFixed(0)}`
};