import PrimeiroGrau from '../component/criarFuncao';

describe('PrimeiroGrau', () => {
  test('f(10)=10;f(20)=300', () => {
    const f =  PrimeiroGrau(10,300,10,20);
    expect(f(10)).toBe(10);
    expect(f(20)).toBe(300);
  });
});
