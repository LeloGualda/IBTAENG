import Simpson from '../component/areaDaFuncao';

describe('Simpson', () => {
  test('f(x)= x²-x  ∫ 2 a 3  | n = 4', () => {
    const f = (x) => (x*x) -x;
    expect(Simpson(f,2,3,4)).toBe(23/6);

  });
  test('f(x)= x²-x  ∫ 1 a 3  | n = 4', () => {
    const f = (x) => (x*x) -x;
    expect(Simpson(f,1,3,4)).toBe(14/3);
  });
  test('f(x)= x²-x  ∫ 1 a 3  | n = 10', () => {
    const f = (x) => (x*x) -x;
    expect(Simpson(f,1,3,10)).toBe(14/3);
  });
  test('error: n é impar: f(x)= x', () => {
    const f = (x) => x;
    expect(() => Simpson(f,1,3,1)).toThrowError(new Error("valor n precisa ser par!"));
  });
test('error:f não é função', () => {
    expect(() => Simpson(null,1,3,1)).toThrowError(new Error("parâmetro f não é uma função"));
  });
  test('error:f() não devolve numero', () => {
    expect(() => Simpson(()=>{},1,3,2)).toThrowError(new Error("A função não retorna um valor válido"));
  });
  test('error: n invalido', () => {
    const f = (x) => x;
    expect(() => Simpson(f,1,3,null)).toThrowError(new Error("Os valores de n, x0 e x1 precisam ser números"));
  });
  test('error: x0 invalido', () => {
    const f = (x) => x;
    expect(() => Simpson(f,1,null,2)).toThrowError(new Error("Os valores de n, x0 e x1 precisam ser números"));
  });
  test('error: x1 invalido', () => {
    const f = (x) => x;
    expect(() => Simpson(f,null,2,2)).toThrowError(new Error("Os valores de n, x0 e x1 precisam ser números"));
  });
});
