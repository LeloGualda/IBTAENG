function simpson(f,x0,x1,n){
   // validação de erros
   if (typeof f !== 'function')
        throw new Error('parâmetro f não é uma função');
   if (n % 2 === 1 || n < 0)
        throw new Error('valor n precisa ser par!');
   if (typeof n !== 'number' || typeof x0 !== 'number' ||  typeof x1 !== 'number')
         throw new Error('Os valores de n, x0 e x1 precisam ser números');
   if (typeof f(x0) !== 'number' || typeof f(x1) !== 'number')
         throw Error('A função não retorna um valor válido');
// inicio da função simpson
  let area = -f(x0);
  const h = (x1-x0)/n;
    for(let i = 0;i<=n;i++)
      area += (i%2?4:2) * f(x0 + (h*i));
  return (area-f(x1))*h/3;
}
module.exports = simpson;
