const PrimeiroGrau = (y0,y1,x0,x1) => (x) => ((y1-y0)/(x1-x0))*(x-x0) + y0;

module.exports = PrimeiroGrau;
